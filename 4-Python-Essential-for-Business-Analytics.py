import copy # import copy for deepcopy

# Task 1: Sales Data Cloning and Modification

weekly_sales = { # Original given sales
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

new_weekly_sales = copy.deepcopy(weekly_sales) # Deep copy of weekly_sales
new_weekly_sales["Week 2"]["Electronics"] = 18000 # Update value of electronics in week 2

print(weekly_sales) # Original remains unchanged
print(new_weekly_sales) # print out the new weekly sales with updated value