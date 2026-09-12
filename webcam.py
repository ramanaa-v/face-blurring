import os
import cv2
import mediapipe as mp
import argparse


def process_img(img, face_detection):

    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data 
            bounding_box = location_data.relative_bounding_box

            x1, y1, w, h = bounding_box.xmin, bounding_box.ymin, bounding_box.width, bounding_box.height 

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)

            # blur faces
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (50, 50))

    return img


args = argparse.ArgumentParser()

args.add_argument("--mode", default='webcam')
args.add_argument("--filePath", default=None)

args = args.parse_args()

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    if args.mode in ["image"]:

        img = cv2.imread(args.filePath)

        img = process_img(img, face_detection)

        cv2.imwrite(os.path.join(output_dir, 'output.jpg'), img)

    elif args.mode in ['video']:

        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()

        fps = cap.get(cv2.CAP_PROP_FPS)

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'MP4V'),
                                       fps,
                                       (frame.shape[1], frame.shape[0]))


        while ret:
            frame = process_img(frame, face_detection)

            output_video.write(frame)

            ret, frame = cap.read()
        
        cap.release()
        output_video.release()

    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()
        while ret:
            frame = process_img(frame, face_detection)

            cv2.imshow('frame', frame)
            cv2.waitKey(25)

            ret, frame = cap.read()

        cap.release()