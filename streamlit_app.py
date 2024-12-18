import streamlit as st
from streamlit_webrtc import webrtc_streamer , VideoHTMLAttributes
import av
import cv2

st.title("⭐مستقبل التقنية⭐")
st.write("ُمدرسة أسراري")
st.write("ُEnjaz: AI team")


title = st.text_input('(بالانجليزي لوسمحت🙏)وش اسمك🤔؟')
if len(title) > 0:
    st.write('Perfect! now click on "Start"')


#flag = False 
class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200
        # Load pre-trained face detection cascade classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_smile.xml')
        


    def recv(self, frame):
        #global flag
        img = frame.to_ndarray(format="bgr24")

        # Detect faces
        faces = self.face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        font = cv2.FONT_HERSHEY_SIMPLEX 
        # org 
        org = (50, 50) 
          
        # fontScale 
        fontScale = 1
           
        # Blue color in BGR 
        color = (255, 0, 0) 
          
        # Line thickness of 2 px 
        thickness = 2
           
        for (x, y, w, h) in faces:
            #cv2.rectangle(img, (10, 10), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, 'Hi, :) SMILE!' , (20, 40), font,  fontScale, color, thickness, cv2.LINE_AA)
            
            # Region of interest for smile detection within the face
            roi_gray = img[y:y+h, x:x+w]
            smiles = self.smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=30, minSize=(20, 20))

            for (sx, sy, sw, sh) in smiles:
                #cv2.rectangle(roi_gray, (x+sx, y+sy), (x+sx+sw, y+sy+sh), (0, 255, 0), 2)
                cv2.putText(img, 'Welcome ' + title , (x, y), font,  fontScale, (255,5,171), thickness, cv2.LINE_AA)                
                #cv2.rectangle(roi_gray, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
                #cv2.rectangle(roi_gray, (x+sx, y+sy), (sx+sw, sy+sh), (0, 255, 0), 2)


            
        return av.VideoFrame.from_ndarray(img, format="bgr24")

        

ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    } , video_html_attrs=VideoHTMLAttributes(
        autoPlay=True, controls=True, style={"width": "100%"}, muted=True )
)


    




