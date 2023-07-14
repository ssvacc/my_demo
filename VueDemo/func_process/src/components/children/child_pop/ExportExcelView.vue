<template>
  <div>
    <el-button v-if="request_type === 'GET'" @click="exportExcelGET(request_url, request_param)" type="primary">导出</el-button>
    <el-button v-if="request_type === 'POST'" @click="exportExcelPOST(request_url, request_param)" type="primary">导出</el-button>
    <el-button v-if="request_type === 'DOWNOLAD'" @click="downloadExcel(request_url, filename)" type="primary">导出</el-button>
  </div>
</template>

<script>
export default {
  // 调用接口直接导出excel组件
  name: 'exportExcelView',
  props: {
    request_type: { type: String, require: true },
    request_url: { type: String, require: true },
    request_param: { type: String, require: false },
    filename: { type: String, require: false }
  },
  methods: {
    // 导出
    exportExcelGET (url, param) {
      if (param) {
        url += param
      }
      this.$http
        .get(url, { responseType: 'blob' })
        .then((res) => {
          const blob = res.data
          const a = document.createElement('a')
          // 由于后台返回文件名称是通过response返回的
          // 因此需要从response headers中content-disposition响应头中获取文件名称fileName，如上图所示
          const headers = res.headers
          let fileName = headers['content-disposition']
          fileName = fileName.split('=')[1]
          // download是a标签的一个属性，可以自定义文件名称
          a.download = fileName
          a.href = URL.createObjectURL(blob)
          document.body.appendChild(a)
          a.click()
          document.body.removeChild(a)
        })
    },
    // 导出，post请求未开发
    exportExcelPOST (url, param) {

    },
    // 根据配置的链接，从OSS下载已生成的excel
    downloadExcel (url, filename) {
      console.log('download')
      const a = document.createElement('a')
      a.href = url
      a.download = filename // 下载后文件名
      a.style.display = 'none'
      document.body.appendChild(a)
      a.click() // 点击下载
      document.body.removeChild(a) // 下载完成移除元素
    }
  }
}
</script>
