import tkinter as tk
from tkinter import *
import tkinter.messagebox
 
root = tk.Tk() 

root.title("Currency Conversion")

Tops = Frame(root,bg = '#663300',pady = 2, relief = "ridge")
Tops.grid(row=0,column=0,columnspan=2)

headlabel = tk.Label(Tops,font=('lato black', 19,'bold'), text = 'Currency Converter', bg= 'coral',fg='white',borderwidth=2, relief="groove") 
headlabel.grid(row=1, column=0,columnspan=2)
 
variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 
 
variable1.set("currency") 
variable2.set("currency") 

def RealTimeCurrencyConversion(): 
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()
    
    from_currency = variable1.get() 
    to_currency = variable2.get()
    
    if (Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Error !!","Amount Not Entered.\n Please a valid amount.")
        
    elif (from_currency=="currency" or to_currency=="currency"):
        tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")
        
    else:
        new_amt = c.convert(from_currency,to_currency,float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount)) 

def clear_all() : 
	Amount1_field.delete(0, tk.END) 
	Amount2_field.delete(0, tk.END)
    
    
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]


root.configure(background = '') 

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "Amount  :  ", bg="#e6e5e5",fg = "black",justify="right") 
label1.grid(row=2, column=0)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "From Currency  :  ", bg="#e6e5e5",fg = "black",justify="right") 
label1.grid(row=3, column=0)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "To Currency  :  ", bg="#e6e5e5",fg = "black",justify="right") 
label1.grid(row=4, column=0)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "Converted Amount  :  ", bg="#e6e5e5",fg = "black",justify="right") 
label1.grid(row=8, column=0)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list) 
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list) 

FromCurrency_option.grid(row = 3, column = 1, padx = 5) 
ToCurrency_option.grid(row = 4, column = 1, padx = 5) 

Amount1_field = tk.Entry(root) 
Amount1_field.grid(row=2,column=1,padx=5)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8,column=1,padx=5) 

Label_9 =Button(root, font=('arial', 15,'bold'), text="   Convert  ",padx=2,pady=2, bg="blue",fg = "white",command=RealTimeCurrencyConversion,activebackground="coral")
Label_9.grid(row=6, column=0,columnspan=2)

Label_9 =Button(root, font=('arial', 15,'bold'), text="   Clear All  ",padx=2,pady=2, bg="white",fg = "red",command=clear_all,activebackground="red",activeforeground="white")
Label_9.grid(row=10, column=0,columnspan=2,pady=5)

root.mainloop()
