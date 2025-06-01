<template>
  <div class="mb-4">
    <div class="form-floating">
      <input 
        type="text" 
        class="form-control form-control-lg" 
        id="queryInput"
        placeholder="Введите ваш запрос..."
        @input="get_text($event.target.value)" 
        v-model="zapros"
      >
      <label for="queryInput">Введите ваш запрос...</label>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      zapros: ''
    }
  },
  props: {
    get_text: {
      type: Function,
      required: true
    }
  }
}
</script>
  