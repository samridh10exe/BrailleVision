# BrailleVision
## SBUHacks 2024
Winner at SBUHacks 2024
BrailleVision is a Python-based tool designed to translate braille text from images into readable text. It utilizes image processing and computer vision techniques to detect braille dots, create a grid representing their arrangement, and translate the braille patterns into corresponding characters.

## Features

- **Braille Translation**: Convert braille text from images into readable text.
- **Image Preprocessing**: Enhance image quality through preprocessing techniques such as blurring and sharpening.
- **Braille Dot Detection**: Identify braille dots within images using contour detection methods.
- **Grid Creation**: Generate a grid representation of the arrangement of braille dots for translation.
- **User-friendly Interface**: Simple and intuitive interface for easy usage.

## Requirements

- Python 3.11
- OpenCV library
- Pytorch
- NumPy library

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/samridh10exe/BrailleVision.git
   ```

2. Install the required dependencies:

   ```
   pip install numpy opencv-python imutils scikit-image matplotlib
   ```

## Usage

1. Place the image containing braille text in the project directory.

   Or Put the Url of the image in `url = https://i.imgur.com/example.jpg` in line 294 in Braile/braille_reader.py file.

2. Run the `braille_reader.py` script:

   ```
   python braillevision.py url = '[example](https://i.imgur.com/example).jpg'
   ```

3. Follow the on-screen instructions to view the translated text.


## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.

---

Developed by [Samridh] - [samridh2921(at)gmail.com]
