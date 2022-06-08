#Question 5

Hydrogen=int(input("Enter the number of hydrogen atoms:"))
Carbon=int(input("Enter the number of carbon atoms:"))
Oxygen=int(input("Enter the number of oxygen atoms:"))
Hydrogen_weight=Hydrogen*1.00794
Carbon_weight=Carbon*12.0107
Oxygen_weight=Oxygen*15.9994
molecular_weight=Hydrogen_weight+Carbon_weight+Oxygen_weight
print("The molecular weight of C6H12O6 is:",molecular_weight)
