import pyttsx3
import redis

r = redis.Redis(host='localhost',port = 6379)
def text_to_speach():
    engine = pyttsx3.init()
    engine.setProperty('rate',130)
    text = r.get('voice').decode()
    print(text)
    engine.say(text)
    return engine.runAndWait()