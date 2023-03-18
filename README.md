# AI-Video-Generator

AI-Video-Generator is a project that uses AI to generate short videos based on user input. It takes textual input from the user and converts it into a visual representation using a pre-trained generative model. The generated images are then compiled into a video using OpenCV.

## Features

- Convert text input into a series of images using a pre-trained generative model (DALL-E, CLIP, or VQ-VAE).
- Create a video from the generated image sequence.
- (Optional) Web application built with Flask for user interaction.

## Installation

1. Clone the repository:

```
bash
git clone https://github.com/your_username/AI-Video-Generator.git
cd AI-Video-Generator
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate  # For Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the command-line version

To generate a video from text input, run the following command:

```bash
python main.py --input "Your input text here" --output "output.mp4"
```

### Running the web application (optional)

To start the Flask web application, run the following command:

```bash
python app/app.py
```

Then, open your web browser and visit \`http://localhost:5000\` to use the AI-Video-Generator web application.

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes and push them to your fork.
4. Create a pull request describing your changes.

## License

This project is licensed under the [MIT License](LICENSE).


