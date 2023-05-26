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
                <!-- <el-col class="user" :gutter="12"> -->
                <el-col class="userData">
                    <el-row class="avatar">
                        <el-icon :size="20"> <UserFilled /> </el-icon>
                    </el-row>
                    <el-row class="name" @click="edit">
                        <span>{{ store.state.username }}</span>
                        <el-icon size="20" class="edit"><Edit /></el-icon>
                    </el-row>
                    <el-row class="button">
                        <el-button type="danger">
                            <el-icon><SwitchButton /></el-icon>
                            退出登陆
                        </el-button>
                    </el-row>
                </el-col>

                <!-- </el-col> -->
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
        router.push('/login');
    });
};

const edit = () => {};
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

.userData {
    width: 100%;
    height: 150px;
    margin-top: 15px;
    justify-content: center;
}
.avatar {
    width: 100%;
    height: 50px;
    justify-content: center;
}

.edit {
    margin-left: 5px;
}

.name {
    font-size: 15px;
    margin: 10px;
    justify-content: center;
}

.button {
    justify-content: center;
    margin: 20px;
    /* margin-bottom: 10px; */
}
</style>
