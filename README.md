# --------------------------------------------------------------
# Sobel Edge Detection:
# 1. Calculate Sobel filters along the x and y directions.
# 2. Convert both results to 8-bit images.
# 3. Combine them using bitwise OR.
# 4. Display the combined edge map.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Canny Edge Detection:
# 1. Ask for lower and upper thresholds.
# 2. Apply Canny edge detection, which:
#    - Smooths the image with a Gaussian filter.
#    - Finds intensity gradients.
#    - Applies non-maximum suppression.
#    - Uses double-thresholding and edge tracking.
# 3. Display the detected edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Laplacian Edge Detection:
# 1. Apply the Laplacian operator (second derivative).
# 2. Take the absolute value of the result to handle negative gradients.
# 3. Convert to 8-bit for display.
# 4. Show the resulting edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Gaussian Smoothing:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply GaussianBlur with the specified kernel.
# 3. Display the smoothed image, which helps reduce noise.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Median Filtering:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply medianBlur, which replaces each pixel with the median of neighbors.
# 3. This helps remove salt-and-pepper noise while preserving edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Exit:
# 1. Print a message confirming exit.
# 2. Break out of the interactive loop.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Make a call to the interactive function with the path to an image.
# e.g., interactive_edge_detection("example.jpg")
# This is where the program starts running and awaits user input.
