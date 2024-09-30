import cv2
import face_recognition
import numpy as np
def faceRecognition():
    # Load multiple known face images and learn how to recognize them.
    known_face_encodings = []
    known_face_names = []

    # List of known images and corresponding names
    known_images = ["image.jpg", "image1.jpg", "me.jpg", "myImage.jpg"]  # Add more images as needed
    known_names = ["Person1", "Person1", "Person1", "Person1"]  # Corresponding names for the images

    # Load and encode each known image
    for image_path, name in zip(known_images, known_names):
        try:
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
        except IndexError:
            print(f"No face found in the image '{image_path}'. Please use an image with a clear face.")
            exit()

    # Initialize some variables
    face_locations = []
    face_encodings = []

    # Capture video from the webcam
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not access the webcam.")
        exit()

    # Parameters for accuracy improvement
    frame_count = 0
    max_frames = 10  # Number of frames to consider for decision
    access_granted_frames = 0

    while frame_count < max_frames:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image from webcam.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (OpenCV uses) to RGB color (face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through each face in this frame of video
    for face_encoding in face_encodings:
        # Compare face with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        
        # Use the known face with the smallest distance to the new face
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index] and face_distances[best_match_index] < 0.45:  # Adjusted threshold
            access_granted_frames += 1
            print(f"Frame {frame_count + 1}: Access granted to {known_face_names[best_match_index]} with distance {face_distances[best_match_index]:.2f}!")
        else:
            print(f"Frame {frame_count + 1}: Access denied with distance {face_distances[best_match_index]:.2f}!")

    # Display the resulting frame
    cv2.imshow('Video', frame)
    frame_count += 1

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return

    if access_granted_frames > max_frames // 2:
        print("Final Decision: Access granted!")
    else:
        print("Final Decision: Access denied!")

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()