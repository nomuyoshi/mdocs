import Vue from 'vue';
import Vuex from 'vuex';
import httpClient from './common/httpClient';

Vue.use(Vuex);

console.log(httpClient.defaults.baseURL);

export default new Vuex.Store({
  state: {
    docs: [],
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
      httpClient.get('/docs')
        .then((response) => {
          commit('setDocs', response.data.docs);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    createDoc({ commit }, newDoc) {
      httpClient.post('/docs/create', {
        title: newDoc.title,
        body: newDoc.body,
      })
        .then((response) => {
          commit('addDoc', response.data.doc);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});
