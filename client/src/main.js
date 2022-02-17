import axios from 'axios';
import VueAxios from 'vue-axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
Vue.prototype.$http = axios;

new Vue({
  router,
  axios,
  VueAxios,
  render: (h) => h(App),
}).$mount('#app');
