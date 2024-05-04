import cv2
import os
import base64
import requests
import numpy as np
import smtplib,ssl
import datetime
from pygame import mixer
import pymongo
from pymongo.mongo_client import MongoClient

weight="C:\\Users\\VIRENDRA\\Desktop\\Netra\\yolov3_w.weights"
cfg='C:\\Users\\VIRENDRA\\Desktop\\Netra\\yolov3_c.cfg'
#Load yolo
mixer.init()
USERNAME = "netra"
PASSWORD = "netra2023"
uri = "mongodb+srv://netra:netra2023@netra.pfaeh8r.mongodb.net/?retryWrites=true&w=majority&appName=Netra"
client = MongoClient(uri)
db = client['Netra']
collection = db['alerts']
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
mixer.music.load('alert.mpeg')

def load_yolo():
    net = cv2.dnn.readNet(weight,cfg)
    classes = []
    with open("obj.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layers_names = net.getLayerNames()
    output_layers = [layers_names[i-1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    return net, classes, colors, output_layers

def display_blob(blob):
    '''
        Three images each for RED, GREEN, BLUE channel
    '''
    for b in blob:
        for n, imgb in enumerate(b):
            cv2.imshow(str(n), imgb)

def detect_objects(img, net, outputLayers):			
    blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs

def get_box_dimensions(outputs, height, width):
    boxes = []
    confs = []
    class_ids = []
    for output in outputs:
        for detect in output:
            scores = detect[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > 0.3:
                center_x = int(detect[0] * width)
                center_y = int(detect[1] * height)
                w = int(detect[2] * width)
                h = int(detect[3] * height)
                x = int(center_x - w/2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)
                
    return boxes, confs, class_ids

def draw_labels(boxes, confs, colors, class_ids, classes, img,street_land,area,city,state,country,zipcode,cameranumip): 
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            date = str(datetime.datetime.now())
            print(label,"detected in frame")
    
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 1.5, color, 2)
            
            mixer.music.play()
            img_name = f"detected_{label}_{date.replace(':', '_')}.png"
            img_path = os.path.join("detected_images", img_name)
            os.makedirs("detected_images", exist_ok=True)
            cv2.imwrite(img_path, img)
            print(f"Image saved: {img_path}")
            # Convert the image to bytes
            _, encoded_image = cv2.imencode('.jpg', img)
            image_buffer = encoded_image.tobytes()
##            encoded_image_str = base64.b64encode(encoded_image).decode('utf-8')
            document = {
                'label': label,
                'timestamp': date,
                'street_land': street_land,
                'area': area,
                'city': city,
                'state': state,
                'country': country,
                'zipcode': zipcode,
                'cameranumip': cameranumip,
                'image_data': image_buffer,
                'contentType':'image/png'
            }
            result = collection.insert_one(document)
            print('Inserted document ID:', result.inserted_id)
            print("Image data stored in the database")
    img=cv2.resize(img, (1000,800))
    cv2.imshow("Image", img)

def start_video(street_land,area,city,state,country,zipcode,cameranumip):
    print("Street/Landmark :", street_land)
    print("Area :", area)
    print("City :", city)
    print("State :", state)
    print("Country :", country)
    print("Zip Code :",zipcode)
    model, classes, colors, output_layers = load_yolo()
    cap = cv2.VideoCapture(cameranumip)
    start=datetime.datetime.now()
    fps=0
    total=0
    
    font=cv2.FONT_HERSHEY_COMPLEX
    frame_no = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if ret==True:
            dt = str(datetime.datetime.now())
            print("for frame : " + str(frame_no) + "   timestamp is: ", str(cap.get(cv2.CAP_PROP_POS_MSEC)))
            frame = cv2.putText(frame, dt,(5, 80),font, 1,(0, 0, 255),1, cv2.LINE_8)
            total=total+1
            end_time=datetime.datetime.now()
            time_diff=end_time - start
            
            if time_diff.seconds==0:
                fps=0.0
            else: 
                fps=(total/time_diff.seconds)
            
            fps_text="FPS : {:.2f}".format(fps)
            cv2.putText(frame,fps_text,(5,30),cv2.FONT_HERSHEY_COMPLEX,1 ,(0,0,255),1)
            height, width, channels = frame.shape
            blob, outputs = detect_objects(frame, model, output_layers)
            boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
            draw_labels(boxes, confs, colors, class_ids, classes, frame,street_land,area,city,state,country,zipcode,cameranumip)
            
            

            key = cv2.waitKey(1)
            if key==ord('q'):
                break
        else:
            print("video is end")
            break
        frame_no+=1
    cap.release()
    cv2.destroyAllWindows()
    print("video end")
