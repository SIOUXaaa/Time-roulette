
import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
 
const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../pages/login.vue')
  },
  { path: '/', redirect: { name: 'Login' } }
]
 
const router = createRouter({
  history: createWebHashHistory(),
  routes
})
 
export default router
