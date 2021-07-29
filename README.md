Before running these files you will need to set up your programming language (python in this case) and coding environment.
For downloading python, just go to the python website (https://www.python.org/) and download python. When downloading python, 
make sure you select add to PATH. This will ensure that the computer terminal can automatically access and use python and its package
manager pip without being in the folder which it is contained and can also sometimes aid coding text editors or IDEs(Integrated Development System) 
to automatically run python as they know its folder location.

Next you want to choose an advanced text editor or IDE to use to read and edit the code. If you are not familiar with coding, I would 
recommend an IDE as it has all the tools necessary to start coding where as text editors usually requires additional plugins 
to do certain stuff like debugging and running code. The IDE I recommend for python is PyCharm (https://www.jetbrains.com/pycharm/download). 

If you are on a government network and you are getting a strange popup every few seconds about some certificate error, follow the instructions in 
this paragraph. Otherwise, you may go to the next paragraph. To fix the error go to the top and select PyCharm < Preferences < Tools < Server Certificates on 
a mac or File < Settings < Tools < Server Certificates on Windows and Linux and select the option "accept all untrusted certificates automatically." Make sure to press
apply and okay. This should fix the error.

Once you download PyCharm, you have to link the python downloaded earlier with the PyCharm so PyCharm can understand and run python code.
To do this, you must go to the top and get to PyCharm < Preferences < Project<project name> < Python Interpreter on a mac or 
File < Settings < Project<project name> < Python Interpreter on Windows and Linux and select the gear button and press add. 
From there you should select System Interpreter instead of Virtualenv Environment. Although Virtualenv Environment can be used, 
it can be inconvenient and confusing as any packages you download will only be applied to that project and if you work on 
another project you may accidentally add a package to the wrong project. In addition, you may need a special command besides "pip 
install <package name>" to download packages from the terminal. After selecting System Interpreter, click the three ellipsis button
and find/enter/drag the path of the python.exe downloaded. Click Ok to get back to the Python Interpreter screen. In the place where 
you can choose a python interpreter, select the python interpreter that you just added. Press Apply and Ok. You should now be set up 
on PyCharm.

Once importing a python project or writing some code, press the run button. Make sure that the path of the file you want to run is properly set. You can check if 
it is properly set if the file you want to run is written to the left of the run button. If not you need to click that and press "edit configurations..." Edit the Script 
Path to the desired file location that you want to run and press apply and okay. 

If you get some error regarding a package not being found, you can install a package by going to PyCharm < Preferences < Project<project name> < Python Interpreter 
on a mac or File < Settings < Project<project name> < Python Interpreter on Windows and Linux and pressing the add button. Search for the package that is needed. 
One thing to keep in mind is that the import statement package name is not necessarily the name of the package. You will have to do a quick google search to find out 
the true package name before installing it. Once you find the package you need, install package and you will be notified if/when the package has been successfully installed.

If there is an issue downloading certain files, especially in a government network, run this command in the command terminal:
"pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>". It is important that you select add to PATH when downloading
python or else the computer will not know what pip is referring to if you are not in the same directory it is contained in.

To run the SIFT Matcher code, you must add the import statement "import SIFTMatcher as Matcher." Once this is done you will need
to create 5 variables: resized_width, distance_coefficient, acceptance_number, photo_directory_path, and save_directory_path.

Resized_width is width of the readjusted photo when photos are matched. The higher the number, the bigger the size of the photo, 
meaning better resolution. The results of this are a longer photo load time and match time due to more data being computed and 
more chances for the SIFT algorithm to find key points. Too high of a number and the SIFT algorithm may pick of background interference 
with longer runtime and too little will result in a shorter runtime but not enough keypoints being found for accurate matching. 
I would recommend starting with 250 and playing with that number to match what best works for you.

The second variable, distance_coefficient, compares how close relatively in distance one keypoint in a photo is to another. 
A high distance_coefficient means more leeway to accept keypoints on different pictures as matches, raising the match score between photos
A low distance_coefficient means the closeness of the keypoints has to be more accurate, likely decreasing the match score 
between photos. I recommend using 0.67 and tweaking it from there.

The variable acceptance_number is a number between 0-100 that is a threshold number needed for a match score to deem two 
pictures a match. A relatively high acceptance_number would require the match score to be really high between two photos, likely rejecting
scores coming from the same specimen in two photos if there is a bit of variation. A relatively low acceptance_number may on the other hand 
accept matches that are not actually matches. I recommend the number 4 as there is likely significant variation between different photos with 
the same specimen and enough differences in photos where there are different specimens that 4 can be considered high.

The string variables cfg_file_path (file that contains general machine learning data to enhance yolo_weight_path data) 
and yolo_weights_path (file with specific object annotation data) are files needed for the custom detector powered by machine learning.

The string variables photo_directory_path and save_directory_path are just the path of what photos are being matched and 
where matched photos will be.

To use the SiftMatcher, you must import that class into the main.py file by writing "from SiftMatcher import SiftMatcher".
Then you must initialize the variables mentioned above through an initializer. An example would be 
"sift_matcher = SiftMatcher(cfg_file_path, yolo_weights_path, resized_width, distance_coefficient, acceptance_number)".
If you would like to use the variables that were recommended, you may use a shorter constructor like this: 
"sift_matcher = Matcher.SiftMatcher(cfg_file_path, yolo_weights_path)". Then you must actually run the function 
that allows the matching to start. To do this, add "sift_matcher.start_matching(photo_directory_path, save_directory_path)". After this you can run the program and look at 
the console to see the results. Note: The constructor does not use photo_directory_path and save_directory path because it is possible that you may want to sort multiple databases, all using the 
same setting. If you want to use different settings for a different database, consider creating a separate initializer and use the start_matching function with the new initializer.

When the program finishes running you will get three new files, a folder containing the photo matches, a csv file containing 
match scores/results, and a text file that states the the value of variables initialized and important information
on the highest match scores for true results, lowest match scores for false results, etc. You should use the text file to tweak
the SiftMatcher program's variables. 

For the other two files that can be run, GetAllSIFTScores.py and SiftComparator.py, similar steps apply. In the main.py file,
Import the correct file (from ...) then grab the specific class you want from that file (import ...). 

To initialize the object,
fill out all necessary parameter values. The necessary parameter values can be found with the constructor (init function) that corresponds to the class
you imported. For example,
    # Initializer with additional customization
    def __init__(self, cfg_file_path, yolo_weights_path, resized_width=250, distance_coefficient=0.67, acceptance_number=4):
        self.resized_width = resized_width
        self.distance_coefficient = distance_coefficient
        self.acceptance_number = acceptance_number
        self.cfg_file_path = cfg_file_path
        self.yolo_weights_path = yolo_weights_path
The variables in the parenthesis in the example above ~ (ignore self as this just creates a connection between variables in 
the function and global variables), cfg_file_path, yolo_weights_path, resized_width, distance_coefficient, and acceptance_number ~
are the variables to be filled out in the initializer that is created in the main.py file. The variables without equal signs ~
cfg_file_path and yolo_weights_path ~ denoting a default value must be filled out in the specific order or with the variable name, 
equal sign, and value it should represent. The other variables ~ resized_width, distance_coefficient, and acceptance_number ~ 
do not have to be filled out, in which they will equal their default value. If those variables are to be filled out, they can 
either be written after the mandatory variables or written in any order with the variable name, equal sign, and value written in 
any order in front of the mandatory variables. To keep things simple, I would recommend just inputting values into the initializer in the 
value in which they are written in the init function.

After the initializer is created and filled out, it can be used to access one of its functions. To do this look through the contents of 
the respective class you are using and search for any functions (denoted by def). After finding the function needed, write this in the main.py
file: <initializer>.<function_name>(<parameters which are filled out the same way as constructor)>). After everything is set, press the 
run button and results should be outputted after the program finishes running.

For certain applications, you may want to create an exe file for a script that has a gooey system which can make it easier for others to use a program without any 
coding knowledge. If you would like to do this, I recommend following the video (https://www.youtube.com/watch?v=Y0HN9tdLuJo&t=166s). To sum up how to make the conversion,
you must first download the python program auto-py-to-exe. Remember, if you are on a government network, you might have to run "pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>"
in the terminal instead of just pip install <package name>. Once the code is downloaded, type in auto-py-to-exe in the terminal. This will pop up a python to exe conversion screen. In the first field, Script Path, you must select
the path of the code (which will be run) that you want to turn into an exe file. Any supporting files(other python files that have classes or functions that are used in the python file that will be run) will be added in the
Additional Files section. For the Onefile section, you must choose whether your code is contained in a directory, usually with supporting files, or just a single script. The Console Window section is the place where you
select whether or not you want the exe file to have a console to print out statements like in the IDE. The Icon section is optional but highly recommended as it helps distinguish your program from other exe files. To create 
an Icon, I would recommend finding a picture supported by a Creative Commons license to avoid any potential legal trouble. After obtaining a photo, I recommend going to convertico.com and uploading the photo you want to be 
the icon and downloading the corresponding ico file. When you have the ico file, you can select the file of that file in the Icon section in auto-py-to-exe. The Advanced section is also optional and should be used if there are any 
complications when converting a python file. In the Output section, select the place you want the exe file to be put. When all settings are set correctly, press Convert .PY to .EXE. Your exe file should appear in its respective 
location shortly after.





