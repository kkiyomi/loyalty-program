import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('/src/views/Home.vue'),
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('/src/views/Dashboard.vue'),
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
