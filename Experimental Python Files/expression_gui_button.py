#  MODEL Citation: @inproceedings{BarsoumICMI2016,
#     title={Training Deep Networks for Facial Expression Recognition with Crowd-Sourced Label Distribution},
#     author={Barsoum, Emad and Zhang, Cha and Canton Ferrer, Cristian and Zhang, Zhengyou},
#     booktitle={ACM International Conference on Multimodal Interaction (ICMI)},
#     year={2016}
# }

import threading
from tkinter import *
from cv2 import dnn
import cv2
from PIL import Image, ImageTk

import MusicPlayer
from MachineLearning import *  # import contains functions for the emotion detection in the fer_live_cam
import FrameGui


# application = Tk()  # Instantiate Tkinker class
#
# # Bind the app with Escape keyboard to
# # quit app whenever pressed
# application.bind('<Escape>', lambda e: application.quit())

# Create a label and display it on app
# label_widget = Label(app)
# label_widget.pack()

# capturing video from the user's webcam


# function that runs the logic for the emotion detection and displays the tkinter GUI
class Emotion:
    def __init__(self, app) -> None:
        self.app = app
        self.cap = cv2.VideoCapture(0)
        self.cancel_cam = False
        # width = self.app.winfo_screenwidth()
        #
        # height = self.app.winfo_screenheight()
        # # setting tkinter window size
        #
        # self.app.geometry("%dx%d" % (width, height))
        self.app.attributes("-fullscreen", True)
        self.app.configure(background="#404040")

        # data structure to catch the most accurate emotion detected
        self.emo = {}
        self.button1 = Button(self.app, text="▶️ PLAY MUSIC", font=("Arial BOLD", 25), fg='black', bg='light blue',
                              height=1, width=20, command=self.action)
        self.button1.grid(row=1, column=0)

        self.thread_start()
        # self.label_widget = Label(app) # option
        # self.label_widget.pack()

        # self.display = FrameGui.Frame_gui(np.zeros(3),self.app)
        self.captured_img = None
        self.photo = None
        self.label = Label(self.app, bg="#404040")

        self.label.grid(row=0, column=0, sticky=NSEW)

    def start_cam(self):
        emotion_dict = {
            0: 'neutral',
            1: 'happiness',
            2: 'surprise',
            3: 'sadness',
            4: 'anger',
            5: 'disgust',
            6: 'fear'
        }

        model = cv2.dnn.readNetFromONNX('ML-MODEL-emotion-ferplus-8.onnx')  # Our machine learning model

        model_path = 'RFB-320/RFB-320.caffemodel'
        proto_path = 'RFB-320/RFB-320.prototxt'
        net = dnn.readNetFromCaffe(proto_path, model_path)
        input_size = [320, 240]
        width = input_size[0]
        height = input_size[1]
        priors = define_img_size(input_size)

        #########################################
        img_ori = None

        rect = None

        frame = None

        while True:
            ret, frame = self.cap.read()
            if self.cancel_cam:
                # cv2.waitKey(0)
                break
            frame[:, :] = frame[:, ::-1]

            if ret:
                img_ori = frame

                rect = cv2.resize(img_ori, (width, height))
                rect = cv2.cvtColor(rect, cv2.COLOR_BGR2RGB)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                net.setInput(dnn.blobFromImage(rect, 1 / 128.0, (width, height), 127))

                boxes, scores = net.forward(["boxes", "scores"])
                boxes = np.expand_dims(np.reshape(boxes, (-1, 4)), axis=0)
                scores = np.expand_dims(np.reshape(scores, (-1, 2)), axis=0)
                boxes = convert_locations_to_boxes(boxes, priors, center_variance, size_variance)
                boxes = center_form_to_corner_form(boxes)
                boxes, labels, probs = predict(img_ori.shape[1], img_ori.shape[0], scores, boxes, threshold)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # print(frame.shape)
                for (x1, y1, x2, y2) in boxes:
                    w = x2 - x1
                    h = y2 - y1
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    resize_frame = cv2.resize(gray[y1:y1 + h, x1:x1 + w], (64, 64))
                    resize_frame = resize_frame.reshape(1, 1, 64, 64)
                    model.setInput(resize_frame)
                    output = model.forward()

                    # fps = 1 / (end_time - start_time)
                    pred = emotion_dict[list(output[0]).index(max(output[0]))]
                    cv2.rectangle(img_ori, (x1, y1), (x2, y2), (215, 5, 247), 2, lineType=cv2.LINE_AA)
                    cv2.putText(frame, pred, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (215, 5, 247), 2,
                                lineType=cv2.LINE_AA)

                    if pred not in self.emo:
                        self.emo[pred] = 1
                    else:
                        self.emo[pred] = self.emo[pred] + 1

                # captured_image = Image.fromarray(frame)  # passing the frame to tkinter to be displayed
                # photo_image = ImageTk.PhotoImage(image=captured_image)
                # self.label_widget.photo_image = photo_image
                # self.label_widget.configure(image=photo_image)
                # self.display.set_pack(frame,True)

                ##########################################################################
                # self.captured_img = Image.fromarray(frame)
                # self.photo = ImageTk.PhotoImage(self.captured_img)
                # self.label.image = self.photo
                # self.label.grid(row=0, column=0, sticky=NSEW)

                self.captured_img = Image.fromarray(frame)
                self.photo = ImageTk.PhotoImage(self.captured_img)
                self.label.photo_image = self.photo
                self.label.configure(image=self.photo)

                ##########################################################################
                try:
                    self.button1.config(text=f"{pred} {self.emo[pred]}")
                except:
                    print("Mood not detected yet")
            # if self.cancel_cam:
            #     # cv2.waitKey(0)
            #     break

    # Create a thread to run the function
    # thread = threading.Thread(target=Start_cam)
    # thread.daemon = True
    # thread.start()

    # Start_cam()

    def thread_start(self):

        # Create a thread to run the function
        thread = threading.Thread(target=self.start_cam)
        # thread.daemon = True
        thread.start()

    def action(self):
        """Event handler for the Play Music Button"""
        mood_count = max(self.emo.values())
        mood = ""
        for k in self.emo.keys():
            if self.emo[k] == mood_count:
                mood = k
                print(f'Your mood is {k}')
        self.cancel_cam = True
        self.cap.release()
        self.button1.destroy()
        thread_music = threading.Thread(target=MusicPlayer.Window, args=(self.app, mood,))
        thread_music.start()


if __name__ == "__main__":
    application = Tk()
    Emotion(application)
    application.mainloop()
