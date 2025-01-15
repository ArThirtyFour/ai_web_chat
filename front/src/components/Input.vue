<template>
    <div class="razdel">
        <h2>Вводи свой запрос сюда:</h2>
        <input placeholder="Здесь запрос..." @input="get_text($event.target.value)" v-model="zarpos">
    </div>
    
</template>
  
<style scoped>
.razdel {
    text-align: center;
    margin: 10px;
}
input {
    width: 400px;
    padding: 10px; 
    font-size: 10px; 
    border-radius: 10px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    font-size:20px;
  }
</style>
  
<script>
export default {
    props: {
        get_text: {
            type:Function,
            required: true
        }
    }
}
</script>
  