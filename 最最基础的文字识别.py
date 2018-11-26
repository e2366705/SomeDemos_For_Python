from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open('C:\\Users\\QAQ\\Desktop\\1.jpg'), lang='chi_sim')
print(text)



###   识别误差很大

