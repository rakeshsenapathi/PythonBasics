""" This is a function that checks if the traverses
    a listthrough recursion to print the elements """
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin",
            "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


def movielist(my_list):
	""" This is moduled named nester.py which prints elements 
	in a list which may or may not contain a nested list"""

    for each_turn in my_list:
        if isinstance(each_turn, list):
            movielist(each_turn)
        else:
            print(each_turn)
movielist(movies)
