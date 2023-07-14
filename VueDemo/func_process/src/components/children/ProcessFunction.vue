<template>
  <div class="processFunction">
    <div class="function-html-box">
      <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer"/>

      <div class="query-box">
        <el-row :gutter="20">
          <el-col :span="9" style="float: left;margin-left:10px;">
            <el-button-group>
              <el-badge
                v-for="item in statusOptions"
                style="margin-right: 10px; padding-bottom: 10px;"
                :key="item.value"
                :value="functionCount[item.value] ? functionCount[item.value] : 0"
                :max="999999"
              >
                <el-button
                  type="primary"
                  @click="clickFunctionList(item)"
                  :plain="onclickStatus != item.value"
                >
                  {{ item.label }}
                </el-button>
              </el-badge>
            </el-button-group>
          </el-col>
          <!--        <el-button v-for="item in statusOptions"-->
          <!--                   style="float:left"-->
          <!--                   :key="item.value"-->
          <!--                   :max="999999" type="primary" @click="selectFunctionList" plain>-->
          <!--          {{ item.label }}-->
          <!--        </el-button>-->
        </el-row>
        <el-row :gutter="20">
          <el-col :span="6">
            <el-input placeholder="请输入内容" @input="selectFunctionList" clearable v-model="condition"
                      class="input-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getFunctionList"></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="addBtn" @click="openAddDialog" type="primary">新增函数</el-button>
          </el-col>
          <!--          <el-col :span="2">-->
          <!--            <el-select v-model="query_status" @change="selectFunctionList">-->
          <!--              <el-option v-for="item in statusOptions" :key="item.value" :label="item.label"-->
          <!--                         :value="item.value"></el-option>-->
          <!--            </el-select>-->
          <!--          </el-col>-->
          <el-col :span="3">
            <el-select v-model="query_class_name" @change="selectFunctionList" filterable @input="$forceUpdate()">
              <el-option
                v-for="item in classQueryOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="2" v-if="query_status === 3">
            <el-select v-model="is_auto_test" @change="selectFunctionList" filterable @input="$forceUpdate()">
              <el-option
                v-for="item in autoTestOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <ApproveComments ref="approveComments"/>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="functionFormVisible" width='50%'
                 @open='openForm' @close="closeForm">
        <el-form id="functionForm" :model="functionForm" ref="functionForm" :rules="functionRules">
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="类名" :label-width="formLabelWidth">
                <el-select v-model="functionForm.class_name" placeholder="请选择类名" :disabled="readOnly" filterable
                           @input="$forceUpdate()">
                  <el-option
                    v-for="item in functionTypeOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="返回码" :label-width="formLabelWidth" prop="error_code_list">
                <el-select v-model="functionForm.error_code_list" multiple filterable remote reserve-keyword
                           placeholder="请选择返回码"
                           @input="$forceUpdate()" :remote-method="errorCodeSelect">
                  <ul class="infinite-list" style="overflow:auto">
                    <li v-for="item in errorCodeOptions" class="infinite-list-item" :key="item.value">
                      <el-option :label="item.label" :value="item.value" :key="item.value"></el-option>
                    </li>
                  </ul>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="英文名" :label-width="formLabelWidth" prop="function_name">
                <el-input v-model="functionForm.function_name" placeholder="请输入英文名" @input="$forceUpdate()"
                          :disabled="readOnly&&functionForm.status>0" autocomplete="off">
                  <template slot="prepend" v-if="!readOnly && functionForm.class_name === global_function_prefix">
                    <span>{{ global_function_prefix }}</span>
                  </template>
                </el-input>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="中文名" :label-width="formLabelWidth" prop="function_desc">
                <el-input v-model="functionForm.function_desc" placeholder="请输入中文名"
                          @input="$forceUpdate()" maxlength="20" autocomplete="off"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="参数" :label-width="formLabelWidth" prop="param_list">
                <el-select v-model="functionForm.param_list" multiple filterable remote reserve-keyword
                           placeholder="请选择参数"
                           @input="$forceUpdate()" :remote-method="paramSelect"
                           :disabled="readOnly&&functionForm.status>0" @change="checkSubmit">
                  <ul class="infinite-list" style="overflow:auto">
                    <li v-for="item in paramOptions" class="infinite-list-item" :key="item.value">
                      <el-option :label="item.label" :value="item.value" :key="item.value"></el-option>
                    </li>
                  </ul>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="返回值" :label-width="formLabelWidth" prop="return_list">
                <el-select v-model="functionForm.return_list" multiple filterable remote reserve-keyword
                           placeholder="请选择返回值"
                           @input="$forceUpdate()" :remote-method="returnSelect"
                           :disabled="readOnly&&functionForm.status>0">
                  <ul class="infinite-list" style="overflow:auto">
                    <li v-for="item in returnOptions" class="infinite-list-item" :key="item.value">
                      <el-option :label="item.label" :value="item.value" :key="item.value"></el-option>
                    </li>
                  </ul>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="路径" :label-width="formLabelWidth" prop="url">
                <el-input v-model="functionForm.url" placeholder="请输入路径" @input="$forceUpdate()"
                          autocomplete="off">
                  <template slot="prepend" v-if="!readOnly">
                    <span>{{ svn_prefix }}</span>
                  </template>
                </el-input>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="需求人" :label-width="formLabelWidth" prop="s_principal">
                <el-select v-model="functionForm.s_principal" filterable remote reserve-keyword
                           placeholder="请选择需求人"
                           @input="$forceUpdate()">
                  <el-option v-for="item of person_options" :key="item" :label="item" :value="item">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="注释" :label-width="formLabelWidth" prop="function_detail">
                <el-input v-model="functionForm.function_detail" placeholder="请输入注释" autocomplete="off"
                          type="textarea"
                          @input="$forceUpdate()" style="width: 85%" :autosize="{ minRows: 4, maxRows: 8}"></el-input>
              </el-form-item>
              <el-form-item label="测试链接" :label-width="formLabelWidth" prop="test_url">
                <el-input v-model="functionForm.test_url" placeholder="请输入测试链接" autocomplete="off"
                          type="input"
                          @input="$forceUpdate()" style="width: 85%"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="开发人" :label-width="formLabelWidth" prop="developer">
                <el-select filterable placeholder="请选择开发人" v-model="functionForm.developer"
                           @input="$forceUpdate()">
                  <el-option v-for="item of person_options_desc" :key="item.key" :label="item.label"
                             :value="item.label">
                    <span style="float: left;">{{ item.label }}</span>
                    <span style="float: left;margin-right: 20px"></span>
                    <span style="float: right;color: #3a87ad">{{ item.count }}个</span>
                  </el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="Review人" :label-width="formLabelWidth" prop="reviewer">
                <el-select v-model="functionForm.reviewer" filterable remote reserve-keyword
                           placeholder="请选择Review人"
                           @input="$forceUpdate()">
                  <el-option v-for="item of person_options" :key="item" :label="item" :value="item">
                  </el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="测试人" :label-width="formLabelWidth" prop="publish_person">
                <el-select v-model="functionForm.publish_person" filterable remote reserve-keyword
                           placeholder="请选择测试人"
                           @input="$forceUpdate()">
                  <el-option v-for="item of tester_person_options" :key="item" :label="item" :value="item">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="functionFormVisible = false">取 消</el-button>
          <ParamExample style="margin-left: 10px; margin-right: 10px" @saveExample="saveParamExample($event)"
                        v-bind:functionForm="functionForm" ref="paramExample"/>
          <el-button type="primary" @click="submitForm('functionForm')">确 定</el-button>
        </div>
      </el-dialog>
      <div class="table-box">
        <el-pagination id="functionPage" :total="total"
                       @size-change="handleSizeChange" @current-change="handleCurrentChange"
                       :current-page.sync="pageNo" :page-sizes="[10, 50, 100, 500]"
                       :page-size="pageSize" layout="total, sizes, prev, pager, next">
        </el-pagination>
        <el-table stripe :data="functionList" border style="width:100%;padding: 0" :row-class-name="rowStyle">
          <el-table-column type="index" width="80px" label="序号">
            <template scope="scope">
              <el-popover placement="top-start" width="260" trigger="hover">
                <div>
                  <div v-if="scope.row.s_principal">需求人：{{ scope.row.s_principal }}</div>
                  <div v-if="scope.row.author">创建人：{{ scope.row.author }}</div>
                  <div v-if="scope.row.create_time">创建时间：{{ scope.row.create_time }}</div>
                  <div v-if="scope.row.status !== 1 && scope.row.release_person">审核人：{{ scope.row.release_person }}
                  </div>
                  <div v-if="scope.row.status !== 1 && scope.row.release_time">审核时间：{{ scope.row.release_time }}
                  </div>
                  <div v-if="scope.row.developer">开发人：{{ scope.row.developer }}</div>
                  <div v-if="scope.row.develop_time">开发时间：{{ scope.row.develop_time }}</div>
                  <div v-if="scope.row.reviewer">Reviewer：{{ scope.row.reviewer }}</div>
                  <div v-if="scope.row.review_time">Review时间：{{ scope.row.review_time }}</div>
                  <div v-if="scope.row.publish_person && scope.row.status ===4">测试人：{{
                      scope.row.publish_person
                    }}
                  </div>

                  <div v-if="scope.row.status === 3 && scope.row.publish_person">发布人：{{ scope.row.publish_person }}
                    <span v-if="scope.row.status === 3 && scope.row.is_auto_test===1">(已实现自动化测试)
                    </span>
                  </div>
                  <div v-if="scope.row.status === 3 && scope.row.release_time">发布/测试时间：{{ scope.row.publish_time }}
                  </div>
                </div>
                <div slot="reference">
                  <span style="margin-right: 10px">{{ scope.row.index }}</span>
                  <span v-if="scope.row.status === 0" class="no_active_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 1" class="submit_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 2" class="release_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 3" class="publish_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 4" class="publish_class">{{ formStatus(scope.row.status) }}</span>
                  <span v-if="scope.row.status === 5" class="publish_class">{{ formStatus(scope.row.status) }}</span>
                </div>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column prop="function_name" maxlength=255 label="函数名" contentEditable="true"
                           align="left" width="220px" min-width="200px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.function_name)"></span>
              <br/>
              <span v-html="showHighLightData(scope.row.function_desc)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="param_list" label="参数" contentEditable="true"
                           align="left" width="250px" min-width="200px">
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
                      <span>:</span>
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
          <el-table-column prop="function_detail" maxlength=500 label="注释" contentEditable="true" align="left"
                           width="300px" min-width="300px">
            <template slot-scope="scope">
              <el-input v-model="scope.row.function_detail" autocomplete="off" type="textarea" readonly
                        @input="$forceUpdate()" style="width: 100%" :autosize="{ minRows: 3}">
                <span v-html="showHighLightData(scope.row.function_detail)"></span>
              </el-input>
            </template>
          </el-table-column>
          <el-table-column label="操作" contentEditable="true" align="center" width="100px">
            <template slot-scope="scope">
              <el-button @click="commitFunction(scope.row, 1)" type="text" size="medium"
                         v-if="(!scope.row.status || scope.row.status===0)">提交审核
              </el-button>
              <el-button @click="commitFunction(scope.row, 0)" type="text" size="medium"
                         v-if="scope.row.status===1">撤回提交
              </el-button>
              <el-button @click="approveFunction(scope.row, 2)" type="text" size="medium"
                         v-if="scope.row.status===1">审核
              </el-button>
              <el-button @click="reviewFunction(scope.row, 5)" type="text" size="medium"
                         v-if="scope.row.status===2">Review
              </el-button>
              <el-button @click="totestFunction(scope.row, 4)" type="text" size="medium"
                         v-if="scope.row.status===5">转测试
              </el-button>
              <el-button @click="toDevelopFunction(scope.row, 5)" type="text" size="medium"
                         v-if="scope.row.status===4 | scope.row.status===5">驳回待实现
              </el-button>
              <el-button @click="approveFunction(scope.row, 1)" type="text" size="medium"
                         v-if="releaseRole && scope.row.status===2">撤回审核
              </el-button>
              <el-button @click="approveFunction(scope.row, 0);
              $refs.approveComments.openComment(2, scope.row.id, scope.row.author)"
                         type="text" size="medium" v-if="releaseRole && scope.row.status===1">驳回
              </el-button>
              <el-button type="text" size="medium"
                         @click="$refs.approveComments.openComment(2, scope.row.id, scope.row.author)">
                审核意见
              </el-button>
              <br/>
              <el-button @click="readyShowFunction(scope.row.id, scope.row.url)" type="text" size="medium">查看
              </el-button>
              <el-button @click="readyRunFunction(scope.row)" type="text" size="medium">调试</el-button>
              <br/>
              <el-button @click="openEditDialog(scope.row)" type="text" size="medium">编辑</el-button>
              <el-button @click="deleteFunction(scope.row)" type="text" size="medium" v-if="scope.row.status < 2">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <el-drawer
        size="50%"
        destroy-on-close
        :visible.sync="drawerVisible"
        :with-header="false">
        <DebugFunction v-bind:debugData="debugData" :closeDrawer="closeDrawer" :readyShowFunction="readyShowFunction"/>
      </el-drawer>
      <ShowFunctionContentView v-bind:showFunctionContent="showFunctionContent"/>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="developerVisible"
                 width='30%'>
        <el-row>
          <el-col>
            <el-select filterable placeholder="请选择开发人" v-model="developer"
                       @input="$forceUpdate()" @change="handleDevelopChange">
              <el-option v-for="item of person_options_desc" :key="item.key" :label="item.label" :value="item.label">
                <span style="float: left;">{{ item.label }}</span>
                <span style="float: left;margin-right: 20px"></span>
                <span style="float: right;color: #3a87ad">{{ item.count }}个</span>
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <div slot="footer" class="dialog-footer">
          <el-button @click="developerVisible = false">取 消</el-button>
          <el-button type="primary" @click="developerSubmit()">确 定</el-button>
        </div>
      </el-dialog>
      <el-dialog :title="Review" :close-on-click-modal="false"
                 :visible.sync="reviewVisible"
                 width='30%'>
        <el-row>
          <el-col>
            <el-select filterable placeholder="请选择Review人" v-model="reviewer"
                       @input="$forceUpdate()" @change="handleReviewChange">
              <el-option v-for="item of person_options" :key="item" :label="item" :value="item">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <div slot="footer" class="dialog-footer">
          <el-button @click="reviewVisible = false">取 消</el-button>
          <el-button type="primary" @click="reviewSubmit()">确 定</el-button>
        </div>
      </el-dialog>
      <el-dialog :close-on-click-modal="false"
                 :visible.sync="testVisible"
                 width='30%'>
        <el-row>
          <el-col>
            <el-select filterable placeholder="请选择测试人员" v-model="tester"
                       @input="$forceUpdate()" @change="handleTestChange">
              <el-option v-for="item of tester_person_options" :key="item" :label="item" :value="item">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <div slot="footer" class="dialog-footer">
          <el-button @click="testVisible = false">取 消</el-button>
          <el-button type="primary" @click="totestSubmit()">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>


</template>
<script>
import DebugFunction from './DebugFunction.vue'
import ParamExample from './child_pop/ParamExample.vue'
import ShowFunctionContentView from './child_pop/ShowFunctionContentView.vue'
import SoftwareMaintainerView from '../maintainPeople/SoftwareMaintainerView.vue'
import ApproveComments from './child_pop/ApproveComments.vue'
import FunctionReturnMessage from './child_pop/FunctionReturnMessage.vue'
import FunctionparamMessage from "./child_pop/FunctionParamMessage.vue";

export default {
  name: "processFunction",
  components: {
    FunctionparamMessage,
    DebugFunction,
    ParamExample,
    ShowFunctionContentView,
    SoftwareMaintainerView,
    ApproveComments,
    FunctionReturnMessage
  },
  data() {
    return {
      // 组件相关
      software_maintainer: '倪恒',
      functionFormVisible: false,
      developerVisible: false,
      formLabelWidth: '100px',
      readOnly: false,
      dialogTitle: '',
      Review: '',
      functionRules: {},
      drawerVisible: false,
      submitFlag: true,
      releaseRole: false,
      // 列表数据相关
      pageNo: 1,
      pageSize: 10,
      total: 0,
      formItemSpan: 12,
      condition: null,
      query_status: 2,
      onclickStatus: 2,
      query_class_name: null,
      is_auto_test: null,
      statusOptions: [
        {value: 'all', label: '全部'},
        {value: 0, label: '草稿'},
        {value: 1, label: '待审核'},
        {value: 2, label: '待实现'},
        {value: 5, label: 'Review'},
        {value: 4, label: '待测试'},
        {value: 3, label: '已发布'}
      ],
      autoTestOptions: [
        {value: null, label: '全部'},
        {value: 0, label: '未自动化'},
        {value: 1, label: '已自动化'}
      ],
      functionList: [],
      functionTypeOptions: [],
      classQueryOptions: [],
      global_function_prefix: 'g_',
      class_name_separate: "::",
      svn_prefix: 'SVN://',
      functionForm: {
        id: null,
        class_name: '',
        function_name: '',
        function_detail: '',
        function_desc: '',
        s_principal: '',
        url: '',
        status: 0,
        param_list: [],
        param_example_list: [],
        return_list: [],
        error_code_list: [],
        developer: '',
        reviewer: '',
        test_url: '',
        publish_person: ''
      },
      code_prefix: '{code: 0, msg: "Success", data: {',
      code_suffix: '}}',
      // 下拉选择框相关
      querySize: 50,
      paramOptions: [],
      returnOptions: [],
      errorCodeOptions: [],
      person_options: [],
      tester_person_options: [],
      person_options_desc: [],
      functionCount: [],
      developerRow: {},
      developer: "",
      reviewRow: {},
      reviewer: "",
      reviewVisible: false,
      testRow: {},
      tester: "",
      testVisible: false,
      // 调试面板数据
      debugData: {
        functionData: {},
        paramList: [],
        returnList: [],
        errorCodeList: [],
        value: null
      },
      // 函数体展示数据
      showFunctionContent: {
        functionContent: '',
        url: '',
        functionContentVisible: false
      },
    }
  },
  created() {
    this.initReleaseRole();
    this.initComment();
    this.getFunctionList();
    this.getPersonOptions();
    this.getTesterOptions();
    this.getPersonOptionsDesc();
  },
  methods: {
    // 自动查询未读的审核意见
    initComment() {
      if (localStorage.getItem("comment_no_read")) {
        this.query_status = 'all'
        this.condition = '未读'
      }
    },
    // 是否有审核权限
    initReleaseRole() {
      var flag = localStorage.getItem("approve_person")
      this.releaseRole = flag === 'true'
    },
    initqueryOption(paramCondition) {
      let query = '?page_size=' + this.querySize + '&release=2'
      if (paramCondition != null) {
        paramCondition = paramCondition.toString().replace('/,/g', '');
        if (paramCondition != '') {
          query += '&condition=' + paramCondition
        }
      }
      return query
    },
    // 参数查询结果集存入选择框
    // 搜索参数下拉框输入
    async paramSelect(paramCondition) {
      let isParam = 'isParam'
      this.getParamListByName(paramCondition, isParam);
    },
    // 搜索返回值下拉框输入
    async returnSelect(paramCondition) {
      let isReturn = 'isReturn'
      this.getParamListByName(paramCondition, isReturn);
    },
    // 搜索返回值下拉框输入
    async errorCodeSelect(paramCondition) {
      let query = this.initqueryOption(paramCondition)
      const {data: result} = await this.$http.get(ERROR_CODE_LIST + query);
      if (result.code == 0 && result.data.length > 0) {
        this.errorCodeOptions = result.data.map(item => {
          return {value: item.id, label: item.name + ":" + item.code + ":" + item.msg};
        });
      } else {
        this.errorCodeOptions = []
      }
    },
    // 根据参数名查询参数列表
    async getParamListByName(paramCondition, type) {
      let query = this.initqueryOption(paramCondition)
      const {data: result} = await this.$http.get(PARAM_LIST + query);
      if (result.code == 0 && result.data.length > 0) {
        if (type === 'isParam') {
          this.paramOptions = result.data.map(item => {
            return {value: item.id, label: item.param_name + ":" + item.param_desc};
          });
        } else {
          this.returnOptions = result.data.map(item => {
            return {value: item.id, label: item.param_name + ":" + item.param_desc};
          });
        }
      } else {
        if (type === 'isParam') {
          this.paramOptions = []
        } else {
          this.returnOptions = []
        }
      }
    },
    // 根据函数id查询下拉框数据
    async showSelectOptions(param_list, result_list, error_code_list) {
      this.paramOptions = param_list.map(item => {
        return {value: item.id, label: item.param_name + ":" + item.param_desc};
      });
      this.returnOptions = result_list.map(item => {
        return {value: item.id, label: item.param_name + ":" + item.param_desc};
      });
      this.errorCodeOptions = error_code_list.map(item => {
        return {value: item.id, label: item.name + ":" + item.code + ":" + item.msg};
      });
    },
    // 搜索列表
    selectFunctionList() {
      this.pageNo = 1
      this.getFunctionList()
    },
    clickFunctionList(item) {
      this.pageNo = 1
      this.query_status = item.value
      this.getFunctionList()
      this.onclickStatus = item.value
    },
    // 查询列表
    async getFunctionList() {
      this.getFunctionCount();
      let query = '?page_no=' + this.pageNo + '&page_size=' + this.pageSize
      if (this.condition != null && this.condition != '') {
        this.condition = this.condition.trim()
        query += '&condition=' + this.condition
      }
      if (this.query_status !== 'all') {
        query += '&status=' + this.query_status
      }
      if (this.query_class_name !== null) {
        query += '&class_name=' + this.query_class_name
      }
      if (this.is_auto_test !== null) {
        query += '&is_auto_test=' + this.is_auto_test
      }
      const {data: result} = await this.$http.get(FUNCTION_LIST + query);
      if (result.code != 0) {
        this.$message.error(result.msg);
      }
      this.functionList = result.data.data;
      this.total = result.data.total;
    },
    // 删除
    async delFunction(id) {
      var func_data = {
        id: id
      }
      const {data: result} = await this.$http.post(FUNCTION_DEL, func_data);
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.$message.success(result.msg)
      }
      this.functionFormVisible = false
      this.getFunctionList()
    },
    // 删除二次确认
    deleteFunction(row) {
      this.$confirm('确定删除' + row.function_name + '吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delFunction(row.id)
      })
    },
    // 调整分页数据大小
    handleSizeChange(newSize) {
      this.pageSize = newSize;
      this.getFunctionList();
    },
    // 调整当前页码
    handleCurrentChange(newPage) {
      this.pageNo = newPage;
      this.getFunctionList();
    },
    // 打开新增表单，先执行openAddDialog后执行openForm
    openAddDialog() {
      this.readOnly = false
      this.dialogTitle = '新增函数'
      this.functionForm = {
        class_name: this.global_function_prefix,
        function_name: "",
        function_desc: "",
        function_detail: "",
        url: "",
        status: 0,
        param_list: [],
        return_list: [],
        error_code_list: [],
      }
      this.functionFormVisible = true
    },
    // 打开编辑表单，先执行openEditDialog后执行openForm
    openEditDialog(row) {
      this.readOnly = true
      this.displayForm(row)
      this.dialogTitle = '编辑函数'
    },
    //回显数据
    displayForm(row) {
      this.functionForm.id = row.id
      if (row.class_name) {
        this.functionForm.class_name = row.class_name
      } else {
        this.functionForm.class_name = this.global_function_prefix
      }
      if (row.function_name.search(this.class_name_separate) != -1) {
        this.functionForm.function_name = row.function_name.split(this.class_name_separate)[1]
      } else {
        this.functionForm.function_name = row.function_name
      }
      this.functionForm.function_desc = row.function_desc
      this.functionForm.function_detail = row.function_detail
      this.functionForm.s_principal = row.s_principal
      this.functionForm.developer = row.developer
      this.functionForm.develop = row.develop_time
      this.functionForm.reviewer = row.reviewer
      this.functionForm.publish_person = row.publish_person
      this.functionForm.test_url = row.test_url
      this.functionForm.url = row.url
      this.functionForm.status = row.status
      // 下拉框数据
      let param_list = row.param_list === undefined ? [] : row.param_list
      let return_list = row.return_list === undefined ? [] : row.return_list
      let error_code_list = row.error_code_list === undefined ? [] : row.error_code_list
      this.showSelectOptions(param_list, return_list, error_code_list)
      let param_id_list = []
      let return_id_list = []
      let error_code_id_list = []
      for (var item of param_list) {
        param_id_list.push(item.id)
      }
      for (var item of return_list) {
        return_id_list.push(item.id)
      }
      for (var item of error_code_list) {
        error_code_id_list.push(item.id)
      }
      this.functionForm.param_list = param_id_list
      this.functionForm.param_example_list = param_list
      this.functionForm.return_list = return_id_list
      this.functionForm.error_code_list = error_code_id_list
      this.functionFormVisible = true
    },
    // 先执行openAddDialog/openEditDialog后执行openForm
    openForm() {
      this.initValidRule()
      if (!this.readOnly) {
        this.paramSelect()
        this.returnSelect()
        this.errorCodeSelect()
      }
      this.$forceUpdate()
    },
    // 表单关闭时触发
    closeForm() {
      this.paramOptions = []
      this.returnOptions = []
      this.errorCodeOptions = []
      this.functionForm = {}
      this.resetForm()
    },
    // 全局下拉框枚举值查看效果,类列表查询时触发
    async enumClassTypeShow(classAll) {
      const baseOption = [{value: this.global_function_prefix, label: '全局函数'}]
      const classOptions = classAll.map(item => {
        return {value: item.class_name, label: item.class_name};
      });
      this.functionTypeOptions = baseOption.concat(classOptions)
      const allQueryOption = [{value: null, label: '全部'}]
      this.classQueryOptions = allQueryOption.concat(this.functionTypeOptions)
    },
    // 手动校验
    emptyCheck() {
      var flag = true
      if (this.functionForm.error_code_list.length == 0) {
        this.$message.info("返回码不能为空")
        flag = false
      }
      if (flag && (!this.functionForm.function_name || !this.functionForm.function_name.trim())) {
        this.$message.info("英文名不能为空")
        flag = false
      }
      if (flag && (!this.functionForm.function_desc || !this.functionForm.function_desc.trim())) {
        this.$message.info("中文名不能为空")
        flag = false
      }
      if (flag && (!this.functionForm.url || !this.functionForm.url.trim())) {
        this.$message.info("路径不能为空")
        flag = false
      }
      if (flag && (!this.functionForm.function_detail || !this.functionForm.function_detail.trim())) {
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
        let function_data = {
          param_example_list: this.functionForm.param_example_list,
          function_desc: this.functionForm.function_desc === undefined ? null : this.functionForm.function_desc.trim(),
          function_detail: this.functionForm.function_detail === undefined ? null : this.functionForm.function_detail.trim(),
          param_list: this.functionForm.param_list,
          return_list: this.functionForm.return_list,
          error_code_list: this.functionForm.error_code_list
        }
        if (this.functionForm.s_principal) {
          function_data.s_principal = this.functionForm.s_principal.trim()
        }
        if (this.functionForm.developer) {
          function_data.developer = this.functionForm.developer.trim()
        }
        if (this.functionForm.reviewer) {
          function_data.reviewer = this.functionForm.reviewer.trim()
        }
        if (this.functionForm.publish_person) {
          function_data.publish_person = this.functionForm.publish_person.trim()
        }
        if (this.functionForm.test_url) {
          function_data.test_url = this.functionForm.test_url.trim()
        }
        if (this.functionForm.id == null) {
          if (this.functionForm.class_name == this.global_function_prefix) {
            function_data.class_name = null
            function_data.function_name = this.global_function_prefix + this.functionForm.function_name.trim()
          } else {
            function_data.class_name = this.functionForm.class_name
            function_data.function_name = this.functionForm.class_name + this.class_name_separate + this.functionForm.function_name.trim()
          }
          function_data.url = this.functionForm.url === undefined ? null : this.svn_prefix + this.functionForm.url.trim()
          const {data: result} = await this.$http.post(FUNCTION_ADD, function_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        } else {
          function_data.url = this.functionForm.url === undefined ? null : this.functionForm.url.trim()
          function_data.id = this.functionForm.id
          function_data.class_name = null
          if (this.functionForm.class_name == this.global_function_prefix) {
            function_data.function_name = this.functionForm.function_name.trim()
          } else {
            function_data.function_name = this.functionForm.class_name + this.class_name_separate + this.functionForm.function_name.trim()
          }
          const {data: result} = await this.$http.post(FUNCTION_EDIT, function_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        }
        this.submitFlag = true
        this.functionFormVisible = false
        this.getFunctionList()
      })
    },
    // 打开调试页面
    readyRunFunction(row) {
      this.debugData.functionData = row
      this.debugData.paramList = []
      this.debugData.returnList = []
      this.debugData.errorCodeList = row.error_code_list
      this.selectFunctionParams(row.id)
      this.drawerVisible = true
    },
    closeDrawer(status) {
      this.query_status = status
      this.getFunctionList()
      this.drawerVisible = false
    },
    // 显示函数体内容
    async readyShowFunction(function_id, url) {
      let query = '?function_id=' + function_id
      const {data: result} = await this.$http.get(FUNCTION_SHOW + query)
      if (result.code != 0) {
        this.showFunctionContent.functionContent = result.msg
      } else {
        this.showFunctionContent.functionContent = result.data
      }
      this.showFunctionContent.url = url
      this.showFunctionContent.functionContentVisible = true
    },
    // 查询函数的参数数据和返回信息数据
    async selectFunctionParams(function_id) {
      let query = '?function_id=' + function_id
      const {data: result} = await this.$http.get(FUNC_PARAM_BYFUNID + query);
      if (result.code == 0 && result.data.length > 0) {
        for (var item of result.data) {
          if (item.example === null && (item.data_type === 1 || item.data_type === 2)) {
            item.example = undefined
          }
          item.value = item.example
          if (item.type == 1) {
            this.debugData.paramList.push(item)
          } else {
            this.debugData.returnList.push(item)
          }
        }
      }
    },
    // 设置校验规则
    initValidRule() {
      this.functionRules = {
        "function_name": [{
          required: true, message: '请输入英文名', trigger: 'blur'
        }],
        "function_desc": [{
          required: true, message: '请输入中文名', trigger: 'blur'
        }],
        "error_code_list": [{
          required: true, message: '请选择返回码', trigger: ['blur', 'change']
        }],
        "url": [{
          required: true, message: '请输入路径', trigger: 'blur'
        }],
        "function_detail": [{
          required: true, message: '请输入注释', trigger: 'blur'
        }],
        "s_principal": [{
          required: true, message: '选择需求人', trigger: ['blur', 'change']
        }]
      }
      this.$nextTick(() => {
        this.$refs['functionForm'].clearValidate();
      })
    },
    // 重置表单校验
    resetForm() {
      this.$refs['functionForm'].clearValidate();
      this.$refs['functionForm'].resetFields();
    },
    // 保存参数示例
    saveParamExample(value) {
      this.functionForm.param_example_list = value
    },
    // 校验参数是否设置示例值
    checkSubmit() {
      var exampleMap = this.$refs.paramExample.param_example_list_map
      var temp_list = []
      for (var item of this.functionForm.param_list) {
        if (exampleMap[item]) {
          temp_list.push(exampleMap[item])
        }
      }
      this.$refs.paramExample.param_change_flag = true
      this.functionForm.param_example_list = temp_list
    },
    formStatus(status) {
      if (!status) {
        status = 0
      }

      const map = {
        0: '草稿',
        1: '待审核',
        4: '待测试',
        3: '已发布',
        2: '待实现',
        5: 'Review'
      }
      return map[status]
    },
    // 提交审核
    async commitFunction(row, status) {
      var release = '?id=' + row.id + '&status=' + status
      const {data: result} = await this.$http.get(FUNCTION_COMMIT + release);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success('操作成功!');
        this.getFunctionList()
      }
    },
    async approveFunction(row, status) {
      if (status == 2) {
        this.getPersonOptionsDesc();
        this.developerRow = row;
        this.developer = "";
        this.developerVisible = true;
      } else {
        var release = '?id=' + row.id + '&status=' + status
        const {data: result} = await this.$http.get(FUNCTION_APPROVE + release);
        if (result.code != 0) {
          this.$message.error(result.msg);
        } else {
          this.$message.success('操作成功!');
          this.getFunctionList()
        }
      }
    },
    //转测试
    async totestSubmit(row, status) {
      if (this.tester) {
        var release = '?id=' + this.testRow.id + '&status=4' + '&tester=' + this.tester;
        const {data: result} = await this.$http.get(FUNCTION_TOTEST + release);
        if (result.code != 0) {
          this.$message.error(result.msg);
        } else {
          this.$message.success('操作成功!');
          this.testVisible = false
          this.testRow = {}
          this.tester = ''
          this.getFunctionList()
        }
      } else {
        this.$message.error('请选择测试人员');
      }
    },
    //驳回开发
    async toDevelopFunction(row, status) {
      var release = '?id=' + row.id + '&status=2'
      const {data: result} = await this.$http.get(FUNCTION_DEVELOP + release);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success('操作成功!');
        this.getFunctionList()
      }
    },

    async reviewFunction(row, status) {
      this.reviewRow = row;
      this.reviewer = "";
      this.reviewVisible = true;
    },
    async totestFunction(row, status) {
      this.testRow = row;
      this.tester = "";
      this.testVisible = true;
    },
    // 转开发
    async developerSubmit() {
      if (this.developer) {
        var release = '?id=' + this.developerRow.id + '&status=2' + '&developer=' + this.developer;
        const {data: result} = await this.$http.get(FUNCTION_APPROVE + release);
        if (result.code != 0) {
          this.$message.error(result.msg);
        } else {
          this.$message.success('操作成功!');
          this.developerVisible = false
          this.developerRow = {}
          this.getFunctionList()
        }
      } else {
        this.$message.error('请选择实现人');
      }
    },
    //review
    async reviewSubmit() {
      if (this.reviewer) {
        var release = '?id=' + this.reviewRow.id + '&status=5' + '&reviewer=' + this.reviewer;
        const {data: result} = await this.$http.get(FUNCTION_REVIEW + release);
        if (result.code != 0) {
          this.$message.error(result.msg);
        } else {
          this.$message.success('操作成功!');
          this.reviewVisible = false
          this.reviewRow = {}
          this.getFunctionList()
        }
      } else {
        this.$message.error('请选择Review人');
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
    rowStyle({row, rowIndex}) {
      row.index = rowIndex + 1
    },
    handleDevelopChange(val) {
      this.developer = val;
    },
    handleReviewChange(val) {
      this.reviewer = val;
    },
    handleTestChange(val) {
      this.tester = val;
    },
    async getPersonOptions() {
      if (this.person_options.length > 0) {
        return
      }
      const {data: result} = await this.$http.get(IT_USER);
      if (result.code == 0) {
        this.person_options = result.data.it_user
      } else {
        this.$message.error(result.msg);
      }
    },
    async getTesterOptions() {
      if (this.tester_person_options.length > 0) {
        return
      }
      const {data: result} = await this.$http.get(IT_TESTUSER);
      if (result.code == 0) {
        this.tester_person_options = result.data.it_user
      } else {
        this.$message.error(result.msg);
      }
    },
    async getFunctionCount() {
      const {data: result} = await this.$http.get(FUNCTION_COUNT);
      if (result.code == 0) {
        this.functionCount = result.data.function_count[0]
      } else {
        this.$message.error(result.msg);
      }
    },
    async getPersonOptionsDesc() {
      if (this.person_options_desc.length > 0) {
        return
      }
      const {data: result} = await this.$http.get(IT_USERDESC);
      if (result.code == 0) {
        this.person_options_desc = result.data.it_test_user.data
      } else {
        this.$message.error(result.msg);
      }
    },
    // 从页面管理中跳转过来
    // 打开页面函数列表
    async openPageFunction(s_function_name) {
      this.query_status = null
      this.query_class_name = null
      this.condition = s_function_name
      let query = '?page_no=1&page_size=10'
      query += '&condition=' + this.condition
      const {data: result} = await this.$http.get(FUNCTION_LIST + query);
      if (result.code != 0) {
        this.$message.error(result.msg);
      }
      this.functionList = result.data.data;
      this.total = result.data.total;
      this.openEditDialog(this.functionList[0]);
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.function-html-box {
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

#functionPage {
  text-align: left;
}

#functionForm .el-select {
  width: 85%;
}

#functionForm .el-input {
  width: 85%;
}
</style>

<style>
.processFunction .el-table__header {
  width: 100% !important;
}

.processFunction .el-table__body {
  width: 100% !important;
}

.el-badge__content {
  z-index: 999;
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

.publish_class {
  font-weight: bold;
  color: black;
}
</style>
