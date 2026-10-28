# -*- coding: utf-8 -*-
"""
Created on 2025 Sep 07 23:48:54 
@author: ArthurVVVV
"""

#import tkinter.filedialog
from tkinter import filedialog
import os
from datetime import datetime
from PIL import Image
Image.MAX_IMAGE_PIXELS = None   # Disables the DecompressionBomb warning


Prefix="Forge of Empires"

PicAlbum = filedialog.askopenfilenames(filetypes=(("JPG", "*.jpg"),("All Files", "*.*")))

for Pics in PicAlbum:
    FolderPath,PhotoName = os.path.split(Pics)
    if PhotoName.lower().endswith(".jpg"):
        try:
            #Photo Taken Date Time
            exif = Image.open(Pics)._getexif()
            if exif is None:
                PhotoTakenTimeStamp = 999999999999.999
            elif 36867 in exif:
                    PhotoTakenTimeStamp = datetime.timestamp(datetime.strptime(exif[36867],"%Y:%m:%d %H:%M:%S"))
            else:
                PhotoTakenTimeStamp = 999999999999.999
            #Create Date Time
            FileCreatedTimeStamp = os.path.getctime(Pics)
            #Modified Date Time            
            FileModifiedTimeStamp = os.path.getmtime(Pics)
            
            FileTimeStamp = min(PhotoTakenTimeStamp,FileCreatedTimeStamp,FileModifiedTimeStamp)
            
            FileDateTime = datetime.fromtimestamp(FileTimeStamp)            
            new_name_prefix = FileDateTime.strftime("%Y-%m-%d %H-%M-%S")
            new_filename = f"{Prefix} {new_name_prefix}.jpg"
            new_file_path = os.path.join(FolderPath, new_filename)
            # Handle potential filename conflicts 
            counter = 1
            while os.path.exists(new_file_path):
                new_filename = f"{Prefix} {new_name_prefix}_{counter}.jpg"
                new_file_path = os.path.join(FolderPath, new_filename)
                counter += 1
    
            # Rename the file
            os.rename(Pics, new_file_path)
            print(f"Renamed to |{new_filename}| from |{PhotoName}| ")
            
    
        except OSError as e:
            print(f"Error processing '{PhotoName}': {e}")
  