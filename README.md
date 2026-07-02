# User-Defined Bookshelf Sorting Algorithm

## This project is a sorting algorithm that sorts books based on the user's preference for organization and is interactive through a GUI. 

This project works by the user inputting a list of books through a GUI and sorting them based on up to two preferences that the user can choose. The user will have to manually put in the following information about each book they have: 

* Title, Author (Last, First), Genre, Height(cm), Type-Standalone or Part of a Series
* If Type = Part of a Series: Series Name, Volume #

There will be an "Add Book to Shelf" button that the user will press after entering the information to add the book to the list. This will be on the left side of the GUI, while the right side will have the list of books the user input. 

The user has the following options as preferences to organize the books by: 

* None, Genre, Author, Height, Standalone vs Series
* Ascending(A-Z / Smallest), Descending (Z-A / Tallest)

After choosing their preferences, the user will press the "Sort Bookshelf" button to sort the list of books. The list of books on the left side of the GUI will be updated.  

## How the algorithm works
Python has a built-in function called cmp_to_key, which works as a personalized comparison function. The program will have an object passed into the function that represents the preference the user wants books to be sorted by. Then the algorithm will find what the preference is, then get the values of the two book objects for that specific preference. Then it will compare them based on the order the user chose and sort them. 

## How to use the project
To use this algorithm on your own, you will first need to have the Python 3 extension. After, you will need to do the following depending on the method best for you: 

* Terminal- Click on the Code button on the GitHub page, copy the Repository URL, open Terminal, type "cd" followed by the folder and its directory path you want it to go to, type "git clone " and paste the URL, press Enter

* VS Code- Click on the Code button on the GitHub page, copy the Repository URL, launch VS Code, open Command Palette, type "Git: Clone", press Enter, paste the URL, press Enter, select the folder you want the project to be in

* ZIP- Click on the Code button on the GitHub page, select Download ZIP

## Known Issues
While I have not run into any syntax issues, I have noticed some logic issues. 

* If the user wants to add more books after first sorting the list, they will need to press the "Sort Bookshelf" button again to update the list with the new book. When the user inputs new books after sorting a list of books, the list will reset to the order in which the user inputted them.
* The user can only enter an integer as input for the height of the book. I forgot to change it to a float so that users can have a more accurate result. 
* I should also let the user put in a float for the volume number to represent novellas in series. 
* Put in a "Clear Bookshelf" button to get rid of the current list of books if users want to start on a new set of books. 
* A way to represent a book with more than one author. 

## Expansion
I also have some ideas I want to add to make this algorithm better and expand it into an app:  

* Access to a dataset of all books created. I want it specifically linked to an app called Goodreads that most book readers use to track the books they read or want to read. Goodreads dataset has a lot of books, and it is easy to search for books. I want to expand this algorithm to let the user search for books rather than manually input them. I also want to allow the user to transfer the books they have in their Goodreads app to my app so that it is less work for them to input books.
* I want to turn this into an app that also has a visual representation of the bookshelf and allows users to make their own bookcases, customize each bookshelf, and have multiple bookcases. I want to let book readers be able to show off their book collection on an app rather than having to take pictures of their shelves. 
* I was thinking that I want to earn money on this app by letting users buy decorations, like string lights or bookends, for their bookshelves or bookcases. I was also thinking that they could pay for a request for a personal decoration. They will need to send an email with a description or photo of what their personalized decor is. I could also implement an AI generator for the personalized decor as well. 
