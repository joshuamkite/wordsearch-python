# Wordsearch Python

## Overview

This Python project generates a customizable word search puzzle using words from the WordNet lexical database. The resulting word search is output as a PDF file, making it easy to print and enjoy. The word search puzzle can be tailored in terms of grid size, the number of words, and the title displayed at the top of the PDF. Some example output is included.

- [Wordsearch Python](#wordsearch-python)
  - [Overview](#overview)
    - [Inspiration](#inspiration)
  - [Technical Decisions](#technical-decisions)
    - [Word List Source](#word-list-source)
    - [Grid and Layout](#grid-and-layout)
    - [PDF Output](#pdf-output)
  - [Installation and Setup](#installation-and-setup)
    - [Prerequisites](#prerequisites)
    - [Required Python Packages](#required-python-packages)
    - [Installing Dependencies](#installing-dependencies)
    - [Download WordNet Data](#download-wordnet-data)
  - [How to Run](#how-to-run)
    - [On Windows](#on-windows)
    - [On Mac](#on-mac)
    - [On Linux](#on-linux)
  - [Customization Options](#customization-options)
    - [Title](#title)
    - [Grid Size and Word Count](#grid-size-and-word-count)
    - [Output Directory](#output-directory)
    - [Cell Size](#cell-size)
      - [Practical Example:](#practical-example)
    - [Word Length Filtering](#word-length-filtering)
  - [Acknowledgements](#acknowledgements)


### Inspiration

This project was inspired by [a request on the PythonLearning subreddit](https://old.reddit.com/r/PythonLearning/comments/1es3wfj/python_coding_help/) by the user Mysterious_Lab5934.

## Technical Decisions

### Word List Source

- **WordNet via NLTK**: The word list is sourced from WordNet, a large lexical database of English, provided by the Natural Language Toolkit (NLTK). WordNet was chosen for its extensive coverage of English words, allowing for a rich and varied word search experience. Phrases (words containing underscores) and hyphenated words are automatically excluded to ensure only single, unhyphenated words are used.
- **Word filtering**: We attempt to filter out words that are considered offensive but cannot guarantee that this will be effective or correct in all cases.

### Grid and Layout

- **Grid Size**: The default grid size is set to 25x25, providing a challenging and engaging puzzle size.
- **Word Placement**: Words can be placed in any direction: horizontally, vertically, or diagonally, in both forward and backward orientations, ensuring a high level of difficulty.
- **Word List Display**: The word list is displayed in three columns at the bottom of the PDF, with a smaller font size to fit neatly within the available space.

### PDF Output

- **Dynamic Filename**: The output PDF file is named with a timestamp (`wordsearch_YYYYMMDD_HHMMSS.pdf`) to avoid overwriting previous files.
- **Output Directory**: By default, PDFs are saved to a `wordsearch` directory. This directory can be customized by modifying the `output_dir` variable in the script.
- **Title Customization**: The title of the word search puzzle can be customized by modifying a variable in the script.
- **Cell Size**: The size of each cell in the word search grid can be automatically calculated to fit the grid width within the page. Alternatively, it can be set manually by adjusting the `cell_size` variable in the script.

## Installation and Setup

### Prerequisites

- **Python 3.6 or greater**: Ensure you have Python installed on your system.
- **pip**: Python's package installer, typically included with Python.

### Required Python Packages

This project uses the following Python packages:
- `nltk`: For accessing the WordNet word list.
- `reportlab`: For generating the PDF output.
- `better_profanity`: For screening out offensive words

### Installing Dependencies

All the necessary packages are listed in the `requirements.txt` file. To install them, use the following command:

```bash
pip install -r requirements.txt
```

This will install the packages required to run the script successfully.

### Download WordNet Data

The first time you run the script, it will download the WordNet data if it is not already present. This data will be cached locally for subsequent runs.

## How to Run

### On Windows

1. Open the Command Prompt.
2. Navigate to the directory containing the script using the `cd` command.
3. Run the script with Python:

    ```bash
    python main.py
    ```

### On Mac

1. Open Terminal.
2. Navigate to the directory containing the script using the `cd` command.
3. Run the script with Python:

    ```bash
    python3 main.py
    ```

### On Linux

1. Open Terminal.
2. Navigate to the directory containing the script using the `cd` command.
3. Run the script with Python:

    ```bash
    python3 main.py
    ```

## Customization Options

### Title

To change the title of the word search, modify the `title` variable in the script:

```python
title = "Your Custom Title"
```

### Grid Size and Word Count

You can adjust the grid size and the number of words by changing the following variables:

```python
default_grid_size = 25  # Change this to your preferred grid size
default_num_words = 20  # Change this to set how many words are in the puzzle
```

### Output Directory

The PDF files are saved by default in a `wordsearch` directory. To change this directory, modify the `output_dir` variable:

```python
output_dir = "your_custom_directory"
```

### Cell Size

The `cell_size` variable in the script controls the size of each individual cell in the word search grid when it is rendered on the PDF. Specifically, it determines:

1. **Letter Spacing**: The amount of space (in points) that each letter occupies on the grid. A larger `cell_size` will space the letters farther apart, while a smaller `cell_size` will place them closer together. This affects both the readability of the letters and how much of the page the grid will fill.

2. **Grid Dimensions on the Page**: The overall physical dimensions of the grid on the page. If you increase the `cell_size`, the grid will take up more space on the page, and if you decrease it, the grid will be more compact. For example, a large `cell_size` might be useful if you want to create a word search with large, easily readable letters.

3. **Automatic Calculation**: If the `cell_size` is set to `None` (which is the default), the script will automatically calculate an appropriate `cell_size` that allows the entire grid to fit neatly within the available width of the A5 page. This ensures that the grid is fully displayed, regardless of the number of rows or columns.

4. **Manual Adjustment**: You can manually set the `cell_size` if you want to control exactly how large or small the cells should be. For example:
    ```python
    cell_size = 12  # Sets each cell to be 12 points wide and high
    ```

#### Practical Example:

- **Small `cell_size` (e.g., 8 points)**:
  - The letters will be placed close together.
  - The grid will appear more compact on the page.
  - This is useful if you want to fit a larger grid on a small page.

- **Large `cell_size` (e.g., 15 points)**:
  - The letters will be spaced further apart.
  - The grid will occupy more space on the page.
  - This might be necessary if you're creating a word search for younger children or for someone who might prefer larger text.

By adjusting the `cell_size`, you can control the appearance and layout of the word search grid to best suit your needs.

### Word Length Filtering

By default, the script filters words to include only those with a minimum length of 4 characters, excluding phrases and hyphenated words. You can adjust this filter in the script:

```python
filtered_words = [word for word in sorted(list(words_set)) if len(word) >= 4 and "_" not in word and "-" not in word]
```

## Acknowledgements

Special thanks to the user `Mysterious_Lab5934` for their inquiry and the PythonLearning subreddit for providing a platform for learning and collaboration.
