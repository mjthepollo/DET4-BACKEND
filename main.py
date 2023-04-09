import datetime
from io import BytesIO

from flask import Flask, jsonify, request

from setup import *
from utility import (add_assistant_message_to_messages,
                     add_user_message_to_messages, create_input_file_name,
                     decode_audio, generate_text,
                     get_audio_file_url_using_polly, get_message_by_chatgpt,
                     save_audio)

app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def generate_answer():
    #When you are debugging the code, I recommend delete this try-except block for debugging.
    try : 
        input_data = request.get_json()
        audio_data = decode_audio(input_data["audio"])
        messages = input_data["messages"]
        save_audio(audio_data, create_input_file_name())
        text_gotten_by_input_data = generate_text(audio_data)
        messages =  add_user_message_to_messages(messages, text_gotten_by_input_data)
        answer_by_chat_gpt = get_message_by_chatgpt(messages)
        output_audio_url = get_audio_file_url_using_polly(answer_by_chat_gpt)
        messages = add_assistant_message_to_messages(messages, answer_by_chat_gpt)
        return jsonify({'messages': messages, "audio_url":output_audio_url}), 200
    except Exception as e:
        return jsonify({"ERROR MSG":e}), 500



def lambda_handler(event, context):
    logger.info(f"Received event: {event}")
    return awsgi.response(app, event, context)


'''
# Without encoding audio file (multipart/form-data, binary file) 
@app.route('/answer', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file in request'}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No audio file selected'}), 400

    try:
        save_file_to_s3(audio_file, audio_file.filename)
        return jsonify({'message': f'{audio_file.filename} uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
'''
