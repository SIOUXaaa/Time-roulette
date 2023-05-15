
import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('../pages/login.vue')
    },
    {
        path: '/schedule',
        name: 'schedule',
        component: ()=> import('../pages/schedule.vue')
    },
    {
        path: '/memo',
        name: 'memo',
        component: ()=>import('../pages/memo.vue')
    },
    { path: '/', redirect: { name: 'Login' } }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
