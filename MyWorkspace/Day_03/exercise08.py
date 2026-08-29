cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
print([cart[i] for i in range(len(cart)) if cart.index(cart[i]) == i])


# next_index,output = 0,[]
# for i in range(len(cart)):
#     next_index = cart.index(cart[i])
#     if next_index == i:
#         output.append(cart[i])
# print(output)