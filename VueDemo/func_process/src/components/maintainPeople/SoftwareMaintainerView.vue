<template>
  <p style="text-align: left;margin-top: 0px;">
    <span style="font-size: 15px;color: #5cb85c;cursor: pointer;margin-right: 40px;">功能维护员:{{software_maintainer || "无"}}
    </span>
    <span style="font-size: 15px;color: #5cb85c;cursor: pointer;margin-right: 40px;">功能更新日期: <el-button type="text">{{software_update_time}}</el-button></span>
    <span style="font-size: 15px;color: #5cb85c;cursor: pointer;margin-right: 40px;">历史需求单号:
      <el-link  @click="jumpTask" v-if="this.order_no_history">查看详情</el-link>
      <el-link v-if="!this.order_no_history">无</el-link>
    </span>
  </p>
</template>

<script>

export default {
  name: 'SoftwareMaintainerView',
  props: {
    software_maintainer: { type: String, require: true }
  },
  data () {
    return {
      software_update_time: '',
      order_no_history: '',
      AddVisiable: false
    }
  },
  mounted () {
    // this.get_current_sm_name();
  },

  methods: {
    get_current_sm_name () {
      this.$http.get('/global_cache_app/get_current_sm_name/', {
        params: {
          flag: 1,
          current_page_url: window.location.href,
          flow_no: ''
        }
      }).then((res) => {
        if (res.code == 0) {
          this.software_maintainer = res.data.software_maintainer
          this.software_update_time = res.data.software_update_time
          this.order_no_history = res.data.order_no_history
        }
      })
    },
    handleAddAttrData () {
      this.AddVisiable = true
      this.$nextTick(() => {
        this.$refs.adddialog.init(this.software_maintainer)
      })
    },
    jumpTask () {
      window.open('https://online.fancyqube.net/Project/admin/skuapp/t_task_trunk/?status=all&alls=all&Order=' + this.order_no_history)
    },
    softwareMainData (data) {
      this.software_maintainer = data
    }
  }
}
</script>

<style>
  .el-button.el-button--text {
    padding-bottom: 1px
  }
</style>
