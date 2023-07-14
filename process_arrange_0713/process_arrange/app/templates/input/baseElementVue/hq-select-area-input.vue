<template>
  <div style="width: 520px">
    <el-col style="text-align: right" :span="5">
      <div>sku与规格对应关系对象列表:</div>
    </el-col>
    <el-col style="text-align: left" :span="19">
      <div>
        <el-input size="small" placeholder="sku与规格对应关系对象列表(多个搜索词空格分隔)" style="width:240px;margin-left: 10px" clearable v-model="aa"></el-input>
        <el-select size="small" style="width:140px;margin-left: 10px" v-model="aa_query_type">
          <el-option v-for="item in aa_query_type_option" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </div>
    </el-col>
  </div>
</template>
<script>
export default {
  data() {
    return {
      aa: '',
      aa_query_type: 0,
      aa_query_type_option: [
        { value: 0, label:'整个语句'},
        { value: 1, label: '多个搜索词“与”关系' },
        { value: 2, label: '多个搜索词“或”关系' }
      ]
  }
  },
}
</script>
