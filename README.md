# Face Blurring using OpenCV and MediaPipe

A computer vision project that detects faces and blurs them in images, videos, and webcam footage.

I built this project to get hands-on experience with OpenCV and MediaPipe and to understand how face detection can be applied to different types of input.

## What it does

* Detects and blurs faces in images
* Detects and blurs faces in videos
* Detects and blurs faces from a webcam in real time

## Libraries used

* Python
* OpenCV
* MediaPipe

## Installation

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

### Image

```bash
python main.py
```

The input image is read from the `data` folder and the blurred image is displayed.

### Video

```bash
python video.py
```

The video is read from the `data` folder and the processed video is saved in the `output` folder.

### Webcam

```bash
python webcam.py
```

The webcam opens and detected faces are blurred in real time.

## How it works

The program uses MediaPipe's face detection model to locate faces in each image or video frame.

The detected face is identified using its bounding box, and OpenCV's blur function is then applied to that region.

For video and webcam input, this process is repeated for each frame.

## Project structure

```text
Face-Blurring/
│
├── main.py
├── webcam.py
├── video.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
└── output/
```
