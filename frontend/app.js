const routes=[
    {path:'/home',component:home},
    {path:'/employee',component:employee},
    {path:'/department',component:department},
]

const router=new VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes, // short for `routes: routes`
    });

const app = Vue.createApp({})
// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router)

app.mount('#app')
