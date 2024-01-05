import os
import cv2

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    success, image = cap.read()
    count = 0

    while success:
        frame_path = os.path.join(output_folder, f"frame_{count}.png")

        # Eğer video 16 bit veya 32 bit derinliğine sahipse, cv2.normalize kullanarak normalleştirin.
        if image.dtype != 'uint8':
            normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
            cv2.imwrite(frame_path, normalized_image.astype('uint8'))
        else:
            cv2.imwrite(frame_path, image)

        success, image = cap.read()
        count += 1

    cap.release()

video_folder = "C:\\Users\\User\\Desktop\\okul\\4\\bitirme projesi\\dfdc_train_part_11"
output_folder = "C:\\Users\\User\\Desktop\\okul\\4\\bitirme projesi\\frames_for_11pt3"

# Videoların olduğu klasördeki her bir videoyu işleyin
for video_file in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video_file)
    extract_frames(video_path, output_folder)
