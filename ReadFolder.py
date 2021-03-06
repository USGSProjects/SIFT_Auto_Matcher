import cv2
import os
from CustomDetector import CustomDetector


# Function that resizes an image
def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    try:
        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)
    except:
        return None


# Class that creates a processed version of a photo for SIFT Matching and holds relevant information for image
class MyImage:
    def __init__(self, img, img_name, width, cfg_file_path, yolo_weights_path):
        self.img = img
        self.cfg_file_path = cfg_file_path
        self.yolo_weights_path = yolo_weights_path
        new_image = self.img
        custom_detector = CustomDetector(cfg_file_path, yolo_weights_path)
        new_image = custom_detector.crop(new_image)
        new_image = resize_with_aspect_ratio(new_image, width=width)
        self.processed_img = new_image
        self.__name = img_name

    def __str__(self):
        return self.__name


# Loads images for SIFT Matching
class ImageLoader:
    def __init__(self, cfg_file_path, yolo_weights_path, resized_width):
        self.cfg_file_path = cfg_file_path
        self.yolo_weights_path = yolo_weights_path
        self.resized_width = resized_width

    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                print(filename + ' has been loaded')
                images.append(MyImage(img, filename, self.resized_width, self.cfg_file_path, self.yolo_weights_path))
        return images

