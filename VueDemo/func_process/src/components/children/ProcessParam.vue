<template>
  <div class="processParam">
    <div class="param-html-box">
      <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer"/>
      <div class="query-box">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-input placeholder="请输入内容" @input="selectParamList" clearable v-model="condition"
                      class="input-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getParamList"></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="addBtn" @click="openAddDialog" type="primary">新增参数</el-button>
          </el-col>
          <el-col :span="2">
            <el-select v-model="query_status" @change="selectParamList">
              <el-option v-for="item in statusOptions" :key="item.value" :label="item.label"
                         :value="item.value"></el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <ApproveComments ref="approveComments"/>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="paramFormVisible" width='40%'
                 @open='openForm' @close="closeForm">
        <el-form id="paramForm" :model="paramForm" ref="paramForm" :rules="paramRules">
          <el-form-item label="类型" :label-width="formLabelWidth" prop="data_type">
            <el-select popper-class="data_type_select" v-model="paramForm.data_type" placeholder="请选择类型" length="3"
                       :disabled="readOnly" @change="clearChildOptions">
              <el-option v-for="item in paramOptions" :key="item.value" :label="item.data_type"
                         :value="item.value"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="子类型" :label-width="formLabelWidth" prop="list_child_type"
                        v-show="paramForm.data_type===11">
            <el-select v-model="paramForm.list_child_type" filterable remote placeholder="请选择子类型"
                       :remote-method="listTypeSelect" :disabled="readOnly&&paramForm.status>0"
                       @change="$forceUpdate()">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in listTypeOptions" class="infinite-list-item" :key="item.value">
                  <el-option :disabled="item.value==paramForm.id" :label="item.data_type" :value="item.value"
                             :key="item.value"></el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
          <el-form-item label="子类型" :label-width="formLabelWidth" prop="dict_child_type"
                        v-show="paramForm.data_type===12">
            <el-select v-model="paramForm.dict_child_type" multiple filterable remote placeholder="请选择子类型"
                       :remote-method="dictTypeSelect" :disabled="readOnly&&paramForm.status>0"
                       @change="$forceUpdate()">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in dictTypeOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.data_type" :value="item.value" :key="item.value"></el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
<!-- Field类型 -->
          <el-form-item label="子类型" :label-width="formLabelWidth" prop="dict_child_type"
                        v-show="paramForm.data_type===22">
            <el-select v-model="paramForm.dict_child_type" multiple filterable remote placeholder="请选择子类型"
                       :remote-method="dictTypeSelect" :disabled="readOnly&&paramForm.status>0"
                       @change="saveChange()">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in dictTypeOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.data_type" :value="item.value" :key="item.value"></el-option>
                </li>
              </ul>
            </el-select>   
          </el-form-item>
          <el-form-item v-show="paramForm.data_type===22">
            <template  v-if="paramForm.dict_child_type && paramForm.dict_child_type.length > 0">
              <div v-for="item in selectedValues" :key="index">
                <el-form-item  :label-width="formLabelWidth" :prop="dict_child_value" :key="item.key">
                  <!-- <template slot="label"><div class="custom-label">{{item.field_param_name.split(':').slice(0,1)[0]}}</div></template> -->
                  <template slot="label"><el-text>{{item.field_param_name.split(':').slice(0,1)[0]}}</el-text></template>
                  <el-row>
                    <el-col :span="10">
                      <el-input size="small" placeholder="列宽 例：100px" v-model="item.field_value.width">
                        <template slot="prepend">{{getStyleType(1)}}</template>
                      </el-input>
                    </el-col>
                    <el-col :span="10">
                      <el-input size="small" placeholder="颜色 例：#3a87ad" v-model="item.field_value.color">
                        <template slot="prepend">{{getStyleType(2)}}</template>
                      </el-input>
                    </el-col>
                  </el-row>
                </el-form-item>
              </div>
            </template>
          </el-form-item>

          <el-form-item label="枚举内容" :label-width="formLabelWidth" prop="list_child_type"
                        v-show="paramForm.data_type===13">
            <el-select v-model="paramForm.select_info_id" filterable placeholder="请选择枚举内容"
                       :disabled="readOnly&&paramForm.status>0" @change="changeEnumSelect">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in globalSelectOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.label" :value="item.id" :key="item.id"></el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
          <el-form-item label="查看效果" :label-width="formLabelWidth" prop="list_child_type"
                        v-show="paramForm.data_type===13">
            <el-select v-model="paramForm.enum_select_id" filterable placeholder="查看效果" @change="$forceUpdate()">
              <ul class="infinite-list" style="overflow:auto">
                <li v-for="item in enumParamOptions" class="infinite-list-item" :key="item.value">
                  <el-option :label="item.label" :value="item.value" :key="item.value">
                    <span style="float: left;">{{ item.label }}</span>
                    <span style="float: left;margin-right: 20px"></span>
                    <span style="float: right;color: #3a87ad">{{ item.value }}</span>
                  </el-option>
                </li>
              </ul>
            </el-select>
          </el-form-item>
          <el-form-item label="英文名" :label-width="formLabelWidth" prop="param_name">
            <el-input v-model="paramForm.param_name" autocomplete="off" placeholder="请输入英文名"
                      :disabled="readOnly&&paramForm.status>0" @input="changeMessage">
              <template slot="prepend" v-if="!readOnly && paramForm.data_type">
                <span>{{ getDataTypePrefix(paramForm.data_type) }}</span></template>
            </el-input>
          </el-form-item>
          <el-form-item label="中文名" :label-width="formLabelWidth" prop="param_desc">
            <el-input v-model="paramForm.param_desc" autocomplete="off" placeholder="请输入中文名"
                      @input="changeMessage"></el-input>
          </el-form-item>
          <el-form-item label="注释" :label-width="formLabelWidth" prop="param_detail" @change="$forceUpdate()">
            <el-input v-model="paramForm.param_detail" type="textarea" placeholder="请输入注释" autocomplete="off"
                      @input="changeMessage" style="width: 85%" :autosize="{ minRows: 5, maxRows: 8}"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <div id="formBtn">
            <el-button @click="paramFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="submitForm('paramForm')">确 定</el-button>
          </div>
        </div>
      </el-dialog>
      <div class="table-box">
        <el-pagination id="paramPage"
                       @size-change="handleSizeChange"
                       @current-change="handleCurrentChange"
                       :current-page.sync="pageNo"
                       :page-sizes="[10, 50, 100, 500]"
                       :page-size="pageSize"
                       layout="total, sizes, prev, pager, next"
                       :total="total">
        </el-pagination>
        <el-table stripe :tree-props="{children: 'child_list', hasChildren: 'child_id'}" :row-key="row=>getRowKey(row)"
                  :data="paramList" border lazy :load="loadChildList" :row-class-name="rowStyle"
                  style="width:100%;padding: 0">
          <el-table-column type="index" width="80px" label="序号">
            <template scope="scope">
              <el-popover placement="top-start" width="260" trigger="hover">
                <div>
                  <div v-if="scope.row.create_person">创建人：{{ scope.row.create_person }}</div>
                  <div v-if="scope.row.create_time">创建时间：{{ scope.row.create_time }}</div>
                  <div v-if="scope.row.status !== 0 && scope.row.apply_person">提交人：{{ scope.row.apply_person }}</div>
                  <div v-if="scope.row.status !== 0 && scope.row.apply_time">提交时间：{{ scope.row.apply_time }}</div>
                  <div v-if="scope.row.status !== 1 && scope.row.release_person">审核人：{{ scope.row.release_person }}
                  </div>
                  <div v-if="scope.row.status !== 1 && scope.row.release_time">审核时间：{{ scope.row.release_time }}
                  </div>
                  <div v-if="scope.row.status === 3 && scope.row.release_person">发布人：{{ scope.row.publish_person }}
                  </div>
                  <div v-if="scope.row.status === 3 && scope.row.release_time">发布时间：{{ scope.row.publish_time }}
                  </div>
                </div>
                <div slot="reference">
                  <span style="margin-right: 10px">{{ scope.row.index }}</span>
                  <span v-if="scope.row.status === 0" class="no_active_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 1" class="submit_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 2" class="release_class">{{ formStatus(scope.row.status) }}</span>
                </div>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column prop="param_name" maxlength=255 label="英文名" contentEditable="true" align="left"
                           width="200px" min-width="300px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.param_name)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="param_desc" maxlength=255 label="中文名" contentEditable="true" align="left"
                           width="200px" min-width="300px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.param_desc)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="data_type" label="类型" contentEditable="true" align="left" width="200px"
                           min-width="200px">
            <template scope="scope">
              <div>
                <div v-if="scope.row.data_type!==13">
                  {{ formDataType(scope.row.data_type, scope.row.child_id, scope.row.child_list) }}
                </div>
                <el-row type="flex" class="row-bg" v-if="scope.row.data_type===13">
                  <el-col :span="6">
                    <div style="margin-top: 8px">
                      {{ formDataType(scope.row.data_type, scope.row.child_id, scope.row.child_list) }}
                    </div>
                  </el-col>
                  <el-col :span="17">
                    <el-select v-model="scope.row.empty" filterable placeholder="查看效果"
                               @visible-change="changedEnumOptions($event)"
                               @focus="updateEnumOptions(scope.row.select_info_id)" @change="$forceUpdate()">
                      <ul class="infinite-list" style="overflow:auto">
                        <li v-for="item in enumParamOptions" class="infinite-list-item" :key="item.value">
                          <el-option :label="item.label" :value="item.value" :key="item.value">
                            <span style="float: left;">{{ item.label }}</span>
                            <span style="float: left;margin-right: 20px"></span>
                            <span style="float: right;color: #3a87ad">{{ item.value }}</span>
                          </el-option>
                        </li>
                      </ul>
                    </el-select>
                  </el-col>
                </el-row>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="param_detail" maxlength=255 label="注释" contentEditable="true" align="left"
                           width="300px" min-width="300px">
            <template slot-scope="scope">
              <el-input v-model="scope.row.param_detail" autocomplete="off" type="textarea" readonly
                        @input="$forceUpdate()" style="width: 100%" :autosize="{ minRows: 1}">
                <span v-html="showHighLightData(scope.row.param_detail)"></span>
              </el-input>
            </template>
          </el-table-column>
          <el-table-column label="操作" contentEditable="true" align="center" width="80px" min-width="80px">
            <template slot-scope="scope">
              <el-button @click="commitParam(scope.row, 1)" type="text" size="medium"
                         v-if="(!scope.row.status || scope.row.status===0)">提交审核
              </el-button>
              <el-button @click="commitParam(scope.row, 0)" type="text" size="medium"
                         v-if="scope.row.status===1">撤回提交
              </el-button>
              <el-button @click="approveParam(scope.row, 2)" type="text" size="medium"
                         v-if="releaseRole && scope.row.status===1">审核
              </el-button>
              <el-button @click="approveParam(scope.row, 1)" type="text" size="medium"
                         v-if="releaseRole && scope.row.status===2">撤回审核
              </el-button>
              <el-button @click="approveParam(scope.row, 0);
              $refs.approveComments.openComment(1, scope.row.id, scope.row.create_person)"
                         type="text" size="medium"
                         v-if="releaseRole && scope.row.status===1">驳回
              </el-button>
              <el-button type="text" size="medium"
                         @click="$refs.approveComments.openComment(1, scope.row.id, scope.row.create_person)">
                审核意见
              </el-button>
              <el-button @click="openEditDialog(scope.row)" type="text" size="medium">编辑</el-button>
              <el-button @click="deleteParam(scope.row)" type="text" size="medium" v-if="scope.row.status < 2">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
<script>
import SoftwareMaintainerView from '../maintainPeople/SoftwareMaintainerView.vue'
import ApproveComments from './child_pop/ApproveComments.vue'
import {log} from "util";

export default {
  components: {
    SoftwareMaintainerView,
    ApproveComments
  },
  data() {
    return {
      field_value:{
        width:'',
        color:'',
      },
      input1:null,
      inputValues:{},
      inputData:[],//动态输入框
      selectedOptions:[],
      selectedValues:[], // 清空字典
      styleResultList:[],
      readOnly: false,
      dialogTitle: '',
      paramFormVisible: false,
      formLabelWidth: '80px',
      paramRules: {},
      submitFlag: true,
      releaseRole: false,
      software_maintainer: '倪恒',
      pageNo: 1,
      pageSize: 10,
      total: 0,
      query_status: 2,
      statusOptions: [
        {value: null, label: '全部'},
        {value: 0, label: '草稿'},
        {value: 1, label: '已提交'},
        {value: 2, label: '已审核'}
      ],
      condition: null,
      paramList: [],
      paramForm: {
        id: null,
        param_name: '',
        param_desc: '',
        param_detail: '',
        data_type: null,
        list_child_type: null,
        dict_child_type: [],
        select_info_id: null,
        enum_select_id: null,
        status: 0
      },
      paramOptions: [
        {value: 1, level: 1, data_type: 'Int'},
        {value: 2, level: 1, data_type: 'Float'},
        {value: 3, level: 1, data_type: 'Boolean'},
        {value: 4, level: 1, data_type: 'String'},
        {value: 5, level: 1, data_type: 'Date'},
        {value: 6, level: 1, data_type: 'Datetime'},
        {value: 7, level: 1, data_type: 'Instance'},
        {value: 11, level: 2, data_type: '[ ]'},
        {value: 12, level: 2, data_type: '{ }'},
        {value: 13, level: 2, data_type: 'Enum'},
        {value: 21, level: 1, data_type: 'Page'},
        {value: 22, level: 1, data_type: 'Field'}
      ],
      listTypeOptions: [],
      dictTypeOptions: [],
      tempNode: [],
      enumParamOptions: [], // 绑定下拉框数据，vue不支持子组件更新父组件数据，用来接收enumOptions的数据变更
      tempKey: 0,
      enumParamOptionsMap: {}, // 前端缓存用于存放不同下拉框id对应的值，不必每次都查询数据库
      intervalFun: null,
      querySize: 100,
      input_value_1: null,
      input_value_2: null,
      input_value_3: null,
      input_value_4: null,
    }
  },
  props: {
    globalSelectOptions: {type: Array, require: true},
    enumTypeShow: {type: Function, require: true}
  },
  created() {
    this.initReleaseRole();
    this.initComment();
    this.getParamList();
  },
  methods: {
    getInputValue(id) {
      // 使用动态属性获取不同的v-model名称
      return this.inputValues[id] || '';
    },


async saveChange() {
  if (this.dialogTitle === "新增参数") {
    this.selectedValues = []; // 清空列表
    // 遍历已选择的选项
    this.paramForm.dict_child_type.forEach(option => {
      const selectedOption = this.dictTypeOptions.find(item => item.value === option);
      this.selectedValues.push({
        field_param_id: selectedOption.value,
        field_param_name: selectedOption.data_type.split(':').slice(0, 1)[0],
        field_value: {},
      });
    });
  } else if (this.dialogTitle === "编辑参数") {
    const existingValueIds = this.selectedValues.map(value => value.field_param_id);
    const newValueIds = []; 
    // 更新已存在的选项
    this.selectedValues.forEach(value => {
      const selectedOption = this.dictTypeOptions.find(item => item.value === value.field_param_id);
      if (selectedOption) {
        value.field_param_name = selectedOption.data_type.split(':').slice(0, 1)[0];
        newValueIds.push(value.field_param_id);
      } else {
        // 抛出不再存在的选项，保留其他选项数据
        newValueIds.push(value.field_param_id);
      }
    });
    // 添加新的选项
    this.paramForm.dict_child_type.forEach(option => {
      if (!existingValueIds.includes(option)) {
        const selectedOption = this.dictTypeOptions.find(item => item.value === option);
        if (selectedOption) {
          this.selectedValues.push({
            field_param_id: selectedOption.value,
            field_param_name: selectedOption.data_type.split(':').slice(0, 1)[0],
            field_value: {},
          });
          newValueIds.push(selectedOption.value);
        }
      }
    });
    //如果相对于existingValueIds是减少了选项,计算dict_child_type和existingValueIds的交集
    if (this.paramForm.dict_child_type.length < existingValueIds.length) {
      const intersectedIds = this.paramForm.dict_child_type.filter(option => existingValueIds.includes(option));
      this.selectedValues = this.selectedValues.filter(value => intersectedIds.includes(value.field_param_id));
    }
    // 更新selectedValues并移除不再存在的选项
    this.selectedValues = this.selectedValues.filter(value => newValueIds.includes(value.field_param_id));
  }
},
    handleSelectionChange(selectedItems) {
    // 清空已选择的子类型
    this.selectedOptions = {};

    // 添加选择的子类型到selectedOptions数组中
    selectedItems.forEach(item => {
      if (!this.selectedOptions[item.value]) {
        this.selectedOptions[item.value] = item.data_type;
      }
    });
  },
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
    // 搜索列表
    selectParamList() {
      this.pageNo = 1
      this.getParamList()
    },
    // 查询列表
    async getParamList() {
      let query = '?page_no=' + this.pageNo + '&page_size=' + this.pageSize
      if (this.condition != null && this.condition != '') {
        this.condition = this.condition.trim()
        query += '&condition=' + this.condition
      }
      if (this.query_status !== null) {
        query += '&status=' + this.query_status
      }
      const {data: result} = await this.$http.get(PARAM_CHILD_PAGE + query);
      if (result.code != 0) {
        this.$message.error(result.msg);
      }
      this.paramList = result.data.data;
      this.total = result.data.total;
    },
    // 手动校验
    emptyCheck() {
      var flag = true
      if (!this.paramForm.param_name || !this.paramForm.param_name.trim()) {
        this.$message.info("英文名不能为空")
        flag = false
      }
      if (flag && (!this.paramForm.param_desc || !this.paramForm.param_desc.trim())) {
        this.$message.info("中文名不能为空")
        flag = false
      }
      if (flag && (!this.paramForm.param_detail || !this.paramForm.param_detail.trim())) {
        this.$message.info("注释不能为空")
        flag = false
      }
      return flag
    },
    // 新增、修改
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
        var param_data = {
          param_desc: this.paramForm.param_desc === undefined ? null : this.paramForm.param_desc.trim(),
          param_detail: this.paramForm.param_detail === undefined ? null : this.paramForm.param_detail.trim(),
          data_type: this.paramForm.data_type
        }
        // 列表类型参数
        if (this.paramForm.data_type == 11 && this.paramForm.list_child_type) {
          param_data.child_id = this.paramForm.list_child_type
        }
        // 字典类型参数
        if (this.paramForm.data_type == 12 && this.paramForm.dict_child_type) {
          param_data.child_id = this.paramForm.dict_child_type.join()
        }
        // 枚举类型参数
        if (this.paramForm.data_type == 13 && this.paramForm.select_info_id) {
          param_data.select_info_id = this.paramForm.select_info_id
        }
        // Field类型参数
        if (this.paramForm.data_type == 22 && this.paramForm.dict_child_type) {
          param_data.child_id = this.paramForm.dict_child_type.join()
          param_data.selectedValues = this.selectedValues
        }
        if (this.paramForm.id == null) {
          param_data.param_name = this.getDataTypePrefix(this.paramForm.data_type) + this.paramForm.param_name.trim()
          const {data: result} = await this.$http.post(PARAM_ADD, param_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        } else {
          param_data.id = this.paramForm.id
          param_data.param_name = this.paramForm.param_name.trim()
          const {data: result} = await this.$http.post(PARAM_EDIT, param_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        }
        this.submitFlag = true
        this.paramFormVisible = false
        this.getParamList()
      })
    },
    // 删除
    async delParam(id) {
      var param_data = {
        id: id
      }
      const {data: result} = await this.$http.post(PARAM_DEL, param_data);
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.$message.success(result.msg)
      }
      this.paramFormVisible = false
      this.getParamList()
    },
    // 删除二次确认
    deleteParam(row) {
      this.$confirm('确定删除' + row.param_name + '吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delParam(row.id)
      })
    },
    // 调整分页数据大小
    handleSizeChange(newSize) {
      this.pageSize = newSize;
      this.getParamList();
    },
    // 调整当前页码
    handleCurrentChange(newPage) {
      this.pageNo = newPage;
      this.getParamList();
    },
    //回显数据
    displayForm(row) {
      this.paramForm.id = row.id
      this.paramForm.param_name = row.param_name
      this.paramForm.param_desc = row.param_desc
      this.paramForm.param_detail = row.param_detail
      this.paramForm.data_type = row.data_type
      this.paramForm.status = row.status
      if (row.child_id !== null && row.data_type === 11) {
        this.paramForm.list_child_type = Number(row.child_id)
        var item = row.child_list
        this.listTypeOptions = [{value: item.id, data_type: item.param_name + ":" + item.param_desc}]
      }
      if (row.child_id !== null && row.data_type === 12) {
        this.selectedValues = row.field_list
        var dataStrArr = row.child_id.split(',')
        var dataIntArr = []
        dataStrArr.forEach(item => {
          dataIntArr.push(+item);
        });
        this.paramForm.dict_child_type = dataIntArr
        this.dictTypeOptions = row.child_list.map(item => {
          return {value: item.id, data_type: item.param_name + ":" + item.param_desc};
        });
      }
      //Field类型
      if (row.child_id !== null && row.data_type === 22) {
        var dataStrArr = row.child_id.split(',')
        var dataIntArr = []
        dataStrArr.forEach(item => {
          dataIntArr.push(+item);
        });
        this.paramForm.dict_child_type = dataIntArr
        this.dictTypeOptions = row.child_list.map(item => {
          return {value: item.id, data_type: item.param_name + ":" + item.param_desc, field_list: item.field_list};
        });
      }
      if (row.data_type === 13) {
        if (row.select_info_id == null) {
          this.crearEnumOptions()
        } else {
          this.paramForm.select_info_id = row.select_info_id
          this.updateEnumOptions(this.paramForm.select_info_id)
        }
      }
      this.paramFormVisible = true
    },
    // 打开新增表单
    openAddDialog() {
      this.paramSelect()
      this.readOnly = false
      this.dialogTitle = '新增参数'
      this.paramForm = {}
      this.paramFormVisible = true
    },
    // 打开编辑表单
    openEditDialog(row) {
      this.paramForm = {}
      this.readOnly = true
      this.selectedValues = row.field_list
      this.displayForm(row)
      this.dialogTitle = '编辑参数'
    },
    // 打开表单
    openForm() {
      this.initValidRule()
      this.$forceUpdate()
    },
    // 关闭表单
    closeForm() {
      this.paramForm = {}
      this.resetForm()
    },
    // 设置校验规则
    initValidRule() {
      this.paramRules = {
        "data_type": [{
          required: true, message: '请输入类型', trigger: 'blur'
        }],
        "param_name": [{
          required: true, message: '请输入英文名', trigger: 'blur'
        }],
        "param_desc": [{
          required: true, message: '请输入中文名', trigger: 'blur'
        }],
        "param_detail": [{
          required: true, message: '请输入注释', trigger: 'blur'
        }]
      }
      this.$nextTick(() => {
        this.$refs['paramForm'].clearValidate();
      })
    },
    // 重置表单校验
    resetForm() {
      this.$refs['paramForm'].clearValidate();
      this.$refs['paramForm'].resetFields();
    },
    // 参数查询结果集存入选择框
    // 搜索参数下拉框输入
    // 根据参数名查询参数列表(下拉框，拉到最底触发)
    listTypeSelect(paramCondition) {
      this.paramSelect(paramCondition, 'listType')
    },
    dictTypeSelect(paramCondition) {
      this.paramSelect(paramCondition, 'dictType')
    },
    async paramSelect(paramCondition, type) {
      let query = '?page_size=' + this.querySize
      if (paramCondition) {
        paramCondition = paramCondition.toString().replace('/,/g', '');
        if (paramCondition != '') {
          query += '&condition=' + paramCondition
        }
      }
      const {data: result} = await this.$http.get(PARAM_LIST + query);
      if (result.code == 0 && result.data.length > 0) {
        if (type == 'dictType') {
          this.dictTypeOptions = result.data.map(item => {
            return {value: item.id, data_type: item.param_name + ":" + item.param_desc};
          });
        } else if (type == 'listType') {
          this.listTypeOptions = result.data.map(item => {
            return {value: item.id, data_type: item.param_name + ":" + item.param_desc};
          });
        } else {
          this.listTypeOptions = result.data.map(item => {
            return {value: item.id, data_type: item.param_name + ":" + item.param_desc};
          });
          this.dictTypeOptions = result.data.map(item => {
            return {value: item.id, data_type: item.param_name + ":" + item.param_desc};
          });
        }
      } else {
        this.listTypeOptions = []
        this.dictTypeOptions = []
      }
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
    formDataType(type, child_id, child_list) {
      const map = {
        1: 'Int', 2: 'Float', 3: 'Boolean', 4: 'String', 5: 'Date', 6: 'Datetime', 7: 'Instance',
        11: '[ ]', 12: '{ }', 13: 'Enum', 21: 'Page', 22:'Field'
      }
      var res = ''
      if (type === 11) {
        if (child_id && child_list) {
          res = child_list.param_name
        }
      }
      res += map[type]
      return res
    },
    getDataTypePrefix(type) {
      const map = {
        1: 'i_', 2: 'f_', 3: 'b_', 4: 's_', 5: 'dt_', 6: 'dt2_', 7: 'obj_',
        11: 'a_', 12: 'o_', 13: 'e_', 21: 'P_',22:'Fi_'
      }
      return map[type]
    },
    getStyleType(type){
      const map = {
        1:'width:',2:'color:'
      }
      return map[type]
    },
    // 解决表格树形展示问题
    getRowKey(row) {
      return row.key
    },
    // 懒加载重复查询接口响应，（解决不同后端节点响应时间不一样问题）
    loadChildList(tree, treeNode, resolve) {
      this.getChildParam(tree.child_id, tree.data_type)
      let timer = setInterval(() => {
        this.resolveNode(resolve, timer)
      }, 100)
      setTimeout(() => {
        if (timer && this.tempNode.length == 0) {
          clearInterval(timer)
        }
      }, 1500)
    },
    resolveNode(resolve, timer) {
      setTimeout(() => {
        if (this.tempNode.length > 0) {
          resolve(this.tempNode)
          clearInterval(timer)
        }
      }, 0)
    },
    async getChildParam(child_id, data_type) {
      var query = '?child_id=' + child_id + '&data_type=' + data_type
      this.tempNode = []
      const {data: result} = await this.$http.get(PARAM_CHILD + query);
      if (result.code != 0) {
        this.$message.error(result.msg);
      }
      this.tempNode = result.data
    },
    // 提交审核
    async commitParam(row, status) {
      var release = '?id=' + row.id + '&status=' + status
      const {data: result} = await this.$http.get(PARAM_COMMIT + release);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success('操作成功!');
        this.getParamList()
      }
    },
    // 审批
    async approveParam(row, status) {
      var release = '?id=' + row.id + '&status=' + status
      const {data: result} = await this.$http.get(PARAM_APPROVE + release);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success('操作成功!');
        this.getParamList()
      }
    },
    // 文字高亮显示
    showHighLightData(val) {
      if (val && this.condition) {
        return val.replaceAll(this.condition, '<font style="background-color: yellow" color="black">' + this.condition + "</font>");
      } else {
        return val;
      }
    },
    // 输入框触发
    changeMessage() {
      this.$forceUpdate()
    },
    // 下拉框改变
    changedEnumOptions(isOpen) {
      if (!isOpen) {
        this.crearEnumOptions()
      }
    },
    // 更新下拉框数据
    updateEnumOptions(select_info_id) {
      if (select_info_id) {
        this.changeEnumSelect(select_info_id)
      } else {
        this.crearEnumOptions()
      }
    },
    // 渲染下拉框数据
    renderEnumOptions(id, enumOptions) {
      if (id) { // 从map中取数据
        this.enumParamOptions = this.enumParamOptionsMap[id.toString()]
      } else { // 调接口查询到新的数据，存入map
        this.enumParamOptions = enumOptions
        this.enumParamOptionsMap[this.tempKey] = enumOptions
      }
    },
    // 清空下拉框数据
    crearEnumOptions() {
      this.enumParamOptions = []
    },
    // 输入框触发,默认查完渲染
    changeEnumSelect(select_info_id) {
      var id = 0
      if (select_info_id) {
        id = select_info_id
      } else {
        id = this.paramForm.select_info_id
      }
      var keys = Object.keys(this.enumParamOptionsMap)
      this.tempKey = id
      if (keys.includes(id.toString())) {
        // 从页面缓存map中取数据
        this.renderEnumOptions(id, null)
        return
      }
      var arr = this.globalSelectOptions
      var type = 0
      var sql = ''
      for (var item of arr) {
        if (item.id == id) {
          type = item.type
          sql = item.sql
          break
        }
      }
      this.$forceUpdate()
      // 调接口查询下拉框数据，并在返回数据后调用渲染函数，将数据放到enumParamOptionsMap
      this.enumTypeShow(type, sql, true)
    },
    clearChildOptions(data) {
      this.paramForm.list_child_type = undefined
      this.paramForm.dict_child_type = undefined
    },
    rowStyle({row, rowIndex}) {
      row.index = rowIndex + 1
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.param-html-box {
  padding: 20px;
  min-width: 600px;
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

#paramPage {
  text-align: left;
}

#paramForm .el-select {
  width: 85%;
}

#paramForm .el-input {
  width: 85%;
}

#formBtn {
  margin-right: 24px
}
</style>
<style>
.processParam .el-table__header {
  width: 100% !important;
}

.processParam .el-table__body {
  width: 100% !important;
}

.el-scrollbar .el-scrollbar__wrap--hidden-default {
  max-height: 390px !important;
}

.custom-label {
  width: 80px; /* 设置固定宽度 */
  word-wrap: break-word; /* 在过长时自动换行 */
}

.mx-1{
  width: 80px; /* 设置固定宽度 */
  word-wrap: break-word; /* 在过长时自动换行 */
}

</style>
