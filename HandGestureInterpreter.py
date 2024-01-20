import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandGestureInterpreter:
    def __init__(self):
        # Create videoCapture object with the default webcam
        self.vid = cv.VideoCapture(0)
        # Create a gesture recognizer object
        base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(base_options=base_options)
        self.recognizer = vision.GestureRecognizer.create_from_options(options)

    def get_hand_gesture(self):
        """
        :return: A string representing the hand gesture captured with webcam footage
        """
        # Get a video frame from live camera footage
        ret, frame = self.vid.read()

        # Convert to a mediapipe image and detect hands
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        recognizer_result = self.recognizer.recognize(mp_image)

        # # Flip the image because it is mirrored by default
        # frame = cv.flip(frame, 1)
        #
        # # Show the image
        # cv.imshow('frame', frame)

        # Display the result of the recognizer
        gestures = recognizer_result.gestures
        if len(gestures) > 0:
            print(gestures[0][0].category_name)
            return gestures[0][0].category_name
        else:
            print("No Hands")
            return "No Hands"

    def stop_video(self):
        """
        Stops the webcam footage and closes all openCV windows
        """
        self.vid.release()
        cv.destroyAllWindows()
