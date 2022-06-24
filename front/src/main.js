import Vue from 'vue'
import App from './App.vue'

import router from '@/routes/index.js'
import store from '@/assets/script/store.js'

import GoogleSignInButton from 'vue-google-signin-button-directive'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  GoogleSignInButton,
  render: h => h(App),
}).$mount('#app')
