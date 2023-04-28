""" 
Inspired by: https://www.analyticsvidhya.com/blog/2021/07/an-interesting-opencv-application-creating-filters-like-instagram-and-picsart/#h2_6
"""
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel
import random
import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline


def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))

# greyscale filter
def apply_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# bright filter
def apply_bright(img):
    return cv2.convertScaleAbs(img, beta=60)

# dark filter
def apply_dark(img):
    return cv2.convertScaleAbs(img, beta=-60)

# sharp filter
def apply_sharp(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    return cv2.filter2D(img, -1, kernel)

# sepia filter
def apply_sepia(img):
    img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img_sepia = cv2.transform(  # multipying image with special sepia matrix
        img_sepia, 
        np.matrix([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])
    ) 
    img_sepia[np.where(img_sepia > 255)] = 255  # normalizing values greater than 255 to 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return

# pencil filter
def apply_pencil(img):
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return sk_gray

# pencil color filter
def apply_pencil_color(img):
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return sk_color

# hdr filter
def apply_hdr(img):
    return cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)

# invert filter
def apply_invert(img):
    return cv2.bitwise_not(img)

# summer filter
def apply_summer(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    return cv2.merge((blue_channel, green_channel, red_channel ))

# winter filter
def apply_winter(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    return cv2.merge((blue_channel, green_channel, red_channel))


class ApplyCV2FilterFromBytestringOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        """
        Get image bytestring, convert to cv2 image, apply filter, return bytestring
        """
        encoding = 'ISO-8859-1' # TODO add to model?
        img = cv2.imdecode(np.frombuffer(input_model.bytestring_image.encode(encoding), np.uint8), cv2.IMREAD_COLOR)

        effect_types_map = dict(
            grayscale = apply_grayscale,
            bright = apply_bright,
            dark = apply_dark,
            sharp = apply_sharp,
            sepia = apply_sepia,
            pencil = apply_pencil,
            pencil_color = apply_pencil_color,
            hdr = apply_hdr,
            invert = apply_invert,
            summer = apply_summer,
            winter = apply_winter
        )
        
        chosen_effect = input_model.effect
        if chosen_effect == "random":
            effects_list = list(effect_types_map.keys())
            chosen_effect = effects_list[random.randint(0, len(effects_list) - 1)]
        
        image_processed = effect_types_map[chosen_effect](img=img)
        _, buffer = cv2.imencode('.jpg', image_processed)
        
        bytes_image = buffer.tobytes().decode(encoding)
        return OutputModel(
            bytestring_image=bytes_image
        )