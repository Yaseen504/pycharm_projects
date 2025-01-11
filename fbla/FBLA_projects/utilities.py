import os
import textwrap

from fbla.classes.font import print_fonts


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Display text unless s is pressed
def display_text_conditionally():
    pass
    #     (text: str, font_type: str =
    #     "default",
    #     color: tuple = (255, 255, 255),

    #     delay: float = 0.0):
    # choice = input("<s?>")
    # if choice != "s":
    #     display_text()


# Function to display text line by line with formatting
def display_text(text, lines_per_chunk, font_type, color, delay):
    clear_terminal()
    text = textwrap.dedent(text).strip()
    """
    Args:
        text (str): The text to display line by line.
        lines_per_chunk (int): Number of lines to display at a time.
        font_type (str): Font style for the text.
        color (tuple): RGB values for text color.
        delay (float): Delay between characters.
    """
    choice = input("<s?>")
    if choice != "s":
        lines = text.splitlines()
        for i in range(0, len(lines), lines_per_chunk):
            chunk = lines[i : i + lines_per_chunk]
            for line in chunk:
                print_fonts(line, font_type=font_type, color=color, delay=delay)
            input("\n\t->\n")
            print("____________________")
    else:
        print("Text skipped")
