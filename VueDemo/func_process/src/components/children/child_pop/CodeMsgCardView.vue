<template>
  <el-col :span="12">
    <el-card shadow="hover" class="box-card" style=" max-height: 500px">
      <el-table :data="errorCodeList" max-height="400" stripe border>
        <el-table-column width="150" property="name" label="变量名"></el-table-column>
        <el-table-column width="70" property="code" label="code"></el-table-column>
        <el-table-column width="180" property="msg" label="msg"></el-table-column>
      </el-table>
    </el-card>
  </el-col>
</template>

<script>
export default {
  name: 'CodeMsgCardView',
  props: {
    errorCodeList: { type: Array, require: true }
  }
}
</script>

<style scoped>
.box-card {
  overflow-y: auto
}
</style>
