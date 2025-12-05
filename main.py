# Festival Inventory Disaster – Real‑World Python Collections Challenge
# Scenario
# You are hired as the Data Assistant for the Chicago Fall Music & Food Festival.
# The festival opens in 3 hours, but the digital system has scrambled the inventory lists, vendor data, and safety rules. Your job is to fix the data using Python lists, sets, and tuples.
# If you fail, the festival cannot legally open.

# Starting Data
foods = ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"]
stages = ("Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley")
restricted = {"glass bottles", "weapons", "alcohol", "alcohol"}
attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]

# Task 1 — Clean the Food Vendor List
    # 1. Remove duplicates while keeping only the first occurrence.

food2 = list(dict.fromkeys(foods))


    # 2. Add "ramen" and "fried rice".
food2.append("ramen")
food2.append("fried rice")



    # 3. Insert "smoothies" at index 2.
food2.insert(2, "smoothies")




    # 4. Sort the list alphabetically.

food2.sort()


    # 5. Print the final vendor list.

print("The final vendors list is : ", food2)


#Task 1.5 
    # combine all the list into a nested list called festival_data

festival_data = (food2, stages, restricted, attendance)

    #print out the new nested list(use a for loop to print each item on a new line)


for sublist in festival_data:
    for item in sublist:
        print(item, end =' ')
    print()


# Task 2 — Stage Map
    # 1. Print the second stage.

print(stages[1])
    # 2. Print the last two stages.

print(stages[-2:])
    # 3. Convert the tuple into a list and add "Rock Arena".

stages2 = list(stages)
stages2.append("Rock Arena")



    # 4. Convert it back into a tuple.

stages3 = tuple(stages2)


    # 5. Print the updated tuple.
print(stages3)

# Task 3 — Restricted Items
    # 1. Add "fireworks".

restricted.add("fireworks")


    # 2. Try adding "weapons" again.

restricted.add("weapons")
    # 3. Remove "alcohol".

restricted.remove("alcohol")
    # 4. Check if "glass bottles" is still restricted.

item_check = "glass bottles"

if item_check in restricted:
    print("Glass bottles are still restricted! ")

    # 5. Print the final restricted set.

print(restricted)




# Task 4 — Attendance Analysis

attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]

    # 1. Print the first three hours.
print(attendance[0:3])
    # 2. Print the last hour.
print(attendance[-1])
    # 3. Print every 2nd hour.
third_hour = attendance[::2]
print(third_hour)
    # 4. Remove the 5th hour using pop().
attendance.pop(4)


    # 5. Add five projected values using extend(range(...)).
attendance.extend(range(165,175, 2))

print(attendance)
    # 6. Delete every 3rd value using del attendance[::3].
del attendance[::3]

print(attendance)
    # 7. Print the length and cleaned list.
att_len = len(attendance)
print(att_len)

print(attendance)


# Task 5 — Festival Master List
    # 1. Convert vendors, restricted set, and stages into lists.

food5 = list(food2)


restricted5 = list(restricted)

stages5 = list(stages3)


    # 2. Combine everything into festival_data.

festival_data = [food5, restricted5, stages5]

    # 3. Print: total items, first 10, last 10.

festival_data = food5 + restricted5 + stages5
total_items = len(festival_data)

print(f"Total items: {total_items}")

    # 4. Remove duplicates.

print(festival_data)

    # 5. Print final cleaned festival_data.




# Extension
# Write a function festival_search(item) that returns True/False if item appears in festival_data.



