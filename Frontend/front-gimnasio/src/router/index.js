import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/Login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
import MenuView from '../components/Menu.vue'
import dashboardView from '../components/dashboard.vue'
import PersonaView from '../components/Usuario.vue'
import UsuarioView from '../components/Persona.vue'

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
      component: RegisterUserView,
      children:[
        {path: '/personas', name: 'personas', component:RegisterUserView},
      ]
    },
    {
      path: '/menu',
      name: 'dashboard',
      component: dashboardView,
      children:[
        {path: '/personas', name: 'personas', component:RegisterUserView},
      ]
    },
    {
      path: '/usuario',
      name: 'usuario',
      component: UsuarioView
    },
    {
      path: '/persona',
      name: 'persona',
      component: PersonaView
    },
    {
      path: '/menuMalo',
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
