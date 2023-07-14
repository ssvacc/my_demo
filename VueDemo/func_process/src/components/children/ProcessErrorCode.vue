<template>
  <div class="processErrorCode">
    <div class="error-code-html-box">
      <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer"/>
      <div class="query-box">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-input placeholder="请输入内容" @input="selectErrorCodeList" clearable v-model="condition"
                      class="input-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getErrorCodeList"></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="addBtn" @click="openAddDialog" type="primary">新增返回码</el-button>
          </el-col>
          <el-col :span="2">
            <CodeMsgPopoverView/>
          </el-col>
        </el-row>
      </div>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="errorCodeFormVisible" width='40%'
                 @open='openForm' @close="closeForm">
        <el-form id="errorCodeForm" :model="errorCodeForm" ref="errorCodeForm" :rules="errorCodeRules">
          <el-form-item label="变量名" :label-width="formLabelWidth" prop="name">
            <el-input v-model="errorCodeForm.name" autocomplete="off" placeholder="请输入变量名" :disabled="readOnly">
              <template slot="prepend" v-if="!readOnly"><span>ER_</span></template>
            </el-input>
          </el-form-item>
          <el-form-item label="code" :label-width="formLabelWidth" prop="code">
            <el-input v-model.number="errorCodeForm.code" autocomplete="off" placeholder="请输入code"
                      :disabled="readOnly"></el-input>
          </el-form-item>
          <el-form-item label="msg" :label-width="formLabelWidth" prop="msg">
            <el-input v-model="errorCodeForm.msg" autocomplete="off" placeholder="请输入msg"
                      @input="changeMessage"></el-input>
          </el-form-item>
          <el-form-item label="作者" :label-width="formLabelWidth" prop="author">
            <el-input v-model="errorCodeForm.author" autocomplete="off" placeholder="请输入作者"
                      @input="changeMessage"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <div id="formBtn">
            <el-button @click="errorCodeFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="submitForm('errorCodeForm')">确 定</el-button>
          </div>
        </div>
      </el-dialog>
      <div class="table-box">
        <el-table stripe
                  :data="errorCodeList" border
                  style="width:100%;padding: 0">
          <el-table-column type="index" label="序号" width="50px">
          </el-table-column>
          <el-table-column prop="name" label="变量名" contentEditable="true" align="left" min-width="150px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.name)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="code" label="code" contentEditable="true" align="left" width="150px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.code)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="msg" label="msg" contentEditable="true" align="left" min-width="150px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.msg)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="author" label="作者" contentEditable="true" align="left" width="150px">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.author)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="status" label="状态" contentEditable="true" align="left" width="100px">
            <template scope="scope">
              {{ formStatus(scope.row.status) }}
            </template>
          </el-table-column>
          <el-table-column prop="create_time" label="创建时间" contentEditable="true" align="left" width="160px">
          </el-table-column>
          <el-table-column prop="update_time" label="更新时间" contentEditable="true" align="left" width="160px">
          </el-table-column>
          <el-table-column label="操作" contentEditable="true" align="center" width="150px">
            <template slot-scope="scope">
              <el-button @click="openEditDialog(scope.row)" type="text" size="medium">编辑</el-button>
              <el-button @click="deleteErrorCode(scope.row)" type="text" v-if="scope.row.status < 1"
                         size="medium">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
<script>
import SoftwareMaintainerView from '../maintainPeople/SoftwareMaintainerView.vue'
import CodeMsgPopoverView from './child_pop/CodeMsgPopoverView.vue'
import {msg} from "@babel/core/lib/config/validation/option-assertions";

export default {
  components: {
    CodeMsgPopoverView,
    SoftwareMaintainerView
  },
  data() {
    return {
      readOnly: false,
      dialogTitle: '',
      errorCodeFormVisible: false,
      formLabelWidth: '80px',
      errorCodeRules: {},
      submitFlag: true,
      software_maintainer: '倪恒',
      condition: null,
      errorCodeList: [],
      errorCodeForm: {
        id: null,
        name: '',
        code: '',
        msg: '',
        author: '',
        status: 0
      }
    }
  },
  created() {
    this.getErrorCodeList();
  },
  methods: {
    // 查询列表
    async getErrorCodeList() {
      const {data: result} = await this.$http.get(ERROR_CODE_LIST);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.errorCodeAll = result.data
        this.selectErrorCodeList()
      }
    },
    // 查询列表
    selectErrorCodeList() {
      if (this.condition) {
        var condition = this.condition.trim()
        this.errorCodeList = this.errorCodeAll.filter(item =>
          item.name.toLowerCase().includes(condition.toLowerCase()) ||
          String(item.code).toLowerCase().includes(condition.toLowerCase()) ||
          item.msg.toLowerCase().includes(condition.toLowerCase()) ||
          item.author.toLowerCase().includes(condition.toLowerCase()))
      } else {
        this.errorCodeList = this.errorCodeAll
      }
    },
    // 手动校验
    emptyCheck() {
      var flag = true
      if (!this.errorCodeForm.name || !this.errorCodeForm.name.trim()) {
        this.$message.info("变量名不能为空")
        flag = false
      }
      if (flag && (!this.errorCodeForm.code || !this.errorCodeForm.name.trim())) {
        this.$message.info("code不能为空")
        flag = false
      }
      if (flag && (!this.errorCodeForm.msg || !this.errorCodeForm.msg.trim())) {
        this.$message.info("msg不能为空")
        flag = false
      }
      if (flag && (!this.errorCodeForm.author || !this.errorCodeForm.author.trim())) {
        this.$message.info("作者不能为空")
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
        var error_code_data = {
          msg: this.errorCodeForm.msg === undefined ? null : this.errorCodeForm.msg.trim(),
          author: this.errorCodeForm.author === undefined ? null : this.errorCodeForm.author.trim()
        }
        if (this.errorCodeForm.id == null) {
          if (!this.errorCodeForm.name) {
            this.submitFlag = true
            return;
          }
          error_code_data.name = this.errorCodeForm.name === undefined ? null : 'ER_' + this.errorCodeForm.name.trim()
          error_code_data.code = this.errorCodeForm.code === undefined ? null : this.errorCodeForm.code.toString().trim()
          const {data: result} = await this.$http.post(ERROR_CODE_ADD, error_code_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        } else {
          error_code_data.id = this.errorCodeForm.id
          error_code_data.name = this.errorCodeForm.name === undefined ? null : this.errorCodeForm.name.trim()
          const {data: result} = await this.$http.post(ERROR_CODE_EDIT, error_code_data);
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        }
        this.submitFlag = true
        this.errorCodeFormVisible = false
        this.getErrorCodeList()
      })
    },
    // 删除
    async delErrorCode(id) {
      var error_code_data = {
        id: id
      }
      const {data: result} = await this.$http.post(ERROR_CODE_DEL, error_code_data);
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.$message.success(result.msg)
      }
      this.errorCodeFormVisible = false
      this.getErrorCodeList()
    },
    // 删除二次确认
    deleteErrorCode(row) {
      this.$confirm('确定删除' + row.name + '吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delErrorCode(row.id)
      })
    },
    formStatus(status) {
      const map = {
        0: '草稿',
        1: '已发布'
      }
      return map[status]
    },
    //回显数据
    displayForm(row) {
      this.errorCodeForm.id = row.id
      this.errorCodeForm.name = row.name
      this.errorCodeForm.code = row.code
      this.errorCodeForm.msg = row.msg
      this.errorCodeForm.author = row.author
      this.errorCodeFormVisible = true
    },
    // 打开新增表单
    openAddDialog() {
      this.readOnly = false
      this.dialogTitle = '新增返回码'
      this.errorCodeForm = {}
      this.errorCodeFormVisible = true
    },
    // 打开编辑表单
    openEditDialog(row) {
      this.readOnly = true
      this.displayForm(row)
      this.dialogTitle = '编辑返回码'
    },
    // 打开表单
    openForm() {
      this.errorCodeRules = {
        "name": [{
          required: true, message: '请输入变量名', trigger: 'blur'
        }],
        "code": [
          {required: true, message: '请输入code', trigger: 'blur'},
          { type: 'number', message: 'code必须为数字值'}
        ],
        "msg": [{
          required: true, message: '请输入msg', trigger: 'blur'
        }],
        "author": [{
          required: true, message: '请输入作者', trigger: 'blur'
        }]
      }
      this.$nextTick(() => {
        this.$refs['errorCodeForm'].clearValidate();
      })
    },
    // 关闭表单
    closeForm() {
      this.errorCodeForm = {}
      this.resetForm()
    },
    // 重置表单校验
    resetForm() {
      this.$refs['errorCodeForm'].clearValidate();
      this.$refs['errorCodeForm'].resetFields();
    },
    // 文字高亮显示
    showHighLightData(val) {
      if (val !== null && this.condition !== null && this.condition !== "") {
        return String(val).replaceAll(this.condition, '<font style="background-color: yellow" color="black">' + this.condition + "</font>");
      } else {
        return val;
      }
    },
    // 输入框触发
    changeMessage() {
      this.$forceUpdate()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.error-code-html-box {
  padding: 20px;
  min-width: 600px;
}

.query-box {
  margin-bottom: 20px;
}

.element.style {
  height: 650px;
}

.table-box {
  height: 100%;
  text-align: left;
}

#errorCodeForm .el-select {
  width: 85%;
}

#errorCodeForm .el-input {
  width: 85%;
}

#formBtn {
  margin-right: 24px
}
</style>

<style>
.processErrorCode .el-table__header {
  width: 100% !important;
}

.processErrorCode .el-table__body {
  width: 100% !important;
}

.processErrorCode .el-input__prefix {
  left: 2px;
}
</style>
