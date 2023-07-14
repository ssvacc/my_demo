<template>
  <div>
    <div v-if="functionRow.param_list != null && functionRow.param_list.length > 0">
      <span style="font-weight: bold">参数：</span>
      <el-tree :data="tree_data" :props="defaultProps"></el-tree>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FunctionparamMessage',
  props: {
    functionRow: { type: Object, require: true }
  },
  created () {
    this.renderTreeNode()
  },
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
      const param_list = this.functionRow.param_list
      const tree_data = []
      for (const item of param_list) {
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
