from google.cloud import texttospeech


# pt convert("heyy", "output") => se returneaza

def get_text_as_speech_binary(input_text, file_name):

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    # Saves to disk
    with open("%s.mp3" % file_name, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    return response.audio_content

# INSTALL
# google-cloud-texttospeech

# EXAMPLE
# @simple_page.route('/texttospeech', methods=["POST"])
# def texttospeech():
#     try:
#         input_text = request.form['text']
#         file_name = request.form['filename']
#         audio_binary = text_to_speech_api.get_text_as_speech_binary(input_text, 'output')
#         response = jsonify({"status": "success"})
#     except Exception as e:
#         response = jsonify({"status": "failure", 'message': str(e)})
#
#     return response