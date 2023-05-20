<template>
    <el-menu
        class="TopMenu"
        :default-active="activeIndex"
        mode="horizontal"
        @select="handleSelect"
        router
    >
        <el-menu-item index="me">
            <el-icon :size="20">
                <UserFilled />
            </el-icon>
        </el-menu-item>
        <el-menu-item index="login" class="barButton">
            <el-button type="primary" class="button">登录</el-button>
        </el-menu-item>
        <el-menu-item index="login" class="barButton">
            <el-button class="button">注册</el-button>
        </el-menu-item>
    </el-menu>
</template>

<script lang="ts" setup>
import { UserFilled } from '@element-plus/icons-vue';
import { defineComponent, ref } from 'vue';

defineComponent({
    name: 'TopBar'
});

const activeIndex = ref('home');

const handleSelect = (index: string) => {
    activeIndex.value = index;
};
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
.barButton{
    width: min-content;
    height: min-content;
    padding: 0px;
    margin: 10px;
}

</style>
