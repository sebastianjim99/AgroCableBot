import { createRouter, createWebHistory } from 'vue-router'

import Inicio from '../views/InicioView.vue'
import Admin from '../views/AdminView.vue'
import Crear from '../views/CrearView.vue'
import Editar from '../views/EditarView.vue'
import LoginView from '../components/loginView.vue'
import Signup from '../components/signup.vue'

const routes = [
  {path: '/', name: 'inicio', component: Inicio },
  {path: '/loginview', name: 'loginview', component: LoginView},
  {path: '/CrearCuenta', name: 'singnup', component: Signup},
  {path: '/Admin', name: 'Admin', component: Admin},
  {path: '/crear',name: 'Crear', component: Crear },
  {path: '/editar/:id', name: 'Editar', component: Editar, props:true},


  ]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

const protecdRoutes= [
  'Admin'
]

router.beforeEach((to, from, next) => {
  const isProtected = protecdRoutes.includes(to.name);
  if(isProtected && !localStorage.getItem('token')){
    next({
      path:'/',
      query: {redirect: to.fullpath}
    })
  }else{
    if (!isProtected && localStorage.getItem('token') && (to.name == 'loginview' || to.name == 'Signup')){
      next({
        path: '/Admin'
      })
    }else{
      next();
    }
  }
})

export default router
