<script setup lang="ts">
import '../style.css';
import { reactive, computed, ref } from 'vue';
import TopBar from '../components/TopBar.vue';
import LeftMenu from '../components/LeftMenu.vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import MemoDetails from '../components/MemoDetails.vue';

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

const listRef = reactive({
    list: [
        { id: 1, contents: '今天要吃饭', done: false,remained: false, time: '2000-1-1 0:0:0' },
        { id: 2, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 3, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 4, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 5, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 6, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 7, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 8, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 9, contents: '今天要吃饭', done: false ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 10, contents: '今天要吃饭', done: false,reminded: false, time: '2000-1-1 0:0:0' }
    ]
});

const listDone = reactive({
    list: [
        { id: 11, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 12, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 13, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 14, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 15, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 16, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 17, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'},
        { id: 18, contents: '今天要吃饭', done: true ,reminded: false, time: '2000-1-1 0:0:0'}
    ]
});


const activeCollapse = ref('unfinished');
const memoValue = ref(memoDefault);
const showMemo = ref(false)

const updateDone = (memo: memoInfo) => {
    console.log(memo);
    const index = listRef.list.findIndex(item => item.id === memo.id);
    listRef.list.splice(index, 1);
    listDone.list.push(memo);
};

const updateMemo = (memo: memoInfo) => {};

const addMemo = () => {
    showMemo.value = true;
    console.log(listRef.list);
    console.log(listDone.list);
};

const clearDone = () => { };

const handleClose = () => {
    showMemo.value = false;
}
</script>

<template>
    <div class="all">
        <div class="TopMenu">
            <TopBar />
        </div>
        <el-row class="main">
            <MemoDetails 
                :memo="memoValue"
                :visible="showMemo"
                :update-memo="addMemo"
                :before-close="handleClose"
            />
            <el-col :span="4" class="left">
                <el-row class="control" justify="space-evenly" align="middle">
                    <el-row :gutter="20">
                        <el-col :span="12">
                            <el-button type="primary" @click="addMemo">添加</el-button>
                        </el-col>
                        <el-col :span="12">
                            <el-button type="primary" @click="">清空</el-button>
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
                            <el-collapse-item class="collapse-item" title="已完成" name="finished">
                                <el-row class="" :span="24">
                                    <transition-group name="el-zoom-in-center">
                                        <el-col
                                            :span="12"
                                            v-for="item in listDone.list"
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
    margin-top: 10px;
    width: 500px;
}

.collapse-item {
    margin: 25px;
}
</style>
