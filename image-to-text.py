import pytesseract as tess
from PIL import Image
import time



# Main program
def get_text_from_image(path):
    img = Image.open(path)
    text = tess.image_to_string(img)
    text = text.strip()
    text = text.replace('\n', ' ')
    text = text.lower()
    print(text)
    return text


print("\n")
# Testing the function
# path = "images/test-image-1.jpeg"
# text = get_text_from_image(path)
# assert text == "city of westminster pay by phone 02071259090 or text 07860022205 quoting location 8231 4 hours no return within 1 hour", "Comparison failed: Test image 1"

path = "images/test-image-4.jpeg"
text = get_text_from_image(path)

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

# Check wehre the text contains no return within
# return the index of the no return text
def contains_no_return_within(text):
    check = text.find("no return within")
    if(check >= 0):
        return check
    else:
        return False

# Get the time if it contains the return message
def get_no_return_time(text):
    check = contains_no_return_within(text)
    # parse the input
    if(check >= 0):
        # print(check)
        print("Contains 'no return within' message: True")
        check = check + 17
        time = text[check: check+2]
        time = time.strip()
        units = text[check+2: check+8]
        units = units.strip()
        output = time +" " + units
        print("No return within " + output)
        return output
    else:
        print("Contains 'no return within' message: False")
        print("No timer")


# Print time
def get_current_time():
    seconds = time.time()
    time_struct = time.localtime(seconds)
    print(time_struct)
    current_time = time.asctime(time_struct)
    print(current_time)


def set_timer(minutes):
    seconds = 60 * minutes
    while(seconds >0):
        print(seconds)
        time.sleep(1)
        seconds = seconds - 1
        if(seconds == 15):
            print("Alarm: Time to pick up your car!")
    
    
        



get_current_time()
for_resident_permit_holders_only(text)
for_resident_permit_holders(text)
for_permit_holders_only(text)
get_no_return_time(text)

print("\n")