from PIL import Image
import pytesseract
import numpy as np
import cv2
# from Dictionary import spell_check
import io

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 3)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)[1]
    # return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)

    else:
        angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


# filename = '3.png'
# img = np.array(Image.open(filename))

def main(inputfile, langs, mode):
    img = cv2.imread(inputfile)
    # img = cv2.medianBlur(img, 5)
    # ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # ret3,img = cv2.threshold(img,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # img = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    # table_c = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (3, 3), 0, 0)
    # # Threshold
    # img = table_c
    # _, img = cv2.threshold(table_c, 180, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
    # cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
    # img = cv2.normalize(img, cv2norm_img, 0, 255, cv2.NORM_MINMAX)
    # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    # img = cv2.GaussianBlur(img, (1, 1), 0)

    gray = get_grayscale(img)
    # gray = deskew(gray)
    # gray = erode(gray)
    # thresh = thresholding(gray)
    # thresh = remove_noise(gray)
    # opening = opening(gray)
    # canny = canny(gray)
    img = gray
    # cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
    # img = cv2.normalize(img, cv2norm_img, 0, 255, cv2.NORM_MINMAX)
    # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    # img = cv2.GaussianBlur(img, (1, 1), 0)
    if langs == "fa":
        if mode == "t":
            custom_config = r'-l fas --psm 6 -c tessedit_char_blacklist="۰١۲۳۴۵۶۷۸۹«»1234567890#"'
        if mode == "tn":
            custom_config = r'-l fas --psm 6 -c tessedit_char_whitelist="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ۰١۲۳۴۵۶۷۸۹.?!,،:;/"'
        if mode == "table":
            custom_config = r'-l fas --psm 1 -c tessedit_char_whitelist="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ۰١۲۳۴۵۶۷۸۹"'

    elif langs == "en":
        custom_config = r'-l eng --psm 6'
    elif langs == "faen":
        custom_config = r'-l fas+eng --psm 1 --oem 3'
    else:
        print("Choose a valid Language.")
        exit(0)
    # img = np.array(gray)
    # for i in [1,3,4,5,6,7,8,9,10,11,12]:
    #     custom_config = fr'-l fas --psm {i}'
    text = pytesseract.image_to_string(img, config=custom_config)
    # print(i)
    # print(text)
    # with io.open('data.txt', 'w', encoding='utf8') as f:
    #     f.write(text)

    # text = str(text.encode("utf-8"))
    # # open text file
    # text_file = open("data.txt", "w")
    #
    # # write string to file
    # text_file.write(text)
    #
    # # close file
    # text_file.close()
    # return text
    # print(text.split())
    # spc = []
    # for word in text.split():
    #     # print(word)
    #     # print(0, spell.correction(word))
    #     spc.append(spell.correction(word))
    # print(spc)
    # tmp2 = spc.split(',')
    # print(spell.correction("سلان"))
    # text2 = pytesseract.image_to_string(thresh, config=custom_config)
    # print(text2)
    # text3 = pytesseract.image_to_string(opening, config=custom_config)
    # print(text3)
    # text4 = pytesseract.image_to_string(canny, config=custom_config)
    # print(text4)
    # return text
    print(text)
    cv2.imshow('image window', img)
    # add wait key. window waits until user presses a key
    cv2.waitKey(0)
    # and finally destroy/close all open windows
    cv2.destroyAllWindows()



if __name__ == "__main__":
    print(main("../Inputs/1.jpg", "fa", "t"))
