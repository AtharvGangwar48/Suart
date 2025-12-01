import cv2
import numpy as np

class FrameExtractor:
    def extract_frames(self, video_path: str, interval: int = 30):
        cap = cv2.VideoCapture(video_path)
        frames = []
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % interval == 0:
                frames.append(frame)
            
            frame_count += 1
        
        cap.release()
        return frames