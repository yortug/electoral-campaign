
QUICKSTART

To start the program simply navigate to the assignment directory and run ```python mainMenu.py``` to begin the process. 

As outlined in the ‘requirements.txt’ file there are four (4) outside packages which I’ve used, but three of these four package were used when I gathered the electorate distance data file and are not actually required in the execution of the program. The only outside package required for the program to run is numpy (version 1.15.2 was used during writing). 

When making a menu selection simply press the key outlined in the square brackets, and then press ‘enter/return’ on your keyboard to confirm the selection. When you are able to enter multiple selections it should be quite obvious as the text you read will indicate it’s a plural and not a singular. Quitting from a submenu or from the main menu will always be carried out through entering the lower case ‘q’ character into the selection space.

Once you come across an option which allows you to make multiple selections you are required to enter your selections in a comma separated format, no extra white-spaces, just a set of integers with commas in-between. If you want to include all selections then you can enter the character ‘a’ or ‘A’ to indicate you want all options to be factored in.

  i.e. “Please select your state(s)” - plural
	e.g ```1,2,5,7,9``` or ```a``` or ```A```
  i.e. “Please select your starting position” - singular
	e.g ```1``` or ```23```

All file reading & writing is done using relative paths, that means we’re making reference to the directory in which you executed the file from. When you’re reading or writing to a CSV file it is crucial that your filename ends with “.csv”, and the same is of course true with “.txt” for text files (important because ‘Itinerary by Margin’ writes to a .txt file not a .csv file.

Just incase something goes horribly wrong, or you're feeling lazy, I've included "marginalALP_6pct.csv" which is the output of 'List by Margin' when you select Australian Labor Party and set the margin to 6%. And, then I've also included "marginalALP_6pct_itinerary.txt" which is the output of 'Itinerary by Margin' when you input that corresponding .csv file.

ENJOY!

==================================================================

ADDED NOTE FROM AFTER FORCED CSV CHANGES FOLLOWS:

I went through and painfully changed everything to get rid of the Python csv module dependency, and any sorted() function calls that I used as placeholders when creating my code (all changes are documented within 'changelog.txt'). No inbuilt Python data structures are being used in this assignment. 

Although I made these changes, I still consider it completely UNFAIR that we were ever forced to make them. We were never marked down for using the csv module during pracs, we were never told we couldn't use it, there's no mention in the assignment specifications that we couldn't use it, and then less then a week before the assignment is due we are told we have to change an integral part of our program... Unfair.

Now, as I stated before I make no use of Python's inbuilt data structures throughout this assignment. However, considering we were forced to change the csv module (which we all never knew was a data structure to begin with), then I think I better make a few other things clear.

You can't actually go from a set() object straight to a numpy array, so I was forced to briefly type cast from a set(), to a list(), and then straight to a numpy array. The list() is of course NEVER used, it is simply a necessary intermediary between the set() and the numpy array. This is the only time I ever call the list() function, and as you can tell it's never actually used - it's instantly switched to an array on the same line it's called.

Now, if there're questions regarding my use of sets. There was no mention of us NOT being able to use the set() function within Python; and considering we were briefly taught set notation during one of our lectures I assumed it was allowed. It's never actually used to do any union/intersection operations, just as a quick, easily readable way of finding the unique set within some array.

If you are considering deducting marks from me for simply casting to a list() as an intermediary, or for my use of sets here then please contact me IMMEDIATELY, as I consider this COMPLETELY unfair, and will definitely be arguing my case further.
 
- Troy Engelhardt (18815179)
