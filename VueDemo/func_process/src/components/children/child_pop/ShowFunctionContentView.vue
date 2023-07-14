<template>
  <el-dialog
    :visible.sync="showFunctionContent.functionContentVisible" width='75%'>
    <el-card class="box-card">
      <div class="text item" style="text-align: left; white-space: pre-wrap">
        <div v-if="showFunctionContent.url" style="font-weight: bold">路径：{{ showFunctionContent.url }}</div>
        <div style="font-weight: bold">代码：</div>
        <pre style="font-size: 16px !important; max-width: 100%; overflow: auto;">{{ showFunctionContent.functionContent }}</pre>
      </div>
    </el-card>
  </el-dialog>
</template>

<script>
export default {
  name: 'ShowFunctionContentView',
  props: {
    showFunctionContent: { type: Object, require: true }
  }
}
</script>

<style scoped>
.box-card {
  overflow-y: auto
}
</style>
