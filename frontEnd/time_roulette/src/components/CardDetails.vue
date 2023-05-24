<script setup lang="ts">
import { defineComponent, ref, toRef, watch, toRefs } from 'vue';
import { cardInfo } from '../pages/schedule.vue';
import { Check, Delete } from '@element-plus/icons-vue';
import { useDateFormat } from '@vueuse/shared';

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
    visible: Boolean
});
const cardDefault: cardInfo = {
    id: -1,
    title: '',
    time: '',
    address: '',
    contents: ''
};
const time = ref('');
// const card = toRef(props, 'card');
let tempCard = ref(cardDefault);
// const tempCardRef = ref(tempCard);

const visible = toRef(props, 'visible');

const handleEdit = () => {
    // tempCardRef.value.time = time.value;
    // console.log(time.value.toString());
    // card.value = tempCard.value;
    tempCard.value.time = time.value;
    props.updateCard(tempCard.value);
};

const handleCancel = () => {
    // card.value = cardDefault;
    tempCard.value = cardDefault;
};

watch(
    () => props.visible,
    newValue => {
        if (newValue) {
            tempCard.value = JSON.parse(JSON.stringify(props.card));
            // console.log(tempCard);
        } else {
            tempCard.value = cardDefault;
        }
    }
);
</script>

<template>
    <el-dialog v-model="visible" align-center class="dialog">
        <el-form class="form">
            <el-form-item label="标题">
                <el-input
                    type="text"
                    v-model="tempCard.title"
                    placeholder="输入标题谢谢喵"
                    clearable
                />
            </el-form-item>
            <el-form-item label="内容">
                <el-input
                    type="textarea"
                    v-model="tempCard.contents"
                    placeholder="输入日程内容谢谢喵"
                    clearable
                />
            </el-form-item>
            <el-form-item label="地点">
                <el-input
                    type="text"
                    v-model="tempCard.address"
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
                    value-format="YYYY-MM-DD hh:mm:ss"
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
