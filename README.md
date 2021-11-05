# Cartoonify-an-Image

<p align="center">
    <img src="https://repository-images.githubusercontent.com/400706498/2b71af19-fc0c-4041-80f6-ad9640b645d8" width="700">
</p>


# Steps to develop Image Cartoonifier

<b>Beginning with image transformations:</b>

<p align="center">
<img src="https://www.cronj.com/blog/wp-content/uploads/Geometric-Transformation-of-images.png" width="480">
</p>

To convert an image to a cartoon, multiple transformations are done. Firstly, an image is converted to a Grayscale image. Yes, similar to the old day’s pictures.! Then, the Grayscale image is smoothened, and we try to extract the edges in the image. Finally, we form a color image and mask it with edges. This creates a beautiful cartoon image with edges and lightened color of the original image.


## Step1: Importing the required modules
<b> Importing the required modules: </b>

<p align="center">
<img src="https://www.telematika.org/images/slide/scipy_hu8f53708275f345343ccb3a7bdf88cdc6_78431_900x500_fit_q75_box.jpg" width="480">
</p>



1. <b>CV2</b> : Imported to use OpenCV for image processing.</br>
2. <b>easygui</b> : Imported to open a file box. It allows us to select any file from our system.</br>
3. <b>Numpy</b> : Images are stored and processed as numbers. These are taken as arrays. We use NumPy to deal with arrays.</br>
4. <b>Imageio</b> : Used to read the file which is chosen by file box using a path.</br>
5. <b>Matplotlib</b> : This library is used for visualization and plotting. Thus, it is imported to form the plot of images.</br>
6. <b>OS</b> : For OS interaction. Here, to read the path and save images to that path.</br>

## Step 2: Building a File Box to choose a particular file

```diff
- In this step, we will build the main window of our application,
- where the buttons, labels, and images will reside. We also give it a title by title() function.
```

## Step 3: How to store an image?


```diff
! For a computer, everything is just numbers. Thus, in the below code, we will convert our image into a numpy array.
```

## Step 4: Transforming an image to grayscale
<b> Importing the required modules: </b>

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Beyoglu_4671_tricolor.png" width="480">
</p>

cvtColor(image, flag) is a method in cv2 which is used to transform an image into the colour-space mentioned as ‘flag’. Here, our first step is to convert the image into grayscale. Thus, we use the BGR2GRAY flag. This returns the image in grayscale.

## Step 5: Smoothening a grayscale image
``` diff
+ To smoothen an image, we simply apply a blur effect. This is done using medianBlur() function.
```
## Step 6: Retrieving the edges of an image
Cartoon effect has two specialties:
``` diff
! 1.	Highlighted Edges
! 2. Smooth color 
```

## Step 7: Preparing a Mask Image

<p align="center">
<img src="https://forum.processing.org/two/uploads/imageupload/590/6BNAEVJJF8PB.jpg" width="480">
</p>

We prepare a lightened color image that we mask with edges at the end to produce a cartoon image. We use bilateralFilter which removes the noise. It can be taken as smoothening of an image to an extent.

<b>It’s similar to BEAUTIFY or AI effect in cameras of modern mobile phones.<b>

## Step 8: Giving a Cartoon Effect
 
<p align="center">
<img src="https://www.psfreebies.com/wp-content/uploads/2020/02/Cartoon-effect.jpg" width="300">
</p>
 
Combine the two specialties. This will be done using MASKING. We perform bitwise and on two images to mask them.

## Step 9: Plotting all the transitions together
 <p align="center">
<img src="https://matplotlib.org/stable/_static/logo2_compressed.svg" width="300">
</p>
 
To plot all the images, we first make a list of all the images. The list here is named “images” and contains all the resized images. Now, we create axes like subl=plots in a plot and display one-one images in each block on the axis using imshow() method.

## Step 10: Functionally of save button
 
imwrite() method of cv2 is used to save the file at the path mentioned. 
cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR) is used to assure that no color get extracted or highlighted while we save our image.

## Step 11: Making the main window
 
Using Tkinter Module, created the main window.

## Step 12: Making the Cartoonify button in the main window
 
Using the <b>button<b> function.

# Summary
Yes, now we have a reason to tease our sibling by saying “You look like a cartoon”. Just cartoonify his/ her image, and show it!

We have successfully developed Image Cartoonifier with OpenCV in Python. This is the magic of openCV which let us do miracles.
 

# Connect With Me
<img src ="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-linkedin-3.png" width="50"> : [https://www.linkedin.com/in/akshatjaingeu/](https://www.linkedin.com/in/akshatjaingeu/)<br/>
<img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Logo_Gmail_%282015-2020%29.svg/2560px-Logo_Gmail_%282015-2020%29.svg.png" width="50"> : [akshat.kodia@gmail.com ](akshat.kodia@gmail.com)<br/>
<img src ="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-twitter-1.png" width="50"> : [www.twitter.com/akki_aj89](www.twitter.com/akki_aj89)<br/>
<img src ="https://toppng.com/uploads/preview/file-svg-world-wide-web-website-logo-11563356036uvwy5cvxhx.png" width="50"> : [https://akshatprogrammer.github.io/portfolio/](https://akshatprogrammer.github.io/portfolio/)

# Personal
<img
  align="right"
  width="275x"
  src="https://miro.medium.com/max/1400/1*0FqDC0_r1f5xFz3IywLYRA.jpeg"
/>
- 💬 Name : Akshat Jain
- 🏫 University : Graphic Era University, Dehradun(UK)
- 4️⃣Roll Number : 1918006
- 🇩4️⃣ Section : D4
- ✨Batch : 2023

     

    
If any problem with this program reach me at Telegram<br/>
<img src="https://e7.pngegg.com/pngimages/772/115/png-clipart-computer-icons-telegram-logo-angle-white.png" width="70"> -> [Telegram](https://t.me/akki_aj89)

# Gratitude
Thank You, if you like it please leave a Star.
