import cv2


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

my_camera = cv2.VideoCapture(1)

while True:

    validation, frame =  my_camera.read()

    if validation is not True:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols = frame_gray.shape

    half_frame = frame_gray[: , 0:cols//2 ]

    flipped_half_frame = cv2.flip(half_frame, 1)

    frame_gray[: , cols//2:] = flipped_half_frame

   
    cv2.imshow('output', frame_gray)
    cv2.waitKey(1)

