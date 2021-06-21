import pytesseract as tess
from PIL import Image

img = Image.open("images/test-image-1.jpeg")
text = tess.image_to_string(img)
text = text.strip()
text = text.replace('\n', ' ')
text = text.lower()
print(text)

print("\n")

# Checks if it is for resident permit holders only
# Means it is for permit holders at all times
def for_resident_permit_holders_only(text):
    check = text.find("resident permit holders only")
    if(check >0):
        print("For resident permit holders only: True")
        return True
    else:
        print("For resident permit holders only: False")
        return False

# Checks if it is for resident permit holders only
# Means it is for permit holders at all times
def for_resident_permit_holders(text):
    check = text.find("resident permit holders")
    if(check >0):
        print("For resident permit holders: True")
        return True
    else:
        print("For resident permit holders: False")
        return False


# Checks if it is for resident permit holders only
# Means it is for permit holders at all times
def for_permit_holders_only(text):
    check = text.find("permit holders only")
    if(check > 0):
        print("For permit holders only: True")
        return True
    else:
        print("For permit holders only: False")
        return False

def contains_no_return_within(text):
    check = text.find("no return within")
    if(check >= 0):
        return check
    else:
        return False


def get_no_return_time(text):
    check = contains_no_return_within(text)
    # Get no return time if it contains the return message
    if(check >= 0):
        print("Contains 'no return within' message: True")
        check = check + 17
        time = text[check: check+1]
        time = time.strip()
        units = text[check+1: check+6]
        units = units.strip()
        output = time +" " + units
        print("No return within " + output)
        return output


        print("Timer started")

    else:
        print("Contains 'no return within' message: False")
        print("No timer")





for_resident_permit_holders_only(text)
for_resident_permit_holders(text)
for_permit_holders_only(text)
get_no_return_time(text)

print("\n")