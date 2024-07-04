import cv2
import numpy as np
from PIL import Image
import streamlit as st

MODEL = 'model/MobileNetSSD_deploy.caffemodel'
PROTOTXT = 'model/MobileNetSSD_deploy.prototxt.txt'


def detect_object(image):
    image = cv2.resize(image, (300, 300))
    blob = cv2.dnn.blobFromImage(
        image=image, scalefactor=0.007843, size=(300, 300), mean=127.5)
    model = cv2.dnn.readNetFromCaffe(prototxt=PROTOTXT, caffeModel=MODEL)
    model.setInput(blob=blob)
    detections = model.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    (h, w) = image.shape[:2]

    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            start_x, start_y, end_x, end_y = box.astype("int")
            cv2.rectangle(image, (start_x, start_y),
                          (end_x, end_y), (0, 255, 0), 2)

    return image


def main():
    st.write('# Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        image = Image.open(file)
        image = np.array(image)
        detections = detect_object(image)
        processed_img = annotate_image(image=image, detections=detections)

        col1, col2 = st.columns(2)
        col1.image(file, caption='Uploaded Image')
        col2.image(processed_img, caption='Processed Image')


if __name__ == '__main__':
    main()
