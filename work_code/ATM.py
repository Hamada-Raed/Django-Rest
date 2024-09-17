import tkinter as tk 
from tkinter import messagebox 

balance = 1000 

def check_balance(): 
    messagebox.showinfo("Balance", f"Your current balance is: ${balance}")
    
def deposit():
    global balance

    try: 
        amount = float(entry_amount.get())
        if amount <= 0: 
            raise ValueError
        
        balance += amount 
        messagebox.showinfo("Deposit", f"Deposited: ${amount}\n New balance: ${balance}")
        entry_amount.delete(0, tk.END) 

    except: 
        messagebox.showerror("Invalid input", "Please enter a valid amount.")

def withdrow(): 
    global balance

    try: 
        amount = float(entry_amount.get())
        if amount <= 0: 
            raise ValueError 
        
        if amount > balance: 
            messagebox.showwarning("Insufficient Funds", "You do not have enough balance.")

        else: 
            balance -= amount
            messagebox.showinfo("Withdraw", f"Withdraw: ${amount}\n New balance: ${balance}")

        entry_amount.delete(0, tk.END)

    except: 
        messagebox.showerror("Invalid input:", "Please enter a valid amount.")

root = tk.Tk()
root.title ("ATM")
root.geometry("300x300")

label = tk.Label(root, text="Enter amount:")
label.pack(pady=10)

entry_amount = tk.Entry(root)
entry_amount.pack(pady=10)

btn_ckeck_balance = tk.Button(root, text="Doposit", command=deposit)
btn_ckeck_balance.pack(pady=10)

btn_withdraw = tk.Button(root, text="Withdraw", command=withdrow)
btn_withdraw.pack(pady=10) 

root.mainloop()
