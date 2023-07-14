<template>
  <div>
    <el-button type="info" style="float:left;" slot="reference" @click="showCodeMsg">源码展示</el-button>
    <el-dialog :visible.sync="showErrorCodeVisible" width='50%'>
      <el-card shadow="hover" class="box-card" style=" max-height: 500px">
        <div class="text item" style="text-align: left; white-space: pre-wrap">
          {{ codeMsgData }}
        </div>
      </el-card>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CodeMsgPopoverView',
  data () {
    return {
      codeMsgData: '',
      showErrorCodeVisible: false
    }
  },
  methods: {
    // 返回码展示
    async showCodeMsg () {
      this.showErrorCodeVisible = true
      if (this.codeMsgData !== '') {
        return
      }
      const { data: result } = await this.$http.get(ALL_CODE_MSG)
      if (result.code == 0 && result.data.length > 0) {
        this.codeMsgData = result.data
      }
    }
  }
}
</script>

<style scoped>
.box-card {
  overflow-y: auto
}
</style>
