# fruits=("apple","orange","banana")
# (green,yellow,blue)=fruits

# print(green)
# print(blue)
# print(yellow)

fruits=("apple","orange","banana")
(green,yellow,*blue)=fruits

print(green)
print(blue)
print(yellow)