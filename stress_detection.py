import tkinter as tk
from tkinter import messagebox
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def detect_stress():
    text = entry.get()
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)

    if sentiment['compound'] <= -0.2:
        result = "Stress"
    else:
        result = "No Stress"

    result_label.config(text=f"Stress Level: {result}")

# Create the main window
root = tk.Tk()
root.title("Stress Detection")

# Load the background image
background_image = tk.PhotoImage(file=r"C:\Users\thupa\Downloads\Background image.png")


# Create a Canvas to display the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
canvas.pack()

# Create and place a label
label = tk.Label(root, text="Enter a caption:")
label.pack()

# Create and place an entry widget
entry = tk.Entry(root, width=80)
entry.pack()

# Create and place a button
detect_button = tk.Button(root, text="Detect Stress", command=detect_stress)
detect_button.pack()

# Create and place a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
