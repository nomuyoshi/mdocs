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
  },
  actions: {
    fetchDocs({ commit }) {
      httpClient.get('/docs')
        .then((response) => {
          commit('setDocs', response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});
