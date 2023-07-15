# Lynn's Ascii Art Converter

Lynn's Ascii Art Converter is a Python script that converts an image into reasonably high resolution colored ASCII art and generates an HTML file with the output. It provides a fun and creative way to transform images into ASCII representations.

## Installation

1.  Clone the repository to your local machine using the following command:

    shell

-   `git clone https://github.com/your-username/ascii-art-converter.git`

    -   Navigate to the project directory:

    shell

    -   `cd ascii-art-converter`

    -   Create a virtual environment to install the dependencies. You can use either `venv` or `conda`:

    -   Using `venv`:

        shell

        -   `python3 -m venv env
    source env/bin/activate`

    -   Using `conda`:

    shell

    -   -   `conda create --name ascii-converter python=3.9
        conda activate ascii-converter`

        -   Install the required dependencies using `pip`:

    shell

1.  `pip install -r requirements.txt`

    This will install the necessary packages, including `argparse`, `Pillow`, and `numpy`.

## Usage

To convert an image to colored ASCII art and generate the HTML output, follow these steps:

1.  Place your image file in the project directory or provide the relative path to the image file.

2.  Open a terminal or command prompt and navigate to the project directory:

    shell

-   `cd ascii-art-converter`

    -   Run the Python script using the following command:

    shell

`python ascii_converter.py image_path`

Replace `image_path` with the relative path to your image file. For example:

shell

1.  `python ascii_converter.py images/my_image.png`

    This will convert the image to colored ASCII art and generate an HTML file named `output.html` in the project directory.

2.  Open `output.html` in a web browser to view the generated ASCII art.

## Customization

-   **ASCII Characters:** The script uses a predefined set of ASCII characters to represent different levels of pixel intensity. You can modify the `ascii_chars` variable in the `ascii_converter.py` file to use your preferred characters. Ensure that the characters are arranged in ascending order of intensity.

-   **Output Size:** By default, the script resizes the image to a fixed size of 320x160 pixels. If you want a different size for your ASCII art, modify the `resize` function call in the `ascii_converter.py` file.

## License


This project is licensed under the MIT License. Feel free to use and modify it according to your needs.
