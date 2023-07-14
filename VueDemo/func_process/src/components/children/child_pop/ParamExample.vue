<template>
  <span>
    <el-button type="warning" @click="openExampleForm">参数示例</el-button>
    <el-dialog title="参数示例" append-to-body
               :visible.sync="paramExampleFormVisible" width='40%'
               @close="closeForm">
      <el-form id="paramExampleForm" ref="paramExampleFormRef">
        <template>
          <div v-for="item in param_example_list">
            <el-form-item :label="item.param_name" :label-width="formLabelWidth">
              <el-input-number v-if="item.data_type === 1" controls-position="right" style="width: 70%"
                               v-model="item.example" placeholder="请输入示例值" autocomplete="off">
              </el-input-number>
              <el-input-number v-if="item.data_type === 2" controls-position="right" style="width: 70%"
                               v-model="item.example" placeholder="请输入示例值" autocomplete="off">
              </el-input-number>
              <el-select v-if="item.data_type === 3" v-model="item.example" style="width: 70%">
                <el-option label="True" value="True"></el-option>
                <el-option label="False" value="False"></el-option>
              </el-select>
              <el-input type="textarea" v-if="item.data_type === 4" style="width: 70%"
                        :autosize="{ minRows: 1, maxRows: 5}"
                        v-model="item.example" placeholder="请输入示例值" autocomplete="off"></el-input>
              <el-date-picker value-format="yyyy-MM-dd"
                              v-if="item.data_type === 5"
                              v-model="item.example"
                              type="date"
                              placeholder="选择日期">
              </el-date-picker>
              <el-date-picker value-format="yyyy-MM-dd HH:mm:ss"
                              v-if="item.data_type === 6"
                              v-model="item.example"
                              type="datetime"
                              placeholder="选择日期时间">
              </el-date-picker>
              <el-input type="textarea" v-if="item.data_type === 11" style="width: 70%"
                        :autosize="{ minRows: 1, maxRows: 5}"
                        v-model="item.example" placeholder="请输入示例值" autocomplete="off"></el-input>
              <el-input type="textarea" v-if="item.data_type === 12" style="width: 70%"
                        :autosize="{ minRows: 1, maxRows: 5}"
                        v-model="item.example" placeholder="请输入示例值" autocomplete="off"></el-input>
              <el-input v-if="item.data_type === 13" v-model="item.example" placeholder="请输入示例值" autocomplete="off">
              </el-input>
              <el-radio v-model="item.required" :label="1" style="margin-left: 10px;margin-right: 10px;" >必填</el-radio>
              <el-radio v-model="item.required" :label="0" >非必填</el-radio>
            </el-form-item>
          </div>
        </template>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="paramExampleFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveExampleForm">确 定</el-button>
      </div>
    </el-dialog>
  </span>
</template>

<script>
export default {
  name: 'ParamExample',
  props: {
    functionForm: { type: Object, require: true }
  },
  data () {
    return {
      formItemSpan: 6,
      formLabelWidth: '150px',
      paramExampleFormVisible: false,
      param_example_list: [],
      param_example_list_map: {},
      param_change_flag: false
    }
  },
  methods: {
    async openExampleForm () {
      if (!this.param_change_flag) {
        this.param_example_list = []
        if (!this.functionForm.param_example_list) {
          return
        }
        for (var item of this.functionForm.param_example_list) {
          if (!item.required) {
            item.required = 0
          }
          if (item.example === null && (item.data_type === 1 || item.data_type === 2)) {
            item.example = undefined
          }
          this.param_example_list.push(item)
        }
        for (var item of this.param_example_list) {
          this.param_example_list_map[item.id] = item
        }
        this.paramExampleFormVisible = true
        return
      }
      if (this.functionForm.param_list.length === 0) {
        return
      }
      const query = '?param_id_list=' + this.functionForm.param_list
      const { data: result } = await this.$http.get(PARAM_BY_IDLIST + query)
      if (result.code !== 0) {
        return
      } else {
        for (var item of result.data) {
          if (!this.param_example_list_map[item.id]) {
            item.required = 0
            this.param_example_list_map[item.id] = item
          }
          this.param_example_list.push(this.param_example_list_map[item.id])
        }
      }
      this.param_change_flag = false
      this.paramExampleFormVisible = true
    },
    closeForm () {
      this.param_example_list = []
    },
    saveExampleForm () {
      this.$emit('saveExample', this.param_example_list)
      this.paramExampleFormVisible = false
    }
  }
}
</script>

<style scoped>
.box-card {
  overflow-y: auto
}

#paramExampleForm .el-input {
  width: 70%;
}
</style>
