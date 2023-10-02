import frappe
import json
import requests
import base64
from frappe.utils import logger
logger.set_log_level("DEBUG")
logger = frappe.logger("api", allow_site=True, file_count=50)

API_KEY = "Your_API_KEY_here"
INFERENCE_URL = "Your_INFERENCE_URL_here"

@frappe.whitelist(allow_guest=True, methods=['POST'])
def transcribe_audio():
    try:
        logger.info('STARTS - voice-to-text transcribe_audio  ------------')
        req_data = json.loads(frappe.request.data)
        service_id = req_data.get('service_id')
        src_lang_code = req_data.get('src_lang_code')
        audio_url = req_data.get('audio_url')


        if not (service_id and src_lang_code and audio_url):
            logger.info('missing paramters')
            frappe.response.http_status_code = 400
            return {'error': 'Missing required parameters'}

        # Download the audio content from the URL as binary data
        audio_response = requests.get(audio_url)

        if audio_response.status_code != 200:
            frappe.response.http_status_code = 500
            return {'error': 'Failed to retrieve audio content from the URL'}

        audio_binary = audio_response.content

        # Convert binary audio content to base64
        audio_content = base64.b64encode(audio_binary).decode("utf-8")

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
            frappe.response.http_status_code = 500
            return {'error': 'Request failed'}

        clip_transcript = response.json()["output"][0]["source"]
        logger.info('ENDS - - voice-to-text transcribe_audio  ------------')
        return {'transcript': clip_transcript}

    except Exception as e:
        frappe.response.http_status_code = 500
        logger.error(e, exc_info=True)
        logger.info('ENDS - - voice-to-text transcribe_audio  ------------')
        return {'error': str(e)}