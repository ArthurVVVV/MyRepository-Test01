# -*- coding: utf-8 -*-
"""
Created on 2025 Sep 07 23:48:54 
@author: Arthur
"""

#import tkinter.filedialog
from tkinter import filedialog
import os
import datetime

Prefix="Travellers Rest"

VideoList = filedialog.askopenfilenames(filetypes=(("Videos", "*.mp4 *.mov"),("All Files", "*.*")))

for Videos in VideoList:
    FolderPath,VideoName = os.path.split(Videos)
    if VideoName.lower().endswith(tuple([".mp4",".mov"])):
        try:
            #Create Date Time
            FileCreatedTimeStamp = os.path.getctime(Videos)
            #Modified Date Time            
            FileModifiedTimeStamp = os.path.getmtime(Videos)
            
            FileTimeStamp = min(FileCreatedTimeStamp,FileModifiedTimeStamp)
            
            FileDateTime = datetime.datetime.fromtimestamp(FileTimeStamp)            
            new_name_prefix = FileDateTime.strftime("%Y-%m-%d %H-%M-%S")
            new_filename = f"{Prefix} {new_name_prefix}.mp4"
            new_file_path = os.path.join(FolderPath, new_filename)
            # Handle potential filename conflicts 
            counter = 1
            while os.path.exists(new_file_path):
                new_filename = f"{Prefix} {new_name_prefix}_{counter}.mp4"
                new_file_path = os.path.join(FolderPath, new_filename)
                counter += 1
    
            # Rename the file
            os.rename(Videos, new_file_path)
            print(f"Renamed to |{new_filename}| from |{VideoName}|")
            
    
        except OSError as e:
            print(f"Error processing '{VideoName}': {e}")
  