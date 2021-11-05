from budget import budget2_

file1 = open("food_budget.txt", "r")
list1 = file1.readlines()
food = budget2_(int(list1[0]))
file1.close()

file2 = open("bills_budget.txt", "r")
list2 = file2.readlines()
bills = budget2_(int(list2[0]))
file1.close()

file3 = open("entertainment_budget.txt", "r")
list3 = file3.readlines()
entertainment = budget2_(int(list3[0]))
file1.close()

file4 = open("clothes_budget.txt", "r")
list4 = file4.readlines()
clothes = budget2_(int(list4[0]))
file1.close()


# print(food)
# print(entertainment)
# print(bills)
# print(clothes)

food.deposit(bills.withdraw(10))
food.deposit(100)


file1= open("food_budget.txt","w")
file1.write(str(food.balance))
file1.close()

file2 = open("bills_budget.txt", "w")
file2.write(str(bills.balance))
file2.close()

file3 = open("entertainment_budget.txt", "w")
file3.write(str(entertainment.balance))
file3.close()

file4 = open("clothes_budget.txt", "w")
file4.write(str(clothes.balance))
file4.close()