import { createRouter, createWebHistory } from 'vue-router'


import Inicio from '../views/InicioView.vue'
import Admin from '../views/AdminView.vue'
import Crear from '../views/CrearView.vue'
import Editar from '../views/EditarView.vue'

const routes = [
  { path: '/Imacuna', name: 'inicio', component: Inicio },
  {path: '/Admin', name: 'Admin', component: Admin},
  {path: '/crear',name: 'Crear', component: Crear },
  {path: '/editar/:id', name: 'Editar', component: Editar, props:true},



  ]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
