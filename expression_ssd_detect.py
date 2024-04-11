import threading
import webbrowser
from machine_learning import *  # import contains functions for the emotion detection in the fer_live_cam

app = Tk()  # Instantiate tkinker class

# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())

# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()

# capturing video from the user's webcam
cap = cv2.VideoCapture(0)

# data structure to catch the most accurate emotion detected
emo = {}


# function that runs the logic for the emotion detection and displays the tkinter GUI
def Start_cam():
    emotion_dict = {
        0: 'neutral',
        1: 'happiness',
        2: 'surprise',
        3: 'sadness',
        4: 'anger',
        5: 'disgust',
        6: 'fear'
    }

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)

    model = cv2.dnn.readNetFromONNX('emotion-ferplus-8.onnx')

    model_path = 'RFB-320/RFB-320.caffemodel'
    proto_path = 'RFB-320/RFB-320.prototxt'
    net = dnn.readNetFromCaffe(proto_path, model_path)
    input_size = [320, 240]
    width = input_size[0]
    height = input_size[1]
    priors = define_img_size(input_size)

    while True:
        ret, frame = cap.read()
        frame[:, :] = frame[:, ::-1]
        x = 0
        if ret:
            img_ori = frame
            rect = cv2.resize(img_ori, (width, height))
            rect = cv2.cvtColor(rect, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


            net.setInput(dnn.blobFromImage(rect, 1 / 128.0, (width, height), 127))
            start_time = time.time()
            boxes, scores = net.forward(["boxes", "scores"])
            boxes = np.expand_dims(np.reshape(boxes, (-1, 4)), axis=0)
            scores = np.expand_dims(np.reshape(scores, (-1, 2)), axis=0)
            boxes = convert_locations_to_boxes(boxes, priors, center_variance, size_variance)
            boxes = center_form_to_corner_form(boxes)
            boxes, labels, probs = predict(img_ori.shape[1], img_ori.shape[0], scores, boxes, threshold)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            for (x1, y1, x2, y2) in boxes:
                w = x2 - x1
                h = y2 - y1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                resize_frame = cv2.resize(gray[y1:y1 + h, x1:x1 + w], (64, 64))
                resize_frame = resize_frame.reshape(1, 1, 64, 64)
                model.setInput(resize_frame)
                output = model.forward()
                end_time = time.time()
                fps = 1 / (end_time - start_time)
                pred = emotion_dict[list(output[0]).index(max(output[0]))]
                cv2.rectangle(img_ori, (x1, y1), (x2, y2), (215, 5, 247), 2, lineType=cv2.LINE_AA)
                cv2.putText(frame, pred, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (215, 5, 247), 2,
                            lineType=cv2.LINE_AA)

                if pred not in emo:
                    emo[pred] = 1
                else:
                    emo[pred] = emo[pred] + 1

            captured_image = Image.fromarray(frame)  # passing the frame to tkinter to be displayed
            photo_image = ImageTk.PhotoImage(image=captured_image)
            label_widget.photo_image = photo_image
            label_widget.configure(image=photo_image)

            cv2.waitKey(10)


# Create a thread to run the function
thread = threading.Thread(target=Start_cam)
thread.daemon = True
thread.start()


def action():
    url = "file:///C:/Users/Deandre/Downloads/Soulja%20Boy-%20Doo%20Doo%20Head.mp3"
    webbrowser.open(url)
    maxx = max(emo.values())
    for k in emo.keys():
        if emo[k] == maxx:
            print(f'Your mood is {k}')

    app.quit()  # freeing resources


button1 = Button(app, text="Open Music", command=action)  # Dummy command, since camera is already open
button1.pack()
Button2 = Button

# Create an infinite loop for displaying app on screen
app.mainloop()
