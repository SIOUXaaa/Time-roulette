<template>
    <div class="TopBar">
        <el-menu :default-active="activeIndex" class="menu" mode="horizontal" @select="handleSelect">
            <el-menu-item index="home">首页</el-menu-item>
            <el-menu-item index="about">关于</el-menu-item>
            <el-menu-item index="contact">联系我们</el-menu-item>
        </el-menu>
    </div>
</template>

<script lang="ts">

export default {
    name: "TopBar",
    data() {
        return {
            activeIndex: "home" as string
        };
    },
    methods: {
        handleSelect(index: string) {
            this.activeIndex= index;
        },
    },
    components:{
    }
}
</script>
  
<style scoped>
.TopBar {
    background-color: #fff;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.menu {
  border: none;
}
</style>
  