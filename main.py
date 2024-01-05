"""Bu script, belirtilen bir video klasöründeki her videoyu açar, her kareyi ayırır ve belirtilen bir çıkış klasörüne kaydeder."""

import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    success, image = cap.read()
    count = 0

    while success:
        frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, image)
        success, image = cap.read()
        count += 1

    cap.release()

video_folder = "C:\\Users\\User\\Desktop\\okul\\4\\bitirme projesi\\dfdc_train_part_10"
output_folder = "C:\\Users\\User\\Desktop\\okul\\4\\bitirme projesi\\frames_for_10"

# Videoların olduğu klasördeki her bir videoyu işleyin
for video_file in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video_file)
    extract_frames(video_path, output_folder)
