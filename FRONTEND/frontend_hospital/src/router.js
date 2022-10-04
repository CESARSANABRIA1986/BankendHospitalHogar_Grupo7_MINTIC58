import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'

import LogIn from './components/LogIn.vue'
import Home from './components/Home.vue'
import SignUp from './components/registro.vue'


const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },

  {
    path: '/usuario/ingreso',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/usuario/Home',
    name: 'home',
    component: Home
  },
  {
    path: '/usuario/registro',
    name: 'SignUp',
    component: SignUp
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
