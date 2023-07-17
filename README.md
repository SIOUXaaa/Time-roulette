# Time-roulette
szu数据库系统大作业
基于vue3 element-plus django的前后端分离项目
## 1.front end
##### 安装工具
```
    cd ./frontEnd/time_roulette/
    npm install vue
    npm install element-plus --save-dev
    npm install typescript --save-dev
    npm install vue @types/vue --save-dev
    npm install @element-plus/icons-vue
    npm install vue-router@4
    npm install vuex 
    npm install axios
    npm install js-md5 --save
    npm i --save jsencrypt


```
有些依赖忘记记录了，啥报错就装啥
##### 启动
###### 前端启动
```
    
    cd ./frontEnd/time_roulette/
    npm install
    npm run dev
    如果端口冲突 就npm run dev -- --port + 不冲突端口

```

###### 后端启动
```
    cd ./backEnd/
    python manage.py runserver 0.0.0.0:8000或者 127.0.0.1:8000
```








