import gmail
import os
from gtts import gTTS
import uuid

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

g = gmail.login('username','password')
g.inbox().mail()
unread = g.inbox().mail(unread=True)
for key in unread:
    key.fetch()
    text1 = remove_non_ascii_1(key.body)
    filename = str(uuid.uuid4())
    tts = gTTS(text=text1, lang='en')
    tts.save(filename + ".mp3")
    key.read()


