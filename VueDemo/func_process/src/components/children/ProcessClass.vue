<template>
  <div class="processClass">
    <div class="class-html-box">
      <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer"/>
      <div class="query-box">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-input placeholder="请输入内容" @input="selectClassList" clearable v-model="condition"
                      class="input-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getClassList"></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="addBtn" @click="openAddDialog" type="primary">新增类</el-button>
          </el-col>
        </el-row>
      </div>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="classFormVisible" width='40%'
                 @open='openForm' @close="closeForm">
        <el-form id="classForm" :model="classForm" ref="classForm" :rules="classRules">
          <el-form-item label="英文名" :label-width="formLabelWidth" prop="class_name">
            <el-input v-model="classForm.class_name" autocomplete="off" placeholder="请输入英文名"
                      @input="$forceUpdate()">
            </el-input>
          </el-form-item>
          <el-form-item label="中文名" :label-width="formLabelWidth" prop="class_desc">
            <el-input v-model="classForm.class_desc" autocomplete="off" placeholder="请输入中文名"
                      @input="$forceUpdate()">
            </el-input>
          </el-form-item>
          <el-form-item label="注释" :label-width="formLabelWidth" prop="class_detail">
            <el-input v-model="classForm.class_detail" type="textarea" placeholder="请输入注释" autocomplete="off"
                      @input="$forceUpdate()" style="width: 85%" :autosize="{ minRows: 5, maxRows: 8}"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <div id="formBtn">
            <el-button @click="classFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="submitForm('classForm')">确 定</el-button>
          </div>
        </div>
      </el-dialog>
      <div class="table-box">
        <el-table stripe :data="classList" border style="width:100%;padding: 0">
          <el-table-column type="index" width="3%" min-width="3%" label="序号">
          </el-table-column>
          <el-table-column prop="class_name" maxlength=255 label="英文名" contentEditable="true" align="left"
                           width="22.5%" min-width="22.5%">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.class_name)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="class_desc" maxlength=255 label="中文名" contentEditable="true" align="left"
                           width="22.5%" min-width="22.5%">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.class_desc)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="class_detail" maxlength=255 label="注释" contentEditable="true" align="left"
                           width="22.5%" min-width="22.5%">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.class_detail)"></span>
            </template>
          </el-table-column>
          <el-table-column label="操作" contentEditable="true" align="center" width="7%" min-width="7%">
            <template slot-scope="scope">
              <el-button @click="openEditDialog(scope.row)" type="text" size="medium">编辑</el-button>
              <el-button @click="deleteClass(scope.row)" type="text" size="medium">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
<script>
import SoftwareMaintainerView from '../maintainPeople/SoftwareMaintainerView.vue'

export default {
  components: {
    SoftwareMaintainerView
  },
  props: {
    FunctionVueEnumClassTypeShow: { type: Function, require: true }
  },
  data () {
    return {
      dialogTitle: '',
      classFormVisible: false,
      formLabelWidth: '80px',
      classRules: {},
      submitFlag: true,
      software_maintainer: '倪恒',
      condition: null,
      classList: [],
      classAll: [],
      classForm: {
        id: null,
        class_name: '',
        class_desc: '',
        class_detail: ''
      }
    }
  },
  created () {
    this.getClassList()
  },
  methods: {
    // 查询列表
    async getClassList () {
      const { data: result } = await this.$http.get(CLASS_LIST)
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.classAll = result.data
        this.selectClassList()
        // 触发ProcessFunction中类下拉框数据变化
        this.FunctionVueEnumClassTypeShow(this.classAll)
      }
    },
    // 搜索列表
    selectClassList () {
      if (this.condition) {
        const condition = this.condition.trim()
        this.classList = this.classAll.filter(item =>
          item.class_name.toLowerCase().includes(condition.toLowerCase()) ||
          item.class_desc.toLowerCase().includes(condition.toLowerCase()) ||
          item.class_detail.toLowerCase().includes(condition.toLowerCase()))
      } else {
        this.classList = this.classAll
      }
    },
    // 手动校验
    emptyCheck () {
      let flag = true
      if (!this.classForm.class_name || !this.classForm.class_name.trim()) {
        this.$message.info('英文名不能为空')
        flag = false
      }
      if (flag && (!this.classForm.class_desc || !this.classForm.class_desc.trim())) {
        this.$message.info('中文名不能为空')
        flag = false
      }
      if (flag && (!this.classForm.class_detail || !this.classForm.class_detail.trim())) {
        this.$message.info('注释不能为空')
        flag = false
      }
      return flag
    },
    // 新增、修改
    async submitForm (formName) {
      this.$refs[formName].validate(async (valid) => {
        if (!valid) {
          return
        }
        // 手动校验
        if (!this.emptyCheck()) {
          return
        }
        if (!this.submitFlag) {
          return
        }
        this.submitFlag = false
        const class_data = {
          class_name: this.classForm.class_name === undefined ? null : this.classForm.class_name.trim(),
          class_desc: this.classForm.class_desc === undefined ? null : this.classForm.class_desc.trim(),
          class_detail: this.classForm.class_detail === undefined ? null : this.classForm.class_detail.trim()
        }
        if (this.classForm.id == null) {
          const { data: result } = await this.$http.post(CLASS_ADD, class_data)
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        } else {
          class_data.id = this.classForm.id
          const { data: result } = await this.$http.post(CLASS_EDIT, class_data)
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        }
        this.submitFlag = true
        this.classFormVisible = false
        this.getClassList()
      })
    },
    // 删除
    async delClass (id) {
      const class_data = {
        id: id
      }
      const { data: result } = await this.$http.post(CLASS_DEL, class_data)
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.$message.success(result.msg)
      }
      this.classFormVisible = false
      this.getClassList()
    },
    // 删除二次确认
    deleteClass (row) {
      this.$confirm('确定删除' + row.class_name + '吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delClass(row.id)
      })
    },
    // 回显数据
    displayForm (row) {
      this.classForm.id = row.id
      this.classForm.class_name = row.class_name
      this.classForm.class_desc = row.class_desc
      this.classForm.class_detail = row.class_detail
      this.classFormVisible = true
    },
    // 打开新增表单
    openAddDialog () {
      this.dialogTitle = '新增类'
      this.classForm = {}
      this.classFormVisible = true
    },
    // 打开编辑表单
    openEditDialog (row) {
      this.classForm = {}
      this.displayForm(row)
      this.dialogTitle = '编辑类'
    },
    // 打开表单
    openForm () {
      this.initValidRule()
      this.$forceUpdate()
    },
    // 关闭表单
    closeForm () {
      this.classForm = {}
      this.resetForm()
    },
    // 设置校验规则
    initValidRule () {
      this.classRules = {
        class_name: [{
          required: true, message: '请输入英文名', trigger: 'blur'
        }],
        class_desc: [{
          required: true, message: '请输入中文名', trigger: 'blur'
        }],
        class_detail: [{
          required: true, message: '请输入注释', trigger: 'blur'
        }]
      }
      this.$nextTick(() => {
        this.$refs.classForm.clearValidate()
      })
    },
    // 重置表单校验
    resetForm () {
      this.$refs.classForm.clearValidate()
      this.$refs.classForm.resetFields()
    },
    // 文字高亮显示
    showHighLightData (val) {
      if (val && this.condition) {
        return val.replaceAll(this.condition, '<font style="background-color: yellow" color="black">' + this.condition + '</font>')
      } else {
        return val
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.class-html-box {
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

#classForm .el-select {
  width: 85%;
}

#classForm .el-input {
  width: 85%;
}

#formBtn {
  margin-right: 24px
}
</style>
<style>
.processClass .el-table__header {
  width: 100% !important;
}

.processClass .el-table__body {
  width: 100% !important;
}
</style>
