<template>
    <div>
        <span class="count">{{ count }}</span>
        <button :disabled="count !== 0" @click="increment">Increment</button>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        count: 0
      }
    },
    methods: {
      increment() {
        this.count++;
      }
    },
    name: "Counter"
  }
</script>

<style scoped>

</style>
