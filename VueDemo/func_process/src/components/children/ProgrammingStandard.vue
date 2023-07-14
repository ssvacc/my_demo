<template>
  <div class="processStandard">
    <div class="standard-html-box">
      <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer"/>
      <div class="query-box">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-input placeholder="请输入内容" @input="selectStandardList" clearable v-model="condition"
                      class="input-with-select">
              <el-button slot="append" icon="el-icon-search" @click="getStandardList"></el-button>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="addBtn" @click="openAddDialog" type="primary">新增规范</el-button>
          </el-col>
<!--          <el-col :span="1">-->
<!--            <exportExcelView v-bind:request_type="'GET'" v-bind:request_url="downloadUrl"/>-->
<!--            <exportExcelView v-bind:request_type="'DOWNOLAD'" v-bind:request_url="downloadUrl" v-bind:excel_filename="excel_filename"/>-->
<!--          </el-col>-->
        </el-row>
      </div>
      <el-dialog :title="dialogTitle" :close-on-click-modal="false"
                 :visible.sync="standardFormVisible" width='50%'
                 @open='openForm' @close="closeForm(standardForm)">
        <el-form id="standardForm" :model="standardForm" ref="standardFormRef" :rules="standardPage">
          <!-- 页面-->
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="规范类别" :label-width="formLabelWidth" prop="return_list">
                <el-select v-model="standardForm.e_develop_require_specification_type" placeholder="请选择" @input="$forceUpdate()">
                  <el-option
                    v-for="item in standardtype"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="对应考核人员" :label-width="formLabelWidth" prop="return_list">
                <el-select v-model="standardForm.e_develop_require_specification_station" placeholder="请选择" @input="$forceUpdate()">
                  <el-option
                    v-for="item in person"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='formItemSpan'>
              <el-form-item label="开发规范" :label-width="formLabelWidth" prop="s_desc">
                <el-input v-model="standardForm.s_desc" placeholder="请输入开发规范" :disabled="readOnly"
                          autocomplete="off" type="textarea"
                          style="width: 85%" :autosize="{ minRows: 4, maxRows: 8}" @input="$forceUpdate()"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span='formItemSpan'>
              <el-form-item label="备注信息" :label-width="formLabelWidth" prop="url">
                <el-input v-model="standardForm.s_remarks" placeholder="请输入备注信息" :disabled="readOnly"
                          autocomplete="off" type="textarea"
                          style="width: 85%" :autosize="{ minRows: 4, maxRows: 8}" @input="$forceUpdate()"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="standardFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="submitForm">确 定</el-button>
        </div>
      </el-dialog>
      <div class="table-box">
        <el-table stripe
                  :data="standardList" border
                  style="width:100%;padding: 0">
          <el-table-column type="index" width="50" label="序号" align="center">
          </el-table-column>
          <el-table-column prop="s_desc" maxlength=500 label="开发规范" contentEditable="true" align="left">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.s_desc)"></span>
            </template>
          </el-table-column>
          <el-table-column :key="Math.random()" prop="s_pic_url" maxlength=255 label="样例图片" align="center"
                           contentEditable="true" width="180">
            <template slot-scope="scope">
              <el-upload
                ref="upload"
                class="avatar-uploader"
                :action="uploadImg"
                :show-file-list="false"
                name="img_obj"
                :data="{i_develop_require_specification_id: scope.row.i_develop_require_specification_id}"
                :on-success="successUpload"
                :on-error="failUpload"
                :on-change="reload">
                <el-popover effect="light" trigger="hover" placement="right" width="auto">-->
                  <template #default>
                    <img :src='scope.row.s_pic_url' style="width:600 px;">
                  </template>
                  <template #reference>
                    <img :src='scope.row.s_pic_url' style="width: 160px;"/>
                  </template>
                </el-popover>
                <img v-if="scope.row.s_pic_url">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </template>
          </el-table-column>
          <el-table-column prop="e_develop_require_specification_type" label="规范类别" contentEditable="true" align="center" width="100">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.e_develop_require_specification_type)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="s_desc" maxlength=455 label="对应考核人" contentEditable="true" align="center"
                           width="100">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.e_develop_require_specification_station)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="s_remarks" label="备注信息" contentEditable="true" align="center" width="150">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.s_remarks)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="s_apply_person" maxlength=255 label="提交人" contentEditable="true" align="center"
                           width="80">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.s_apply_person)"></span>
            </template>
          </el-table-column>
          <el-table-column prop="dt2_update_time" show-overflow-tooltip maxlength=300 label="更新时间"
                           contentEditable="true" align="center" width="160">
            <template slot-scope="scope">
              <span v-html="showHighLightData(scope.row.dt2_update_time)"></span>
            </template>
          </el-table-column>
          <el-table-column label="操作" contentEditable="true" align="center" width="100">
            <template slot-scope="scope">
              <el-button @click="openEditDialog(scope.row)" type="text" size="medium">编辑</el-button>
              <el-button @click="deleteStandard(scope.row)" type="text" size="medium">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
<script>
import SoftwareMaintainerView from '../maintainPeople/SoftwareMaintainerView.vue'
import ExportExcelView from './child_pop/ExportExcelView.vue'

export default {
  name: 'processStandard',
  components: {
    ExportExcelView,
    SoftwareMaintainerView
  },
  data() {
    return {
      // 组件相关
      // imageUrl: '',
      standardtype: [
        {
          value: '展示规范',
          label: '展示规范'
        },
        {
          value: '编码规范',
          label: '编码规范'
        },
        {
          value: 'SQL规范',
          label: 'SQL规范'
        },
        {
          value: '数据库操作规范',
          label: '数据库操作规范'
        },
        {
          value: '上线规范',
          label: '上线规范'
        },
        {
          value: '大数据操作规范',
          label: '大数据操作规范'
        },
        {
          value: '定时任务规范',
          label: '定时任务规范'
        },
        {
          value: '命名规范',
          label: '命名规范'
        },
        {
          value: '权限设置规范',
          label: '权限设置规范'
        },
        {
          value: '全局函数规范',
          label: '全局函数规范'
        },
        {
          value: '日志规范',
          label: '日志规范'
        },
        {
          value: '上传下载规范',
          label: '上传下载规范'
        },
        {
          value: '设计规范',
          label: '设计规范'
        },
        {
          value: '审核跳转规范',
          label: '审核跳转规范'
        },
        {
          value: '数据容错机制',
          label: '数据容错机制'
        },
        {
          value: '数字校验',
          label: '数字校验'
        },
      ],
      uploadImg: UPLOAD_IMG,
      fit: 'fill',
      url: '',
      software_maintainer: '盛荣凯',
      fits: [],
      src_list: [],
      standardFormVisible: false,
      formLabelWidth: '100px',
      readOnly: false,
      dialogTitle: '',
      standardPage: {},
      drawerVisible: false,
      submitFlag: true,
      // 列表数据相关
      pageNo: 1,
      pageSize: 100,
      total: 0,
      formItemSpan: 12,
      condition: '',
      standardList: [],
      standardAll: [],
      standardForm: {
        i_develop_require_specification_id: null,
        e_develop_require_specification_station: '',
        e_develop_require_specification_type: '',
        s_desc: '',
        s_pic_url: '',
        s_remarks: '',
        s_apply_person: '',
        dt2_apply_time: '',
        s_update_person: [],
        dt2_update_time: [],
      },
      // 下拉选择框相关
      querySize: 100,
      // 考核人员
      person: [
        {
          value: '开发人员',
          label: '开发人员'
        },
        {
          value: '开发人员+测试人员',
          label: '开发人员+测试人员'
        }
      ],
      fileList: [],
      task_name: "",
      param_list: [],
      excel_filename: '开发规范.xls',
      // downloadUrl: 'https://fancyqube-download.oss-cn-shanghai.aliyuncs.com/software_develop_standard/DevelopRequireSpecification.xls'
    }
  },
  created() {
    this.getStandardList()
  },
  methods: {
    reload(){
      this.getStandardList();
    },
    failUpload() {
      this.$message.error("服务器异常，上传失败！");
    },
    successUpload(res, file) {
      if (res.code ===0) {
        this.$message.success('上传成功！');
      } else {
        this.$message.error(res.msg);
      }
    },

    // 查询列表
    async getStandardList() {
      const {data: result} = await this.$http.get(STANDARD_DATA)
      if (result.code !== 0) {
        this.$message.error(result.msg)
      } else {
        this.standardAll = result.data.a_develop_require_specification
        this.selectStandardList()
      }
    },
    selectStandardList() {
      if (this.condition) {
        var condition = this.condition.trim()
        this.standardList = this.standardAll.filter(item =>
          item.s_desc.includes(condition) ||
          item.e_develop_require_specification_station.includes(condition) ||
          item.e_develop_require_specification_type.includes(condition) ||
          item.s_remarks.includes(condition) ||
          item.s_apply_person.includes(condition) ||
          item.dt2_update_time.includes(condition))
      } else {
        this.standardList = this.standardAll
      }
    },

    // 删除
    async delStandard(i_develop_require_specification_id) {
      const stand_data = {
        i_develop_require_specification_id: i_develop_require_specification_id
      }
      const {data: result} = await this.$http.post(STANDARD_DEL, stand_data)
      if (result.code != 0) {
        this.$message.error(result.msg)
      } else {
        this.$message.success(result.msg)
      }
      this.standardFormVisible = false
      this.getStandardList()
    },
    // 删除二次确认
    deleteStandard(row) {
      this.$confirm('确定删除此条数据吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delStandard(row.i_develop_require_specification_id)
      })
    },
    // 打开新增表单
    openAddDialog() {
      this.readOnly = false
      this.dialogTitle = '新增规范'
      this.standardForm = {}
      this.standardFormVisible = true
    },
    // 打开编辑表单
    openEditDialog(row) {
      this.readOnly = false
      this.displayForm(row)
      this.dialogTitle = '编辑规范'
    },
    // 回显数据
    displayForm(row) {
      this.standardForm.i_develop_require_specification_id = row.i_develop_require_specification_id
      this.standardForm.e_develop_require_specification_station = row.e_develop_require_specification_station
      this.standardForm.e_develop_require_specification_type = row.e_develop_require_specification_type
      this.standardForm.s_desc = row.s_desc
      this.standardForm.s_remarks = row.s_remarks
      this.standardForm.s_apply_person = row.s_apply_person
      this.standardForm.dt2_update_time = row.dt2_update_time
      this.standardFormVisible = true
    },
    openForm() {
      if (!this.readOnly) {
      }
      this.standardPage = {}
    },
    closeForm() {
      this.returnOptions = []
      this.standardForm = {}
    },
    async submitForm() {
      if (!this.submitFlag) {
        return
      }
      this.submitFlag = false
      if (this.standardForm.e_develop_require_specification_station == null || this.standardForm.s_desc == null || this.standardForm.e_develop_require_specification_type == null) {
        this.$message.error('规范类别、对应考核人员、开发规范皆为必填项!')
        this.standardFormVisible = false
        this.submitFlag = true
        return
      }
      var standard_data = {
        e_develop_require_specification_station: this.standardForm.e_develop_require_specification_station === undefined ? null : this.standardForm.e_develop_require_specification_station,
        e_develop_require_specification_type: this.standardForm.e_develop_require_specification_type === undefined ? null : this.standardForm.e_develop_require_specification_type,
        s_desc: this.standardForm.s_desc === undefined ? null : this.standardForm.s_desc,
        s_remarks: this.standardForm.s_remarks === undefined ? null : this.standardForm.s_remarks,
      }
      if (this.standardForm.i_develop_require_specification_id == null) {
        standard_data.e_develop_require_specification_station = this.standardForm.e_develop_require_specification_station
        standard_data.e_develop_require_specification_type = this.standardForm.e_develop_require_specification_type
        standard_data.s_desc = this.standardForm.s_desc
        standard_data.s_remarks = this.standardForm.s_remarks
        console.log(standard_data)
        const {data: result} = await this.$http.post(STANDARD_ADD, standard_data);

        if (result.code != 0) {
          this.$message.error('操作失败!请联系李萌萌操作规范列表！')
        } else {
          this.$message.success(result.msg)
        }
      } else {
        standard_data.i_develop_require_specification_id = this.standardForm.i_develop_require_specification_id
        const {data: result} = await this.$http.post(STANDARD_EDIT, standard_data);
        if (result.code != 0) {
          this.$message.error(result.msg)
        } else {
          this.$message.success(result.msg)
        }
      }
      this.submitFlag = true
      this.standardFormVisible = false
      this.getStandardList()
    },
    beforeRemove() {
    },
    //上传图片

    // 文字高亮显示
    showHighLightData(val) {
      if (typeof val != "string") {
        return
      }
      if (val.indexOf(this.condition) !== -1 && this.condition !== '') {
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
.standard-html-box {
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

#standardPage {
  text-align: right;
  margin-right: 10px;
  margin-top: 30px;
  margin-bottom: 30px;
}

#standardForm .el-select {
  width: 85%;
}

#standardForm .el-input {
  width: 85%;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 150px;
  height: 150px;
  line-height: 150px;
  text-align: center;
}

.avatar {
  width: 150px;
  height: 150px;
  display: block;
}

</style>
