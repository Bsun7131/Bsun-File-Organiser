# Bsun File Organiser

A lightweight desktop file organisation utility built with Python and Tkinter.

Bsun File Organiser helps organise files in a selected folder by automatically sorting them into categories based on their file extensions.

## Features

- Select any folder using a simple desktop interface
- Preview files before organising them
- Automatically categorise files
- Supports images, documents, videos, audio files, archives and 3D model files
- Places unrecognised file types into an Other folder
- Protects against duplicate filenames
- Displays the number of files found in each category
- Confirmation before files are moved
- Simple and lightweight desktop interface

## File Categories

### Images
JPG, JPEG, PNG, GIF, BMP, WEBP, SVG

### Documents
PDF, TXT, DOC, DOCX, XLS, XLSX, PPT, PPTX

### Videos
MP4, MOV, AVI, MKV, WMV

### Audio
MP3, WAV, AAC, FLAC, M4A

### Archives
ZIP, RAR, 7Z, TAR, GZ

### 3D Models
FBX, OBJ, GLB, GLTF, BLEND, STL

Files with extensions that are not recognised are placed in the `Other` folder.

## Built With

- Python
- Tkinter
- pathlib
- shutil

## How It Works

1. Launch Bsun File Organiser.
2. Select a folder.
3. Click **Preview Files** to see how the files will be categorised.
4. Review the results.
5. Click **Organise Files**.
6. Confirm the operation.
7. The files are moved into their corresponding category folders.

## Safety

The application includes a preview feature so users can review file categorisation before moving files.

When a file with the same name already exists in the destination folder, Bsun File Organiser creates a unique filename instead of overwriting the existing file.

It is recommended to test the application with copied or non-critical files before using it with important data.

## Platform

Windows desktop.

The application is written in Python and can also be run directly from the Python source code on compatible systems.

## Developer

**Bisan Subba**

Independent Multi-Platform Software Engineer • Solo Game Developer • 3D Generalist • Archviz & World Creator

## Copyright

Copyright © 2026 Bisan Subba. All rights reserved.
