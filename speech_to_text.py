import os
from google.cloud import speech

# กำหนด path ไปยัง credentials.json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

client = speech.SpeechClient()

# โหลดไฟล์เสียง (ควรเป็น .wav หรือ .flac ที่แปลงมาแล้ว)
with open("test.wav", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # ถ้าเป็น wav
    sample_rate_hertz=16000,  # ต้องตรงกับความถี่ของไฟล์เสียง
    language_code="th-TH"     # ภาษาไทย
)

# ขอผลลัพธ์
response = client.recognize(config=config, audio=audio)

# แสดงผล
for result in response.results:
    print("ข้อความที่รู้จำได้:", result.alternatives[0].transcript)
