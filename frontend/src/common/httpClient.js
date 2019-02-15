import axios from 'axios';
import * as Cookies from 'js-cookie';

console.log(Cookies.get('csrftoken'));
const httpClient = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
  headers: { 'X-CSRFToken': Cookies.get('csrftoken') },
});

httpClient.defaults.headers.common.Accept = 'application/json';
httpClient.defaults.headers.post['Content-Type'] = 'application/json';
export default httpClient;
