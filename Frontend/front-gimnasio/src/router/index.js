import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/Login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
import MenuView from '../components/Menu.vue'
import dashboardView from '../components/dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboardView
    },
    {
      path: '/menu',
      name: 'menu',
      component: MenuView
    },
    {
      path: '/page/:sectionSlug',
      name: 'dynamicContent',
      // route level code-splitting
      // this generates a separate chunk (dynamicContent.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "dynamicContent" */ '../views/DynamicContent.vue')
    },
  ]
})

export default router
