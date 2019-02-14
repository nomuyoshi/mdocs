import axios from 'axios';
import * as Cookie from 'js-cookie';

const httpClient = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
  headers: { 'X-CSRFToken': Cookies.get('csrftoken') },
});

httpClient.defaults.headers.common.Accept = 'application/json';
httpClient.defaults.headers.post['Content-Type'] = 'application/json';
export default httpClient;
