
// const baseURL = 'http://106.15.224.155:10065'
const baseURL = 'http://172.26.9.103:8010'
// var baseURL = 'http://172.26.9.36:8010/'

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/static/js/func_process',
  outputDir: 'dist/func_process',
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: baseURL,
    port: 8082
  }
})
