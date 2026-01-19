import cv2 
import numpy as np
from matplotlib import pyplot as plt
def display_image(image,title="Image"):
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()
def interactive_edge_detection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    display_image(gray_image,"Grayscale Image")
    print("Select an option")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4.Gaussian Edge Detection")
    print("5. Median Edge Detection")
    print("6. Exit")
    while True:
        choice=input("Enter your choice (1-6): ")
        if choice=='1':
            sobel_x=cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=5)
            sobel_y=cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=5)
            sobel_edge=cv2.magnitude(sobel_x,sobel_y)
            display_image(sobel_edge.astype(np.uint8),"Sobel Edge Detection")
        elif choice=='2':
            canny_edge=cv2.Canny(gray_image,100,200)
            display_image(canny_edge,"Canny Edge Detection")
        elif choice=='3':
            laplacian_edge=cv2.Laplacian(gray_image,cv2.CV_64F)
            display_image(np.absolute(laplacian_edge).astype(np.uint8),"Laplacian Edge Detection")
        elif choice=='4':
            gaussian_blurred=cv2.GaussianBlur(gray_image,(5,5),0)
            edges=cv2.Canny(gaussian_blurred,100,200)
            display_image(edges,"Gaussian Edge Detection")
        elif choice=='5':
            median_blurred=cv2.medianBlur(gray_image,5)
            edges=cv2.Canny(median_blurred,100,200)
            display_image(edges,"Median Edge Detection")
        elif choice=='6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
interactive_edge_detection('example.jpg')
