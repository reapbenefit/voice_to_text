from flask import Flask, request, jsonify
import base64
import requests
import json

app = Flask(__name__)

# Load API key and inference URL from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

API_KEY = config.get('api_key')
INFERENCE_URL = config.get('inference_url')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    service_id = request.form.get('service_id')
    src_lang_code = request.form.get('src_lang_code')
    audio_file = request.files.get('audio_content')

    if not (service_id and src_lang_code and audio_file):
        return jsonify({'error': 'Missing required parameters'}), 400

    audio_content = base64.b64encode(audio_file.read()).decode("utf-8")

    inference_cfg = {
        "language": {"sourceLanguage": src_lang_code}
    }

    inference_inputs = [{"audioContent": audio_content}]

    headers = {"authorization": API_KEY}

    response = requests.post(
        f"{INFERENCE_URL}/asr?serviceId={service_id}",
        headers=headers,
        json={"config": inference_cfg, "audio": inference_inputs}
    )

    if response.status_code != 200:
        return jsonify({'error': 'Request failed'}), 500

    clip_transcript = response.json()["output"][0]["source"]
    return jsonify({'transcript': clip_transcript})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
 
