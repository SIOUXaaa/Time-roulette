<script lang="ts" setup>
import {ElMessage, FormInstance} from 'element-plus';
import { onMounted, reactive, ref, defineComponent } from 'vue'
import registerDiv from './register.vue';
import { useRouter } from 'vue-router'

defineComponent({
    name: 'loginDiv'
});

const router = useRouter();

const activeName = ref("first");
const loginForm = ref({
    account: "",
    password: ""
});
const rules = ref({
    account: [
        { required: true, message: "请输入用户名！", trigger: "blur" },
        { min: 2, max: 12, message: "用户名长度为2-12个字", trigger: "blur" }
    ],
    password: [
        { required: true, message: "请输入密码", trigger: "blur" },
        { min: 6, max: 18, message: "密码长度为6-18位", trigger: "blur" }
    ]
});

const handleClick = () => { }
const handleLogin = () => {
    if (loginForm.value.account === 'test' && loginForm.value.password === '123456') {
                router.push('/index')
            } else {
                ElMessage.error("用户密码错误")
            }
}
const login= ref(null);
onMounted: {
    const handleReset = () => {
    console.log("reset");
    login.value.resetFields()
}
}


// export default ({
//     name: 'loginDiv',
//     data() {
//         return {
//             activeName: "first",
//             loginForm: {
//                 account: "",
//                 password: ""
//             },
//             rules: {
//                 account: [
//                     { required: true, message: "请输入用户名！", trigger: "blur" },
//                     { min: 2, max: 12, message: "用户名长度为2-12个字", trigger: "blur" }
//                 ],
//                 password: [
//                     { required: true, message: "请输入密码", trigger: "blur" },
//                     { min: 6, max: 18, message: "密码长度为6-18位", trigger: "blur" }
//                 ]
//             },

//         }
//     },
//     methods: {
//         // eslint-disable-next-line @typescript-eslint/no-empty-function
//         handleClick() { },
//         handleLogin() {
//             if (this.loginForm.account === 'test' && this.loginForm.password === '123456') {
//                 this.$router.push('/index')
//             } else {
//                 ElMessage.error("用户密码错误")
//             }
//         },
//         handleReset() {
//             console.log("reset");
//             (this.$refs.login as FormInstance).resetFields();
//         }
//     },
//     components: {
//         registerDiv,
//     },
    
// })

</script>

<template>
    <div class="loginDiv">
        <div class="login-form">
            <p>时光轮盘</p>
            <el-tabs v-model="activeName" @tab-click="handleClick" stretch>
                <el-tab-pane label="登录" name="first" class="tab">
                    <el-form ref="login" label-position="left" :rules="rules" :model="loginForm"> <!-- reset要绑定model -->           
                        <el-form-item label="" prop="account">
                            <el-input type="text" v-model="loginForm.account" autocomplete="off" prefix-icon="User"
                                placeholder="请输入用户名" />
                        </el-form-item>
                        <el-form-item label="" prop="password">
                            <el-input type="password" v-model="loginForm.password" autocomplete="off" prefix-icon="Lock"
                                placeholder="请输入密码" />
                        </el-form-item>
                        <el-form-item class="btns">
                            <el-button type="primary" @click="handleLogin">登陆</el-button>
                            <el-button @click="handleReset">重置</el-button>
                        </el-form-item>
                    </el-form>
                </el-tab-pane>
                <el-tab-pane label="注册" name="second" class="tab">
                    <registerDiv />
                </el-tab-pane>
            </el-tabs>
        </div>
    </div>
</template>


<style scoped>
.loginDiv {
    width: 100%;
    height: 100vh;
    background-color: white;
    overflow: auto;
    position: relative;
}

.login-form {
    width: 500px;
    height: 600px;
    left: 78%;
    top: 50%;
    margin: auto 0;
    margin-top: 50px;
    margin-left: 50px;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 0 10px #ddd;
    text-align: center;
}

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

.tab {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>