# movies = ["The Holy Grail", "The Life of Brian"]
# for each_turn in movies:
#     print(each_turn)
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin",
            "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# for each_turn in movies:
#     if isinstance(each_turn, list):
#         for each_inner_turn in each_turn:
#             if isinstance(each_inner_turn, list):
#                 for each_last_turn in each_inner_turn:
#                     print(each_last_turn)
#             else:
#                 print(each_inner_turn)
#     else:
#         print(each_turn)


def movielist(my_list):
    for each_turn in my_list:
        if isinstance(each_turn, list):
            movielist(each_turn)
        else:
            print(each_turn)
movielist(movies)