<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
    <p>용돈 : {{ child.balance }}</p>
    <button @click="$emit('giveMeAllowance', child)">용돈 주세요.</button>
  </div>
</template>

<script setup>
defineProps({
  child: { type: Object, required: true }
})
defineEmits(['giveMeAllowance'])
</script>
