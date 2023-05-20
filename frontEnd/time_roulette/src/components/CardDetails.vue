<script setup lang="ts">
import { defineComponent, ref, toRefs } from 'vue';
import { cardInfo } from '../pages/schedule.vue';
import { Check, Delete } from '@element-plus/icons-vue';

defineComponent({
    name: 'CardDetail'
});

const props = defineProps({
    card: {
        type: Object as () => cardInfo,
        required: true
    },
    updateCard: {
        type: Function,
        required: true
    },
    visible: {
        type: Boolean,
        required: true
    }
});
const time = ref('2023-1-1 0:0:0');
const card = ref({ ...props.card });

const visible = ref(false);

const handleEdit = () => {
    props.updateCard(card.value);
    visible.value = false;
};

const handleCancel = () => {
    card.value = {
        id: -1,
        title: '',
        time: '',
        address: '',
        contents: ''
    };
};
</script>

<template>
    <el-dialog v-model="visible" align-center class="dialog">
        <el-form class="form" :model="card">
            <el-form-item label="标题">
                <el-input type="text" v-model="card.title" placeholder="输入标题谢谢喵" clearable />
            </el-form-item>
            <el-form-item label="内容">
                <el-input
                    type="text"
                    v-model="card.contents"
                    placeholder="输入日程内容谢谢喵"
                    clearable
                />
            </el-form-item>
            <el-form-item label="地点">
                <el-input
                    type="text"
                    v-model="card.address"
                    placeholder="输入日程地点谢谢喵"
                    clearable
                />
            </el-form-item>
            <el-form-item label="时间">
                <el-date-picker
                    v-model="time"
                    type="datetime"
                    placeholder="选择时间谢谢喵"
                    class="selectTime"
                />
            </el-form-item>

            <el-form-item>
                <el-row class="button" justify-content="center">
                    <el-col :span="6" :offset="6">
                        <el-button type="success" @click="handleEdit" :icon="Check">完成</el-button>
                    </el-col>
                    <el-col :span="6">
                        <el-button type="danger" @click="handleCancel" :icon="Delete"
                            >重置</el-button
                        >
                    </el-col>
                </el-row>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<style scoped>
.button {
    width: 100%;
}
.selectTime {
    width: 100%;
}
</style>

<style>
.dialog {
    border-radius: 25px;
}
</style>
