# Cartoonify-an-Image
Mini Project for Vth Sem 2021

# Steps to develop Image Cartoonifier

<b>Beginning with image transformations:</b></br>
To convert an image to a cartoon, multiple transformations are done. Firstly, an image is converted to a Grayscale image. Yes, similar to the old day’s pictures.! Then, the Grayscale image is smoothened, and we try to extract the edges in the image. Finally, we form a color image and mask it with edges. This creates a beautiful cartoon image with edges and lightened color of the original image.


## Step1: Importing the required modules
<b> Importing the required modules: </b></br>
1. CV2: Imported to use OpenCV for image processing.</br>
2. easygui: Imported to open a file box. It allows us to select any file from our system.</br>
3. Numpy: Images are stored and processed as numbers. These are taken as arrays. We use NumPy to deal with arrays.</br>
4. Imageio: Used to read the file which is chosen by file box using a path.</br>
5. Matplotlib: This library is used for visualization and plotting. Thus, it is imported to form the plot of images.</br>
6. OS: For OS interaction. Here, to read the path and save images to that path.</br>

## Step 2: Building a File Box to choose a particular file
In this step, we will build the main window of our application, where the buttons, labels, and images will reside. We also give it a title by title() function.</br>

## Step 3: How to store an image?
For a computer, everything is just numbers. Thus, in the below code, we will convert our image into a numpy array.</br>

## Step 4: Transforming an image to grayscale
cvtColor(image, flag) is a method in cv2 which is used to transform an image into the colour-space mentioned as ‘flag’. Here, our first step is to convert the image into grayscale. Thus, we use the BGR2GRAY flag. This returns the image in grayscale.

## Step 5: Smoothening a grayscale image
To smoothen an image, we simply apply a blur effect. This is done using medianBlur() function. 

## Step 6: Retrieving the edges of an image
Cartoon effect has two specialties:

1.	Highlighted Edges
2. Smooth colors

## Step 7: Preparing a Mask Image
We prepare a lightened color image that we mask with edges at the end to produce a cartoon image. We use bilateralFilter which removes the noise. It can be taken as smoothening of an image to an extent.</br>
<b>It’s similar to BEAUTIFY or AI effect in cameras of modern mobile phones.<b>

## Step 8: Giving a Cartoon Effect
Combine the two specialties. This will be done using MASKING. We perform bitwise and on two images to mask them.

## Step 9: Plotting all the transitions together
To plot all the images, we first make a list of all the images. The list here is named “images” and contains all the resized images. Now, we create axes like subl=plots in a plot and display one-one images in each block on the axis using imshow() method.



# Connect With Me
LinkedIn : https://www.linkedin.com/in/akshatjaingeu/<br/>
Email : akshat.kodia@gmail.com<br/>
Twitter : www.twitter.com/akki_aj89<br/>
Website : https://akshatprogrammer.github.io/portfolio/

# Personal
Name : Akshat Jain<br/>
University : Graphic Era University, Dehradun(UK)

If any problem with this program reach me at Telegram<br/>
Here is the link -> https://t.me/akki_aj89

# Gratitude
Thank You, if you like it please leave a Star.
