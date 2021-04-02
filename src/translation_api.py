import six
from google.cloud import translate_v2 as translate


def translate_text(target, input_text):
    translate_client = translate.Client()
    result = translate_client.translate(input_text, target_language=target)
    return {
        'text': result['input'],
        'translation': result['translatedText'],
        'detected_language': result['detectedSourceLanguage']
    }


# Example
#
# import translation_api

# @simple_page.route('/translate', methods=["POST"])
# def translate():
#     language = request.form['language']
#     input_text = request.form['text']
#     return translation_api.translate_text(language, input_text)

