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
    },
    {
        path: '/promo/:promo_uid',
        name: 'test',
        component: () => import('/src/views/Promo.vue'),
    },
    {
        path: '/code/:promo_suid',
        name: 'Code',
        component: () => import('/src/views/Code.vue'),
    },
    {
        path: '/instance/:pinstance_uid',
        name: 'PromoInstance',
        component: () => import('/src/views/PromoInstance.vue'),
    },
    {
        path: '/settings',
        name: 'Settings',
        component: () => import('/src/views/Settings.vue'),
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
