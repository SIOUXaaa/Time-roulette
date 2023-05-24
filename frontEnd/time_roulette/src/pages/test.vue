<script lang="ts" setup>
import card from '../components/Card.vue';
import CardDetails from '../components/CardDetails.vue';
import MemoItem from '../components/MemoItem.vue';
import MemoDetails from '../components/MemoDetails.vue';

const memo = {
    id: 1,
    contents: '今天要吃饭',
    done: false,
    reminded: false,
    time: '2000-1-1 0:0:0'
};
</script>

<template>
    <!-- <CardDetails /> -->
    <!-- <MemoItem /> -->
    <MemoDetails :memo="memo" :visible="true" :updateMemo="void"/>
</template>

<style scoped></style>
