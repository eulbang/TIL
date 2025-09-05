<template>
  <section class="parent-card">
    <h3>부모 컴포넌트</h3>
    <p class="parent-line">{{ family.father }}</p>
    <p class="parent-line muted">{{ family.mother }}</p>

    <ChildPage
      v-for="c in family.children"
      :key="c.name"
      :child="c"
    />
  </section>
</template>

<script setup>
import ChildPage from './ChildPage.vue'

defineProps({
  family: { type: Object, required: true },
})
</script>

<style scoped>
.parent-card {
  margin: 24px 0;
  padding: 24px;
  border: 1px solid #e5e5e5;
  border-radius: 10px;
  background: #f7f7f7;
}
h3 {
  margin: 0 0 8px;
  text-align: center;
  font-size: 1.25rem;
  font-weight: 800;
}
.parent-line {
  margin: 2px 0;
  text-align: center;
}
.muted { color: #666; }
</style>
