import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/Index'
import Category from '@/components/Category'
import Subject from '@/components/Subject'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'Index',
    component: Index
  }, {
    path: '/cotegory/:id',
    name: 'Category',
    component: Category
  }, {
    path: '/:id',
    name: 'Subject',
    component: Subject
  }]
})
