import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from textwrap import wrap
from braille_reader import *

# Function to handle file selection and processing
def process_file():
    # Prompt user to select a file
    file_path = filedialog.askopenfilename(initialdir="C:/Users/fsamridh/Desktop", title="Select a file")

    if file_path:
        # Process the selected file
        image, ctrs, paper, gray, edged, thresh = get_image(file_path, iter=0, width=1500)
        diam = get_diameter()
        dotCtrs = get_circles()
        questionCtrs, boundingBoxes, xs, ys = sort_contours(dotCtrs)
        draw_contours(questionCtrs)
        linesV, d1, d2, d3, spacingX, spacingY = get_spacing()
        letters = get_letters()
        ans = translate(letters)

        # Display the processed image and converted text
        display_image(image)
        display_text(ans)

# Function to display the processed image
def display_image(image):
    image = ImageTk.PhotoImage(Image.fromarray(image))
    image_label.config(image=image)
    image_label.image = image

# Function to display the converted text
def display_text(text):
    text_output.config(state=tk.NORMAL)
    text_output.delete('1.0', tk.END)
    for line in wrap(text, width=80):
        text_output.insert(tk.END, line + '\n')
    text_output.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Braille Reader")

# Create buttons
process_button = tk.Button(root, text="Select File", command=process_file)
process_button.pack(pady=10)

# Create label for displaying image
image_label = tk.Label(root)
image_label.pack()

# Create text output widget
text_output = tk.Text(root, height=10, width=80)
text_output.pack(pady=10)
text_output.config(state=tk.DISABLED)

# Run the GUI main loop
root.mainloop()
