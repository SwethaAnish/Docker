
from flask import Flask, render_template, Response
import cv2
app = Flask("face-recognition")
def face_recognition():
    face_detector = cv2.CascadeClassifier("harcascade-face.xml")
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            det = face_detector.detectMultiScale(frame,1.3,5)
            for (x,y,w,h) in det:
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)
            ret_, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()  
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(face_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)



