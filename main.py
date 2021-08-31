# 28-08-2021
import cv2          # for image processing
import easygui      # to open the File box
import numpy as np  # to store image
import imageio      # to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

# 29-08-2021

""" fileopenbox opens the box to choose file
and help us store file path as string """
def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)

    # Explanation : code opens the file box, i.e the pop-up box to choose the file from the device,
    # which opens every time you run the code.
    # fileopenbox() is the method in easyGUI module which returns the path of the chosen file as a string.

# 30-08-2021 and 31-08-2021
def cartoonify(ImagePath):
    # read the image
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    #print(image)  # image is stored in form of numbers

    # confirm that image is chosen
    if originalmage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()

    ReSized1 = cv2.resize(originalmage, (960, 540))
    #plt.imshow(ReSized1, cmap='gray')
 """
Imread is a method in cv2 which is used to store images in the form of numbers.
This helps us to perform operations according to our needs.
The image is read as a numpy array, in which cell values depict R, G, and B values of a pixel.
 """