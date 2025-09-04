<template>
  <nav class="nav">
    <RouterLink :to="{ name: 'main' }">main</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.nav { padding: 12px; }
a { margin-right: 8px; }
</style>
