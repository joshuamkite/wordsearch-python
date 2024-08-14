import os
import random
import string
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
import nltk
from nltk.corpus import wordnet
from datetime import datetime

# Download WordNet data if not already downloaded
try:
    wordnet.ensure_loaded()  # Ensures that WordNet data is loaded
except LookupError:
    nltk.download('wordnet', quiet=True)  # Download WordNet data if not already present

# Function to generate a word search puzzle


def generate_word_search(words, grid_size=25):  # Default grid size to 25x25
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]

    def place_word(word):
        word_len = len(word)
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            direction = random.choice(directions)
            start_row = random.randint(0, grid_size - 1)
            start_col = random.randint(0, grid_size - 1)
            end_row = start_row + direction[0] * word_len
            end_col = start_col + direction[1] * word_len

            if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
                can_place = True
                for i in range(word_len):
                    r = start_row + i * direction[0]
                    c = start_col + i * direction[1]
                    if grid[r][c] not in (' ', word[i]):
                        can_place = False
                        break

                if can_place:
                    for i in range(word_len):
                        r = start_row + i * direction[0]
                        c = start_col + i * direction[1]
                        grid[r][c] = word[i]
                    placed = True
            attempts += 1

    for word in words:
        place_word(word.upper())

    # Fill remaining empty spaces with random letters
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == ' ':
                grid[r][c] = random.choice(string.ascii_uppercase)

    return grid

# Function to create the PDF


def create_pdf(grid, words, title, output_dir="wordsearch", cell_size=None):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Dynamically calculate cell size based on grid size and A5 page width
    page_width, page_height = A5
    grid_size = len(grid)
    margin = 30  # Margin from the sides

    if cell_size is None:
        cell_size = (page_width - 2 * margin) / grid_size  # Calculate cell size to fit the grid width

    # Append date and time to filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_dir, f"wordsearch_{timestamp}.pdf")

    c = canvas.Canvas(output_filename, pagesize=A5)
    c.setFont("Helvetica", 10)

    # Title
    c.drawCentredString(page_width / 2, page_height - 40, title)

    # Draw the grid
    start_x = margin
    start_y = page_height - 70  # Adjusted starting Y to fit title

    for row in range(grid_size):
        for col in range(grid_size):
            c.drawString(start_x + col * cell_size, start_y - row * cell_size, grid[row][col])

    # Draw the word list
    c.setFont("Helvetica", 8)  # Smaller font size for the word list
    columns = 3  # Number of columns for the word list
    words_per_column = (len(words) + columns - 1) // columns  # Words per column
    column_width = (page_width - 2 * margin) / columns  # Width of each column

    for i, word in enumerate(words):
        col = i // words_per_column
        row = i % words_per_column
        x_position = margin + col * column_width
        y_position = start_y - grid_size * cell_size - 20 - row * 12  # Adjust Y position

        c.drawString(x_position, y_position, word.upper())

    c.showPage()
    c.save()


# Example usage
if __name__ == "__main__":
    # Set default options
    title = "Mysterious_Lab5934 Word Search"  # Customizable title
    default_grid_size = 25
    default_num_words = 20
    output_dir = "wordsearch"  # Default output directory
    cell_size = None  # Automatically calculate cell size

    # Get words from WordNet and filter out phrases (no underscores or hyphens)
    words_set = set(wordnet.words())
    filtered_words = [word for word in sorted(list(words_set)) if len(word) >= 4 and "_" not in word and "-" not in word]
    words_to_find = random.sample(filtered_words, default_num_words)

    # Generate grid
    grid = generate_word_search(words_to_find, grid_size=default_grid_size)

    # Generate PDF with custom title and directory
    create_pdf(grid, words_to_find, title, output_dir=output_dir, cell_size=cell_size)
