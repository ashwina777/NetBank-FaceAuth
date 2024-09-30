# NetBank-FaceAuth

**NetBank-FaceAuth** is a modern, user-friendly net banking website that allows customers to log in securely using either face authentication or traditional username/password methods. This project showcases the integration of web technologies with Python libraries to create an interactive and secure banking interface.

## Features

- **Face Authentication**: Customers can log in seamlessly by clicking the "Login" button to authenticate via facial recognition.
- **Fallback to Password Authentication**: If face authentication fails, users are redirected to a username and password login page.
- **Multiple Payment Options**:
    - Payment by Card
    - Payment by Bank Transfer
    - Apple Pay / Google Pay
- **Form Validation**: Implements form validation to ensure users provide valid details such as card number, CVV, expiry date, and email before proceeding with payments.
- **Confirmation Page**: After a successful transaction, users are greeted with a "Thank You" page confirming the payment.

> **Note**: This project is an initial blueprint and does not yet support real financial transactions. Payment API integration is pending in future updates.

## Technologies Used

- **Frontend**: 
  - `HTML` for structure
  - `CSS` for styling
  - `JavaScript` for interactivity
- **Backend**: 
  - `Python` for core logic
  - `Flask` as the web framework
- **Face Authentication**: 
  - OpenCV (`cv2`) for capturing video from the webcam
  - `face_recognition` library for detecting and recognizing faces

## Setup Instructions

### Step 1: Clone the Repository
   ```bash
   git clone https://github.com/ashwina777/NetBank-FaceAuth.git
   ```
2. Install the required Python libraries referenced in the `requirements.txt` file:
   ```bash
   requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```

## Project Structure

```
FACERECOGNITIONPROJECT/
├── static/
│   ├── style/
│   │   ├── style1.css
│   │   ├── style2.css
│   └── images/
├── js/
│   ├── script1.js
│   ├── script3.js
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── thanks.html
|   ├── website.html
|── main.py
|
|── demo
|   ├── ex.py
|   ├── face_recognition.py
|   ├── face.py
|   ├── face2.py
|
|
├── requirements.txt

```

## License

This project is licensed under the GNU License.
