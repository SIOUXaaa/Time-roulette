<template>
    <el-menu
        class="TopMenu"
        :default-active="activeIndex"
        mode="horizontal"
        @select="handleSelect"
        router
    >
        <el-row v-if="login_success">
            <el-sub-menu index="">
                <template #title>
                    <el-icon :size="20"> <UserFilled /> </el-icon>
                    <span>{{ store.state.username }}</span>
                </template>
                <el-menu-item index="me">
                    <el-icon><User /></el-icon>
                    <span>我的主页</span>
                </el-menu-item>
                <el-menu-item @click="handleQuit">
                    <el-icon><SwitchButton /></el-icon>
                    <span>退出登陆</span>
                </el-menu-item>
            </el-sub-menu>
        </el-row>
        <el-row v-else>
            <el-menu-item index="login" class="barButton">
                <el-button type="primary" class="button">登录</el-button>
            </el-menu-item>
            <el-menu-item index="login" class="barButton">
                <el-button class="button">注册</el-button>
            </el-menu-item>
        </el-row>
    </el-menu>
</template>

<script lang="ts" setup>
import { UserFilled } from '@element-plus/icons-vue';
import { defineComponent, ref } from 'vue';
import { mapActions, useStore, mapState } from 'vuex';
import router from '../router';

defineComponent({
    name: 'TopBar'
});

const store = useStore();
const activeIndex = ref('home');
const login_success = mapState(['login_success']);

const handleSelect = (index: string) => {
    activeIndex.value = index;
};

const handleQuit = () => {
    store.dispatch('quit').then(() => {
        router.push('/login')
    })
}
</script>

<style scoped>
.TopMenu {
    display: flex;
    width: 100%;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: right;
    padding: 0 20px;
    box-shadow: 0 0 4px #cdd0d6;
}
.barButton {
    width: min-content;
    height: min-content;
    padding: 0px;
    margin: 10px;
}
</style>
