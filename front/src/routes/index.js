import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/login', 
        name: 'Login',
        component: () => import('@/views/Login.vue')
    },
    {
        path: '/client.apk', 
        name: 'Apk',
        component: () => import('@/views/Apk.vue')
    },
    {
        path: '/', 
        name: 'Board', 
        component: () => import('@/views/Board.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    const publicUrl = ['/login', '/client.apk']
    const auth_req = !publicUrl.includes(to.path)
    const token = localStorage.getItem('token')

    if (auth_req && !token)
        next('/login')
    else
        next()
})

export default router