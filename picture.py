import pytesseract
from PIL import Image
import PATH
import re
pytesseract.pytesseract.tesseract_cmd = PATH.TESSERACT_EXE

class Picture:
#gets img and returns number of lines and text
    def __init__(self, picture):
        self.picture = picture

    def process(self):
        basic_process = pytesseract.image_to_string(picture)
        return basic_process

    def count_lines(self,basic_process):
        num_lines = basic_process.count('\n')+1
        return num_lines


class Date:
    #takes text and returns the date or 0 if there is no date in it
    def __init__(self,image_text):
        self.image_text = image_text
    def get_simple_date_no_year(self):
        date = re.findall('(\d{1,4}([.\-/])\d{1,2})',self.image_text)
        return date
    def get_simple_date_with_year(self):
        date = re.search('(\d{1,4}([.\-/])\d{1,2}([.\-/])\d{1,4})', self.image_text)
        return date




picture =Image.open('img_test/simple_text_line_drop.jpg')
img = Picture(picture)
text = img.process()
date = Date(text)
print(date.get_simple_date_with_year())


