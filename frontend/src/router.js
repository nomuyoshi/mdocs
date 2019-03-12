import Vue from 'vue';
import Router from 'vue-router';
import DocListView from './views/DocListView.vue';
import DocEditorView from './views/DocEditorView.vue';
import DocDetailView from './views/DocDetailView.vue';
import NotFoundView from './views/NotFoundView.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: '/',
  routes: [
    {
      path: '/',
      name: 'root',
      component: DocListView,
      props: true,
    },
    {
      path: '/docs',
      name: 'doc-list',
      component: DocListView,
      props: true,
    },
    {
      path: '/docs/new',
      name: 'doc-new',
      component: DocEditorView,
    },
    {
      path: '/docs/:id(\\d+)',
      name: 'doc-detail',
      component: DocDetailView,
    },
    {
      path: '/docs/:id(\\d+)/edit',
      name: 'doc-edit',
      component: DocEditorView,
    },
    {
      path: '*',
      name: 'not-found',
      component: NotFoundView,
    },
  ],
});
