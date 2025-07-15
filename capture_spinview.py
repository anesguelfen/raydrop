import cv2
import numpy as np

def capture_and_analyze_image(image_path="droplet.png"):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    diameters = [cv2.minEnclosingCircle(c)[1]*2 for c in contours if len(c) > 5]
    if diameters:
        avg_diameter = np.mean(diameters)
        print(f"Avg droplet diameter (pixels): {avg_diameter:.2f}")
        return avg_diameter
    else:
        print("No droplets detected.")
        return None

if __name__ == "__main__":
    capture_and_analyze_image("sample_image.png")
