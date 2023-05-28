<script setup lang="ts">
import { ref, defineComponent, watch, toRef } from 'vue';
import { Check, Delete } from '@element-plus/icons-vue';
import { memoInfo } from '../pages/memo.vue';

defineComponent({
    name: 'MemoDetails'
});

const props = defineProps({
    memo: {
        type: Object as () => memoInfo,
        required: true
    },
    updateMemo: {
        type: Function,
        required: true
    },
    visible: Boolean
});

const memoDefault: memoInfo = {
    id: -1,
    contents: '',
    done: false,
    reminded: false,
    time: ''
};

const visible = toRef(props, 'visible');
const memoRef = toRef(props, 'memo');
const remain = ref(false);
const remainContents = ref('否');
const time = ref('');
const tempMemo = ref(memoDefault);

watch(remain, newValue => {
    remainContents.value = newValue ? '是' : '否';
});

// watch(() => props.visible, newValue => {
//     if (newValue) {
//         tempMemo.value = JSON.parse(JSON.stringify(props.memo));
//     }
//     else {
//         tempMemo.value = memoDefault;
//     }
// });

const addMemo = () => {
    if (remain.value) {
        tempMemo.value.time = time.value;
    }
    // console.log(tempMemo.value);
    props.updateMemo(tempMemo.value)
}
</script>

<template>
    <el-dialog v-model="visible" align-center class="dialog">
        <el-form>
            <el-form-item label="内容">
                <el-input
                    type="text"
                    placeholder="输入代办事项"
                    clearable
                    v-model="tempMemo.contents"
                />
            </el-form-item>
            <!-- <el-form-item label="提醒">
                <el-switch v-model="remain" :label="remainContents" />
            </el-form-item>
            <transition name="el-zoom-in-top">
                <el-form-item v-show="remain" label="时间">
                    <el-date-picker
                        v-model="time"
                        type="datetime"
                        placeholder="选择提醒时间"
                        value-format="YYYY-MM-DD hh:mm:ss"
                    />
                </el-form-item> -->
            <!-- </transition> -->
            <el-form-item>
                <el-row justify-content="center" class="buttons">
                    <el-col :span="6" :offset="6">
                        <el-button type="success" @click="addMemo" :icon="Check" />
                    </el-col>
                    <el-col :span="6">
                        <el-button type="danger" @click="" :icon="Delete" />
                    </el-col>
                </el-row>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<style scoped>
.buttons {
    width: 100%;
}
</style>

<style>
.dialog {
    border-radius: 25px;
}
</style>
