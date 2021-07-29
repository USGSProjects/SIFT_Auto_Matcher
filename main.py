from SiftMatcher import SiftMatcher
from SiftComparator import SiftComparator
from GetAllSIFTScores import GetAllSIFTScores


# Variables to initialize a class should be stated in the beginning and put into the parameter as variables.
# This will make things much easier than directly inputting value of variables in parameters.
resized_width = 250
distance_coefficient = 0.67
acceptance_number = 4
cfg_file_path = "yolov3_testing.cfg"
yolo_weights_path = "yolov3_training_1000.weights"
specimen = "Turtle"
photo_directory_path = r"C:\Users\williamhuang\Downloads\Sample Turtles"
save_directory_path = "NewDatabase"

# # Initializes the class
# sift_matcher = SiftMatcher(cfg_file_path, yolo_weights_path, resized_width, distance_coefficient, acceptance_number)
# # Starts matching
# sift_matcher.start_matching(photo_directory_path, save_directory_path, specimen)

image_path_1 = r"C:\Users\williamhuang\Downloads\Sample Turtles\UnknownOld-2019-05-07_carapace copy.jpg"
image_path_2 = r"C:\Users\williamhuang\Downloads\Sample Turtles\UMJ3-2020-10-7-carapace copy.jpg"
image_path_3 = r"C:\Users\williamhuang\Downloads\Sample Turtles\TurtleOldSystem-2020-07-21-carapace copy.JPG"

# Initializes the class
# sift_tester = SiftComparator(cfg_file_path, yolo_weights_path, resized_width, distance_coefficient)
# # Starts Comparing two photos. Will output results in a screen to show you how SIFT is working.
# sift_tester.start_matching(image_path_2, image_path_3)

# # Initializes the class
# get_all_sift_scores = GetAllSIFTScores(cfg_file_path, yolo_weights_path, resized_width, distance_coefficient, acceptance_number)
# # Starts applying the SIFT algorithm to all photos in directory
# get_all_sift_scores.start_matching(photo_directory_path)