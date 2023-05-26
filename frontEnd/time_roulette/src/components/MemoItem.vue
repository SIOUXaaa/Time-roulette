<script setup lang="ts">
import { defineComponent, ref, toRef, watch } from 'vue';
import { memoInfo } from '../pages/memo.vue';

defineComponent({
    name: 'MemoItem'
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
    updateDone: {
        type: Function,
        required: true
    }
});

const memoRef = toRef(props, 'memo');

watch(
    () => props.memo.done,
    newValue => {
        setTimeout(() => {
            props.updateDone(memoRef.value);
        }, 250);
        // props.updateDone(memoRef.value);
    }
);
</script>

<template>
    <el-checkbox class="memo" v-model="memo.done" :label="memo.contents" size="large" border />
</template>

<style scoped>
.memo {
    width: 80%;
    height: 50px;
    margin: 20px;
}
</style>
