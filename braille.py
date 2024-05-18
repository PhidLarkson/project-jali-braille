import streamlit as st
from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import os

def braille(text: str) -> Any:
    """
    Convert text to Braille using Unicode characters.
    """
    # Braille characters are 2x3 grids of dots, which we represent as
    # a 6-character string. Each character in the string is either a
    # space or a dot, and we use the ord() function to convert the
    # string to a number.
    braille = {
        ' ': 0x2800, 'a': 0x2801, 'b': 0x2803, 'c': 0x2809,
        'd': 0x2819, 'e': 0x2811, 'f': 0x280b, 'g': 0x281b,
        'h': 0x2813, 'i': 0x280a, 'j': 0x281a, 'k': 0x2805,
        'l': 0x2807, 'm': 0x280d, 'n': 0x281d, 'o': 0x2815,
        'p': 0x280f, 'q': 0x281f, 'r': 0x2817, 's': 0x280e,
        't': 0x281e, 'u': 0x2825, 'v': 0x2827, 'w': 0x283a,
        'x': 0x282d, 'y': 0x283d, 'z': 0x2835
    }
    return chr(braille.get(text, 0x2800))


# We can use the braille function to convert text to Braille.
# The function returns a string of Braille characters, which we can display
# using st.write.   

text = st.text_input("Enter some text")
if text == "":
    st.write("Enter some text")

braille_text = "".join(braille(c) for c in text.lower())
st.write(braille_text)


def render_unicode_with_formula(unicode_char, character, output_dir="output_images"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a new figure
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.text(0.5, 0.5, f"{character}", fontsize=20, ha='center', va='center', color='black')
    ax.text(0.5, 0.3, unicode_char, fontsize=20, ha='center', va='center', color='blue')
    
    # Remove axes
    ax.axis('off')

    # Save the figure as an image
    output_path = os.path.join(output_dir, f"{ord(unicode_char)}.png")
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)
    print(f"Saved {unicode_char} with formula '{character}' to {output_path}")
    st.image(output_path)

# Example usage
unicode_char = '_'  # Alpha symbol
char = text
render_unicode_with_formula(unicode_char, char)

# Render the Braille text with the corresponding formula
for unicode, b in zip(braille_text, text):
    render_unicode_with_formula(unicode, b.lower() if b.isupper() else b)
