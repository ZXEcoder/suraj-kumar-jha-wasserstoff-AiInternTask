import cv2
import pytesseract

def preprocess_image_for_ocr(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to load.")
    return image

def extract_text_from_object(image_path):
    #use below command only if you have linux machine or else use windows command else if you want to deploy in huggingface don't use it
    #pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    preprocessed_image = preprocess_image_for_ocr(image_path)
    text = pytesseract.image_to_string(preprocessed_image)
    return text
def extract_image_as_whole(image_path):
    #pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    image = cv2.imread(image_path)
    txt= pytesseract.image_to_string(image)
    return txt
