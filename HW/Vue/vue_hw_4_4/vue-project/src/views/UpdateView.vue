<template>
  <main class="wrap">
    <h1>데이터 수정 페이지</h1>
    <p>name(param): {{ name }}</p>

    <div v-if="target">
      <p>이름: {{ target.name }}</p>
      <p>잔고: {{ target.balance }}</p>
      <button @click="plus">+ 1000</button>
    </div>
    <p v-else>대상이 없습니다.</p>
  </main>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '../stores/balance'

const route = useRoute()
const name = route.params.name

const store = useBalanceStore()
// 인자를 받는 getter 사용
const target = computed(() => store.byName(name))

const plus = () => store.increment(name, 1000)
</script>

<style scoped>
.wrap { max-width: 680px; margin: 24px auto; padding: 0 12px; }
button { padding: 6px 10px; border-radius: 6px; background: #2b78ff; color: #fff; border: 0; }
</style>
