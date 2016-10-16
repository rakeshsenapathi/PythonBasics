movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", [
    "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
for each_turn in movies:
    if isinstance(each_turn, list):
        for each_inner_turn in each_turn:
            if isinstance(each_inner_turn, list):
             for each_last_turn in each_inner_turn:
             	print (each_last_turn)
            # print(each_inner_turn)
            else:
            	print(each_inner_turn)
    else:
        print(each_turn)