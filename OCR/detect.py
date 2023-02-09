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


def main(inputfile,outputfile="result.txt", langs="faen", mode="t"):
    from PIL import Image
    import tempfile

    im = Image.open(inputfile)
    length_x, width_y = im.size
    # factor = min(1, float(1024.0 / length_x))
    factor = float(1024.0 / length_x)
    # factor = float(2)
    # size = int()
    size = int(factor * length_x), int(factor * width_y)
    # size = 1000, 1000
    image_resize = im.resize(size, Image.Resampling.LANCZOS)
    # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='1.png')
    # temp_filename = temp_file.name
    # im.save("test-600.png", dpi=(300, 300))
    image_resize.save("test-600.png", dpi=(300, 300))

    img = cv2.imread("test-600.png")
    gray = get_grayscale(img)
## Different Modes for image proccessing
    img = gray
    # deskew = deskew(gray)
    # erode = erode(gray)
    # thresh = thresholding(gray)
    # thresh = remove_noise(gray)
    # opening = opening(gray)
    # canny = canny(gray)

##Configs for Different OCR configs
    # custom_config = r'-l faen --psm 6"'
    if langs == "fa":
        if mode == "t":
            custom_config = r'-l fas --psm 6 -c tessedit_char_blacklist="۰١۲۳۴۵۶۷۸۹«»1234567890#"'
            # custom_config = r'-l fas --psm 6 -c tessedit_char_whitelist="آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی "'
        if mode == "tn":
            custom_config = r'-l fas --psm 6 -c tessedit_char_whitelist="آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ۰١۲۳۴۵۶۷۸۹.?!,،:;/"'
            # custom_config = r'-l fas --psm 6 -c tessedit_char_whitelist="آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ۰١۲۳۴۵۶۷۸۹"'
        if mode == "table":
            custom_config = r'-l fas --psm 6 -c tessedit_char_whitelist="آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی۰١۲۳۴۵۶۷۸۹"'
    elif langs == "en":
        custom_config = r'-l eng --psm 6'
    elif langs == "faen":
        custom_config = r'-l fas+eng --psm 6 '
    else:
        print("Choose valid Options.")
        exit(0)


    ## Convert Image to Text
    text = pytesseract.image_to_string(img, config=custom_config)

    ## Write Results to Result.txt with UTF-8 Encoding.
    with io.open(outputfile, 'w', encoding='utf8') as f:
        f.write(text)
    # return text
## Spell Checking (STILL IN PROGRESS)
    # print(text.split())
    # spc = []
    # for word in text.split():
    #     # print(word)
    #     # print(0, spell.correction(word))
    #     spc.append(spell.correction(word))

## Show Proccessed Image that is being used by pytesseract.
    # cv2.imshow('image window', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main(inputfile="Inputs/1.jpg", langs="fa", mode="t")
    # print(main(inputfile="test.jpg", langs="fa", mode="tn"))
