<template>
    <el-menu
        class="TopMenu"
        :default-active="activeIndex"
        mode="horizontal"
        background-color="#f1f5f9"
        text-color="#000"
        active-text-color="#ffd04b"
        @select="handleSelect"
        router
    >
        <el-menu-item index="me">
            <el-avatar :icon="UserFilled" />
        </el-menu-item>
        <el-menu-item index="login"> 
            登陆
        </el-menu-item>
        <el-menu-item index="login"> 
            注册
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
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

</style>
