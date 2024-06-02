from flask import Flask, request, jsonify
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech
import openai
import os
from credentials import config

app = Flask(__name__)

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/google-cloud-service-account.json"

# Set up OpenAI API key
openai.api_key = config.OPENAI_API_KEY


# Speech-to-Text
def transcribe_audio(content):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        return result.alternatives[0].transcript

# OpenAI API for generating response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Text-to-Speech
def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response.audio_content

@app.route('/process_audio', methods=['POST'])
def process_audio():
    file = request.files['file']
    content = file.read()
    
    # Step 1: Transcribe audio to text
    transcribed_text = transcribe_audio(content)
    
    # Step 2: Generate response using OpenAI API
    response_text = generate_response(transcribed_text)
    
    # Step 3: Convert response text to audio
    audio_content = text_to_speech(response_text)
    
    return audio_content, 200, {'Content-Type': 'audio/mpeg'}

if __name__ == '__main__':
    app.run(debug=True)
