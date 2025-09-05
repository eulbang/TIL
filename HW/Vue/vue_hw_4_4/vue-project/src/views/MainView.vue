<template>
  <main class="wrap">
    <h1>pinia + router 연습하기</h1>

    <h2>메인 페이지</h2>
    <MainPage
      v-for="b in store.balances"
      :key="b.name"
      :item="b"
    />
  </main>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import MainPage from '@/components/MainPage.vue'

const store = useBalanceStore()
</script>

<style scoped>
.wrap { max-width: 680px; margin: 24px auto; padding: 0 12px; }
h1 { margin-bottom: 24px; }
h2 { margin: 16px 0; }
</style>
