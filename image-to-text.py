import pytesseract as tess
from PIL import Image

img = Image.open("images/test-image-2.jpeg")
text = tess.image_to_string(img)

print(text)

# Process the text
text = text.lower()

def for_permit_holders_only(text):
    print("true")
