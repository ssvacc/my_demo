<template>
  <div id="testPage">

    <el-row type="flex" justify="space-around" class="select_row">
      <el-col :span="7">
        <div style="width: 520px">
          <el-col style="text-align: right" :span="5">
            <div>查询条件:</div>
          </el-col>
          <el-col style="text-align: left" :span="19">
            <div>
              <el-input size="small" placeholder=" 多个搜索词空格分隔" style="width:240px;margin-left: 10px" clearable v-model="s_condition"></el-input>
              <el-select size="small" style="width:140px;margin-left: 10px" v-model="s_condition_query_type">
                <el-option v-for="item in s_condition_query_type_option" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </div>
          </el-col>
        </div>
      </el-col>
      <el-col :span="7">
            <div style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <div>图片路径:</div>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div>
          <el-input size="small" placeholder=" 多个搜索词空格分隔" style="width:240px;margin-left: 10px" clearable v-model="s_pic_url"></el-input>
          <el-select size="small" style="width:140px;margin-left: 10px" v-model="s_pic_url_query_type">
            <el-option v-for="item in s_pic_url_query_type_option" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </div>
      </el-col>
    </div>
      </el-col>
      <el-col :span="7">
            <div style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <div>总数:</div>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div>
          <el-input-number v-model="i_count_start" size="small"  :controls="false" style="width: 140px;margin-left: 10px;"></el-input-number>
          <span>-</span>
          <el-input-number v-model="i_count_end" size="small"  :controls="false" style="width: 140px;"></el-input-number>
        </div>
      </el-col>
    </div>
      </el-col>
    </el-row>
    <el-row type="flex" justify="space-around" class="select_row">
      <el-col :span="7">
            <div style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <div>总价:</div>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div>
          <el-input-number v-model="i_price_start" size="small" :precision="2" :step="0.01"  :controls="false" style="width: 140px;margin-left: 10px;"></el-input-number>
          <span>-</span>
          <el-input-number v-model="i_price_end" :precision="2" :step="0.01" size="small"  :controls="false" style="width: 140px;"></el-input-number>
        </div>
      </el-col>
    </div>
      </el-col>
      <el-col :span="7">
        
    <div class="block" style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <span class="demonstration">创建日期:</span>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div style="margin-left: 10px">
          <el-date-picker v-model="dt_create_time" size="small" value-format="yyyy-MM-dd" type="daterange" align="right" unlink-panels range-separator="至"
                          start-placeholder="开始日期" end-placeholder="结束日期" :picker-options="dt_create_time_picker_options">
          </el-date-picker>
        </div>
      </el-col>
    </div>
      </el-col>
      <el-col :span="7">
        
    <div class="block" style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <span class="demonstration">修改时间:</span>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div style="margin-left: 10px">
          <el-date-picker v-model="dt2_update_time" size="small" value-format="yyyy-MM-dd HH:mm:ss" type="datetimerange" align="right" unlink-panels range-separator="至"
                          start-placeholder="开始时间" end-placeholder="结束时间" :picker-options="dt2_update_time_picker_options">
          </el-date-picker>
        </div>
      </el-col>
    </div>
      </el-col>
    </el-row>
    <el-row type="flex" justify="space-around" class="select_row">
      <el-col :span="7">
        
    <div style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <span>是或否:</span>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div style="margin-left: 10px">
          <el-select size="small" style="width:140px" v-model="b_flag" clearable>
            <el-option v-for="item in b_flag_options" :key="item.value" :label="item.label" :value="item.value" :disabled="item.disabled">
            </el-option>
          </el-select>
        </div>
      </el-col>
    </div>
      </el-col>
      <el-col :span="7">
        
    <div style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <span>样品图类型:</span>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div style="margin-left: 10px">
          <el-select v-model="e_sample_image_type" filterable size="small" multiple style="width: 240px"
                 @visible-change="changedEnumOptions($event, 'e_sample_image_type')"
                 @change="$forceUpdate()">
            <ul class="infinite-list" style="overflow:auto">
              <li>
                <el-option disabled value="">
                  <span style="float: left;">key</span>
                  <span style="float: left;margin-right: 20px"></span>
                  <span style="float: right;color: #3a87ad">value</span>
                </el-option>
              </li>
              <li v-for="item in enumOptions" class="infinite-list-item">
                <el-option :label="item.label" :value="item.value">
                  <span style="float: left;">{{ item.value }}</span>
                  <span style="float: left;margin-right: 20px"></span>
                  <span style="float: right;color: #3a87ad">{{ item.label }}</span>
                </el-option>
              </li>
            </ul>
          </el-select>
        </div>
      </el-col>
    </div>
      </el-col>
      <el-col :span="7">
        
    <div style="width: 520px">
      <el-col style="text-align: right" :span="5">
        <span>产品外包装:</span>
      </el-col>
      <el-col style="text-align: left" :span="19">
        <div style="margin-left: 10px">
          <el-select v-model="e_product_packaging" filterable size="small" multiple style="width: 240px"
                 @visible-change="changedEnumOptions($event, 'e_product_packaging')"
                 @change="$forceUpdate()">
            <ul class="infinite-list" style="overflow:auto">
              <li>
                <el-option disabled value="">
                  <span style="float: left;">key</span>
                  <span style="float: left;margin-right: 20px"></span>
                  <span style="float: right;color: #3a87ad">value</span>
                </el-option>
              </li>
              <li v-for="item in enumOptions" class="infinite-list-item">
                <el-option :label="item.label" :value="item.value">
                  <span style="float: left;">{{ item.value }}</span>
                  <span style="float: left;margin-right: 20px"></span>
                  <span style="float: right;color: #3a87ad">{{ item.label }}</span>
                </el-option>
              </li>
            </ul>
          </el-select>
        </div>
      </el-col>
    </div>
      </el-col>
    </el-row>    <div class="hq_br"/>
    <el-button size="medium" @click="demo2_list" type="primary">查询</el-button>
    <el-button size="medium" @click="confirm_delete_by_ids" type="danger">批量删除</el-button>
    <div class="hq_br"/>
    <el-pagination id="hq_pagination"
         @size-change="handleSizeChange"
         @current-change="handleCurrentChange"
         :current-page.sync="pageNo"
         :page-sizes="[10, 100]"
         :page-size="pageSize"
         :total="total" background
         layout="total, sizes, prev, pager, next">
    </el-pagination>
    <div id="hq_table">
      <el-table border :data="table_data" stripe @selection-change="handleSelectionChange">
        <el-table-column type="selection" width="55">
        </el-table-column>
        <el-table-column key="0" label="英文名" prop="param_name" width="200px" min-width="100px" align="left">
        </el-table-column>
        <el-table-column key="1" label="中文名" prop="param_desc" width="200px" min-width="100px" align="left">
        </el-table-column>
        <el-table-column key="2" label="类型" prop="data_type" width="200px" min-width="100px" align="left">
        </el-table-column>
        <el-table-column key="3" label="注释" prop="param_detail" width="200px" min-width="100px" align="left">
        </el-table-column>
      </el-table>
    </div>

  </div>
</template>
<script>

export default {
  name: "testPage",
  
  data() {
    return { 
      s_condition: '',
      s_condition_query_type: 0,
      s_condition_query_type_option: [
        { value: 0, label: '整个语句'},
        { value: 1, label: '多个搜索词“与”关系' },
        { value: 2, label: '多个搜索词“或”关系' }
      ],
      s_pic_url: '',
      s_pic_url_query_type: 0,
      s_pic_url_query_type_option: [
        { value: 0, label: '整个语句'},
        { value: 1, label: '多个搜索词“与”关系' },
        { value: 2, label: '多个搜索词“或”关系' }
      ],
      i_count_start: null,
      i_count_end: null,
      i_price_start: null,
      i_price_end: null,
      dt_create_time: '',
      dt_create_time_picker_options: {
        shortcuts: [{
          text: '最近7天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近15天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 15);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近30天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
            picker.$emit('pick', [start, end]);
          }
        }]
      },
      dt2_update_time: '',
      dt2_update_time_picker_options: {
        shortcuts: [{
          text: '最近7天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近15天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 15);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近30天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
            picker.$emit('pick', [start, end]);
          }
        }]
      },
      b_flag: null,
      b_flag_options: [{value: null, label: '全部'}, {value: true, label: '是'}, {value: false, label: '否'}],
      e_sample_image_type: null,
      enumOptions: [],
      enumOptionsMap: new Map(),
      e_product_packaging: null,
      pageNo: 1,
      pageSize: 10,
      total: 0,
      multipleSelection: [],
      multipleSelectionIds: [],
      table_data: [],
    }
  },
  created() { 
    this.demo2_list();
  },
  methods: { 
    // 下拉框改变
    changedEnumOptions(callback, s_enum_name) {
      if (callback) {
        this.getEnumOptions(s_enum_name)
      } else {
        this.enumOptions = []
      }
    },
    // 获取下拉框数据
    getEnumOptions(s_enum_name) {
      // 从缓存获取
      if (this.enumOptionsMap.has(s_enum_name)) {
        this.enumOptions = this.enumOptionsMap.get(s_enum_name)
      } else {
        this.queryEnumOptions(s_enum_name)
      }
    },
    // 从后台获取
    async queryEnumOptions(s_enum_name) {
      var query = '?s_enum_name=' + s_enum_name
      const {data: result} = await this.$axios.get(GET_ENUM_OPTIONS + query);
      if (result.code != 0) {
        this.$message.error(result.msg);
      } else {
        this.enumOptions = result.data.a_enum_option.map(item => {
          return {value: item.s_enum_key, label: item.s_enum_value}
        })
        this.enumOptionsMap.set(s_enum_name, this.enumOptions)
      }
    },
    confirm_delete_by_ids() {
      if (this.multipleSelectionIds.length === 0) {
        this.$message.info('请选择要删除的数据!');
        return;
      }
      this.$confirm('确定删除选中的内容吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delete_by_ids()
      })
    },
    async delete_by_ids() {
      if (this.multipleSelectionIds.length === 0) {
        this.$message.info('请选择要删除的数据!');
        return;
      }
      let request_data = { id_list: this.multipleSelectionIds }
      const {data: result} = await this.$axios.post('/public_params/delByIdList', request_data);
      if (result.code !== 0) {
        this.$message.error(result.msg);
      } else {
        this.$message.success(result.msg);
      }
      this.demo2_list();
    },
    // 调整分页数据大小
    handleSizeChange(newSize) {
      this.pageSize = newSize;
      this.demo2_list();
    },
    // 调整当前页码
    handleCurrentChange(newPage) {
      this.pageNo = newPage;
      this.demo2_list();
    },
    handleSelectionChange(rows) {
      this.multipleSelection = rows;
      this.multipleSelectionIds = rows.map(row => {return row.id})
    },
    async demo2_list() {
      let query = ''
      query += '?page_no=' + this.pageNo + '&page_size=' + this.pageSize 
      if (this.condition) {
        query += '&condition='+ this.condition
      }
      const {data: result} = await this.$axios.get('/public_params/page_child' + query);
      if (result.code !== 0) {
        this.$message.error(result.msg);
      } else {
        this.table_data = result.data.data;
        this.total = result.data.total;
      }
    },
  }
}
</script>

<style scoped>
.hq_br {
  margin-bottom: 10px;
}
.select_row {
  margin-bottom: 10px;
}
#hq_table {
  padding: 20px;
}
</style>
<style>
#hq_table .el-table__header {
  width: 100% !important;
}
#hq_table .el-table__body {
  width: 100% !important;
}
</style>