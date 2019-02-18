import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from './router';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    docs: [],
  },
  getters: {
    getDocById: state => id => state.docs.find(doc => doc.id === id),
  },
  mutations: {
    setDocs(state, docs) {
      state.docs = docs;
    },
    addDoc(state, newDoc) {
      state.docs.unshift(newDoc);
    },
  },
  actions: {
    fetchDocs({ commit }) {
      axios.get('/docs')
        .then((response) => {
          commit('setDocs', response.data.docs);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    createDoc({ commit }, newDoc) {
      axios.post('/docs/create', {
        title: newDoc.title,
        body: newDoc.body,
      })
        .then((response) => {
          commit('addDoc', response.data.doc);
          router.push('/');
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});
