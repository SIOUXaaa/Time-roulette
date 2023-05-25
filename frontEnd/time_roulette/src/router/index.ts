
import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import store from '../store';

const routes: Array<RouteRecordRaw> = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('../pages/login.vue')
    },
    {
        path: '/schedule',
        name: 'schedule',
        component: () => import('../pages/schedule.vue'),
        meta: {
            requiresAuth: true, // 需要身份验证
        }
    },
    {
        path: '/memo',
        name: 'memo',
        component: () => import('../pages/memo.vue'),
        meta: {
            requiresAuth: true, // 需要身份验证
        }
    },
    {
        path: '/test',
        name: 'test',
        component: () => import('../pages/test.vue'),
        meta: {
            requiresAuth: true, // 需要身份验证
        }
    },
    {
        path: '/', redirect: { name: 'Login' },
        meta: {
            requiresAuth: true, // 需要身份验证
        }
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth) {
        // 检查用户是否已经登录
        if (store.state.login_success) {
            next();
        } else {
            // 未登录，重定向到登录页面
            next('/login');
        }
    } else {
        next();
    }
});

export default router
