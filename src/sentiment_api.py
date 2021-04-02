from google.cloud import language_v1


def analyze(input_text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=input_text, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    result = {'overall_sentiment_score': score,
              'overall_sentiment_magnitude': magnitude,
              }
    sentiments = []
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        sentiments.append({'sentence_number': index, 'sentence_sentiment': sentence_sentiment})

    result['sentiments'] = sentiments
    return result

# INSTALL
# google-cloud-translate
# google-cloud-storage
# google-cloud-language

# Example

# import sentiment_api
#
# @simple_page.route('/sentiment', methods=["POST"])
# def get_sentiment():
#     input_text = request.form['text']
#     analysis = sentiment_api.analyze(input_text)
#     return jsonify(analysis)

#         "formdata": [
#             {
#                 "key": "text",
#                 "value": "I'm a depressed pacient from Bucharest!",
#                 "type": "text"
#             }
# ]
