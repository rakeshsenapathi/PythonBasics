list = [111,2911,1211,241,135,241,88,120,155,88,120,155,2001]

def remove_duplicates(list):

    new_list = []
    seen = set()

    for element in list:
        if( element not in seen):
            seen.add(element)
            new_list.append(element)
    return new_list

print(remove_duplicates(list))
