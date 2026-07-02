## User-Defined Bookshelf Sorting Algorithm

# This project is an sorting algorithm that sorts books based on the user's preference of organization and is interactable through a GUI. 

This project works by the user inputing a list of books through an GUI and sorts them based on up to two preferences the user can choose. The user will have to manually put in the following information about each book they have: 

* Title, Author (Last, First), Genre, Height(cm), Type-Standalone or Part of a Series
* If Type = Part of a Series: Series Name, Volume #

There will be a "Add Book to Shelf" button the user will press after putting down the information to add the book to the list. This will be on the left side of the GUI while the right side will have the list of books the user inputed. 

The user has the following options as preferences to organize the books by: 

* None, Genre, Author, Height, Standalone vs Series
* Ascending(A-Z / Smallest), Descending (Z-A / Tallest)

After choosing their preferences the user will press the "Sort Bookshelf" button to sort the list of books. The list of books on the left side of the GUI will be updated.  

# How the algorithm works
Python has a built in function called cmp_to_key, which works as a personalized comparing function. The program will have a object passed into the function that represents the preference the user wants books to be sorted by. Then the algorithm will find what the preference is, then get the values of the two book objects for that specific preference. Then it will compare them based on the order the user chose, and sort them. 

# How to use the project
In order to use this algorithm on your own, you will first need to have python3 extension. After, you will need to do the following depending on the method best for you: 

* Terminal- Click on Code button on the GitHub page, copy the Repository URL, open Terminal, type "cd" followed by the folder and its directory path you want it to go to, type "git clone " and paste the URL, press Enter

* VS Code- Click on Code button on the GitHub page, copy the Repository URL, launch VS Code, open Command Pallete, type "Git: Clone", press Enter, psste URL, press Enter, select folder you want the project to be on

* ZIP- Click on Code button on the GitHub page, select Download ZIP

# Known Issues
While I have not run into any syntax issues, I have noticed a logic one. 

* If the user wants to add more books after first sorting the list, they will need to press the "Sort Bookshelf" button again to update the list with the new book. When the user inputs new books after sorting a list of books, the list will reset to the order in which the user inputted them. 

# Expansion
I also have some ideas I want to add to make this algorithm better and expand it into an app:  

* Access to a dataset of all books created. I want it specifically linked to an app called Goodreads that most book readers use to track the books they read or want to read. Goodreads a dataset that has a lot of books and it is easy to search for books. I want to expand this algorithm to let the user search for books rather than manually inputing them. I also want to allow the user to transfer the books they have in their Goodreads app to my app so that it is less work for them to input books.
* I want to turn this into a app that also has a visual representation of the bookshelf and allows users to make their own bookcases and customize each bookshelf and have mutlitple bookcases. I want to let book readers be able to show off thier book collection on an app rather than having to take pictures of thier shelves. 
* I was thinking that I want to earn money on this app by letting users buy decoration, like string lights or bookends, for their bookshelves or bookcases. I was also thinking that they could also pay for a request of a personal decoration. They will need to send an email with a discription or photo of what their personalized decor is. I could also implement an AI generator for the personalized decor as well. 