import Vue from 'vue';
import Router from 'vue-router';
import DocList from './components/DocList.vue';
import DocEditor from './components/DocEditor.vue';
import DocDetail from './components/DocDetail.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: '/',
  routes: [
    {
      path: '/',
      name: 'root',
      component: DocList,
    },
    {
      path: '/docs',
      name: 'doc-list',
      component: DocList,
    },
    {
      path: '/docs/new',
      name: 'doc-new',
      component: DocEditor,
    },
    {
      path: '/docs/:id(\\d+)',
      name: 'doc-detail',
      component: DocDetail,
    },
    {
      path: '/docs/:id(\\d+)/edit',
      name: 'doc-edit',
      component: DocEditor,
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
