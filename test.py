import os

emotion_dict = {
    0: 'neutral',
    1: 'happiness',
    2: 'surprise',
    3: 'sadness',
    4: 'anger',
    5: 'disgust',
    6: 'fear'
}
# os.mkdir("Emotion")
os.chdir("Emotion")
os.getcwd()

for i in emotion_dict.values():
    path = i
    os.mkdir(path)