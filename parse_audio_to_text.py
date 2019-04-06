from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
import io


def extract_text(speech_file):
    credentials = service_account.Credentials.from_service_account_file('My First Project-837cb436b57d.json')
    client = speech.SpeechClient(credentials=credentials)
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.types.RecognitionAudio(content=content)
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code='en-US',
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True)

    response = client.recognize(config, audio)
    sentences_with_timemarks = []
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        start = alternative.words[0].start_time.seconds
        end = alternative.words[-1].end_time.seconds
        sentences_with_timemarks.append((alternative.transcript, start, end))
    return sentences_with_timemarks