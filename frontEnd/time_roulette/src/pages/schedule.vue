<script setup lang="ts">
import '../style.css';
import { reactive, computed, ref } from 'vue';
import TopBar from '../components/TopBar.vue';
import LeftMenu from '../components/LeftMenu.vue';
import Card from '../components/Card.vue';
import CardDetails from '../components/cardDetails.vue';

export type cardInfo = {
    id: number;
    title: string;
    time: string;
    address: string;
    contents: string;
};
let list: cardInfo[] = reactive([
    {
        id: 1,
        title: 'a',
        time: '2023.1.2',
        address: '南区大饭店',
        contents:
            '今天要吃饭金天要吃饭今天要吃饭今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭'
    },
    {
        id: 2,
        title: 'a',
        time: '2023.1.15',
        address: '南区大饭店',
        contents:
            '今天要吃饭<br />金天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭'
    },
    {
        id: 3,
        title: 'a',
        time: '2023.1.4',
        address: '南区大饭店',
        contents:
            '今天要吃饭<br />金天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭<br />今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭今天要吃饭'
    }
    // { id: 15, title: 'a', time: '2023.1.8', address: '南区大饭店' },
    // { id: 5, title: 'a', time: '2023.1.6', address: '南区大饭店' },
    // { id: 6, title: 'a', time: '2023.1.7', address: '南区大饭店' },
    // { id: 7, title: 'a', time: '2023.1.8', address: '南区大饭店' },
    // { id: 8, title: 'a', time: '2023.1.9', address: '南区大饭店' },
    // { id: 9, title: 'a', time: '2023.1.10', address: '南区大饭店' },
    // { id: 10, title: 'a', time: '2023.1.11', address: '南区大饭店' },
    // { id: 11, title: 'a', time: '2023.1.15', address: '南区大饭店' },
    // { id: 12, title: 'a', time: '2023.1.16', address: '南区大饭店' },
    // { id: 13, title: 'a', time: '2023.1.11', address: '南区大饭店' },
    // { id: 14, title: 'a', time: '2023.1.12', address: '南区大饭店' }
]);

const sortMode = ['按默认排序', '按时间排序'];
// const sortIndex = ref(0);
const sortOpe = ref('按默认排序');
const sortById = () => {
    list = list.sort((a, b) => a.id - b.id);
};

const sort = () => {
    if (sortOpe.value === sortMode[0]) {
        sortById();
    } else if (sortOpe.value === sortMode[1]) {
        sortByDate();
    }
};

const sortByDate = () => {
    list = list.sort((a, b) => {
        const dateA = new Date(a.time);
        const dateB = new Date(b.time);
        return dateA.getTime() - dateB.getTime();
    });
};

const deleteCard = (card: cardInfo) => {
    console.log('delete card:' + card.id);
    const index = list.findIndex(item => item === card);
    if (index !== -1) {
        list.splice(index, 1);
    }
};

const updateCard = (card: cardInfo) => {
    const index = list.findIndex(item => item.id === card.id);
    list[index] = card;
};

sortById();
</script>

<template>
    <div class="all">
        <div class="TopMenu">
            <TopBar />
        </div>
        <el-row class="main">
            <CardDetails :card="list[0]" :updateCard="updateCard" :visible="true" />
            <el-col :span="4" class="left">
                <el-row class="control" justify="space-evenly" align="middle">
                    <el-row :gutter="20">
                        <el-col :span="12">
                            <el-button type="primary">添加</el-button>
                        </el-col>
                        <el-col :span="12">
                            <el-button type="primary">删除</el-button>
                        </el-col>
                    </el-row>
                    <el-row justify="center" align="top">
                        <el-col :span="20">
                            <el-select v-model="sortOpe" @change="sort">
                                <el-option :key="sortOpe" :value="sortMode[0]" />
                                <el-option :key="sortOpe" :value="sortMode[1]" />
                            </el-select>
                        </el-col>
                    </el-row>
                </el-row>

                <LeftMenu class="LeftMenu" />
            </el-col>
            <el-col :span="18" :flex="1" class="right">
                <el-scrollbar>
                    <el-alert
                        class="alertNull"
                        v-show="list.length === 0"
                        title="还没有日程捏，速速创建"
                        type="warning"
                        show-icon
                        center
                    />
                    <el-row class="schedule-items">
                        <!-- <el-col :span="6" v-for="{ id, time } in list" :key="id" class="schedule"> -->
                        <transition-group name="el-zoom-in-center">
                            <Card
                                v-for="item in list"
                                :key="item.id"
                                class="schedule"
                                :card="item"
                                :deleteCard="deleteCard"
                            />
                        </transition-group>

                        <!-- </el-col> -->
                    </el-row>
                </el-scrollbar>
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

.schedule-items {
    max-height: 100%;
    overflow-y: auto;
    justify-content: center;
    margin: 0 auto;
}
.alertNull {
    margin-top: 10px;
    min-width: 500px;
}
</style>
