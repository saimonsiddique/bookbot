# BookBot

BookBot is a guided project from boot.dev. This project is designed to analyze the text of a book, count the words, and provide a detailed report on the frequency of each character. It serves as an introductory project to help understand file handling, string manipulation, and basic data processing in Python.

## Features

- Reads the content of a specified book text file.
- Counts the total number of words in the book.
- Counts the frequency of each alphabetical character.
- Generates a detailed report with the findings.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/saimonsiddique/bookbot.git
    ```
2. Navigate to the project directory:
    ```sh
    cd bookbot
    ```

### Usage

1. Place the text file of the book you want to analyze in the `books` directory.
2. Update the `book_path` variable in `main.py` to point to your book file. For example:
    ```python
    book_path = "books/yourbook.txt"
    ```
3. Run the script:
    ```sh
    python main.py
    ```

### Example Output

--- Begin report of books/frankenstein.txt ---

7500 words found in the document

The e character was found 4500 times  
The t character was found 3000 times  
...

--- End report ---

## Project Structure

- `main.py`: The main script that reads the book file, processes the text, and generates the report.
- `books/`: Directory where book text files are stored.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [boot.dev](https://boot.dev) for providing the initial project idea and resources.
