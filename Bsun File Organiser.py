# ============================================================
# Bsun File Organiser
#
# Copyright © 2026 Bisan Subba. All rights reserved.
# Developed by Bisan Subba
# ============================================================

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import shutil
import sys

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / filename

    return Path(__file__).resolve().parent / filename


# ============================================================
# FILE CATEGORIES
# ============================================================

FILE_CATEGORIES = {
    "Images": [
    ".jpg", ".jpeg", ".jfif", ".png", ".gif",
    ".bmp", ".webp", ".svg"
],

    "Documents": [
        ".pdf", ".txt", ".doc", ".docx",
        ".xls", ".xlsx", ".ppt", ".pptx"
    ],

    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv",
        ".wmv"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac", ".flac",
        ".m4a"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz"
    ],

    "3D Models": [
        ".fbx", ".obj", ".glb", ".gltf",
        ".blend", ".stl"
    ]
}


# ============================================================
# SELECTED FOLDER
# ============================================================

selected_folder = None


# ============================================================
# CHOOSE FOLDER
# ============================================================

def choose_folder():
    global selected_folder

    folder = filedialog.askdirectory()

    if folder:
        selected_folder = Path(folder)

        folder_label.config(
            text=str(selected_folder)
        )

        status_label.config(
            text="Folder selected. Click Preview Files."
        )


# ============================================================
# DETERMINE FILE CATEGORY
# ============================================================

def get_category(file):
    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


# ============================================================
# PREVIEW FILES
# ============================================================

def preview_files():
    if selected_folder is None:
        messagebox.showwarning(
            "No Folder",
            "Please choose a folder first."
        )
        return

    preview_box.delete("1.0", tk.END)

    files = [
        file
        for file in selected_folder.iterdir()
        if file.is_file()
    ]

    if not files:
        preview_box.insert(
            tk.END,
            "No files found in this folder."
        )
        return

    category_counts = {}

    for file in files:
        category = get_category(file)

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

        preview_box.insert(
            tk.END,
            f"{file.name}  →  {category}\n"
        )

    preview_box.insert(
        tk.END,
        "\n----------------------------------------\n"
    )

    preview_box.insert(
        tk.END,
        f"Total files: {len(files)}\n\n"
    )

    for category, count in category_counts.items():
        preview_box.insert(
            tk.END,
            f"{category}: {count}\n"
        )

    status_label.config(
        text="Preview complete. No files have been moved."
    )


# ============================================================
# CREATE UNIQUE DESTINATION
# ============================================================

def get_unique_destination(destination):
    if not destination.exists():
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix

    number = 1

    while True:
        new_destination = parent / f"{stem}_{number}{suffix}"

        if not new_destination.exists():
            return new_destination

        number += 1


# ============================================================
# ORGANISE FILES
# ============================================================

def organise_files():
    if selected_folder is None:
        messagebox.showwarning(
            "No Folder",
            "Please choose a folder first."
        )
        return

    files = [
        file
        for file in selected_folder.iterdir()
        if file.is_file()
    ]

    if not files:
        messagebox.showinfo(
            "Nothing to Organise",
            "No files were found in this folder."
        )
        return

    answer = messagebox.askyesno(
        "Organise Files",
        f"Organise {len(files)} files into category folders?"
    )

    if not answer:
        return

    moved_files = 0

    try:
        for file in files:
            category = get_category(file)

            category_folder = selected_folder / category

            category_folder.mkdir(
                exist_ok=True
            )

            destination = category_folder / file.name

            destination = get_unique_destination(
                destination
            )

            shutil.move(
                str(file),
                str(destination)
            )

            moved_files += 1

        preview_box.delete(
            "1.0",
            tk.END
        )

        preview_box.insert(
            tk.END,
            f"Successfully organised {moved_files} files.\n"
        )

        status_label.config(
            text="Organisation complete."
        )

        messagebox.showinfo(
            "Complete",
            f"{moved_files} files were organised successfully."
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"An error occurred:\n{error}"
        )


# ============================================================
# CLEAR PREVIEW
# ============================================================

def clear_preview():
    preview_box.delete(
        "1.0",
        tk.END
    )

    status_label.config(
        text="Preview cleared."
    )


# ============================================================
# CREATE APPLICATION WINDOW
# ============================================================

root = tk.Tk()
root.iconbitmap(str(resource_path("BsunFileOrganiser.ico")))

root.title("Bsun File Organiser")
root.geometry("700x600")
root.minsize(600, 500)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="Bsun File Organiser",
    font=("Arial", 22, "bold")
)

title_label.pack(
    pady=(20, 5)
)

developer_label = tk.Label(
    root,
    text="Developer: Bisan Subba",
    font=("Arial", 14)
)

developer_label.pack(
    pady=(0, 3)
)

subtitle_label = tk.Label(
    root,
    text="Python Desktop Utility"
)

subtitle_label.pack(
    pady=(0, 20)
)


# ============================================================
# FOLDER SELECTION
# ============================================================

choose_button = tk.Button(
    root,
    text="Choose Folder",
    command=choose_folder,
    width=20
)

choose_button.pack(
    pady=5
)

folder_label = tk.Label(
    root,
    text="No folder selected",
    wraplength=600
)

folder_label.pack(
    pady=10
)


# ============================================================
# ACTION BUTTONS
# ============================================================

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)

preview_button = tk.Button(
    button_frame,
    text="Preview Files",
    command=preview_files,
    width=16
)

preview_button.pack(
    side=tk.LEFT,
    padx=5
)

organise_button = tk.Button(
    button_frame,
    text="Organise Files",
    command=organise_files,
    width=16
)

organise_button.pack(
    side=tk.LEFT,
    padx=5
)

clear_button = tk.Button(
    button_frame,
    text="Clear Preview",
    command=clear_preview,
    width=16
)

clear_button.pack(
    side=tk.LEFT,
    padx=5
)


# ============================================================
# PREVIEW AREA
# ============================================================

preview_box = tk.Text(
    root,
    height=18,
    width=75
)

preview_box.pack(
    padx=20,
    pady=15,
    fill=tk.BOTH,
    expand=True
)


# ============================================================
# STATUS
# ============================================================

status_label = tk.Label(
    root,
    text="Choose a folder to begin."
)

status_label.pack(
    pady=(0, 15)
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()