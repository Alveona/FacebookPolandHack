from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
import io

credentials = service_account.Credentials.from_service_account_file('My First Project-837cb436b57d.json')
client = speech.SpeechClient(credentials=credentials)

speech_file = 'harvard.wav'


with io.open(speech_file, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.types.RecognitionAudio(content=content)
config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code='en-US',
    # Enable automatic punctuation
    enable_automatic_punctuation=True)

response = client.recognize(config, audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}'.format(i))
    print('Transcript: {}'.format(alternative.transcript))
print(1)