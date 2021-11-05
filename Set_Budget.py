from budget import budget2_

food =budget2_(200)
entertainment = budget2_(400)
bills = budget2_(50)
clothes = budget2_(600)

# print(food)
# print(entertainment)
# print(bills)
# print(clothes)



food.deposit(bills.withdraw(10))
print(food)
print(bills)

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