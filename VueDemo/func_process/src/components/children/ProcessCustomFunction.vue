<template>
  <div class="processCustonFunction">
    <div class="task-html-box">
      <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer"/>
      <div class="query-box">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-input placeholder="请输入内容" @input="selectTaskList" clearable v-model="condition"
                      class="input-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getTaskList"></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="addBtn" @click="openAddDialog" type="primary">新增流程</el-button>
          </el-col>
          <el-col :span="2">
            <el-select v-model="query_status" @change="selectTaskList">
              <el-option v-for="item in statusOptions" :key="item.value" :label="item.label"
                         :value="item.value"></el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <ApproveComments ref="approveComments"/>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="taskFormVisible" width='40%'
                 @open='openForm' @close="closeForm">
        <el-form id="taskForm" :model="taskForm" ref="taskForm" :rules="taskRules">
          <el-form-item label="英文名" :label-width="formLabelWidth" prop="task_name">
            <el-input v-model="taskForm.task_name" placeholder="请输入英文名" autocomplete="off" @input="$forceUpdate()">
              <template slot="prepend" v-if="!readOnly"><span>p_</span></template>
            </el-input>
          </el-form-item>
          <el-form-item label="中文名" :label-width="formLabelWidth" prop="task_desc">
            <el-input v-model="taskForm.task_desc" @input="$forceUpdate()" maxlength="20"
                      placeholder="请输入中文名" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="函数" :label-width="formLabelWidth" prop="function_id_list">
            <el-select v-model="taskForm.function_id_list" multiple filterable remote reserve-keyword
                       placeholder="请选择函数" @input="$forceUpdate()" @change="clearParamAndReturn"
                       :remote-method="functionSelect">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in functionOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.label" :value="item.value" :key="item.value"></el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
          <el-form-item label="参数" :label-width="formLabelWidth" prop="param_list">
            <el-select v-model="taskForm.param_id_list" multiple filterable remote reserve-keyword
                       placeholder="请选择参数" @focus="paramSelect" @input="$forceUpdate()">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in paramOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.label" :value="item.value" :key="item.value"></el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
          <el-form-item label="返回值" :label-width="formLabelWidth" prop="return_list">
            <el-select v-model="taskForm.return_id_list" multiple filterable remote reserve-keyword
                       placeholder="请选择返回值" @focus="returnSelect" @input="$forceUpdate()">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in returnOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.label" :value="item.value" :key="item.value"></el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
          <el-form-item label="注释" :label-width="formLabelWidth" prop="task_detail">
            <el-input v-model="taskForm.task_detail" type="textarea" @input="$forceUpdate()"
                      style="width: 85%" :autosize="{ minRows: 4, maxRows: 8}"
                      placeholder="请输入注释" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="taskFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="submitForm('taskForm')">确 定</el-button>
        </div>
      </el-dialog>

      <div class="table-box">
        <el-pagination id="taskPage" @size-change="handleSizeChange" :total="total"
                       @current-change="handleCurrentChange" :current-page.sync="pageNo"
                       :page-sizes="[10, 50, 100, 500]" :page-size="pageSize" layout="total, sizes, prev, pager, next">
        </el-pagination>
        <el-table stripe :data="taskList" border style="width:100%;padding: 0" :row-class-name="rowStyle">
          <el-table-column type="index" width="80px" label="序号">
            <template scope="scope">
              <el-popover placement="top-start" width="260" trigger="hover">
                <div>
                  <div v-if="scope.row.create_person">创建人：{{ scope.row.create_person }}</div>
                  <div v-if="scope.row.create_time">创建时间：{{ scope.row.create_time }}</div>
                  <div v-if="scope.row.status !== 1 && scope.row.release_person">审核人：{{ scope.row.release_person }}
                  </div>
                  <div v-if="scope.row.status !== 1 && scope.row.release_time">审核时间：{{ scope.row.release_time }}
                  </div>
                </div>
                <div slot="reference">
                  <span style="margin-right: 10px">{{ scope.row.index }}</span>
                  <span v-if="scope.row.status === 0" class="no_active_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 1" class="submit_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 2" class="release_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 3" class="publish_class">{{ formStatus(scope.row.status) }}</span>
                </div>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column prop="task_name" width="160px" label="流程名"
                           contentEditable="true" align="left">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.task_name)"></span>
              <br/>
              <span v-html="showHighLightData(scope.row.task_desc)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="function_list" label="函数" contentEditable="true" align="left" width="220px">
            <template slot-scope="scope" v-if="scope.row.function_list.length > 0">
              <table>
                <tr v-for="item in scope.row.function_list">
                  <el-popover placement="right" trigger="click">
                    <FunctionparamMessage v-bind:functionRow="item"/>
                    <FunctionReturnMessage v-bind:functionRow="item"/>
                    <td align="left" valign="top" slot="reference">
                      <span style="width: 200px" v-html="showHighLightData(item.function_name)"/>
                      <br/>
                      <span style="width: 200px" v-html="showHighLightData(item.function_desc)"/>
                    </td>
                  </el-popover>
                </tr>
              </table>
            </template>
          </el-table-column>
          <el-table-column prop="param_list" label="参数" contentEditable="true" align="left" width="200px">
            <template slot-scope="scope" v-if="scope.row.param_list.length > 0">
              <el-popover placement="right" trigger="click">
                <FunctionparamMessage v-bind:functionRow="scope.row"/>
                <table slot="reference">
                  <tr v-for="item in scope.row.param_list">
                    <td align="left" valign="top" style="width: 175px"><span
                      v-html="showHighLightData(item.param_name)"></span></td>
                    <span style="width: 10px"></span>
                    <td align="left" valign="top" style="width: 175px"><span
                      v-html="showHighLightData(item.param_desc)"></span></td>
                  </tr>
                </table>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column prop="return_list" label="返回信息" contentEditable="true"
                           align="left" width="200px" min-width="200px">
            <template slot-scope="scope">
              <el-popover placement="right" trigger="click">
                <FunctionReturnMessage v-bind:functionRow="scope.row"/>
                <div slot="reference">
                  <span>{{ code_prefix }}</span><br/>
                  <span v-for="(item, i) in scope.row.return_list">
                    <span style="margin: 0">
                      <span v-html="showHighLightData(item.param_name)"></span>
                        :
                      <span v-html="showHighLightData(item.param_desc)"></span>
                    </span>
                    <span style="margin: 0" v-if="i < (scope.row.return_list.length-1)">,</span>
                    <br/>
                  </span>
                  <span>{{ code_suffix }}</span>
                </div>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column prop="task_detail" label="注释" contentEditable="true" align="left"
                           width="350px" min-width="300px">
            <template slot-scope="scope">
              <el-input v-model="scope.row.task_detail" autocomplete="off" type="textarea" readonly
                        @input="$forceUpdate()" style="width: 100%" :autosize="{ minRows: 3}">
                <span v-html="showHighLightData(scope.row.task_detail)"></span>
              </el-input>
            </template>
          </el-table-column>
          <el-table-column label="操作" contentEditable="true" align="center" width="100px">
            <template slot-scope="scope">
              <el-button @click="commitTask(scope.row, 1)" type="text" size="medium"
                         v-if="(!scope.row.status || scope.row.status===0)">提交审核
              </el-button>
              <el-button @click="commitTask(scope.row, 0)" type="text" size="medium"
                         v-if="scope.row.status===1">撤回提交
              </el-button>
              <el-button @click="approveTask(scope.row, 2)" type="text" size="medium"
                         v-if="releaseRole && scope.row.status===1">审核
              </el-button>
              <el-button @click="approveTask(scope.row, 1)" type="text" size="medium"
                         v-if="releaseRole && scope.row.status===2">撤回审核
              </el-button>
              <el-button @click="approveTask(scope.row, 0);
              $refs.approveComments.openComment(3, scope.row.id, scope.row.create_person)" type="text" size="medium"
                         v-if="releaseRole && scope.row.status===1">驳回
              </el-button>
              <el-button type="text" size="medium"
                         @click="$refs.approveComments.openComment(3, scope.row.id, scope.row.create_person)">
                审核意见
              </el-button>
              <br/>
              <el-button @click="readyRunTask(scope.row)" type="text" size="medium">调试</el-button>
              <br/>
              <el-button @click="openEditDialog(scope.row)" type="text" size="medium">编辑</el-button>
              <el-button @click="deleteTask(scope.row)" type="text" size="medium" v-if="scope.row.status < 2">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <el-drawer
        size="50%"
        destroy-on-close
        :visible.sync="runDrawerVisible"
        :with-header="false">
        <DebugCustomFunction v-bind:debugTaskData="debugTaskData"/>
      </el-drawer>
    </div>
  </div>
</template>
<script>
import DebugCustomFunction from './DebugCustomFunction.vue'
import SoftwareMaintainerView from '../maintainPeople/SoftwareMaintainerView.vue'
import ApproveComments from './child_pop/ApproveComments.vue'
import FunctionReturnMessage from './child_pop/FunctionReturnMessage.vue'
import FunctionparamMessage from "./child_pop/FunctionParamMessage.vue";
export default {
  name: "processCustonFunction",
  components: {
    DebugCustomFunction,
    SoftwareMaintainerView,
    ApproveComments,
    FunctionparamMessage,
    FunctionReturnMessage
  },
  data() {
    return {
      // 组件相关
      software_maintainer: '倪恒',
      taskFormVisible: false,
      flowVisible: false,
      formLabelWidth: '100px',
      readOnly: false,
      dialogTitle: '',
      taskRules: {},
      releaseRole: false,
      runDrawerVisible: false,
      submitFlag: true,
      // 列表数据相关
      pageNo: 1,
      pageSize: 10,
      total: 0,
      condition: null,
      query_status: 2,
      statusOptions: [
        {value: null, label: '全部'},
        {value: 0, label: '草稿'},
        {value: 1, label: '已提交'},
        {value: 2, label: '已审核'}
      ],
      code_prefix: '{code: 0, msg: "Success", data: {',
      code_suffix: '}}',
      taskList: [
        {
          function_list: [],
          param_list: [],
          return_list: []
        }
      ],
      // 新增表单
      taskForm: {
        id: null,
        task_name: '',
        task_desc: '',
        task_detail: '',
        function_id_list: [],
        param_id_list: [],
        return_id_list: []
      },
      // 流程配置表单
      flowFrom: {
        id: null,
        task_name: '',
        task_config_node: '',
        task_config_link: '',
        function_list: []
      },
      // 调试页面数据
      debugTaskData: {
        functionData: {},
        paramList: [],
        returnList: [],
        errorCodeList: [],
        value: null
      },
      // 下拉选择框相关
      querySize: 50,
      functionOptions: [],
      temp_param_function_list: [], // 用于检查表单函数是否变化，变化则调用接口，防止重复查询接口
      temp_return_function_list: [], // 用于检查表单函数是否变化，变化则调用接口，防止重复查询接口
      paramOptions: [],
      returnOptions: []

    }
  },
  created() {
    this.initReleaseRole();
    this.initComment();
    this.getTaskList();
  },
  methods: {
    // 自动查询未读的审核意见
    initComment() {
      if (localStorage.getItem("comment_no_read")) {
        this.query_status = null
        this.condition = '未读'
      }
    },
    // 是否有审核权限
    initReleaseRole() {
      var flag = localStorage.getItem("approve_person")
      this.releaseRole = flag === 'true'
    },
    // 初始化查询
    initQuery(paramCondition) {
      let query = '?page_size=' + this.querySize
      if (paramCondition != null) {
        paramCondition = paramCondition.toString().replace('/,/g', '');
        if (paramCondition != '') {
          query += '&condition=' + paramCondition.trim()
        }
      }
      return query
    },
    // 函数查询结果集存入选择框
    // 根据参数名查询参数列表(下拉框，拉到最底触发)
    async functionSelect(paramCondition) {
      let query = this.initQuery(paramCondition)
      const {data: result} = await this.$http.get(FUNCTION_SIMPLE_LIST + query);
      if (result.code == 0 && result.data.length > 0) {
        this.functionOptions = result.data.map(item => {
          return {value: item.id, label: item.function_name + ":" + item.function_desc};
        });
      } else {
        this.functionOptions = []
      }
    },
    async paramSelect(paramCondition) {
      if (this.taskForm.function_id_list == undefined || this.taskForm.function_id_list == '') {
        return
      }
      if (this.temp_param_function_list == this.taskForm.function_id_list) {
        return
      }
      this.temp_param_function_list = this.taskForm.function_id_list
      let query = '?type=1&function_id_list=' + this.taskForm.function_id_list
      const {data: result} = await this.$http.get(CUSTOM_PARAM_BY_FUNCLIST + query);
      if (result.code == 0 && result.data.length > 0) {
        this.paramOptions = result.data.map(item => {
          return {value: item.id, label: item.param_name + ":" + item.param_desc};
        });
      } else {
        this.paramOptions = []
      }
    },
    async returnSelect(paramCondition) {
      if (this.taskForm.function_id_list == undefined || this.taskForm.function_id_list == '') {
        return
      }
      if (this.temp_return_function_list == this.taskForm.function_id_list) {
        return
      }
      this.temp_return_function_list = this.taskForm.function_id_list
      let query = '?type=2&function_id_list=' + this.taskForm.function_id_list
      const {data: result} = await this.$http.get(CUSTOM_PARAM_BY_FUNCLIST + query);
      if (result.code == 0 && result.data.length > 0) {
        this.returnOptions = result.data.map(item => {
          return {value: item.id, label: item.param_name + ":" + item.param_desc};
        });
      } else {
        this.returnOptions = []
      }
    },
    // 根据流程id查询下拉框数据
    showFunSelectOptions(function_id_list) {
      this.functionOptions = function_id_list.map(item => {
        return {value: item.id, label: item.function_name + ":" + item.function_desc};
      });
    },
    // 根据流程id查询下拉框数据
    showParamSelectOptions(param_id_list) {
      this.paramOptions = param_id_list.map(item => {
        return {value: item.param_id, label: item.param_name + ":" + item.param_desc};
      });
    },
    // 根据流程id查询下拉框数据
    showReturnSelectOptions(param_id_list) {
      this.returnOptions = param_id_list.map(item => {
        return {value: item.param_id, label: item.param_name + ":" + item.param_desc};
      });
    },
    selectTaskList() {
      this.pageNo = 1
      this.getTaskList()
    },
    // 查询列表
    async getTaskList() {
      let query = '?page_no=' + this.pageNo + '&page_size=' + this.pageSize
      if (this.condition != null && this.condition != '') {
        this.condition = this.condition.trim()
        query += '&condition=' + this.condition
      }
      if (this.query_status !== null) {
        query += '&status=' + this.query_status
      }
      const {data: result} = await this.$http.get(CUSTOM_LIST + query);
      if (result.code != 0) {
        this.$message.error(result.msg);
      }
      var taskList = result.data.data
      this.deail_result(taskList)
      this.taskList = taskList;
      this.total = result.data.total;
    },
    // 处理返回值中复杂类型参数的子类型，不在接口中反复查询数据库
    deail_result(taskList) {
      if (taskList.length > 0) {
        for (var task_item of taskList) {
          var task_param_list = task_item.param_list
          if (task_param_list.length > 0) {
            for (var task_param of task_param_list) {
              this.get_child_from_function(task_item, task_param, true)
            }
          }
          var task_return_list = task_item.return_list
          if (task_return_list.length > 0) {
            for (var task_return of task_return_list) {
              this.get_child_from_function(task_item, task_return, false)
            }
          }
        }
      }
    },
    // 从函数列表中取子集参数
    get_child_from_function(task_item, task_param, param_flag) {
      var task_flag = false
      var function_list = task_item.function_list
      for (var func of function_list) {
        if (param_flag) {
          var source_list = func.param_list
        } else {
          var source_list = func.return_list
        }
        if (source_list.length > 0) {
          for (var source of source_list) {
            if (source.id == task_param.param_id) {
              task_param['child_id'] = source.child_id
              task_param['child_list'] = source.child_list
              task_flag = true
              break
            }
          }
        }
        if (task_flag) {
          break
        }
      }
    },
    // 删除
    async delTask(id) {
      var task_data = {
        id: id
      }
      const {data: result} = await this.$http.post(CUSTOM_DEL, task_data);
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.$message.success(result.msg)
      }
      this.taskFormVisible = false
      this.getTaskList()
    },
    // 删除二次确认
    deleteTask(row) {
      this.$confirm('确定删除' + row.task_name + '吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delTask(row.id)
      })
    },
    // 调整分页数据大小
    handleSizeChange(newSize) {
      this.pageSize = newSize;
      this.getTaskList();
    },
    // 调整当前页码
    handleCurrentChange(newPage) {
      this.pageNo = newPage;
      this.getTaskList();
    },
    // 打开新增表单
    openAddDialog() {
      this.readOnly = false
      this.dialogTitle = '新增流程'
      this.taskForm = {}
      this.taskFormVisible = true
    },
    // 打开编辑表单
    openEditDialog(row) {
      this.readOnly = true
      this.displayForm(row)
      this.dialogTitle = '编辑流程'
    },
    //回显数据
    displayForm(row) {
      this.taskForm.id = row.id
      this.taskForm.task_name = row.task_name
      this.taskForm.task_desc = row.task_desc
      this.taskForm.task_detail = row.task_detail
      var fun_list = row.function_list
      var param_list = row.param_list
      var return_list = row.return_list
      if (fun_list != null && fun_list.length > 0) {
        this.showFunSelectOptions(fun_list)
        var function_id_list = []
        for (var item of fun_list) {
          function_id_list.push(item.id)
        }
        this.taskForm.function_id_list = function_id_list
      }
      if (param_list != null && param_list.length > 0) {
        this.showParamSelectOptions(param_list)
        var param_id_list = []
        for (var item of param_list) {
          param_id_list.push(item.param_id)
        }
        this.taskForm.param_id_list = param_id_list
      }
      if (return_list != null && return_list.length > 0) {
        this.showReturnSelectOptions(return_list)
        var return_id_list = []
        for (var item of return_list) {
          return_id_list.push(item.param_id)
        }
        this.taskForm.return_id_list = return_id_list
      }
      this.taskFormVisible = true
    },
    openForm() {
      if (!this.readOnly) {
        this.functionSelect()
      }
      this.initValidRule()
      this.$forceUpdate()
    },
    closeForm() {
      this.functionOptions = []
      this.taskForm = {}
      this.functionOptions = []
      this.paramOptions = []
      this.returnOptions = []
      this.resetForm()
    },
    // 设置校验规则
    initValidRule() {
      this.taskRules = {
        "task_name": [{
          required: true, message: '请输入英文名', trigger: 'blur'
        }],
        "task_desc": [{
          required: true, message: '请输入中文名', trigger: 'blur'
        }],
        "function_id_list": [{
          required: true, message: '请选择函数', trigger: 'blur'
        }],
        "task_detail": [{
          required: true, message: '请输入注释', trigger: 'blur'
        }]
      }
      this.$nextTick(() => {
        this.$refs['taskForm'].clearValidate();
      })
    },
    // 重置表单校验
    resetForm() {
      this.$refs['taskForm'].clearValidate();
      this.$refs['taskForm'].resetFields();
    },
    // 手动校验
    emptyCheck() {
      var flag = true
      if (!this.taskForm.task_name || !this.taskForm.task_name.trim()) {
        this.$message.info("英文名不能为空")
        flag = false
      }
      if (flag && (!this.taskForm.task_desc || !this.taskForm.task_desc.trim())) {
        this.$message.info("中文名不能为空")
        flag = false
      }
      if (flag && this.taskForm.function_id_list.length == 0) {
        this.$message.info("函数不能为空")
        flag = false
      }
      if (flag && (!this.taskForm.task_detail || !this.taskForm.task_detail.trim())) {
        this.$message.info("注释不能为空")
        flag = false
      }
      return flag
    },
    async submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (!valid) {
          return;
        }
        // 手动校验
        if (!this.emptyCheck()) {
          return;
        }
        if (!this.submitFlag) {
          return;
        }
        this.submitFlag = false
        let task_data = {
          task_desc: this.taskForm.task_desc === undefined ? null : this.taskForm.task_desc.trim(),
          task_detail: this.taskForm.task_detail === undefined ? null : this.taskForm.task_detail.trim(),
          function_id_list: this.taskForm.function_id_list,
          param_id_list: this.taskForm.param_id_list,
          return_id_list: this.taskForm.return_id_list
        }
        if (this.taskForm.id == null) {
          task_data.task_name = this.taskForm.task_name === undefined ? null : 'p_' + this.taskForm.task_name.trim()
          const {data: result} = await this.$http.post(CUSTOM_ADD, task_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        } else {
          task_data.id = this.taskForm.id
          task_data.task_name = this.taskForm.task_name === undefined ? null : this.taskForm.task_name.trim()
          const {data: result} = await this.$http.post(CUSTOM_EDIT, task_data);
          if (result.code !== 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        }
        this.submitFlag = true
        this.taskFormVisible = false
        this.getTaskList()
      })
    },
    // 打开流程配置
    openFlowDialog(row) {
      this.flowFrom.id = row.id
      this.flowFrom.task_name = row.task_name
      this.flowFrom.task_config_node = row.task_config_node
      this.flowFrom.task_config_link = row.task_config_link
      this.flowFrom.function_list = row.function_list
      this.flowVisible = true
    },
    // 关闭流程配置
    closeFlowDialog() {
      this.flowFrom.id = ''
      this.flowFrom.task_name = ''
      this.flowFrom.task_config_node = ''
      this.flowFrom.task_config_link = ''
      this.flowFrom.function_list = []
      this.flowVisible = false
    },
    taskFormRef() {
      this.$refs.taskFormRef.resetFields()
    },
    // 打开调试页面
    readyRunTask(row) {
      this.debugTaskData = {}
      this.debugTaskData.id = row.id
      this.debugTaskData.taskDesc = row.task_desc
      this.debugTaskData.taskDetail = row.task_detail
      this.debugTaskData.paramList = row.param_list
      this.debugTaskData.returnList = row.return_list
      this.selectTaskErrorCode(row.id)
    },
    // 查询返回码
    async selectTaskErrorCode(task_id) {
      let query = '?task_id=' + task_id
      const {data: result} = await this.$http.get(ERROR_CODE_BYTASKID + query);
      if (result.code == 0) {
        this.debugTaskData.errorCodeList = result.data
        this.runDrawerVisible = true
      }
    },
    // 表单选中的函数发生变化，情况选中的参数和返回值
    clearParamAndReturn() {
      this.taskForm.param_id_list = []
      this.taskForm.return_id_list = []
    },
    formStatus(status) {
      if (!status) {
        status = 0
      }
      const map = {
        0: '草稿',
        1: '已提交',
        2: '已审核'
      }
      return map[status]
    },
    rowStyle({row, rowIndex}) {
      row.index = rowIndex + 1
    },
    // 提交审核
    async commitTask(row, status) {
      var release = '?id=' + row.id + '&status=' + status
      const {data: result} = await this.$http.get(CUSTOM_COMMIT + release);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success('操作成功!');
        this.getTaskList()
      }
    },
    // 审批
    async approveTask(row, status) {
      var release = '?id=' + row.id + '&status=' + status
      const {data: result} = await this.$http.get(CUSTOM_APPROVE + release);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success('操作成功!');
        this.getTaskList()
      }
    },
    // 文字高亮显示
    showHighLightData(val) {
      if (val && this.condition) {
        return val.replaceAll(this.condition, '<font style="background-color: yellow" color="black">' + this.condition + "</font>");
      } else {
        return val;
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.task-html-box {
  padding: 20px;
  min-width: 400px;
}

.query-box {
  margin-bottom: 15px;
}

.element.style {
  height: 650px;
}

.table-box {
  height: 100%;
  text-align: left;
}

#taskPage {
  text-align: left;
}

#taskForm .el-select {
  width: 85%;
}

#taskForm .el-input {
  width: 85%;
}
</style>

<style>
.processCustonFunction .el-table__header {
  width: 100% !important;
}

.processCustonFunction .el-table__body {
  width: 100% !important;
}

.no_active_class {
  font-weight: bold;
  color: grey;
}

.submit_class {
  font-weight: bold;
  color: yellowgreen;
}

.release_class {
  font-weight: bold;
  color: green;
}
</style>
