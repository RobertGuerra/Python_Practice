#Write your function here
def double_index(lst, index):
#check to see if the index is too large
  if index >= len(lst):
    return lst
#get the original list up to the index
  else:
    newlist = lst[0:index]
#adds double the value at the index to new list
  newlist.append(lst[index] * 2)
#add the rest of original list
  newlist = newlist + lst[index + 1:]
  return newlist

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))