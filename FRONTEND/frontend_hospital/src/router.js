import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'

import logIn from './components/LogIn.vue'
import home from './components/Home.vue'
import signUp from './components/registro.vue'


const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },

  {
    path: '/usuario/ingreso',
    name: 'logIn',
    component: logIn
  },
  {
    path: '/usuario/Home',
    name: 'home',
    component: home
  },
  {
    path: '/usuario/registro',
    name: 'signUp',
    component: signUp
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
