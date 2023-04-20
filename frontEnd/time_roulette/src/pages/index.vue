<script setup lang="ts">
import '../style.css';
import TopBar from '../components/TopBar.vue';
import LeftMenu from '../components/LeftMenu.vue';
</script>

<template>
    <div class="all">
        <div class="TopMenu">
            <TopBar />
        </div>
        <el-row class="main">
            <el-col :span="4" class="left">
                <LeftMenu class="LeftMenu" />
            </el-col>
            <el-col :span="18" :flex="1" class="right">
                <el-row class="schedule-items">
                    <el-col :span="6" v-for="i in 20" :key="i" class="schedule">
                        <div>{{ i }}</div>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
    </div>
</template>

<style scoped>
.all {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    background-color: #f1f5f9;
}
.TopMenu {
    width: 100%;
    height: 60px;
}
.main {
    display: flex;
    height: 100%;
    margin: 10px;
}
.row {
    width: 100%;
    height: 100%;
}

.left {
    width: 100%;
    height: 100%;
    margin-right: 10px;
}
.right {
    width: 100%;
    max-height: calc(100vh - 60px);
    margin-left: 50px;
    padding-right: 10px;
    padding-top: 10px;
    /* box-shadow: 0 0 3px black; */
    border-radius: 15px;
    display: flex;
    position: relative;
    text-align: center;
    justify-content: center;
}
.schedule-items{
    max-height: 100%;
    overflow-y: auto;
    padding-right: 10px;
    justify-content: center;
}



.schedule {
    height: 300px;
    box-shadow: 0 0 3px black;
    background-color: #75d0fa;
    border-radius: 15px;
    margin: 15px;
}
</style>
