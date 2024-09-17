import datetime 

debts = [
    {'description' : "Bank Loan", "amount" : 5000, "interest_rate" : 5, "due_date" : datetime.date(2024, 10 , 1)}, 
    {'description' : "Credit card", "amount" : 10000, "interest_rate" : 15, "due_date" : datetime.date(2024, 11 , 1)}, 
    {'description' : "decription", "amount" : 15000, "interest_rate" : 0, "due_date" : datetime.date(2024, 12 , 1)}, 
]

def calculate_interset(debts):
    return debts["amount"] * (debts['interest_rate']/ 100)

def suggest_payment_plan(debts): 
    debts = sorted(debts, key = lambda x:x['due_date'])
    print ('Suggested Payment Plan')
    for debt in debts: 
        interest = calculate_interset(debt) 
        print (f'-{debt["description"]}: Amount {debt["amount"]}, Interest {interest: .2f}, Due Date {debt["due_date"]}')

def display_debts(debts): 
    print ("Current Debts:")
    for debt in debts: 
        print (f"- {debt['description']}: Amount {debt['amount']}, Interest Rate {debt['interest_rate']}%, Due Date {debt['due_date']}")

display_debts (debts) 
suggest_payment_plan(debts)

