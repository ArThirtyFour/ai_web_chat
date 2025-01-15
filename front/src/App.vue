<template>
  <div class="main">
    <Main/>
    <Input :get_text="get_text"/>
    <div class="button-container">
      <button @click='send_text(zapros)' v-if="zapros !== ''">Отправить запрос</button>
      <button disabled v-else>Напишите запрос!</button>
      <button @click="reset_text">Очистить историю</button>
      <br>
      <button @click="delete_text">Убрать текст</button>
    </div>
  </div>
  <div class="da" v-html="result"></div>  
</template>


<style scoped>
.main {
  margin-top: 20px; 
  margin-left: 20px;
  margin-right: 20px;
  border: 3px solid rgb(204, 204, 204);
  border-radius: 20px;
  background-color: rgba(21, 143, 17, 0.275);
}
.button-container {
  display: flex;
  justify-content: center; 
  margin-top: 10px; 
}

button {
  color: white;
  background-color: aquamarine;
  text-align: center;
  margin: 0 5px;
  border-radius: 20px;
  border: 3px solid white;
  margin-bottom: 10px;
  font-size: 20px;
  font-family: 'Courier New', Courier, monospace;
}

button:disabled {
  background-color: rgba(6, 243, 191, 0.403);
}

button:hover {
  box-shadow: 2px rgb(0, 0, 0);
  
  color:black
}


.da {
  margin:20px;
  border-radius: 10px;
  border: 3px solid black;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: rgba(86, 86, 86, 0.403);
}
</style>

<script>
import axios from 'axios';
import { marked } from 'marked';
import Main from './components/Main.vue'
import Input from './components/Input.vue'

export default {
  components: { Main, Input },
  data() {
    return {
      zapros: '',
      result: ''
    }
  },
  methods: {
    get_text(text) {
      this.zapros = text;
    },
    send_text(da) {
      axios.post('http://127.0.0.1:5000/api/v1', new URLSearchParams({ zapros: da }))
      .then((response) => {
        if (response.data.status === 'yes') {
          this.result = marked(response.data.answer)
        } else {
          this.result = 'Ошибка! ' + response.data.answer
        }
      });
    },
    reset_text() {
      axios.get('http://127.0.0.1:5000/api/reset')
      .then((response) => {
        if (response.data === 'yes') {
          alert('Память была успешно перезапущена!')
        }
      });
    },
    delete_text() {
      this.result = ''
    }
  }
}
</script>
