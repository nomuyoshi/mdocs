import Vue from 'vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import axios from 'axios';
import Notifications from 'vue-notification';

import router from './router';
import store from './store';
import './filters';
import App from './App.vue';

axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;
axios.defaults.headers.common.Accept = 'application/json';
axios.defaults.headers['Content-Type'] = 'application/json';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

Vue.use(Buefy, {
  defaultIconPack: 'fas',
});
Vue.use(Notifications);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
