<template>
  <main class="wrap">
    <h1>pinia 연습하기</h1>

    <ParentPage
      v-for="fam in store.familyInfo"
      :key="fam.familyName"
      :family="fam"
    />
  </main>
</template>

<script setup>
import { useFamilyStore } from '../stores/family'
import ParentPage from './ParentPage.vue'

const store = useFamilyStore()
</script>

<style scoped>
.wrap {
  max-width: 920px;
  margin: 32px auto;
  padding: 0 16px;
}
h1 { margin-bottom: 16px; }
</style>
