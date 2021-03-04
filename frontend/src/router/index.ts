import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'root',
    component: () => import (/* webpackChunkName: "shoppingList" */ '../views/ShoppingList.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'default',
    component: () => import (/* webpackChunkName: "shoppingList" */ '../views/ShoppingList.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
