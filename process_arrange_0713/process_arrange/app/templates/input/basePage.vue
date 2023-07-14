<template>
  <div id="{{ele.page_id|safe}}">
    {{ ele.elements|safe }}
  </div>
</template>

<script>
export default {
  name: "{{ ele.page_code|safe }}",
  data() {
    return { {{ ele.data|safe }}
    }
  },{% if ele.beforeCreate %}
  beforeCreate() {
    {{ ele.beforeCreate|safe }}
  },{% endif %}{% if ele.created %}
  created() {
    {{ ele.created|safe }}
  },{% endif %}{% if ele.beforeMount %}
  beforeMount() {
    {{ ele.beforeMount|safe }}
  },{% endif %}{% if ele.mounted %}
  mounted() {
    {{ ele.mounted|safe }}
  },{% endif %}{% if ele.beforeUpdate %}
  beforeUpdate() {
    {{ ele.beforeUpdate|safe }}
  },{% endif %}{% if ele.updated %}
  updated() {
    {{ ele.updated|safe }}
  },{% endif %}{% if ele.beforeUnmount %}
  beforeUnmount() {
    {{ ele.beforeUnmount|safe }}
  },{% endif %}{% if ele.unmounted %}
  unmounted() {
    {{ ele.unmounted|safe }}
  },{% endif %}{% if ele.errorCaptured %}
  errorCaptured() {
    {{ ele.errorCaptured|safe }}
  },{% endif %}
  methods: { {{ ele.methods|safe }}
  }
}
</script>

<style scoped>
{{ ele.style|safe }}
</style>