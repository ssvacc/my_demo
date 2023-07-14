<template>
  <div id="debug_box" style="padding: 20px">
    <div class="desc-box">
      <h2 style="text-align: left">函数说明
        <el-button @click="readyShowFunction(functionData.id, functionData.url)"
                   style="float: right; margin-right: 200px"
                   type="info" plain>查看源码
        </el-button>
      </h2>
      <p style="text-align: left; margin-left: 10px; font-size: 17px">
        {{ functionData.function_name }} {{ functionData.function_desc }}
      </p>
      <p id="functionDetail">
        {{ functionData.function_detail }}
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
            <el-input-number v-if="scope.row.data_type === 1" controls-position="right" style="width: 100%"
                             v-model="scope.row.value" placeholder="请输入示例值" autocomplete="off">
            </el-input-number>
            <el-input-number v-if="scope.row.data_type === 2" controls-position="right" style="width: 100%"
                             v-model="scope.row.value" placeholder="请输入示例值" autocomplete="off">
            </el-input-number>
            <el-select v-if="scope.row.data_type === 3" v-model="scope.row.value" style="width: 100%">
              <el-option label="True" value="True"></el-option>
              <el-option label="False" value="False"></el-option>
            </el-select>
            <el-input type="textarea" v-if="scope.row.data_type === 4" style="width: 100%"
                      :autosize="{ minRows: 1, maxRows: 5}"
                      v-model="scope.row.value" placeholder="请输入示例值" autocomplete="off"></el-input>
            <el-date-picker value-format="yyyy-MM-dd" style="width: 100%"
                            v-if="scope.row.data_type === 5"
                            v-model="scope.row.value"
                            type="date"
                            placeholder="选择日期">
            </el-date-picker>
            <el-date-picker value-format="yyyy-MM-dd HH:mm:ss" style="width: 100%"
                            v-if="scope.row.data_type === 6"
                            v-model="scope.row.value"
                            type="datetime"
                            placeholder="选择日期时间">
            </el-date-picker>
            <el-input type="textarea" v-if="scope.row.data_type === 11"
                      :autosize="{ minRows: 1, maxRows: 5}"
                      v-model="scope.row.value" placeholder="请输入示例值" autocomplete="off"></el-input>
            <el-input type="textarea" v-if="scope.row.data_type === 12"
                      :autosize="{ minRows: 1, maxRows: 5}"
                      v-model="scope.row.value" placeholder="请输入示例值" autocomplete="off"></el-input>
            <el-input v-if="scope.row.data_type === 13" v-model="scope.row.value" placeholder="请输入示例值" autocomplete="off">
            </el-input>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="result-box">
      <h2 style="text-align: left">返回信息
        <el-button @click="debugFuncion"
                   style="margin-left: 470px"
                   type="primary" plain>调试
        </el-button>
        <el-button @click="publishFuncion(3)" v-if="functionData.status === 4"
                   style="margin-left: 10px"
                   type="warning" plain>发布
        </el-button>
        <el-button @click="publishFuncion(4)" v-if="functionData.status === 3"
                   style=" margin-left: 10px"
                   type="danger" plain>取消发布
        </el-button>
        <el-button @click="addAutoTest(1)" v-if="functionData.status === 3 && functionData.is_auto_test === 0"
                   style=" margin-left: 10px"
                   type="warning" plain>
          <span>未自动化</span>
        </el-button>
        <el-button v-if="functionData.status === 3 && functionData.is_auto_test === 1" disabled
                   style=" margin-left: 10px"
                   type="warning" plain>
          <span>已自动化</span>
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
  name: 'debugFunction',
  components: {
    CodeMsgCardView
  },
  props: {
    closeDrawer: { type: Function, require: true },
    debugData: { type: Object, require: true },
    readyShowFunction: { type: Function, require: true }
  },
  data () {
    return {
      functionData: this.debugData.functionData,
      paramList: this.debugData.paramList,
      returnList: this.debugData.returnList,
      errorCodeList: this.debugData.errorCodeList,
      returnData: {},
      showResult: true,
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
      let res = null
      value = value === null ? '' : value
      switch (dataType) {
        case dataTypeEnum.INT_TYPE:
          res = parseInt(value)
          break
        case dataTypeEnum.FLOAT_TYPE:
          res = parseFloat(value)
          break
        case dataTypeEnum.BOOLEAN_TYPE:
          res = value === 'True'
          break
        case dataTypeEnum.STRING_TYPE:
          res = value
          break
        case dataTypeEnum.DATE_TYPE:
          res = value
          break
        case dataTypeEnum.DATETIME_TYPE:
          res = value
          break
        case dataTypeEnum.INSTANCE_TYPE:
          res = value
          break
        case dataTypeEnum.LIST_TYPE:
          value ? res = JSON.parse(value) : res = []
          break
        case dataTypeEnum.DICT_TYPE:
          value ? res = JSON.parse(value) : res = {}
          break
        case dataTypeEnum.ENUM_TYPE:
          res = value
          break
        case dataTypeEnum.SET_TYPE:
          res = new Set(value.split(','))
          break
        default:
          res = value
      }
      return res
    },
    // 调试函数
    async debugFuncion () {
      const function_data = {}
      function_data.function_id = this.functionData.id
      const param_list = this.paramList
      const req_param_list = {}
      for (const i in param_list) {
        const pub_param = param_list[i]
        const param_name = pub_param.param_name
        req_param_list[param_name] = this.getValueByDataType(pub_param.data_type, pub_param.value)
      }
      function_data.param_list = req_param_list
      const { data: result } = await this.$http.post(FUNCTION_RUN, function_data)
      if (result.code != 0) {
        this.returnData = {}
        this.$message.error(result.msg)
      } else if (result.data.code != 0) {
        this.returnData = result.data
        this.$message.info(result.msg)
      } else {
        this.returnData = result.data
        this.$message.success(result.msg)
      }
    },
    // 发布函数(只能由测试人员点发布)
    async publishFuncion (status) {
      const publish = '?id=' + this.functionData.id + '&status=' + status
      const { data: result } = await this.$http.get(FUNCTION_PUBLISH + publish)
      if (result.code === 0) {
        this.$message.success('操作成功!')
        this.closeDrawer(status)
      } else {
        this.$message.error(result.msg)
      }
    },
    // 加入自动化测试(只能由测试人员点)
    async addAutoTest (is_auto_test) {
      const request_data = '?id=' + this.functionData.id + '&is_auto_test=' + is_auto_test
      const { data: result } = await this.$http.get(FUNCTION_ADD_AUTO_TEST + request_data)
      if (result.code === 0) {
        this.$message.success('操作成功!')
        this.closeDrawer(status)
      } else {
        this.$message.error(result.msg)
      }
    }
  }
}
</script>
<style>
#functionDetail {
  font-size: medium;
  color: grey;
  text-align: left;
  margin-left: 10px;
}

.box-card {
  overflow-y: auto
}
</style>
