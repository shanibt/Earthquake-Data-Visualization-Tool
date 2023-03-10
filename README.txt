ICS32 Workout Project 4: Visualizing Web Information

Main Purpose: To create a scatterplot of the magnitudes of the different
earthquakes that took place on that date given by the user. 

WorkoutProject4.py 
    Collects the input from user and checks to make sure the date given is valid.
    Use the input to extract data from the Earthquake API and upload
    the data into a file, under the given file name. From the data extracted from
    the Earthquake API, check and add the magnitudes of earthquakes that happened
    in California on the date given. 

webAPI.py
    Opens and reads the Earthquake API url based on
    the date that is given by the user.

visual.py
    Sort the extracted data for only California magnitudes and
    create and save the scatterplot that depicts the varying
    magnitudes of the earthquakes on the given date.

fileIO.py
    Uploads data extracted from Earthquake API onto
    file under the name given by the user.

DateChecker.py
    Splits the date string into 3 different parts and
    validates that the year, month, and day are possible
    ad individual values and then together.

WorkoutProject4-16539648.png
    Scatterplot that shows the different magnitudes of the
    number of earthquakes that happened in California on
    2023-02-09. X-axis is the number of earthquake and Y-axis
    is the magnitude. 
