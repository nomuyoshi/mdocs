import Vue from 'vue';
import Router from 'vue-router';
import DocList from './components/DocList.vue';
import DocEditor from './components/DocEditor.vue';
import DocDetail from './components/DocDetail.vue';
import NotFound from './components/NotFound.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: '/',
  routes: [
    {
      path: '/',
      name: 'root',
      component: DocList,
      props: true,
    },
    {
      path: '/docs',
      name: 'doc-list',
      component: DocList,
      props: true,
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
      path: '*',
      name: 'not-found',
      component: NotFound,
    },
  ],
});
