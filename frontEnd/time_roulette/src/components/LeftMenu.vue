<script setup lang="ts">
import { ref, defineComponent } from 'vue';

defineComponent({
    name: "LeftMenu"
})
const activeIndex = ref("schedule")

const handleSelect = (index: string) => {
    activeIndex.value = index;
    console.log(activeIndex.value);
    console.log("select");
}

</script>

<template>
    <el-menu
        class="LeftMenu"
        :default-active="activeIndex"
        background-color="#f1f5f9"
        text-color="#000"
        active-text-color="rgb(34, 142, 108)"
        @select="handleSelect"
        router
    >
        <el-menu-item index="schedule">
            <el-icon><Calendar /></el-icon>
            <span>日程</span>
        </el-menu-item>
        <el-menu-item index="memo">
            <el-icon><List /></el-icon>
            <span>备忘录</span>
        </el-menu-item>
    </el-menu>
</template>

<style scoped>
.LeftMenu{
    width: 100%;
    height: 100%;
    justify-content: center;
    margin: 0 auto;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    /* background-color: rgb(85, 118, 123); */
}

</style>