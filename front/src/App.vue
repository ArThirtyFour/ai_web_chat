<template>
  <div class="container py-4">
    <div class="row">
      <div class="col-12">
        <div class="card shadow-sm">
          <div class="card-body">
            <Main/>
            <Input :get_text="get_text"/>
            <div class="d-flex gap-2 justify-content-center mt-3">
              <button class="btn btn-primary" @click='send_text(zapros)' :disabled="zapros === ''">
                Отправить запрос
              </button>
              <button class="btn btn-warning" @click="reset_text">
                Очистить историю
              </button>
              <button class="btn btn-danger" @click="delete_text">
                Убрать текст
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="row mt-4">
      <div class="col-12">
        <div class="card shadow-sm">
          <div class="card-header bg-light">
            <h5 class="mb-0">История сообщений</h5>
          </div>
          <div class="card-body p-0">
            <div class="chat-history">
              <div v-for="(message, index) in chatHistory" :key="index" class="message-container">
                <div class="message query">
                  <div class="message-header d-flex justify-content-between align-items-center">
                    <h6 class="mb-0">Ваш запрос</h6>
                    <span class="badge bg-primary">{{ message.timestamp }}</span>
                  </div>
                  <div class="message-content">
                    {{ message.query }}
                  </div>
                </div>
                
                <div class="message response" v-if="message.response">
                  <div class="message-header d-flex justify-content-between align-items-center">
                    <h6 class="mb-0">Ответ</h6>
                    <span class="badge bg-success">{{ message.timestamp }}</span>
                  </div>
                  <div class="message-content markdown-body" v-html="message.response"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.markdown-body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
}

.markdown-body pre {
  background-color: #f6f8fa;
  border-radius: 6px;
  padding: 16px;
}

.markdown-body code {
  background-color: rgba(175, 184, 193, 0.2);
  border-radius: 6px;
  padding: 0.2em 0.4em;
}

.badge {
  font-size: 0.8rem;
  padding: 0.5em 0.8em;
}

.chat-history {
  max-height: 600px;
  overflow-y: auto;
}

.message-container {
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}

.message-container:last-child {
  border-bottom: none;
}

.message {
  margin-bottom: 1rem;
}

.message:last-child {
  margin-bottom: 0;
}

.message-header {
  margin-bottom: 0.5rem;
}

.message-content {
  padding: 0.5rem;
  border-radius: 0.5rem;
}

.query .message-content {
  background-color: #e9ecef;
}

.response .message-content {
  background-color: #f8f9fa;
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
      result: '',
      chatHistory: []
    }
  },
  methods: {
    get_text(text) {
      this.zapros = text;
    },
    send_text(da) {
      const timestamp = new Date().toLocaleTimeString();
      const query = da;
      
      // Добавляем запрос в историю
      this.chatHistory.push({
        query,
        timestamp,
        response: null
      });

      axios.post('http://127.0.0.1:5000/api/v1', new URLSearchParams({ zapros: da }))
      .then((response) => {
        if (response.data.status === 'yes') {
          const responseHtml = marked(response.data.answer);
          // Обновляем последний элемент истории с ответом
          this.chatHistory[this.chatHistory.length - 1].response = responseHtml;
          this.result = responseHtml;
        } else {
          const errorMessage = 'Ошибка! ' + response.data.answer;
          this.chatHistory[this.chatHistory.length - 1].response = errorMessage;
          this.result = errorMessage;
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
      this.result = '';
      this.zapros = '';
      this.chatHistory = [];
    }
  }
}
</script>
