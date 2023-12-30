# Import necessary libraries
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageOps

# Function to initialize the webcam
def initializeWebCam():
    videoDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Open the webcam device using OpenCV
    return videoDevice

# Function to terminate the webcam
def terminateWebCam(videoDevice):
    videoDevice.release() # Release the webcam device

# Function to capture an image from the webcam
def getImage(videoDevice):
    return_code, cvImage = videoDevice.read() # Read an image from the webcam
    if return_code==False: # If reading the image failed, exit the program
        exit(-1)
    return Image.fromarray(cvImage) # Convert the image from OpenCV format to PIL format and return it

# Function to apply an emboss filter to an image
def embossFilter(npImage):
    npImageGray = ImageOps.grayscale(npImage) # Convert the image to grayscale
    npImage_emboss = npImageGray.filter(ImageFilter.EMBOSS) # Apply the emboss filter
    return npImage_emboss # Return the filtered image

# Function to equalize the histogram of an image
def equalizeFilter(npImage):
    return ImageOps.equalize(npImage) # Equalize the image histogram and return the result

# Function to invert the colors of an image
def invertFilter(npImage):
    return ImageOps.invert(npImage) # Invert the image colors and return the result

# Function to display an image
def showImage(npImage):
    plt.imshow(npImage, cmap='gray') # Display the image in grayscale
    plt.show() # Show the plot

# Main function
if __name__ == '__main__':
    webcam = initializeWebCam() # Initialize the webcam
    videoFrame = getImage(webcam) # Capture an image from the webcam
    videoFrame = embossFilter(videoFrame) # Apply the emboss filter to the image
    videoFrame = equalizeFilter(videoFrame) # Equalize the image histogram
    videoFrame = invertFilter(videoFrame) # Invert the image colors
    showImage(videoFrame) # Display the image
    terminateWebCam(webcam) # Terminate the webcam
