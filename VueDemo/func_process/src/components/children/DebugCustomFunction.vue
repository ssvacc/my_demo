<template>
  <div id="debug_task_box" style="padding: 20px">
    <div class="desc-box">
      <h2 style="text-align: left">流程说明</h2>
      <p style="text-align: left; margin-left: 10px; font-size: 17px">
        {{ taskDesc }}
      </p>
      <p id="taskDetail" style="text-align: left; margin-left: 10px">
        {{ taskDetail }}
      </p>
    </div>
    <div class="param-box">
      <h2 style="text-align: left">请求参数</h2>
      <el-table :data="paramList" border>
        <el-table-column type="index" width="50" label="序号">
        </el-table-column>
        <el-table-column prop="param_name" label="英文名" width="180" contentEditable="true" align="left">
        </el-table-column>
        <el-table-column prop="param_desc" label="中文名" width="150" contentEditable="true" align="left">
        </el-table-column>
        <el-table-column prop="data_type" label="数据类型" width="100" contentEditable="true" align="left">
          <template scope="scope">
            {{ formDataType(scope.row.data_type) }}
          </template>
        </el-table-column>
        <el-table-column prop="required" label="必填项" width="80" contentEditable="true" align="left">
          <template scope="scope">
            <span v-if="scope.row.required === 1">必填</span>
            <span v-else>非必填</span>
          </template>
        </el-table-column>
        <el-table-column prop="value" label="值" min-width="200" contentEditable="true" align="left">
          <template scope="scope">
            <el-input v-if="scope.row.data_type != 3 && scope.row.data_type != 5" placeholder="请输入值"
                      v-model="scope.row.value" autocomplete="off"></el-input>
            <el-select v-if="scope.row.data_type == 3" v-model="scope.row.value">
              <el-option label="True" value="True"></el-option>
              <el-option label="False" value="False"></el-option>
            </el-select>
            <el-date-picker value-format="yyyy-MM-dd HH:mm:ss" v-if="scope.row.data_type == 5"
                            v-model="scope.row.value" type="datetime" placeholder="选择日期时间">
            </el-date-picker>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="result-box">
      <h2 style="text-align: left">返回信息
        <el-button @click="debugCustomFuncion" style="float: right; margin-right: 200px" type="success" plain>调试
        </el-button>
      </h2>
      <el-row :gutter="12">
        <el-col :span="12">
          <el-card shadow="hover" class="box-card">
            <div class="text item" style="text-align: left; white-space: pre-wrap">
              {{ returnData }}
            </div>
          </el-card>
        </el-col>
        <CodeMsgCardView ref="codeMsg" v-bind:errorCodeList="errorCodeList"/>
      </el-row>
    </div>
  </div>

</template>

<script>
import CodeMsgCardView from './child_pop/CodeMsgCardView.vue'

export default {
  name: 'debugCustomFunction',
  props: {
    debugTaskData: { type: Object, require: true }
  },
  components: {
    CodeMsgCardView
  },
  data () {
    return {
      taskId: this.debugTaskData.id,
      taskDesc: this.debugTaskData.taskDesc,
      taskDetail: this.debugTaskData.taskDetail,
      paramList: this.debugTaskData.paramList,
      returnList: this.debugTaskData.returnList,
      errorCodeList: this.debugTaskData.errorCodeList,
      returnData: {},
      dataTypeMap: {
        1: 'Int',
        2: 'Float',
        3: 'Boolean',
        4: 'String',
        5: 'Date',
        6: 'Datetime',
        7: 'Instance',
        11: '[ ]',
        12: '{ }',
        13: 'Enum',
        14: 'Set',
        21: 'Page'
      },
      dataTypeEnum: {
        INT_TYPE: 1,
        FLOAT_TYPE: 2,
        BOOLEAN_TYPE: 3,
        STRING_TYPE: 4,
        DATE_TYPE: 5,
        DATETIME_TYPE: 6,
        INSTANCE_TYPE: 7,
        LIST_TYPE: 11,
        DICT_TYPE: 12,
        ENUM_TYPE: 13,
        SET_TYPE: 14,
        PAGE_TYPE: 21
      }
    }
  },
  methods: {
    formDataType (type) {
      return this.dataTypeMap[type]
    },
    getValueByDataType (dataType, value) {
      const dataTypeEnum = this.dataTypeEnum
      value = value === null ? '' : value
      let res = null
      switch (dataType) {
        case dataTypeEnum.INT_TYPE: res = parseInt(value); break
        case dataTypeEnum.FLOAT_TYPE: res = parseFloat(value); break
        case dataTypeEnum.BOOLEAN_TYPE: res = value === 'True'; break
        case dataTypeEnum.STRING_TYPE: res = value; break
        case dataTypeEnum.DATE_TYPE: res = value; break
        case dataTypeEnum.DATETIME_TYPE: res = value; break
        case dataTypeEnum.INSTANCE_TYPE: res = value; break
        case dataTypeEnum.LIST_TYPE: value ? res = JSON.parse(value) : res = []; break
        case dataTypeEnum.DICT_TYPE: value ? res = JSON.parse(value) : res = {}; break
        case dataTypeEnum.ENUM_TYPE: res = value; break
        case dataTypeEnum.SET_TYPE: res = new Set(value.split(',')); break
        default: res = value
      }
      return res
    },
    // 调试流程
    async debugCustomFuncion () {
      const task_data = {}
      task_data.task_id = this.taskId
      const param_list = this.paramList
      const req_param_list = {}
      for (const i in param_list) {
        const pub_param = param_list[i]
        if (pub_param.required === 1 && !pub_param.value) {
          this.$message.info(pub_param.param_name + '不能为空!')
          return
        }
        const param_name = pub_param.param_name
        req_param_list[param_name] = this.getValueByDataType(pub_param.data_type, pub_param.value)
      }
      task_data.param_list = req_param_list
      const { data: result } = await this.$http.post(CUSTOM_SIMPLE_RUN, task_data)
      if (result.code === 0) {
        this.returnData = result
        this.$message.success(result.msg)
      } else if (result.code === 44005) {
        this.returnData = result.data
        this.$message.info(result.msg)
      } else {
        this.returnData = {}
        this.$message.error(result.msg)
      }
    }
  }
}
</script>

<style scoped>
#taskDetail {
  font-size: medium;
  color: grey;
  text-align: left;
  margin-left: 10px;
}

.box-card {
  overflow-y: auto
}
</style>
