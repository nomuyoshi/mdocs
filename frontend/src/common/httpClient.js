import axios from 'axios';

const httpClient = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
});

httpClient.defaults.headers.common.Accept = 'application/json';
httpClient.defaults.headers.post['Content-Type'] = 'application/json';
export default httpClient;
