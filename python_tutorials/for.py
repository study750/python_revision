cost = [10,20,30,40,50]
total_cost =0 
for i in cost:
    total_cost+= i 
    print("Cost of item", i, "is added to total cost")

print("Total cost is:", total_cost)

sample_cost= 0 
for i in range(1,3):
    sample_cost += cost[i]
print("Sample cost is:", sample_cost)