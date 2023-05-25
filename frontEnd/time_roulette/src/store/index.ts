import { createStore } from 'vuex'
import axios from 'axios';

export default createStore({
    state: {
        id: "",
        username: "",
        login_success: false
    },
    mutations: {
        SET_LOGIN_STATE(state, login_success) {
            state.login_success = login_success;
        },
        SET_USER(state, username) {
            state.username = username;
        },
        SET_ID(state, id) {
            state.id = id
        },
    },
    actions: {
        login({ commit }, credentials) {
            return new Promise<void>((resolve, reject) => {
                axios.post('user/login/', credentials)
                    .then(response => {
                        if (response.data.login_success === true) {
                            commit('SET_LOGIN_STATE', true);
                            commit('SET_USER', response.data.name);
                            commit('SET_ID', response.data.id);
                            resolve(); // 登录成功，resolve promise
                        } else {
                            reject(new Error('密码错误')); // 登录失败，reject promise，并传递错误信息
                        }
                    })
                    .catch(error => {
                        console.error(error);
                        reject(error); // 捕获axios请求错误，并reject promise
                    });
            });
        },
        register({ commit }, credentials) {
            return new Promise<void>((resolve, reject) => {
                axios.post('user/register/', credentials).then(response => {
                    if (response.status === 201) {
                        console.log("注册成功");
                        resolve();
                    } else {
                        reject(new Error('注册失败，请检查输入是否合法'));
                    }
                }).catch(error => {
                    console.log(error);
                    reject(error);
                })
            })
        },
        quit({ commit }) {
            commit('SET_LOGIN_STATE', false);
            commit('SET_USER', "");
            commit('SET_ID', "");
        }
    },
    modules: {
    }
})

