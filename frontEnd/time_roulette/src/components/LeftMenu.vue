<script setup lang="ts">
import { ref, defineComponent, toRef } from 'vue';

defineComponent({
    name: 'LeftMenu'
});
const props = defineProps({
    activeIndex: {
        type: String,
        required: true
    }
});
const activeIndex = toRef(props,'activeIndex');

const handleSelect = (index: string) => {
    activeIndex.value = index;
    console.log(activeIndex.value);
};
</script>

<template>
    <el-menu class="LeftMenu" :default-active="activeIndex" @select="handleSelect(activeIndex)" router>
        <el-menu-item index="schedule" class="item">
            <el-icon><Calendar /></el-icon>
            <span>日程</span>
        </el-menu-item>
        <el-menu-item index="memo" class="item">
            <el-icon><List /></el-icon>
            <span>代办</span>
        </el-menu-item>
    </el-menu>
</template>

<style scoped>
.LeftMenu {
    min-width: 125px;
    width: 100%;
    height: 100%;
    box-shadow: 0 0 8px #cdd0d6;
    margin-top: 10px;
    margin-left: 30px;
    margin-right: 10px;
    border-radius: 15px;
}

.item {
    text-align: center;
}
</style>
