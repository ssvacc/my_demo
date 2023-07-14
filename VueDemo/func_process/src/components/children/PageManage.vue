<template>
    <div class="processClass">
        <div class="class-html-box">
            <SoftwareMaintainerView v-bind:software_maintainer="software_maintainer" />
            <div class="query-box">
                <el-row :gutter="20">
                    <el-col :span="6">
                        <el-input placeholder="请输入内容" @input="selectClassList" clearable v-model="condition"
                            class="input-with-select">
                            <el-button slot="append" icon="el-icon-search" @click="getPageList"></el-button>
                        </el-input>
                    </el-col>
                    <el-col :span="2">
                        <el-button id="addBtn" @click="openAddDialog" type="primary">新增页面</el-button>
                    </el-col>
                    <!-- <el-col :span="2">
                        <el-button id="aaa" @click="openEditDialog" type="primary">跳转</el-button>
                    </el-col> -->
                </el-row>
            </div>
            <!-- 新增页面   参数选择 -->
            <el-dialog :title="dialogTitle" :close-on-click-modal="false" :visible.sync="pageFormVisible" width='40%'
                @open='openForm' @close="closeForm">
                <el-form id="pageForm" :model="pageForm" ref="pageForm" :rules="classRules">
                    <el-form-item label="参数" :label-width="formLabelWidth" prop="name">
                        <el-select v-model="pageForm.name" placeholder="请选择参数" @input="selectParamDesc" filterable remote reserve-keyword>
                            <el-option v-for="option in Paramslist" :key="option.name" :label="option.name"
                                :value="option.name"></el-option>
                        </el-select>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <div id="formBtn">
                        <el-button @click="pageFormVisible = false">取 消</el-button>
                        <el-button type="primary" @click="submitForm">确 定</el-button>
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
                <el-table stripe :data="classAll" border style="width:100%;padding: 0">
                    <el-table-column type="index" width="3%" min-width="3%" label="序号">
                    </el-table-column>
                    <el-table-column prop="page_name_en" maxlength=255 label="英文名" contentEditable="true" align="left"
                    width="10%" min-width="22.5%">
                    <template slot-scope="scope">
                        <span v-html="showHighLightData(scope.row.page_name_en)"></span>
                    </template>
                    </el-table-column>
                    <el-table-column prop="page_name_cn" maxlength=255 label="中文名" contentEditable="true" align="left"
                        width="10%" min-width="22.5%">
                        <template slot-scope="scope">
                            <span v-html="showHighLightData(scope.row.page_name_cn)"></span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="function_name_cn" label="函数" contentEditable="true"
                    align="center" width="50%" min-width="200px">
                    <template slot-scope="scope">
                        <table slot="reference" style="width: 800px" align="center">
                            <tr v-for="item in scope.row.function_name" color="'#409EFF'" >
                                <td align="center" valign="top" style="width: 150px"><span
                                    v-html="showHighLightData(item.function_name_cn)" ></span></td>
                                <td align="center" valign="top" style="width: 150px"><span
                                v-html="showHighLightData(item.function_name_en)" ></span></td>
                                <td align="center" valign="top" style="width: 100px">
                                    <span><el-button @click="openEditDialog(item.function_name_en)" type="text" size="mini">编辑</el-button>
                                </span></td>
                                <td align="center" valign="top" style="width: 100px">
                                    <span><el-button @click="" type="text" size="mini">预览</el-button>
                                </span></td>
                            </tr>
                          </table>
                      </template>
                    </el-table-column>
                    
                    <el-table-column maxlength=255 label="操作" contentEditable="true" align="center" width="20%"
                        min-width="12.5%">
                        <template slot-scope="scope">
                            <!-- <el-button @click="openEditDialog(scope.row.page_name_en.substring(2))" type="primary" size="mini">编辑</el-button> -->
                            <el-button  @click=" c(scope.row)" type="primary" size="mini">预览</el-button>
                            <el-button @click=" delPageList(scope.row)" type="primary" size="mini">删除</el-button>
                            <!-- <el-button @click=" console.log(scope.row)" type="primary" size="mini">预览</el-button> -->
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
    data() {
        return {
            dialogTitle: '',
            pageFormVisible: false,
            formLabelWidth: '80px',
            classRules: {},
            submitFlag: true,
            software_maintainer: '陈硕',
            first_name: '陈硕',
            function_list: [],
            Paramslist: {
                param_name:'',
                param_desc:'',
                name:'',
            },
            params: '',
            condition: null,
            classList: [],
            classAll: [],
            pageType: [],
            paramList: [],
            paramDescList: [],
            pageForm: {
                id: null,
                page_name_en: '',
                page_name_cn: '',
                class_detail: '',
                param_name: '',
                status: '',
                function_name_en:[],
                function_name_cn:[],
                function_name:[]
            },

            functionForm:{
                id: null,
                page_name_en: '',
                page_name_cn: '',
                class_detail: '',
                param_name: '',
                status: '',
                function_name_en:[],
                function_name_cn:[],
                function_name:[]
            }
        }
    },
    created() {
        this.getPageList()
        this.getParamList()
    },
    props: {
        jumpFunction: {type: Function, require: true}
    },
    methods: {
        handleParamsChange(val) {
            this.params = val
        },
        //删除页面数据
        async delPageList(row){
            var page_data = {
                page_name_en:row.page_name_en,
                function_name:row.function_name
            }
            const {data:result} = await this.$http.post(PAGE_DEL,page_data)
            if (result.code != 0) {
                this.$message.error(result.msg)
            } else {
                this.$message.success(result.msg)
            }
            // this.pageFormVisible = false
            this.getPageList()
        },

        // 查询页面列表
        async getPageList() {
            const { data: result } = await this.$http.get(PAGE_LIST)
            if (result.code != 0) {
                this.$message.error(result.msg)
            } else {
                this.classAll = result.data
                this.selectClassList()
                // // 触发ProcessFunction中类下拉框数据变化
                // this.FunctionVueEnumClassTypeShow(this.classAll)
            }
        },
        // 查询参数列表
        async getParamList() {
            const { data: result } = await this.$http.get(PAGE_PARAMS)
            if (result.code != 0) {
                this.$message.error(result.msg)
            } else {
                this.Paramslist = result.data
                // this.selectClassList()
                // 触发ProcessFunction中类下拉框数据变化
                // this.FunctionVueEnumClassTypeShow(this.classAll)
            }
        },
            // 校验参数是否设置示例值
        checkSubmit() {
            this.pageForm.param_name = this.Paramslist.name
        },
        selectParamDesc() {//参数中文名
            this.getPageList()
        },
        selectParamName() {//参数英文名
            this.getPageList()
        },
        // 搜索列表
        selectClassList() {
            if (this.condition) {
                const condition = this.condition.trim()
                this.classList = this.classAll.filter(item =>
                    item.page_name_cn.toLowerCase().includes(condition.toLowerCase()) ||
                    item.page_name_en.toLowerCase().includes(condition.toLowerCase()) ||
                    item.class_detail.toLowerCase().includes(condition.toLowerCase()))
            } else {
                this.classList = this.classAll
            }
        },
        // 手动校验
        emptyCheck() {
            let flag = true
            if (flag && (!this.pageForm.name || !this.pageForm.class_detail.trim())) {
                this.$message.info('注释不能为空')
                flag = false
            }
            return flag
        },
    async submitForm(){
    // 构造表单数据对象
    const formData = {
        param_name: this.pageForm.name, // 根据表单中实际字段名称进行调整
        first_name: this.first_name
    };
    const { data: result } = await this.$http.post(PAGE_ADD, formData)
          if (result.code != 0) {
            this.$message.error(result.msg)
          } else {
            this.$message.success(result.msg)
          }
        // this.submitFlag = true
        this.pageFormVisible = false
        // this.getFunctionList()
        this.getPageList()
},

    // 删除
    async delClass(id) {
        const class_data = {
            id: id
        }
        const { data: result } = await this.$http.post(CLASS_DEL, class_data)
        if (result.code != 0) {
            this.$message.error(result.msg)
        } else {
            this.$message.success(result.msg)
        }
        this.pageFormVisible = false
        this.getPageList()
        this.pageForm = this.pageForm
    },
    // 删除二次确认
    deleteClass(row) {
        this.$confirm('确定删除' + row.page_name_cn + '吗?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        }).then(() => {
            this.delClass(row.id)
        })
    },
        // 调整分页数据大小
        handleSizeChange(newSize) {
            this.pageSize = newSize
            this.getParamList()
        },
    // 回显数据
    displayForm(row) {
        this.pageForm.id = row.id
        this.pageForm.page_name_cn = row.page_name_cn
        this.pageForm.page_name_en = row.page_name_en
        this.pageForm.class_detail = row.class_detail
        this.pageForm.function_name_cn = row.function_name_cn
        this.pageForm.function_name_en = row.function_name_cn
        this.pageForm.status = row.status
        this.pageFormVisible = true
        this.pageForm = this.pageForm
        // this.Paramslist = this.Paramslist
    },
    //回显编辑函数数据
    displayFuncForm(row){
        this.functionForm.id = row.id
        this.functionForm.page_name_cn = row.page_name_cn
        this.functionForm.page_name_en = row.page_name_en
        this.functionForm.class_detail = row.class_detail
        this.functionForm.function_name_cn = row.function_name
        this.functionForm.function_name_en = row.function_name[row.index]
        this.functionForm.status = row.status
        this.funcFormVisible = true
        this.functionForm = this.functionForm
    },
    // 打开新增表单
    openAddDialog() {
        this.dialogTitle = '新增页面'
        this.pageForm = {}
        this.pageFormVisible = true
    },
    // 跳转函数编辑页面
    openEditDialog(value) {
        var s_function_name=value
        this.jumpFunction(s_function_name, 'functionPane')
    // this.$router.push({ path: `/admin/messageCenter/${value}` });
    },

    // 打开表单
    openForm() {
        this.initValidRule()
        this.$forceUpdate()
    },
    // 关闭表单
    closeForm() {
        this.pageForm = {}
        this.resetForm()
    },
    // 设置校验规则
    initValidRule() {
        this.classRules = {
            page_name_cn: [{
                required: true, message: '请输入英文名', trigger: 'blur'
            }],
            page_name_en: [{
                required: true, message: '请输入中文名', trigger: 'blur'
            }],
            class_detail: [{
                required: true, message: '请输入注释', trigger: 'blur'
            }]
        }
        this.$nextTick(() => {
            this.$refs.pageForm.clearValidate()
        })
    },
    // 重置表单校验
    resetForm() {
        this.$refs.pageForm.clearValidate()
        this.$refs.pageForm.resetFields()
    },
    // 文字高亮显示
    showHighLightData(val) {
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
  