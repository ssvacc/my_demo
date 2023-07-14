<template>
  <div>
    <div v-if="functionRow.error_code_list != null && functionRow.error_code_list.length > 0">
      <span style="font-weight: bold">返回码：</span>
      <table>
        <tr v-for="item in functionRow.error_code_list">
          <td width="200px" style="float: left">{{ item.name }}</td>
          <td width="70px" style="float: left; margin-left: 10px">{{ item.code }}</td>
          <td width="200px" style="float: left">{{ item.msg }}</td>
        </tr>
      </table>
    </div>
    <div v-if="functionRow.return_list != null && functionRow.return_list.length > 0">
      <span style="font-weight: bold">返回值：</span>
      <el-tree :data="tree_data" :props="defaultProps"></el-tree>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FunctionReturnMessage',
  props: {
    functionRow: { type: Object, require: true },
    getEnumDataBySelectId: { type: Function, require: true }
  },
  created () {
    this.renderTreeNode()
  },
  // 函数列表中引入多次本组件，行数增多时，创建本组件；函数减少时，更新部分本组件，销毁多余的本组件
  // 生命周期钩子：如果本组件是被更新的，则不会执行created中的函数，需要在functionRow数据变更时执行，否则函数不执行无法更新tree_data数据
  beforeUpdate () {
    this.renderTreeNode()
  },
  data () {
    return {
      tree_data: [],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  methods: {
    renderTreeNode () {
      const return_list = this.functionRow.return_list
      const tree_data = []
      for (const item of return_list) {
        const tree_node = {
          label: item.param_name + ':' + item.param_desc
        }
        this.dealTreeNode(tree_node, item)
        tree_data.push(tree_node)
      }
      this.tree_data = tree_data
    },
    dealTreeNode (tree_node, item) {
      if (item.child_id && item.data_type == 12) {
        var tempNode = []
        for (var child of item.child_list) {
          var child_node = {
            label: child.param_name + ':' + child.param_desc
          }
          this.dealTreeNode(child_node, child)
          tempNode.push(child_node)
        }
        tree_node.children = tempNode
      } else if (item.child_id && item.data_type == 11) {
        var child_node = {
          label: item.child_list.param_name + ':' + item.child_list.param_desc
        }
        this.dealTreeNode(child_node, item.child_list)
        tree_node.children = [child_node]
      } else if (item.data_type == 13 && item.select_info_id) {
        var tempNode = []
        for (var child of item.child_list) {
          var child_node = {
            label: child.key + ':' + child.label
          }
          tempNode.push(child_node)
        }
        tree_node.children = tempNode
      } else {
        tree_node.children = null
      }
    }
  }
}
</script>

<style scoped>
.box-card {
  overflow-y: auto
}
</style>
