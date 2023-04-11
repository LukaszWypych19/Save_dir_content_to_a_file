print('Hello World!')

# listone = [1,2,3]
# listtwo = [4,5,6]
# alternatinglist = []
# for i in range(len(listone)):
#     alternatinglist.append(listone[i])
#     alternatinglist.append(listtwo[i])
# print(alternatinglist)

listone = [1,2,3]
listtwo = [4,5,6]
alternatinglist = []
for item1,item2 in zip(listone,listtwo):
    alternatinglist.append(item1)
    alternatinglist.append(item2)
print(alternatinglist)