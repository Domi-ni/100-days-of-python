print(f"Welcome to the tip calculator.")
base_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons_to_slipt = int(input("how many people to split the bill? "))


tip = (tip_percent) / 100
tip = (base_bill) * tip
total_bill = (base_bill) + tip
pay_per_person = total_bill / (persons_to_slipt)
print(f"Each person should pay: ${round(pay_per_person, 2)}")
