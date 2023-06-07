import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageGUI:
    def __init__(self, root):
        self.root = root
        self.image_label = None
        self.create_widgets()

    def create_widgets(self):
        # Create a button to upload an image
        upload_button = tk.Button(self.root, text="Upload your image", command=self.upload_image)
        upload_button.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            self.image = ImageTk.PhotoImage(image)

            if self.image_label is None:
                self.image_label = tk.Label(self.root, image=self.image)
                self.image_label.bind("<Button-1>", self.get_coordinates)  # Bind left mouse button click event
                self.image_label.pack()
            else:
                self.image_label.configure(image=self.image)

    def get_coordinates(self, event):
        print(f"Clicked at: ({event.x}, {event.y})")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGUI(root)
    root.mainloop()
