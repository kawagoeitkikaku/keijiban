import Vue from 'vue'
import Router from 'vue-router'

import keijiban from '@/components/keijiban'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: keijiban
    },
    {
      path: '/keijiban',
      component: keijiban
    }
  ]
})