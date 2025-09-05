<template>
  <section class="card">
    <p>이름: {{ item.name }}</p>
    <p>잔고: {{ item.balance }}</p>
    <button @click="goUpdate">updateBalance</button>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  item: { type: Object, required: true },
})

const router = useRouter()
const goUpdate = () => {
  router.push({ name: 'update', params: { name: props.item.name } })
}
</script>

<style scoped>
.card { padding: 12px 0; border-bottom: 1px solid #ddd; }
button { padding: 6px 10px; border-radius: 6px; background: #2b78ff; color: #fff; border: 0; }
</style>
