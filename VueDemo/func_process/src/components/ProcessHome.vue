<template>
  <div class="processHome">
    <el-tabs :tab-position="tabPosition" v-model="activePaneName" @tab-click="handleClick">
      <el-tab-pane label="返回码管理" name='errorCodePane'>
        <ProcessErrorCode/>
      </el-tab-pane>
      <el-tab-pane label="类管理" name='classPane'>
        <ProcessErrorClass :FunctionVueEnumClassTypeShow="FunctionVueEnumClassTypeShow"/>
      </el-tab-pane>
      <el-tab-pane label="参数管理" name='paramPane'>
        <processParam :globalSelectOptions="globalSelectOptions"
                      :enumTypeShow="enumTypeShow"
                      ref="processParamRef"/>
      </el-tab-pane>
      <el-tab-pane label="函数管理" name='functionPane'>
        <processFunction ref="processFunctionRef"/>
      </el-tab-pane>
      <el-tab-pane label="流程编排" name='custonFunctionPane'>
        <ProcessCustomFunction/>
      </el-tab-pane>
      <el-tab-pane label="开发规范" name='programmingStandard'>
        <ProgrammingStandard/>
      </el-tab-pane>
      <el-tab-pane label="页面管理" name='pagePane'>
        <PageManage :jumpFunction="jumpFunction"/>
      </el-tab-pane>
      
    </el-tabs>
    <div class="shuoming">
      <p>说明：</p>
      <p>返回码只有常杨能修改</p>
      <p>参数只有丁俊能修改</p>
      <p>函数管理所有人都能修改</p>
      <p>流程编排所有人都能修改</p>
      <p>需要新增返回码请找常杨添加</p>
      <p>需要新增参数请找丁俊添加</p>
    </div>
  </div>
</template>
<script>

import ProcessParam from './children/ProcessParam.vue'
import ProcessErrorCode from './children/ProcessErrorCode.vue'
import ProcessErrorClass from './children/ProcessClass.vue'
import ProcessFunction from './children/ProcessFunction.vue'
import ProcessCustomFunction from './children/ProcessCustomFunction.vue'
import ProgrammingStandard from './children/ProgrammingStandard.vue'
import PageManage from './children/PageManage.vue'

export default {
  name: 'processHome',
  components: {
    ProcessParam,
    ProcessErrorCode,
    ProcessErrorClass,
    ProcessFunction,
    ProcessCustomFunction,
    ProgrammingStandard,
    PageManage
  },
  data() {
    return {
      activePaneName: 'errorCodePane',
      tabPosition: 'left',
      globalSelectOptions: [],
      enumOptions: [],
      comment_tag: 'deal_with_id'
    }
  },
  created() {
    this.initUrl()
    this.initTab()
    this.initUserApprove()
    this.enumTypeSelect()
  },
  methods: {
    initUrl() {
      var a = window.location.href
      if (a.includes(this.comment_tag)) {
        localStorage.setItem("comment_no_read", true)
      } else {
        localStorage.removeItem("comment_no_read")
      }
    },
    // 刷新页面时，展示之前点击的tab
    handleClick(tab, event) {
      localStorage.setItem("func_process_tab", tab.name)
    },
    initTab() {
      var defaultTab = localStorage.getItem("func_process_tab")
      if (defaultTab) {
        this.activePaneName = defaultTab
      }
    },
    async initUserApprove() {
      const {data: result} = await this.$http.get(APPROVE_PERSON);
      if (result.code == 0) {
        var flag = result.data
        localStorage.setItem("approve_person", flag)
      }
    },
    // 枚举类型全局下拉框
    async enumTypeSelect() {
      if (this.globalSelectOptions.length == 0) {
        const {data: result} = await this.$http.get(GET_SELECT_LIST);
        this.globalSelectOptions = result.data.map(item => {
          return {
            id: item.id,
            label: item.name + ":" + item.key_val,
            type: item.db_type,
            sql: item.get_info_sql
          };
        });
      }
    },
    // 全局下拉框枚举值查看效果
    async enumTypeShow(type, sql, changeAble) {
      this.enumOptions = []
      if (sql) {
        var request_data = {
          type: type,
          sql: sql
        }
        const {data: result} = await this.$http.post(QUERY_SELECT, request_data);
        if (result.code == 0) {
          this.enumOptions = result.data.map(item => {
            return {value: item.key, label: item.label};
          });
          if (changeAble) {
            this.$refs.processParamRef.renderEnumOptions(null, this.enumOptions)
          }
        }
      }
    },
    jumpFunction(s_function_name, s_tabs_name) {
      this.activePaneName = s_tabs_name;
      this.$refs.processFunctionRef.openPageFunction(s_function_name);
    },
    // 调用ProcessVue组件中的enumClassTypeShow
    FunctionVueEnumClassTypeShow(classAll) {
      this.$refs.processFunctionRef.enumClassTypeShow(classAll)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.shuoming {
  position: fixed;
  text-align: left;
  top: 40%;
  left: 0.8%;
  font-size: small;
  height: 300px;
  width: 100px;
  background-color: 5cb85c;
  border: black 1px;
}
</style>

<style>
.processHome {
  min-width: 800px;
  overflow: auto;
}

.processHome .el-tabs {
  display: flex;
}

.processHome .el-tabs--left .el-tabs__header.is-left {
  clear: both;
}

.processHome .el-tabs__content {
  flex: 1;
}
</style>
