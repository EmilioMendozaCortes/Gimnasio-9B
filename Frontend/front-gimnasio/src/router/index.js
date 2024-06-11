import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/Login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
import MenuView from '../components/Menu.vue'
import dashboardView from '../components/dashboard.vue'
import UsuarioView from '../components/Usuario.vue'
import PersonaView from '../components/Persona.vue'
import HomeView from '../components/Home.vue'
import DietaView from '../components/Dietas.vue'
import IndicadorNView from '../components/IndicasdorN.vue'
import PreguntaNView from '../components/PreguntaN.vue'
import ValoracionNView from '../components/ValoracionN.vue'

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
      path: '/menu',
      name: 'dashboard',
      component: dashboardView,
      children:[
        {path: '/personas', name: 'personas', component:PersonaView},
        {path: '/home', name: 'home', component:HomeView},
        {path: '/dieta', name: 'dieta', component:DietaView},
        {path: '/indicadorNutricional', name: 'indicadorNutricional', component:IndicadorNView},
        {path: '/preguntaNutricional', name: 'preguntaNutricional', component:PreguntaNView},
        {path: '/valoracionNutricional', name: 'valoracionNutricional', component:ValoracionNView}
      ]
    },
    // {
    //   path: '/usuario',
    //   name: 'usuario',
    //   component: UsuarioView
    // },
    // {
    //   path: '/persona',
    //   name: 'persona',
    //   component: PersonaView
    // },
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
