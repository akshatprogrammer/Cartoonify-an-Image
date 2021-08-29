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