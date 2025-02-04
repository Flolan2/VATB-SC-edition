from ultralytics import YOLO
import cv2
import torch

#ask pytorch to fallback to CPU if the function is not implemented in MPS
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"]="1"


def YOLOTracker(filePath, modelPath, device='cpu'):
    
    device = 'cuda' if torch.cuda.is_available() else device
    device = 'mps' if torch.backends.mps.is_available() else device

    model = YOLO(modelPath)
    cap = cv2.VideoCapture(filePath)

    boundingBoxes = []
    frameNumber = 0

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            if frameNumber%10 == 0 : #only do it every 10 frames

                # Run YOLOv8 tracking on the frame, persisting tracks between frames
                results = model.track(frame, persist=True, classes=[0], verbose=False, device=device)
                data = []

                if len(results) > 0 and results[0].boxes is not None and results[0].boxes.id is not None:
                    ind = results[0].boxes.id.cpu().numpy().astype(int)
                    box = results[0].boxes.xyxy.cpu().numpy().astype(int)
                    for i in range(len(ind)):
                        temp = dict()
                        temp['id'] = int(ind[i])
                        temp['x'] = int(box[i][0])
                        temp['y'] = int(box[i][1])
                        temp['width'] = int(box[i][2] - box[i][0])
                        temp['height'] = int(box[i][3] - box[i][1])
                        temp['Subject'] = False
                        data.append(temp)

                frameResults = {'frameNumber': frameNumber, 'data': data}
                boundingBoxes.append(frameResults)
                # print(frameResults)

            else:
                frameResults = {'frameNumber': frameNumber, 'data': data}
                boundingBoxes.append(frameResults)

        else:
            # Break the loop if the end of the video is reached
            break

        frameNumber += 1

    outputDictionary = dict()
    outputDictionary['fps'] = cap.get(cv2.CAP_PROP_FPS)
    outputDictionary['boundingBoxes'] = boundingBoxes
    cap.release()
    return outputDictionary
