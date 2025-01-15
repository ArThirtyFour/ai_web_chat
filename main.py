import json
from ai import get_ai , reset_memory
from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/v1', methods=['POST'])
def get_from_api():
    try:
        da = request.form['zapros']
        response = get_ai(da)
        answer = {
            'status': 'yes',
            'answer': response
        }
        return json.dumps(answer,ensure_ascii=False)  
    except Exception as e:
        error = {'status': 'error', 'answer': str(e)}
        return json.dumps(error,ensure_ascii=False)  
@app.route('/api/reset')
def reset():
    reset_memory()
    return 'yes'


if __name__ == "__main__":
    app.run(debug=True)
