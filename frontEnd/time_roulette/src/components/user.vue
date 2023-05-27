<script setup lang="ts">
import { ref, toRefs, defineComponent, reactive, onMounted } from 'vue';
import { ElMessage } from 'element-plus';
import type { UploadProps } from 'element-plus';
import store from '../store';
import axios from 'axios';

defineComponent({
    name: 'user'
});
const props = defineProps({
    visible: Boolean
});

const { visible } = toRefs(props);
const changePass = ref(false);
const password = ref('');
const newPassword = ref('');
const passwordCheck = ref('');
const postURL = 'http://127.0.0.1:8000/user/upload/avatar/' + store.state.id;
const { avatar, username, id, login_success } = toRefs(store.state);
const newUserName = ref('')
const handleAvatarSuccess: UploadProps['onSuccess'] = (response, uploadFile) => {
    // avatar.value = URL.createObjectURL(uploadFile.raw!);
    // imageUrl.value = response.data.file_path;
    store.dispatch('getAvatar').catch(error => {
        ElMessage.error(error.message);
    });
};

const beforeAvatarUpload: UploadProps['beforeUpload'] = rawFile => {
    if (rawFile.type !== 'image/jpeg') {
        ElMessage.error('Avatar picture must be JPG format!');
        return false;
    } else if (rawFile.size / 1024 / 1024 > 2) {
        ElMessage.error('Avatar picture size can not exceed 2MB!');
        return false;
    }
    return true;
};

const handleChange = () => {
    axios
        .put('user/update/username/' + id.value, {
            username: newUserName.value
        })
        .then(() => {
            ElMessage.success('更改昵称成功');
        })
        .catch(error => {
            ElMessage.error(error.response.data.msg);
        });
    if (changePass.value) {
        axios
            .put('user/update/password/' + id.value, {
                password: password.value,
                newPassword: newPassword.value
            })
            .then(() => {
                ElMessage.success('更改密码成功');
            }).catch(error => {
                ElMessage.error(error.response.data.msg);
            });
    }
};

const uploadAvatar = () => {};
</script>

<template>
    <el-dialog v-model="visible" title="个人信息" class="dialog" style="width: 350px">
        <el-col>
            <el-row>
                <el-col @click="uploadAvatar">
                    <el-upload
                        :action="postURL"
                        :show-file-list="false"
                        :on-success="handleAvatarSuccess"
                        :before-upload="beforeAvatarUpload"
                    >
                        <img
                            v-if="avatar"
                            :src="'http://127.0.0.1:8000' + avatar"
                            class="avatar"
                            style="
                                background-color: #cdd0d6;
                                border-radius: 99%;
                                width: 75px;
                                height: 75px;
                            "
                        />
                        <el-icon
                            v-else
                            class="avatar-uploader-icon"
                            :size="25"
                            style="
                                background-color: #cdd0d6;
                                border-radius: 99%;
                                width: 75px;
                                height: 75px;
                            "
                            ><Plus
                        /></el-icon>
                    </el-upload>
                </el-col>
            </el-row>
            <!-- <el-row>
                <el-col>
                    <span>{{ username }}</span>
                </el-col>
            </el-row> -->

            <el-form label-position="top">
                <el-form-item label="昵称">
                    <el-input
                        type="text"
                        v-model="newUserName"
                        :placeholder="username"
                        prefix-icon="User"
                        clearable
                    />
                </el-form-item>
                <el-form-item>
                    <span style="margin-right: 10px">修改密码</span>
                    <el-switch v-model="changePass"></el-switch>
                </el-form-item>
                <transition name="el-zoom-in-top">
                    <el-col v-show="changePass">
                        <el-form-item>
                            <el-input
                                type="password"
                                v-model="password"
                                autocomplete="off"
                                prefix-icon="Lock"
                                placeholder="请输入当前密码"
                                show-password
                            />
                        </el-form-item>
                        <el-form-item>
                            <el-input
                                type="password"
                                v-model="newPassword"
                                autocomplete="off"
                                prefix-icon="Lock"
                                placeholder="请输入新密码"
                                show-password
                            />
                        </el-form-item>
                        <el-form-item>
                            <el-input
                                type="password"
                                v-model="passwordCheck"
                                autocomplete="off"
                                prefix-icon="Lock"
                                placeholder="请再次输入新密码"
                                show-password
                            />
                        </el-form-item>
                    </el-col>
                </transition>

                <el-row>
                    <el-col>
                        <el-button type="primary" @click="handleChange">保存</el-button>
                    </el-col>
                </el-row>
            </el-form>
        </el-col>
    </el-dialog>
</template>

<style scoped></style>
