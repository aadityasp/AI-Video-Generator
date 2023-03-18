import argparse  # Import argparse for parsing command-line arguments
from models.text_to_image import generate_images  # Import generate_images from text_to_image.py
from models.image_to_video import images_to_video  # Import images_to_video from image_to_video.py

def main(input_text, output_path, num_images=10, fps=24):
    """
    Main function to generate a video from input text using the AI-Video-Generator project.

    :param input_text: The input text to generate images from
    :param output_path: The path to save the output video
    :param num_images: The number of images to generate (default: 10)
    :param fps: The frames per second for the output video (default: 24)
    :return: None
    """
    # Generate images from the input text
    images = generate_images(input_text, num_images=num_images)

    # Convert the images to a video
    images_to_video(images, output_path, fps=fps)

if __name__ == "__main__":
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="AI-Video-Generator")
    parser.add_argument("--input", required=True, help="Input text to generate images from")
    parser.add_argument("--output", required=True, help="Path to save the output video")
    parser.add_argument("--num_images", type=int, default=10, help="Number of images to generate (default: 10)")
    parser.add_argument("--fps", type=int, default=24, help="Frames per second for the output video (default: 24)")

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.input, args.output, args.num_images, args.fps)
