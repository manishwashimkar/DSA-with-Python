# Time Complexity measures how the running time of an algorithm increases as the size of the input (n) increases.

# It helps us analyze efficiency — not in exact seconds, but in terms of growth rate.

my_list = [1,2,3,4,5,6,7,8,9]

print(my_list[6])   # TC = O(1) => constant time

copied = my_list.copy()    # TC = O(n) => ieterate each item

appended = my_list.append(45)   # TC = O(1) => appends at last, independent of input size

poped = my_list.pop()   # TC = O(1) => remove at last, independent of input size

popInter = my_list.pop(6)  #TC = O(n) => index can be a last element

inserted = my_list.insert(0, "Manish")
# print(my_list)

