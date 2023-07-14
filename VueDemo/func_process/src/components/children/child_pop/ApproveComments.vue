<template>
  <div>
    <el-dialog title="审核意见" :visible.sync="approveVisible" width="60%">
      <div class="comment_table">
        <el-table :data="table_data" border stripe style="width:100%;padding: 0">
          <el-table-column type="index" width="50px" label="序号"></el-table-column>
          <el-table-column prop="comment_person" label="评论人" width="80px"></el-table-column>
          <el-table-column prop="comment_time" label="评论时间" width="190px"></el-table-column>
          <el-table-column prop="comment_desc" label="评论内容" min-width="200px"></el-table-column>
          <el-table-column label="提及信息" min-width="130px">
            <template slot-scope="scope" v-if="scope.row.comment_mention_list.length > 0">
              <span v-for="(item, i) in scope.row.comment_mention_list">
                <span>{{ item.mention_person }}:</span>
                <span @click="readComment(item)" v-if="item.mention_read===0" style="color: red">未读</span>
                <span v-if="item.mention_read===1" style="color: green">已读</span>
                <span style="margin: 0" v-if="i < (scope.row.comment_mention_list.length-1)">，</span>
              </span>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="comment_form">
        <el-form ref="commentFormRef" :model="commentForm" label-width="80px">
          <el-form-item label="评论内容">
            <el-input type="textarea" v-model="commentForm.comment_desc" style="width: 95%"
                      :autosize="{ minRows: 3, maxRows: 4}"></el-input>
          </el-form-item>
          <el-form-item label="提及人员">
            <el-select v-model="commentForm.mention_persons" multiple filterable placeholder="请选择提及人员"
                       style="width: 95%">
              <el-option v-for="item of person_options" :key="item" :label="item" :value="item">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <div id="formBtn">
            <el-button @click="approveVisible=false">取 消</el-button>
            <el-button type="primary" @click="submitComment">确 定</el-button>
          </div>
        </div>
      </div>
    </el-dialog>
  </div>
</template>
<script>

export default {
  data () {
    return {
      approveVisible: false,
      person_options: [],
      table_data: [],
      create_person: '',
      comment_table_type: 0,
      data_id: 0,
      commentForm: {
        comment_desc: '',
        mention_persons: []
      }
    }
  },
  mounted () {
    this.approveVisible = false
  },

  methods: {
    // 打开评论组件
    openComment (comment_table_type, data_id, create_person) {
      this.create_person = create_person
      this.comment_table_type = comment_table_type
      this.data_id = data_id
      this.getComment()
      this.approveVisible = true
    },
    // 获取评论数据（提及人，评论内容）
    async getComment () {
      this.person_options = []
      const query = '?comment_table_type=' + this.comment_table_type + '&data_id=' + this.data_id
      const { data: result } = await this.$http.get(GET_COMMENTS + query)
      if (result.code == 0) {
        this.person_options = result.data.related_person
        this.table_data = result.data.comment_list
      } else {
        this.$message.error(result.msg)
      }
      if (this.create_person) {
        this.commentForm = {
          comment_desc: '',
          mention_persons: [this.create_person]
        }
      } else {
        this.commentForm = {
          comment_desc: '',
          mention_persons: []
        }
      }
    },
    // 标记为已读
    async readComment (item) {
      if (!item.mention_person_self) {
        return
      }
      const query = '?id=' + item.id
      const { data: result } = await this.$http.get(READ_COMMENT + query)
      if (result.code == 0) {
        this.$message.success('已读成功!')
        this.getComment()
      } else {
        this.$message.error('已读失败!')
      }
    },
    // 提交评论
    async submitComment () {
      if (!this.commentForm.comment_desc) {
        this.$message.error('请填写评论!')
        return
      }
      const comment_data = {
        mention_person_list: this.commentForm.mention_persons,
        comment_table_type: this.comment_table_type,
        data_id: this.data_id,
        comment_desc: this.commentForm.comment_desc
      }
      const { data: result } = await this.$http.post(ADD_COMMENT, comment_data)
      if (result.code == 0) {
        this.$message.success('评论成功!')
        this.getComment()
      } else {
        this.$message.error('评论失败!')
      }
    }
  }
}
</script>
<style scoped>
.comment_form {
  margin-top: 40px;
}
</style>
<style>
.el-select__input.is-default {
  cursor: pointer;
}
</style>
