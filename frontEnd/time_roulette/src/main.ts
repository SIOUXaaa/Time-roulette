import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import router from './router'
import { ElCollapseTransition } from 'element-plus'
import axios from 'axios';
import store from './store'


const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.component(ElCollapseTransition.name, ElCollapseTransition)
app.use(ElementPlus)
app.use(router)
app.use(store)
app.mount('#app')

axios.defaults.baseURL = store.state.url;
app.config.globalProperties.$http = axios;
