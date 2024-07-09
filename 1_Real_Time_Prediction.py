import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import time
from Home import face_rec
import streamlit_modal as st_modal
from Home import face_rec


# Define a function to show notification
def show_notification(message):
    st.main.success(message)

# Streamlit UI setup
st.subheader('Real-Time Attendance System')


# Retrieve data from Redis Database
with st.spinner('Retrieving Data from Redis DB ...'):
    redis_face_db = face_rec.retrive_data(name='academy:register')
    st.dataframe(redis_face_db)

st.success("Data successfully retrieved from Redis")

# Initialize variables
waitTime = 30  # Time in seconds
setTime = time.time()
realtimepred = face_rec.RealTimePred()  # Real-time prediction class

# Define video frame callback function
def video_frame_callback(frame):
    global setTime

    img = frame.to_ndarray(format="bgr24")
    pred_img = realtimepred.face_prediction(img, redis_face_db, 'facial_features', ['Name', 'Role'], thresh=0.5)

    timenow = time.time()
    difftime = timenow - setTime
    if difftime >= waitTime:
        realtimepred.saveLogs_redis()
        setTime = time.time()

        # Check if known face was detected
        if pred_img is not None:
            show_notification(f'Tahniah {username}! Kehadiran anda telah direkod.')
            

    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")

# Streamlit app entry point
def main():
    webrtc_streamer(key="realtimePrediction", video_frame_callback=video_frame_callback,
                    rtc_configuration={
                        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                    })

    # Sidebar notification with close button
    with st.sidebar:
        notification_text = st.empty()
        if notification_text.button("Close"):
            notification_text.empty()

if __name__ == "__main__":
    main()
