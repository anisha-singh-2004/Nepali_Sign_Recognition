import cv2
import os

def convert_video_to_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video information
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each frame and save it as an image
    for frame_number in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame as an image
        frame_filename = f"{output_folder}/frame_{frame_number:04d}.jpg"
        cv2.imwrite(frame_filename, frame)

        print(f"Processed frame {frame_number}/{frame_count}")

    # Release the video capture object
    cap.release()

    print("Video to frames conversion complete.")

# Example usage
video_path = r'C:\Users\anish\AppData\Local\Temp\d8cba927-1483-4ea3-a38d-77c4fb669767_NSL_Vowel.zip.767\NSL_Vowel\S1_NSL_Vowel_Unprepared_Bright\S1_A.MOV'
output_folder = r'C:\Users\anish\Desktop\NGA bright'
convert_video_to_frames(video_path, output_folder)


