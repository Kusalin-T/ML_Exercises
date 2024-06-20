result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
n=0
for r in result:
    if r == "heads":
        n+=1
print(f"Heads: {n}")
print([x**2 for x in range(1,11) if x%2==1])

expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter expense: "))
print(f"Expense month: {str(expense_list.index(expense)+1) if expense in expense_list else 'Not found'}")

for i in range (5):
    print(f"{i+1} Km")
    tired = input("Are u tired? ")
    if tired=="yes":
        print("Stop running")
        break
    else:
        print("Keep running")
    if i==4: print("Race Over Congrats")    





