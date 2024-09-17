

salary = float(input("Enter the father's monthly  salary:")) 
num_family_members = int(input("Enter the number of family members:"))

family_needs = []

for i in range(num_family_members): 
    needs = float(input(f"Enter the needs of number {i+1}: "))
    family_needs.append(needs)

total_needs = sum(family_needs) 

allocated_budget = salary / num_family_members 

print ('\n Allocated budget per member:', allocated_budget)
print ('Total needs:', total_needs) 

if total_needs > salary : 
    difference  = total_needs - salary 
    print(f'\n To balance, expenses should be reduced by: {difference: .2f}')
    recommended_reduction = difference  / num_family_members 
    print(f'\n It is recommended to reduce each member"s needs by {recommended_reduction: .2f} to fit the budget.')

