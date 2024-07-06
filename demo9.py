mi_list = [1, 2, 3]

# this creates only an alias to the object mi_list holds, any changes made to mi_list2 affects the original
mi_list2 = mi_list
mi_list2.append(4)

colors = ["red", "blue", "black"]

# SHALLOW COPY
# this copies the original and creates a new object that has the same values as the original, changes made to this doesn't affect the original (Note: mi_colors[i] affects colors[i])
mi_colors = list(colors)
mi_colors.append("yellow")
mi_colors.remove("red")

print(colors, mi_colors)

import copy

# DEEP COPY
# this copies the original perfectly, changes made to the copy doesn't affect the original at all
colors = ["black", "gray", "white"]
copied_colors = copy.deepcopy(colors)
copied_colors.append("brown")
copied_colors[0] = "pink"

print(colors, copied_colors)
