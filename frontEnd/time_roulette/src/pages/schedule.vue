<script setup lang="ts">
import '../style.css';
import { reactive, computed, ref, onMounted } from 'vue';
import TopBar from '../components/TopBar.vue';
import LeftMenu from '../components/LeftMenu.vue';
import Card from '../components/Card.vue';
import CardDetails from '../components/cardDetails.vue';
import user from '../components/user.vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { mapActions, useStore, mapState } from 'vuex';
import axios from 'axios';

export type cardInfo = {
    id: number;
    title: string;
    time: string;
    address: string;
    contents: string;
    [key: string]: any; // 添加字符串类型的索引签名
};

const cardDefault: cardInfo = {
    id: -1,
    title: '',
    time: '',
    address: '',
    contents: ''
};

const store = useStore();
const loginSuccess = mapState(['login_success']);
const sortMode = ['按默认排序', '按时间升序排序', '按时间降序排序'];
const sortOpe = ref('按默认排序');
const showCard = ref(false);
const cardValue = ref(cardDefault);
const showUser = ref(false);

let list: cardInfo[] = [];
const listRef = reactive({
    list: list
});

const getSchedule = () => {
    axios
        .get('schedule/get/' + store.state.id)
        .then(response => {
            // console.log(response.data);
            list = response.data.map((item: any) => {
                return {
                    id: item.schedule_id,
                    title: item.title,
                    time: item.time,
                    address: item.address,
                    contents: item.contents
                };
            });
            listRef.list = list;
            // console.log(list);
            // console.log(listRef.list);
        })
        .catch(error => {
            ElMessage.error(error);
        });
};

onMounted(() => {
    getSchedule();
});

const sortById = () => {
    listRef.list = listRef.list.sort((a, b) => a.id - b.id);
};

const sort = () => {
    if (sortOpe.value === sortMode[0]) {
        sortById();
    } else if (sortOpe.value === sortMode[1]) {
        sortByDate('asc');
    } else {
        sortByDate('desc');
    }
};

const sortByDate = (state: String) => {
    listRef.list = listRef.list.sort((a, b) => {
        const dateA = new Date(a.time);
        const dateB = new Date(b.time);
        if (state === 'asc') return dateA.getTime() - dateB.getTime();
        return dateB.getTime() - dateA.getTime();
    });
};

const handleClose = () => {
    showCard.value = false;
};

const handleUserClose = () => {
    showUser.value = false;
};

const deleteCard = (card: cardInfo) => {
    // console.log('delete card:' + card.id);
    axios
        .delete('schedule/delete/' + card.id)
        .then(() => {
            // const index = listRef.list.findIndex(item => item === card);
            // if (index !== -1) {
            //     listRef.list.splice(index, 1);
            // }
            getSchedule();
        })
        .catch(error => {
            ElMessage.error(error.message);
        });
};

const deleteAll = () => {
    ElMessageBox.confirm('即将清除所有日程，是否继续？', '警告', {
        confirmButtonText: '是',
        cancelButtonText: '否',
        type: 'warning'
    })
        .then(() => {
            ElMessage({
                type: 'success',
                message: '已清除所有日程'
            });
            axios
                .delete('schedule/deleteAll/' + store.state.id)
                .then(() => {
                    listRef.list.splice(0, listRef.list.length);
                })
                .catch(error => {
                    ElMessage.error(error.message);
                });
            // for (let item of listRef.list) {
            //     deleteCard(item);
            // }
        })
        .catch(() => {
            ElMessage({
                type: 'info',
                message: '已取消'
            });
        });
};

const updateCard = (card: cardInfo) => {
    // listRef.list.push(card);
    let same = true;
    // const keys = Object.keys(cardDefault);
    for (let key of Object.keys(cardDefault)) {
        if (card[key] !== cardDefault[key]) {
            same = false;
            break;
        }
    }
    if (same) {
        ElMessage({
            message: '你也妹输入啊，完成啥...',
            type: 'warning'
        });
        handleClose();
        return;
    }
    const data = {
        user: store.state.id,
        title: card.title,
        contents: card.contents,
        address: card.address,
        time: card.time
    };
    // console.log(data);
    if (card.id === -1) {
        axios
            .post('schedule/add/', data)
            .then(response => {
                card.id = response.data.schedule_id;
                listRef.list.splice(-1, 0, card);
            })
            .catch(error => {
                ElMessage.error(error);
            });
    } else {
        axios
            .put('schedule/update/' + card.id, data)
            .then(() => {
                // const index = listRef.list.findIndex(item => item.id === card.id);
                // listRef.list.splice(index, 1, card);
                getSchedule();
            })
            .catch(error => {
                ElMessage.error(error);
            });
    }
    handleClose();
};

const addCard = () => {
    editCard({ id: -1, title: '', time: '', address: '', contents: '' });
};

const editCard = (card: cardInfo) => {
    cardValue.value = card;
    // console.log(cardValue.value);
    showCard.value = true;
};

const editUser = () => {
    showUser.value = true;
};

sortById();
</script>

<template>
    <div class="all">
        <div class="TopMenu">
            <TopBar :editUser="editUser" />
        </div>
        <el-row class="main">
            <CardDetails
                :card="cardValue"
                :updateCard="updateCard"
                :visible="showCard"
                :before-close="handleClose"
            />
            <user :visible="showUser" :handleClose="handleUserClose" :before-close="handleUserClose" />
            <el-col :span="4" class="left">
                <el-row class="control" justify="space-evenly" align="middle">
                    <el-row :gutter="20">
                        <el-col :span="12">
                            <el-button type="primary" @click="addCard">添加</el-button>
                        </el-col>
                        <el-col :span="12">
                            <el-button type="primary" @click="deleteAll">删除</el-button>
                        </el-col>
                    </el-row>
                    <el-row justify="center" align="top">
                        <el-col :span="20">
                            <el-select v-model="sortOpe" @change="sort">
                                <el-option :key="sortOpe" :value="sortMode[0]" />
                                <el-option :key="sortOpe" :value="sortMode[1]" />
                                <el-option :key="sortOpe" :value="sortMode[2]" />
                            </el-select>
                        </el-col>
                    </el-row>
                    <el-row> </el-row>
                </el-row>

                <LeftMenu class="LeftMenu" :activeIndex="'schedule'" />
            </el-col>
            <el-col :span="18" :flex="1" class="right">
                <div class="mask">
                    <el-scrollbar>
                        <el-row class="schedule-items">
                            <el-alert
                                class="alertNull"
                                v-show="listRef.list.length === 0"
                                title="还没有日程捏，速速创建"
                                type="warning"
                                show-icon
                                center
                            />
                            <!-- <el-col :span="6" v-for="{ id, time } in list" :key="id" class="schedule"> -->
                            <transition-group name="el-zoom-in-center">
                                <Card
                                    v-for="item in listRef.list"
                                    :key="item.id"
                                    class="schedule"
                                    :card="item"
                                    :deleteCard="deleteCard"
                                    :editCard="editCard"
                                />
                            </transition-group>

                            <!-- </el-col> -->
                        </el-row>
                    </el-scrollbar>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<style scoped>
.all {
    width: 100%;
    height: 100vh;
    display: inline-block;
    flex-direction: column;
    background-color: #f2f3f5;
}
.TopMenu {
    width: 100%;
    height: 60px;
}
.main {
    display: flex;
    height: calc(100vh - 70px);
    margin-bottom: 10px;
}

.left {
    width: 100%;
    max-height: calc(100vh - 80px - 150px - 10px);
    margin-right: 10px;
}
.right {
    width: 100%;
    background-color: #ffffff;
    max-height: calc(100vh - 80px);
    margin-top: 10px;
    margin-left: 50px;
    margin-bottom: 10px;
    padding-bottom: 10px;
    box-shadow: 0 0 8px #cdd0d6;
    border-radius: 15px;
    display: flex;
    position: relative;
    text-align: center;
    justify-content: center;
}

.mask {
    width: 100%;
    max-height: calc(100vh - 80px);
    padding-bottom: 15px;
    -webkit-mask-image: linear-gradient(rgb(227, 227, 227), 90%, transparent);
}
.control {
    min-width: 125px;
    width: 100%;
    height: 150px;
    background-color: #ffffff;
    box-shadow: 0 0 8px #cdd0d6;
    margin-top: 10px;
    margin-left: 30px;
    margin-right: 10px;
    border-radius: 15px;
}

.schedule-items {
    max-height: 100%;
    overflow-y: auto;
    justify-content: center;
    margin: 0 auto;
}
.alertNull {
    position: fixed;
    z-index: 999;
    margin-top: 10px;
    width: 500px;
}
</style>
