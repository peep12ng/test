import { createRouter, createWebHistory } from 'vue-router'
import Test from '../components/Test.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router