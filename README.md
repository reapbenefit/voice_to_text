# Voice-to-Text

Voice-to-Text is a Python application that leverages AI4BHARAT models to perform voice to text conversion using API calls. This project allows you to transcribe spoken words from audio recordings into written text, making it useful for various applications such as transcription services, voice assistants, and more. 

## Features

- Utilizes AI4BHARAT's pre-trained models for accurate and efficient voice-to-text conversion.
- Easy-to-use Python script for making API calls and obtaining transcriptions.
- Support for various audio formats.
- Customization options for API requests to adapt to different use cases.
- Detailed documentation to help you get started quickly.

## Table of Contents
- [Python](#python)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Configuration](#configuration)
- [Frappe](#frappe)
    - [Installation](#installation)
    - [Locating Samaaja](#locating-samaaja)
    - [Usage](#usage-1)

- [Contributing](#contributing)
- [License](#license)

## Python  
### Installation

To get started with Voice-to-Text, follow these installation steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/voice-to-text.git
   cd voice-to-text
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the Voice-to-Text application and make a POST request via the terminal, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the project directory:

   ```bash
   cd path/to/voice-to-text
   ```

3. Start the Flask application by running the Python script:
    ```bash
   python python_script.py
   ```
   The app will start running with the host set to '127.0.0.1' and port set to 5000.

4. Open another terminal window or tab.

5. Use curl to make a POST request to your Flask API endpoint with the specified parameters, including the audio file:
   ```bash
   curl -X POST -F "service_id=your_service_id" -F "src_lang_code=your_language_code" -F "audio_content=@path/to/your/audio_file.wav" http://localhost:5000/transcribe
   ```
    Replace the following placeholders:
    - your_service_id with the appropriate service ID from service_ids.xlsx.
    - your_language_code with the desired language code.
    - path/to/your/audio_file.wav with the path to your audio file.

6. Press Enter to make the POST request.

This will send a POST request to your Flask API via the terminal, including the specified parameters and audio file. Your Flask server should process the request and return the transcript.

If you encounter any issues, please ensure that your Flask server is running on http://localhost:5000, and that you've followed the steps correctly.

### Configuration

Before using Voice-to-Text, you need to configure the API credentials. Follow these steps:

1. Sign up or log in to your AI4BHARAT account.

2. Generate API credentials, such as an API key or token, from your AI4BHARAT dashboard.

3. Open the config.json file located in the project directory.

4. Replace the placeholder values in config.json with your API credentials:
   ```json
   {
       "api_key": "your_api_key_here",
       "api_url": "https://api.ai4bharat.org/asr/v0.2/recognize"
   }
   ```

   Replace `"your_api_key_here"` with your actual API key/token.

4. Save the `config.json` file.

## Frappe

### Installation

* [**Install Bench & Frappe**](https://github.com/frappe/bench#installation)

* Download the Samaaja app
   ```bash
      bench get-app https://github.com/fossunited/Samaaja
   ```
      

* Install the app on your site
   ```bash
      bench --site <your-site-name-here> install-app samaaja
   ```

### Locating Samaaja
For locatiing your Samaaja app follow the given steps :

1. Navigate to frappe folder, open frappe-bench.

2. Navigate to apps/saamaja

3. Open this folder in a VS Code-like editor.

### Usage

To run the Voice-to-Text application in the samaaja interface and make a POST request via the terminal, follow these steps:

1. Inside the "Samaaja" folder, navigate to the "samaaja/api" folder.

2. Open the "voice_to_text" folder in the VS Code-like editor.

3. Locate the "frappe_script.py" file inside the "voice_to_text" folder.

4. Copy the "frappe_script.py" file.

5. Go back to the "api" folder (step 3), and paste the copied "frappe_script.py" file there.

6. Open the "frappe_script.py" file that you've just pasted into the "api" folder.

7. Inside the "frappe_script.py" file, locate the following lines:
   ```bash
   API_KEY = "Your_API_KEY_here"
   INFERENCE_URL = "Your_INFERENCE_URL_here"
   ```

8. Replace "Your_API_KEY_here" with your actual API key.

9. Replace "Your_INFERENCE_URL_here" with your actual inference URL.

10. Save the changes to the "frappe_script.py" file.

11. Open your terminal or command prompt.

12. Navigate to the project directory:

    ```bash
    cd path/to/frappe-bench
    ```
13. Run frappe-bench:
    ```bash
    bench start
    ```

14. Open another terminal window or tab.

15. Use curl to make a POST request to your Flask API endpoint with the specified parameters, including the audio file:
      ```bash
         curl -X POST -F "service_id=your_service_id" -F "src_lang_code=your_language_code" -F "audio_url=http://example.com/path/to/your/audio_file.wav" http://127.0.0.1:8000/api/method/samaaja.api.frappe_script.transcribe_audio
      ```
      Replace the following placeholders:
       - your_service_id with the appropriate service ID from service_ids.xlsx.
       - your_language_code with the desired language code.
       - http://example.com/path/to/your/audio_file.wav with the URL to your audio file.

16. Press Enter to make the POST request.

This will send a POST request to your Frappe API via the terminal, including the specified parameters and audio file url. Your Frappe server should process the request and return the transcript.

If you encounter any issues, please ensure that your Frappe server is running on http://127.0.0.1:8000, and that you've followed the steps correctly.

## Contributing

We welcome contributions to improve Voice-to-Text. To contribute, follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes, test thoroughly, and ensure proper documentation.

4. Commit your changes with clear and concise messages.

5. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature
   ```

6. Create a pull request to the main repository's `master` branch, describing your changes and their purpose.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for details.
