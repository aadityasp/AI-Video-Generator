import cv2  # Import OpenCV
from PIL import Image  # Import Image from PIL (Python Imaging Library)

def images_to_video(images, output_path, fps=24):
    """
    Convert a sequence of images to a video.

    :param images: A list of PIL Image objects
    :param output_path: The path to save the output video
    :param fps: The frames per second for the output video (default: 24)
    :return: None
    """
    # Get the dimensions of the first image
    width, height = images[0].size

    # Create a VideoWriter object to write the video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Write the images to the video
    for image in images:
        # Convert the PIL Image to an OpenCV-compatible format
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

    # Release the VideoWriter object
    video_writer.release()
