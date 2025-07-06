import os
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
from datetime import datetime
from image_classifier import classify_image  # <-- Your model's function


class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, bg="#1e1e2f", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#1e1e2f")

        self.scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Mouse scroll support
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))
        canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux
        canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux


class ImageClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Image Classifier using CNN")
        self.root.geometry("1000x850")
        self.root.configure(bg="#1e1e2f")

        self.history = []
        self.image_cards = []

        self.FONT_TITLE = ("Helvetica", 22, "bold")
        self.FONT_BODY = ("Consolas", 13)
        self.FONT_BTN = ("Helvetica", 12, "bold")

        tk.Label(self.root, text="🔥 Image Classifier using CNN",
                 font=self.FONT_TITLE, bg="#1e1e2f", fg="#ffffff").pack(pady=20)

        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="📄 Upload Image", command=self.open_image,
                  font=self.FONT_BTN, bg="#ff9800", fg="black", padx=10, pady=5).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="📁 Classify Folder", command=self.classify_folder,
                  font=self.FONT_BTN, bg="#03a9f4", fg="white", padx=10, pady=5).pack(side=tk.LEFT)

        tk.Button(btn_frame, text="🗑 Clear Display", command=self.clear_display,
                  font=self.FONT_BTN, bg="#e91e63", fg="white", padx=10, pady=5).pack(side=tk.LEFT)

        tk.Button(btn_frame, text="🔄 Reset All", command=self.reset_all,
                  font=self.FONT_BTN, bg="#9c27b0", fg="white", padx=10, pady=5).pack(side=tk.LEFT)

        self.folder_output = tk.Text(self.root, height=4, width=85, bg="#2e2e3e",
                                     fg="#ffffff", font=self.FONT_BODY)
        self.folder_output.pack(pady=10)

        tk.Label(self.root, text="📜 Classification History", font=("Arial", 12, "bold"),
                 bg="#1e1e2f", fg="#ffffff").pack()

        self.history_box = tk.Listbox(self.root, height=4, width=80, bg="#2e2e3e", fg="#ffffff")
        self.history_box.pack(pady=5)

        self.scroll_frame = ScrollableFrame(self.root)
        self.scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Button(self.root, text="💾 Save Results", command=self.save_results,
                  font=self.FONT_BTN, bg="#4caf50", fg="white").pack(pady=10)

        tk.Label(self.root, text="By K.V.M Sri Charan", font=("Arial", 10),
                 bg="#1e1e2f", fg="#888").pack(side=tk.BOTTOM, pady=10)

        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.drop_image)

        # Keyboard Shortcuts
        self.root.bind("<Control-o>", lambda e: self.open_image())
        self.root.bind("<Control-s>", lambda e: self.save_results())
        self.root.bind("<Control-Shift-F>", lambda e: self.classify_folder())

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.display_image_with_prediction(file_path)

    def drop_image(self, event):
        try:
            file_path = self.root.tk.splitlist(event.data)[0]
            self.display_image_with_prediction(file_path)
        except Exception as e:
            messagebox.showerror("Drag & Drop Error", str(e))

    def classify_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            images = [os.path.join(folder_path, f)
                      for f in os.listdir(folder_path)
                      if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))]
            self.folder_output.delete(1.0, tk.END)
            self.folder_output.insert(tk.END, f"\n📁 Folder: {folder_path}\n")
            if images:
                for img_path in images:
                    self.display_image_with_prediction(img_path)
            else:
                messagebox.showinfo("No Images", "No image files found in the selected folder.")

    def display_image_with_prediction(self, file_path):
        img = Image.open(file_path)
        img = ImageOps.exif_transpose(img)
        img.thumbnail((180, 180))
        tk_img = ImageTk.PhotoImage(img)

        results = classify_image(file_path)
        timestamp = datetime.now().strftime("[%H:%M:%S]")  # 24-hour format
        summary = f"{timestamp} {os.path.basename(file_path)} → {results[0][0]} ({results[0][1]*100:.2f}%)"

        self.history.append(summary)
        self.history_box.insert(tk.END, summary)

        card = tk.Frame(self.scroll_frame.scrollable_frame, bg="#2e2e3e", bd=2, relief="groove", padx=10, pady=10)
        card.pack(pady=10, anchor="center", padx=10, fill="x")

        img_label = tk.Label(card, image=tk_img, bg="#2e2e3e")
        img_label.image = tk_img
        img_label.grid(row=0, column=0, rowspan=2, padx=10)

        file_label = tk.Label(card, text=os.path.basename(file_path),
                              font=("Consolas", 11, "bold"), fg="white",
                              bg="#2e2e3e", wraplength=300, justify="left")
        file_label.grid(row=0, column=1, sticky="w")

        pred_text = ""
        for i, (label, prob) in enumerate(results[:3], start=1):
            pred_text += f"{i}. {label:<15} — {prob*100:.2f}%\n"

        pred_label = tk.Label(card, text=pred_text, justify="left", anchor="w",
                              font=("Consolas", 10), fg="#ffcc00", bg="#2e2e3e", width=30)
        pred_label.grid(row=1, column=1, sticky="w")

        self.image_cards.append(card)

    def clear_display(self):
        for card in self.image_cards:
            card.destroy()
        self.image_cards.clear()

    def reset_all(self):
        self.clear_display()
        self.history.clear()
        self.history_box.delete(0, tk.END)
        self.folder_output.delete(1.0, tk.END)

    def save_results(self):
        if not self.history:
            messagebox.showinfo("Nothing to Save", "No classifications to save.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            with open(file_path, "w") as f:
                for line in self.history:
                    f.write(line + "\n")
            messagebox.showinfo("Saved", f"Results saved to:\n{file_path}")


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = ImageClassifierApp(root)
    root.mainloop()
