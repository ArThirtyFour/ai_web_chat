import google.generativeai as genai

api_Key = 'da'

genai.configure(api_key=api_Key)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[]
)

def get_ai(message):
    response = chat.send_message(message).text
    chat.history.append({"role": "user", "parts": [message]})
    chat.history.append({"role": "model", "parts": [response]})
    return response

def reset_memory():
    chat.history.clear()
    return 'История чата очищена!'
