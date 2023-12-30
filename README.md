# Webcam Image Processing Project

This project captures an image from a webcam, applies several filters to it, and then displays the result. The filters applied are an emboss filter, a histogram equalization, and a color inversion.

## Project Structure

The project consists of several functions:

- `initializeWebCam()`: This function initializes the webcam and returns the video device.
- `terminateWebCam(videoDevice)`: This function releases the webcam device.
- `getImage(videoDevice)`: This function captures an image from the webcam and returns it in PIL format.
- `embossFilter(npImage)`: This function applies an emboss filter to an image and returns the result.
- `equalizeFilter(npImage)`: This function equalizes the histogram of an image and returns the result.
- `invertFilter(npImage)`: This function inverts the colors of an image and returns the result.
- `showImage(npImage)`: This function displays an image.

In the main function, these functions are used to capture an image from the webcam, apply the filters, and display the result.

## Running the Project

To run the project, simply execute the script. Make sure that the necessary libraries (OpenCV, matplotlib, and PIL) are installed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license. For more information, please refer to the LICENSE file.

## Contact

For any queries or suggestions, please open an issue on this repository. Happy coding!
