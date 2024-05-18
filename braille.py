import streamlit as st
from typing import Any
import matplotlib.pyplot as plt
import os
import time

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
        'x': 0x282d, 'y': 0x283d, 'z': 0x2835, '0': 0x2800,
        '1': 0x2801, '2': 0x2803, '3': 0x2809, '4': 0x2819,
        '5': 0x2811, '6': 0x280b, '7': 0x281b, '8': 0x2813,
        '9': 0x280a, '.': 0x2802, ',': 0x2806, '?': 0x2816,
        '!': 0x2812, "'": 0x2804, '-': 0x2814, '(': 0x280c,
        ')': 0x281c, '/': 0x2818, '&': 0x2808, ':': 0x2810,
        ';': 0x2828, ' ': 0x2800
    }

    return chr(braille.get(text, 0x2800))

def render_unicode_as_braille(unicode_char, character, output_dir="output_images"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a new figure
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.text(0.5, 0.5, f"{character}", fontsize=20, ha='center', va='center', color='black')
    ax.text(0.5, 0.3, unicode_char, fontsize=20, ha='center', va='center', color='blue')
    
    # Remove axes
    ax.axis('off')

    # Save the figure as an image
    output_path = os.path.join(output_dir, f"{[ord(char) for char in unicode_char]}.png")
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)
    print(f"Saved {unicode_char} with formula '{character}' to {output_path}")
    st.image(output_path)


st.title(":heart: _Project_ :blue[JALI!]", anchor="center")
st.write("Braille-Text Feature")

#  We can use the braille function to convert text to Braille.
# The function returns a string of Braille characters, which we can display
text = st.text_input("Enter some text to convert to Braille:")

if text != "":
    
    braille_text = "".join(braille(c) for c in text.lower())
    st.write("---")
    st.write("Text,", text)
    st.write("Braille unicode,", braille_text)
    st.write("---")

    # image rendering
    st.write("Image rendering of the Braille text")
    
    char = text
    render_unicode_as_braille(braille_text, char)

    # divider
    st.write("---")

braille_text = "".join(braille(c) for c in text.lower())
# Render the Braille text with the corresponding formula
for unicode, b in zip(braille_text, text):
    render_unicode_as_braille(unicode, b.lower() if b.isupper() else b)


# Sidebar
st.sidebar.title("Braille-Text Feature")
st.sidebar.write("Project Jali seeks to make accessibility to technology and information easier for all individuals regardless of the language barrier or whether tagged with disability, the Braille-Text feature is one of the many features that will be available on the platform. The Braille-Text feature converts text to Braille using Unicode characters.")
st.sidebar.write("")
st.sidebar.write("The Braille-Text feature is a great tool for students, teachers, and anyone who wants to learn Braille. It is easy to use and can be accessed from any device with an internet connection")

# Example usage
text = time.strftime("%c")
braille_text = "".join(braille(c) for c in text.lower())

st.sidebar.subheader("Example Usage")   
st.sidebar.write(text)
st.sidebar.write(braille_text)

st.sidebar.write("---")

st.sidebar.subheader("How to use the Braille-Text Feature")
st.sidebar.write("1. Enter some text in the text box below.")
st.sidebar.write("2. The text will be converted to Braille.")

# credit
st.sidebar.write("---")
st.sidebar.write("This project is developed by [pkwollfe :heart:](https://x.com/Pkwolffe)")
st.sidebar.write("[Contributors are welcome!](https://github.com/PROJECT-JALI)")
st.sidebar.write("Powered by [Streamlit](https://streamlit.io/)")

