<template>
  <section>
    <h1>부모 페이지입니다.</h1>

    <ChildPage
      v-for="c in children"
      :key="c.name"
      :child="c"
      @giveMeAllowance="updateBalance"
    />
  </section>
</template>

<script setup>
import { reactive } from 'vue'
import ChildPage from './ChildPage.vue'

const children = reactive([
  { name: '김하나', age: 30, balance: 100000 },
  { name: '김두리', age: 20, balance: 10000 },
  { name: '김서이', age: 10, balance: 1000 },
])

function updateBalance(target) {
  target.balance += 1000
}
</script>
