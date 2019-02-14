import Vue from 'vue';
import Router from 'vue-router';
import DocList from './components/DocList.vue';
import CreateDoc from './components/CreateDoc.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'doc-list',
      component: DocList,
    },
    {
      path: '/docs/new',
      component: CreateDoc,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
  ],
});
