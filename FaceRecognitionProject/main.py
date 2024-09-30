from flask import Flask, render_template, jsonify
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)

def faceRecognition():
    known_face_encodings = []
    known_face_names = []
    # add your images in image folder and add the path of the images in known_images list as follows
    # known_images =['image/1.jpg','image/2.jpg','image/3.jpg','image/4.jpg','image/5.jpg']
   
    known_images=['image/6.jpeg','image/7.jpeg','image/8.jpeg','image/9.jpeg']
    known_names = ["Person1", "Person1", "Person1", "Person1"]  

    for image_path, name in zip(known_images, known_names):
        try:
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
        except IndexError:
            return jsonify({"status": "error", "message": f"No face found in the image '{image_path}'."})

    face_locations = []
    face_encodings = []

    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        return jsonify({"status": "error", "message": "Could not access the webcam."})

    frame_count = 0
    max_frames = 10
    access_granted_frames = 0

    while frame_count < max_frames:
        ret, frame = video_capture.read()
        if not ret:
            return jsonify({"status": "error", "message": "Failed to capture image from webcam."})

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index] and face_distances[best_match_index] < 0.45:
                access_granted_frames += 1

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Press 'q' on the keyboard to exit early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_count += 1

    video_capture.release()
    cv2.destroyAllWindows()

    if access_granted_frames > max_frames // 2:
        return jsonify({"status": "success", "message": "Access granted!"})
    else:
        return jsonify({"status": "failure", "message": "Access denied!"})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/website')
def website():
    return render_template('website.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/face_authenticate', methods=['POST'])
def face_authenticate():
    return faceRecognition()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
