from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import requests

app = Flask(__name__, static_folder=r'C:\Users\student1\Desktop\Project_1\Frontend', template_folder=r'C:\Users\student1\Desktop\Project_1\Frontend')

openai_api_key = 'sk-Us7gv-qtD_SU37oqY7_3SjA7_pwSVIx-pN0-EZvHDCT3BlbkFJzjQ-r2zKOKHoR6rgpnJsRmyqMsJI24ova_aWIuWv8A'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text_input = data.get('text')
    print(f"Received text input: {text_input}")

    openai_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}',
    }
    openai_data = {
        'prompt': f'Generate a Blender script based on the input: {text_input}',
        'max_tokens': 1024,
        'temperature': 0.7,
    }
    openai_response = requests.post('https://api.openai.com/v1/completions', json=openai_data, headers=openai_headers)
    blender_script = openai_response.json()['choices'][0]['text']

    script_path = 'blender_script.py'
    with open(script_path, 'w') as script_file:
        script_file.write(blender_script)

    os.system(f'blender --background --python {script_path}')

    return jsonify({"model_path": r'C:\Users\student1\Desktop\Project_1\blender_script.py'})  # Update with actual output path

@app.route('/models/<filename>')
def serve_model(filename):
    return send_from_directory('models', filename)

if __name__ == '__main__':
    app.run(debug=True)