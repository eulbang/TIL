<template>
  <div class="child-card">
    <h4>자식 페이지</h4>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: { type: Object, required: true },
})
</script>

<style scoped>
.child-card {
  margin: 12px 0;
  padding: 16px;
  border: 1px solid #e9e9e9;
  background: #fafafa;
  border-radius: 8px;
}
h4 {
  margin: 0 0 8px;
  text-align: center;
  font-weight: 700;
}
p {
  margin: 0;
  text-align: center;
}
</style>
