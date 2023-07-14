import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
// import './api/api.js'
import './api/api_local.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import SuperFlow from 'vue-super-flow'
import 'vue-super-flow/lib/index.css'
import './assets/css/global.css'
import less from 'less'
import router from './router'


Vue.use(SuperFlow)
Vue.use(ElementUI)
Vue.use(less)

Vue.prototype.$message = ElementUI.Message // $message：自定义属性； Message上面导入的组件
Vue.prototype.$confirm = ElementUI.MessageBox.confirm // $message：自定义属性； Message上面导入的组件
Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  render: h => h(App)
}).$mount('#app')
