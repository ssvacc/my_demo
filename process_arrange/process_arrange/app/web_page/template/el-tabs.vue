<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    {% for e in ele.elTabPanes %}
    <el-tab-pane label="{{ e.label }}" name="{{ e.name }}">{{ e.content }}</el-tab-pane>
    {% endfor %}
  </el-tabs>
</template>
<script>
  export default {
    data() {
      return {
        activeName: '{{ ele.activeName }}'
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    }
  };
</script>