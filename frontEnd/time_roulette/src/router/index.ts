
import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('../pages/login.vue')
    },
    {
        path: '/index',
        name: 'index',
        component: ()=> import('../pages/index.vue')
    },
    { path: '/', redirect: { name: 'Login' } }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
