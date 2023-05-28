<script setup lang="ts">
import '../style.css';
import { reactive, computed, ref, onMounted } from 'vue';
import TopBar from '../components/TopBar.vue';
import LeftMenu from '../components/LeftMenu.vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import MemoDetails from '../components/MemoDetails.vue';
import axios from 'axios';
import store from '../store';

export type memoInfo = {
    id: number;
    contents: string;
    done: boolean;
    reminded: boolean;
    time: string;
    [key: string]: any; // 添加字符串类型的索引签名
};
const memoDefault: memoInfo = {
    id: -1,
    contents: '',
    done: false,
    reminded: false,
    time: '2000-1-1 0:0:0'
};

let list: memoInfo[] = [];
let listDone: memoInfo[] = [];
const listRef = reactive({
    list: list
});
const listDoneRef = reactive({
    list: listDone
});

const activeCollapse = ref('unfinished');
const memoValue = ref(memoDefault);
const showMemo = ref(false);
const showUser = ref(false);

const getMemo = () => {
    axios
        .get('memo/get/' + store.state.id)
        .then(response => {
            list = response.data.map((item: any) => {
                return {
                    id: item.memo_id,
                    contents: item.contents,
                    done: item.done,
                    reminded: item.reminded,
                    time: item.time
                };
            });
            listRef.list = list;
        })
        .catch(error => {
            ElMessage.error(error);
        });
};

const getMemoDone = () => {
    axios
        .get('memo/getDone/' + store.state.id)
        .then(response => {
            list = response.data.map((item: any) => {
                return {
                    id: item.memo_id,
                    contents: item.contents,
                    done: item.done,
                    reminded: item.reminded,
                    time: item.time
                };
            });
            listDoneRef.list = list;
        })
        .catch(error => {
            ElMessage.error(error);
        });
};

const updateDone = (memo: memoInfo) => {
    // console.log(memo);
    let data;
    if (memo.reminded) {
        data = {
            user: store.state.id,
            contents: memo.contents,
            done: memo.done,
            reminded: memo.reminded,
            time: memo.time
        };
    } else {
        data = {
            user: store.state.id,
            contents: memo.contents,
            done: memo.done,
            reminded: memo.reminded
        };
    }
    if (memo.id === -1) {
        updateMemo(memo);
    } else {
        // console.log(data);
        axios
            .put('memo/update/' + memo.id, data)
            .then(() => {
                if (memo.done) {
                    // const index = listRef.list.findIndex(item => item.id === memo.id);
                    // listRef.list.splice(index, 1);
                    // listDoneRef.list.push(memo);
                    getMemo();
                    getMemoDone();
                } else {
                    // const index = listDoneRef.list.findIndex(item => item.id === memo.id);
                    // listDoneRef.list.splice(index, 1);
                    // listRef.list.push(memo);
                    getMemo();
                    getMemoDone();
                }
            })
            .catch(error => {
                ElMessage.error(error.message);
            });
    }
};

const updateMemo = (memo: memoInfo) => {
    let data;
    if (memo.reminded) {
        data = {
            user: store.state.id,
            contents: memo.contents,
            done: memo.done,
            reminded: memo.reminded,
            time: memo.time
        };
    } else {
        data = {
            user: store.state.id,
            contents: memo.contents,
            done: memo.done,
            reminded: memo.reminded
        };
    }
    // console.log(data);
    axios
        .post('memo/add/', data)
        .then(response => {
            memo.id = response.data.memo_id;
            // console.log(memo);
            // listRef.list.splice(-1, 0, memo);
            getMemo();
            getMemoDone();
            // console.log(memo);
        })
        .catch(error => {
            ElMessage.error(error.message);
        });
    handleClose();
};

const addMemo = () => {
    showMemo.value = true;
    // console.log(listRef.list);
    // console.log(listDoneRef.list);
};

const clearDone = () => {
    axios
        .put('memo/deleteAll/' + store.state.id)
        .then(response => {
            ElMessage.success('所有代办已完成');
            getMemo();
            // console.log(listRef.list);
            getMemoDone();
            // console.log(listDoneRef.list);
        })
        .catch(error => {
            ElMessage.error(error.message);
        });
};

const handleClose = () => {
    showMemo.value = false;
};

const handleUserClose = () => {
    showUser.value = false;
};

const editUser = () => {
    showUser.value = true;
};

onMounted(() => {
    getMemo();
    getMemoDone();
});
</script>

<template>
    <div class="all">
        <div class="TopMenu">
            <TopBar :editUser="editUser" />
        </div>
        <el-row class="main">
            <MemoDetails
                :memo="memoValue"
                :visible="showMemo"
                :updateMemo="updateMemo"
                :before-close="handleClose"
            />
            <user
                :visible="showUser"
                :handleClose="handleUserClose"
                :before-close="handleUserClose"
            />
            <el-col :span="4" class="left">
                <el-row class="control" justify="space-evenly" align="middle">
                    <el-row :gutter="20">
                        <el-col :span="12">
                            <el-button type="primary" @click="addMemo">添加</el-button>
                        </el-col>
                        <el-col :span="12">
                            <el-button type="primary" @click="clearDone">清空</el-button>
                        </el-col>
                    </el-row>
                </el-row>

                <LeftMenu class="LeftMenu" :activeIndex="'memo'" />
            </el-col>
            <el-col :span="18" :flex="1" class="right">
                <!-- <el-col :span="6" v-for="{ id, time } in list" :key="id" class="schedule"> -->

                <el-row class="memo-items">
                    <el-alert
                        class="alertNull"
                        v-show="listRef.list.length === 0"
                        title="还没有待办捏，速速创建"
                        type="warning"
                        show-icon
                        center
                    />
                    <div class="mask">
                        <el-scrollbar class="scrollbar">
                            <el-collapse class="collapse" v-model="activeCollapse">
                                <el-collapse-item
                                    class="collapse-item"
                                    title="未完成"
                                    name="unfinished"
                                >
                                    <el-row :span="24">
                                        <transition-group name="el-zoom-in-center">
                                            <el-col
                                                :span="12"
                                                v-for="item in listRef.list"
                                                :key="item.id"
                                            >
                                                <MemoItem
                                                    class="memo"
                                                    :key="item.id"
                                                    :memo="item"
                                                    :updateMemo="updateMemo"
                                                    :updateDone="updateDone"
                                                />
                                            </el-col>
                                        </transition-group>
                                    </el-row>
                                </el-collapse-item>
                                <el-collapse-item
                                    class="collapse-item"
                                    title="已完成"
                                    name="finished"
                                >
                                    <el-row class="" :span="24">
                                        <transition-group name="el-zoom-in-center">
                                            <el-col
                                                :span="12"
                                                v-for="item in listDoneRef.list"
                                                :key="item.id"
                                            >
                                                <MemoItem
                                                    class="memo"
                                                    :key="item.id"
                                                    :memo="item"
                                                    :updateMemo="updateMemo"
                                                    :updateDone="updateDone"
                                                />
                                            </el-col>
                                        </transition-group>
                                    </el-row>
                                </el-collapse-item>
                            </el-collapse>
                        </el-scrollbar>
                    </div>
                </el-row>
                <!-- </el-col> -->
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

.mask {
    width: 100%;
    max-height: calc(100vh - 100px);
    padding-bottom: 15px;
    -webkit-mask-image: linear-gradient(rgb(227, 227, 227), 90%, transparent);
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
    box-shadow: 0 0 8px #cdd0d6;
    border-radius: 15px;
    display: flex;
    position: relative;
    text-align: center;
    justify-content: center;
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

.scrollbar {
    width: 100%;
    max-height: 100%;
}

.memo-items {
    width: 100%;
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

.collapse-item {
    margin: 25px;
}
</style>
