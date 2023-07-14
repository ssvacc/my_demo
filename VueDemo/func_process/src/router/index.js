import Vue from 'vue'
import VueRouter from 'vue-router'
import AxiosPlugin from 'vue-axios-cors'
import ProcessFunction from '@/components/children/ProcessFunction.vue'


Vue.use(AxiosPlugin)

Vue.use(VueRouter)

const routes = [
  {
    path: '/admin/messageCenter/:value',
    name: 'ProcessFunction',
    component: ProcessFunction
  }
]

const router = new VueRouter({
  routes
})

export default router
