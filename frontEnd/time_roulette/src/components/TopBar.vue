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
                    <el-avatar v-if="avatar" :src="store.state.url + avatar" />
                    <el-avatar v-else :icon="UserFilled" />
                    <span style="margin-left: 10px">{{ username }}</span>
                </template>
                <!-- <el-col class="user" :gutter="12"> -->
                <el-col class="userData">
                    <el-row class="avatar">
                        <img
                            v-if="avatar"
                            :src="store.state.url + avatar"
                            class="avatar"
                            style="border-radius: 9999px; width: 50px; height: 50px"
                        />
                        <el-avatar
                            v-else
                            :icon="UserFilled"
                            style="border-radius: 9999px; width: 50px; height: 50px"
                        />
                    </el-row>
                    <el-row class="name" @click="editUser">
                        <span>{{ store.state.username }}</span>
                        <el-icon size="20" class="edit"><Edit /></el-icon>
                    </el-row>
                    <el-row class="button">
                        <el-button type="danger" @click="handleQuit">
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
import { SwitchButton, UserFilled } from '@element-plus/icons-vue';
import { defineComponent, ref, toRefs } from 'vue';
import { mapActions, useStore, mapState } from 'vuex';
import router from '../router';

defineComponent({
    name: 'TopBar'
});

const props = defineProps({
    editUser: Function
});

const store = useStore();
const activeIndex = ref('home');
// const login_success = mapState(['login_success']);
const { avatar, login_success, id, username } = toRefs(store.state);
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

.name:hover span {
    cursor: pointer;
    color: #409eff;
}

.name:hover .edit {
    cursor: pointer;
    color: #409eff;
}
.button {
    justify-content: center;
    margin: 20px;
    /* margin-bottom: 10px; */
}
</style>
