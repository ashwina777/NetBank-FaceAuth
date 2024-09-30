# import cv2
# import dlib
# import face_recognition

# # Load a sample picture and learn how to recognize it.
# known_image = face_recognition.load_image_file("myImage.jpg")
# known_face_encoding = face_recognition.face_encodings(known_image)[0]

# # Initialize some variables
# face_locations = []
# face_encodings = []

# # Capture video from the webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Grab a single frame of video
#     ret, frame = video_capture.read()

#     # Resize frame for faster processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#     # Convert the image from BGR color (OpenCV uses) to RGB color (face_recognition uses)
#     rgb_small_frame = small_frame[:, :, ::-1]

#     # Find all the faces and face encodings in the current frame of video
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     # Loop through each face in this frame of video
#     for face_encoding in face_encodings:
#         # Check if the face matches the known face(s)
#         matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
#         if True in matches:
#             print("Access granted!")
#             break
#         else:
#             print("Access denied!")

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Hit 'q' on the keyboard to quit!
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()

print('h')