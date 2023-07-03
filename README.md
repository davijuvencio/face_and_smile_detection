# Face and Smile Detection

A face and smile detection project that uses OpenCV to classify whether a person is happy or not based on their smile.

## Introduction

The face and smile detection project is an application that utilizes the OpenCV (Open Source Computer Vision Library) to analyze and classify whether a person is happy based on their smile. OpenCV is a popular and widely used library in computer vision projects, providing a comprehensive set of tools and algorithms for image and video processing.

Face and smile detection is an important task in various applications such as facial recognition, facial expression analysis, security, entertainment, and more. This technique involves identifying and locating faces and then analyzing facial attributes such as smiles to perform the desired classification.

To detect faces and smiles, we utilize pre-trained classifiers. These classifiers are based on machine learning algorithms and are trained on large datasets containing positive examples (faces or smiles) and negative examples (images without faces or smiles). In this project, we use the "haarcascade_frontalface_default.xml" and "haarcascade_smile.xml" classifiers provided by OpenCV.

## Functionality

The project utilizes an application called "IP webcam" on an Android device to stream real-time video. The main script, `face_and_smile_detection.py`, uses the OpenCV library to capture and process the received video and perform face and smile detection.

The face detection algorithm uses the "haarcascade_frontalface_default.xml" classifier, which is capable of identifying the presence of faces in an image or video. Once a face is detected, the smile detection algorithm uses the "haarcascade_smile.xml" classifier to check if a smile is present in the mouth region of the detected face.

Based on smile detection, the application classifies the person as happy or not happy. This classification can be displayed in the user interface or used for other purposes such as triggering automated actions or collecting statistical data.

## Installation

1. Clone the repository to your local environment:

```bash
git clone https://github.com/davijuvencio/face_and_smile_detection.git
```

2. Navigate to the project directory:

```bash
cd face_and_smile_detection
```

3. Install the project dependencies:

```bash
pip3 install opencv-python
```

## Usage

1. Open the "IP webcam" application on your Android device.
2. Start the video streaming in the application and note down the displayed IP address and port.
3. In the `face_and_smile_detection.py` file, locate the line that defines the `ip` variable and replace the current URL with the URL of your Android device.
4. Run the `face_and_smile_detection.py` script:

```bash
python3 face_and_smile_detection.py
```

5. The program will detect faces and smiles in the real-time video stream and display whether the person is happy or not.

Make sure you have a stable connection with the Android device to ensure proper detection.

## Contribution

Contributions are always welcome! If you would like to contribute to this project, follow the steps below:

1. Fork this repository.
2. Create a branch for your feature or bug fix: `git checkout -b my-feature`
3. Make your changes and add the modified files: `git add .`
4. Commit your changes: `git commit -m "Add my feature"`
5. Push to the main branch: `git push origin my-feature`
6. Open a pull request on GitHub.

## Contact

If you have any questions or suggestions regarding the project, feel free to contact me.
