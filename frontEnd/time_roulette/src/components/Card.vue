<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import { Delete, Edit } from '@element-plus/icons-vue';
import { cardInfo } from '../pages/schedule.vue';

defineComponent({
    name: 'Card'
});

const props = defineProps({
    card: Object as () => cardInfo,
    deleteCard: Function
});

// const cardId = props.card?.id;
const card = props.card as cardInfo;

const deleteCard = () => {
    if (props.deleteCard !== undefined) props.deleteCard(card);
};

const handleClick = () => {
    console.log(card.id);
};

const handleEdit = () => {};
</script>

<template>
    <transition name="el-zoom-in-top">
        <div class="card">
            <el-button
                class="delete"
                type="danger"
                :icon="Delete"
                circle
                size="small"
                @click="deleteCard"
            />
            <el-button
                class="edit"
                type="primary"
                :icon="Edit"
                circle
                size="small"
                @click="handleEdit"
            />
            <el-card class="box-card" @click="handleClick()">
                <template #header>
                    <div class="card-header">
                        <span>{{ card.id }}</span>
                    </div>
                </template>
                <el-col>
                    <el-row class="details rows">
                        <el-col class="tabs" :span="8">
                            <el-icon><Reading /></el-icon>
                            <span>内容</span>
                        </el-col>
                        <el-col class="contents" :span="16">{{ card.contents }} </el-col>
                    </el-row>
                    <el-row class="address rows">
                        <el-col class="tabs" :span="8">
                            <el-icon><LocationFilled /></el-icon>
                            <span>地点</span>
                        </el-col>
                        <el-col class="contents" :span="16">{{ card.address }}</el-col>
                    </el-row>
                    <el-row class="time rows">
                        <el-col class="tabs" :span="8">
                            <el-icon><Timer /></el-icon>
                            <span>时间</span>
                        </el-col>
                        <el-col class="contents" :span="16">{{ card.time }}</el-col>
                    </el-row>
                </el-col>
            </el-card>
        </div>
    </transition>
</template>

<style scoped>
.card {
    margin: 0 auto;
    position: relative;
}

.delete {
    position: absolute;
    top: 30px;
    right: 30px;
    display: none;
}

.card:hover .delete {
    display: flex;
    z-index: 999;
    cursor: pointer;
}

.edit {
    position: absolute;
    top: 30px;
    left: 25px;
    display: none;
}

.card:hover .edit {
    display: flex;
    z-index: 999;
    cursor: pointer;
}

.box-card {
    max-width: 250px;
    max-height: 400px;
    box-shadow: 0 0 8px #cdd0d6;
    background-color: #ffffff;
    color: #606266;
    border-radius: 35px;
    margin: 15px;
}
.box-card:hover {
    color: #337ecc;
    background-color: #ecf5ff;
}
.rows {
    margin: 3px;
}

.tabs {
    color: #909399;
    min-width: 56px;
}
.box-card:hover .tabs {
    color: #409eff;
}

.contents {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    text-align: left;
    text-overflow: ellipsis;
    -webkit-line-clamp: 8;
    overflow: hidden;
}
</style>
