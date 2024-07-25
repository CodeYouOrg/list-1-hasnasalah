# originalList=["asna","xwomen","mother","kids","ebe","xred","momm","xender","hhh","xx","yellow","red"]
# front_x=[]
# for word in originalList:
#     if word[0]=='x':
#         front_x.append(word)
#         originalList.remove(word)
# sortedList=sorted(originalList)
# sortedFrontX=sorted(front_x)
# sortedFrontX.extend(sortedList)
# print(sortedFrontX)
# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
tuple=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
def last(tuple):
    return tuple[len(tuple)-1]
print(sorted(tuple,key=last))
