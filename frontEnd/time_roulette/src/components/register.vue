<script lang="ts">
import { FormInstance } from 'element-plus';

export default ({
    name: "registerDiv",
    data() {
        return {
            activeName: "second",
            registerForm: {
                account: "",
                password: "",
                checkPassword: ""
            },
            rules: {
                account: [
                    { required: true, message: "请输入用户名！", trigger: "blur" },
                    { min: 2, max: 12, message: "用户名长度为2-12个字", trigger: "blur" }
                ],
                password: [
                    { required: true, message: "请输入密码", trigger: "blur" },
                    { min: 6, max: 18, message: "密码长度为6-18位", trigger: "blur" }
                ],
                checkPassword: [
                    { required: true, message: "请再次输入密码", trigger: "blur" }，
                    {
                        validate: (rule: any, value: any, callback: any) => {
                            if (value !== registerForm.password) {
                                callback(new Error("两次输入的密码不一致"))
                            } else {
                                
                            }
                        },

                    }
                ]
            }
        }
    },
    methods: {
        handlePass() {
            (this.$refs.login as FormInstance).validate((valid: any) => {
                if (valid) {
                    
                }
            }, this.registerForm.password);
        },
        handleRegister() {

        },

    }
})
</script>

<template>
    <el-form label-position="left" :model="registerForm">
        <el-form-item label="" prop="account">
            <el-input type="text" v-model="registerForm.account" autocomplete="off" prefix-icon="User"
                placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="" prop="password">
            <el-input type="password" v-model="registerForm.password" autocomplete="off" prefix-icon="Lock"
                placeholder="请输入密码" />
        </el-form-item>
        <el-form-item label="" prop="checkPassword">
            <el-input type="password" v-model="registerForm.checkPassword" autocomplete="off" prefix-icon="Lock"
                placeholder="请重新输入密码" />
        </el-form-item>
        <el-form-item class="btns">
            <el-button type="primary" @click="void (0)">注册</el-button>
            <el-button @click="void (0)">重置</el-button>
        </el-form-item>
    </el-form>
</template>

<style scoped>
:deep .el-form-item__content {
    flex: none !important;
}

.btns {
    display: flex;
    align-content: center;
    flex: none !important;
    justify-content: center;
    font-weight: 600;
}
</style>