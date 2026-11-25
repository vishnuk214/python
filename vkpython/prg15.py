color_list1=input("Enter colors in list 1 separated by comma :").split(",")
color_list2=input("Enter colors in list 2 separated by comma :").split(",")
for color in color_list1:
   if color not in color_list2:
      print(color)
