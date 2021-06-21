import pytesseract
import cv2


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text


# read the image
img = cv2.imread('test-image.jpeg')

# get the grayscale version of the image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# remove moise from image
def remove_noise(image):
    return cv2.medianBlur(image, 5)

# thresholding

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
