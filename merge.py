from tkinter import *
from tkinter import ttk
import random
import tkinter as tk
import tempfile
import os

from datetime import datetime
from tkinter import messagebox
import sys
def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def  __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Store ")

        self.title_lable = Label(self.win,text="Store Management System",font=('arial',35,'bold'),bg="purple",bd=8,relief=GROOVE)
        self.title_lable.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="cadetblue",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=400)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg ="cadetblue",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="cadetblue",font=('sans-serif',25,'bold'))
        self.entry_frame.pack(fill=BOTH,expand=True)

        self.entus_lbl = Label(self.entry_frame, text="Enter UserName", bd=6,  bg="cadetblue",
                                      font=('sans-serif', 25, 'bold'))
        self.entus_lbl.grid(row=0,column=0)
        #============================================================================
        username = StringVar()
        password = StringVar()



        self.entus_ent = Entry(self.entry_frame,  font=('sans-serif', 25, 'bold'),bd=6,textvariable=username)
        self.entus_ent.grid(row=0, column=1,padx=2,pady=2)

        self.entuspass_ent = Label(self.entry_frame, text="Enter Password", bd=6, bg="cadetblue",
                               font=('sans-serif', 25, 'bold'))
        self.entuspass_ent.grid(row=1, column=0)

        self.entuspass_lbl = Entry(self.entry_frame, font=('sans-serif', 25, 'bold'),bd=6,textvariable=password,show="*")
        self.entuspass_lbl.grid(row=1, column=1, padx=2, pady=2)
        #=============================function===================================================
        def check_login():
            if username.get()  == "" and password.get() == "":
                self.billing_btn.config(state="normal")
            else:
                pass
        def reset():
            username.set("")
            password.set("")

        def billing_sec():
            self.newWindow = Toplevel(self.win)
            self.app = Window1(self.newWindow)

        def iMeset():
                self.newWindow = Toplevel(self.win)
                self.app = Window2(self.newWindow)

            # =============================================================================


        self.button_frame = LabelFrame(self.entry_frame, text="Option", font=('sans-serif', 20, 'bold'), bg="cadetblue",
                                       bd=7, relief=GROOVE)
        self.button_frame.place(x=20, y=200, width=750, height=80)

        self.login_btn = Button(self.button_frame, text="Login", font=('arial', 15), bd=5, width=8,
                                command=check_login)
        self.login_btn.grid(row=0, column=0, padx=20, pady=2)

        self.billing_btn = Button(self.button_frame, text="Billing", font=('arial', 15), bd=5, width=8,
                               command=billing_sec   )
        self.billing_btn.grid(row=0, column=1, padx=20, pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame, text="Reset", font=('arial', 15), bd=5, width=8, command=reset)
        self.reset_btn.grid(row=0, column=3, padx=20, pady=2)

        self.reset_btn = Button(self.button_frame, text="meset", font=('arial', 15), bd=5, width=8, command=iMeset)
        self.reset_btn.grid(row=0, column=4, padx=20, pady=2)











class Window1:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Store Management System")

        self.title_lable = Label(self.win, text="Store Management System", font=('arial', 35, 'bold'), bg="purple",
                                 bd=8, relief=GROOVE)
        self.title_lable.pack(side=TOP, fill=X)
        self.win.resizable(0,0)
        #==================var================================================================
        bill_no = random.randint(100,10000)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var =StringVar()
        Customer_name=StringVar()
        Customer_cot=StringVar()
        Date = StringVar()
        Item = StringVar()
        Quantity = StringVar()
        Cost = StringVar()


        Date.set(datetime.now())
        total_list =[]
        self.grd_total =0




#============================================================================================================
        self.entry_frame = LabelFrame(self.win,text="Enter Details",bg="cadetblue",font=('arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=30,y=80,width=600,height=730)

        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number",bg="cadetblue",font=('arial',20))
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,   font=('arial', 20),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0, column=1, padx=2, pady=2)
        self.bill_no_ent.config(state="disable")

        #
        self.Customer_name_lbl = Label(self.entry_frame, text="Customer_Name", bg="cadetblue", font=('arial', 20))
        self.Customer_name_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.Customer_name_ent = Entry(self.entry_frame, bd=5, textvariable=Customer_name, font=('arial', 20))
        self.Customer_name_ent.grid(row=1, column=1, padx=2, pady=2)
        #
        self.Customer_cot_lbl = Label(self.entry_frame, text="Customer_Contact", bg="cadetblue", font=('arial', 20))
        self.Customer_cot_lbl.grid(row=2, column=0, padx=2, pady=2)

        self.Customer_cot_ent = Entry(self.entry_frame, bd=5, textvariable=Customer_cot, font=('arial', 20))
        self.Customer_cot_ent.grid(row=2, column=1, padx=2, pady=2)
        #
        self.Date_lbl = Label(self.entry_frame, text="Date", bg="cadetblue", font=('arial', 20))
        self.Date_lbl.grid(row=3, column=0, padx=2, pady=2)

        self.Date_ent = Entry(self.entry_frame, bd=5, textvariable=Date, font=('arial', 20))
        self.Date_ent.grid(row=3, column=1, padx=2, pady=2)
        #
        self.Item_lbl = Label(self.entry_frame, text="item Purchased", bg="cadetblue", font=('arial', 20))
        self.Item_lbl.grid(row=4, column=0, padx=2, pady=2)

        self.Item_ent = Entry(self.entry_frame, bd=5, textvariable=Item, font=('arial', 20))
        self.Item_ent.grid(row=4, column=1, padx=2, pady=2)
        #
        self.Quantity_lbl = Label(self.entry_frame, text="Item Quantity", bg="cadetblue", font=('arial', 20))
        self.Quantity_lbl.grid(row=5, column=0, padx=2, pady=2)

        self.Quantity_ent = Entry(self.entry_frame, bd=5, textvariable=Quantity, font=('arial', 20))
        self.Quantity_ent.grid(row=5, column=1, padx=2, pady=2)
        #
        self.Cost_lbl = Label(self.entry_frame, text="Cost Of Each ", bg="cadetblue", font=('arial', 20))
        self.Cost_lbl.grid(row=6, column=0, padx=2, pady=2)

        self.Cost_ent = Entry(self.entry_frame, bd=5, textvariable=Cost, font=('arial', 20))
        self.Cost_ent.grid(row=6, column=1, padx=2, pady=2)
        #===========buttons#]===============================
        def default_bill():
            self.bill_txt.insert(END,"\tApka Store")
            self.bill_txt.insert(END, "\n\tMinar Gate,Palwal")
            self.bill_txt.insert(END,"\n\t Contact =0886554343")
            self.bill_txt.insert(END,"\n===========================================")
            self.bill_txt.insert(END,f"\nBill Number : {bill_no_tk.get()}")

        def generate():
             if Customer_name.get() == "" or (Customer_cot.get() == "" or len(Customer_cot.get())  != 10):
                             messagebox.showerror("Error ! ","Please enter all the fields correctly.",parent=self.win)

             else:

                self.bill_txt.insert(END,f"\nCustomer Name : {Customer_name.get()}")
                self.bill_txt.insert(END, f"\nCustomer Contact : {Customer_cot.get()}")
                self.bill_txt.insert(END,f"\nDate : {Date.get()}")
                self.bill_txt.insert(END, "\n===========================================")
                self.bill_txt.insert(END,"\nProduct Name:       \t\tQuantity      \t\t Per Cost    \t\tTotal  ")
                self.bill_txt.insert(END, "\n===========================================")

                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
                self.save_btn.config(state="normal")

        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n===============================================")
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t Grand Total : {self.grd_total}")
            self.bill_txt.insert(END,"\n===============================================")
        def clear_func():
            Customer_name.set("")
            Customer_cot.set("")
            Item.set("")
            Cost.set("")
            Quantity.set("")
        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.bill_txt.delete("1.0",END)
            default_bill()
        def add_func():
            qty = int (Quantity.get())
            cone =int (Cost.get())
            total = qty * cone
            total_list.append(total)
            self.bill_txt.insert(END, f"\n\n{Item.get()}         \t\t{Quantity.get()}       \t\t {Cost.get()}       \t\t{total}  ")

            self.bill_txt.insert(END,"\n===============================================")
        def save_func():
            user_choice = messagebox.askyesno("Confirm",f"Do you want to save the bill {bill_no_tk.get()}",parent =self.win)
            if user_choice>0:

                self.bill_content= self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/bills/" +str(bill_no_tk.get()) +".txt", "w")
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {e}")
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Sucess !", f"Bill {bill_no_tk.get()} has been saved sucessfully !", parent =self.win)
            else:
                return


        def add_pur():
            pass





        #=======================================================================

        self.button_frame = LabelFrame(self.entry_frame,text="Options",bg="cadetblue",font=('arial',20,'bold'))
        self.button_frame.place(x=20,y=325,width=540 ,height=300 )

        self.add_btn = Button(self.button_frame,bd=2,text="Add",font=('arial',20,'bold'),width=8,height=1,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        self.add_btn.config(state="disable")



        self.generate_btn = Button(self.button_frame, bd=2, text="Generate", font=('arial', 20, 'bold'), width=8,
                                   height=1,command=generate)
        self.generate_btn.grid(row=0, column=1, padx=4, pady=2)

        self.clear_btn = Button(self.button_frame, bd=2, text="Clear", font=('arial', 20, 'bold'), width=8, height=1,command=clear_func)
        self.clear_btn.grid(row=0, column=2, padx=4, pady=2)

        #
        self.total_btn = Button(self.button_frame, bd=2, text="Total", font=('arial', 20, 'bold'), width=8, height=1,command=total_func)
        self.total_btn.grid(row=1, column=0, padx=4, pady=2)
        self.total_btn.config(state="disable")
        self.reset_btn = Button(self.button_frame, bd=2, text="Reset", font=('arial', 20, 'bold'), width=8, height=1,command=reset_func)
        self.reset_btn.grid(row=1, column=1, padx=4, pady=2)
        self.save_btn = Button(self.button_frame, bd=2, text="Save", font=('arial', 20, 'bold'), width=8, height=1,command=save_func)
        self.save_btn.grid(row=1, column=2, padx=4, pady=2)
        self.save_btn.config(state="disable")
#=======================================================================================


        #============================cal frame========================

        self.calc_frame = Frame(self.win,bd=3,bg="cadetblue",relief=GROOVE)
        self.calc_frame.place(x=650,y=80 ,width= 650 ,height=260)

        self.num_ent = Entry(self.calc_frame,bd=15,bg="cadetblue",textvariable=calc_var,font=('arial',15),width=55,justify=LEFT)
        self.num_ent.grid(row=0,column=0,columnspan=5)

#================Buttons======================================
        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = (eval(self.num_ent.get()))
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()

            elif text == "C":
                calc_var.set(" ")
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()


        self.btn1 = Button(self.calc_frame,bg="blue",text="7",bd=5,width=8,height=1,font=('arial',15))
        self.btn1.grid(row=1,column=0,pady=2)
        self.btn1.bind("<Button-1>", press_btn)
        self.btn2 = Button(self.calc_frame, bg="blue", text="8", bd=5, width=8, height=1,font=('arial',15))
        self.btn2.grid(row=1, column=1, pady=2)
        self.btn2.bind("<Button-1>", press_btn)
        self.btn3 = Button(self.calc_frame, bg="blue", text="9", bd=5, width=8, height=1,font=('arial',15))
        self.btn3.grid(row=1, column=2,  pady=2)
        self.btn3.bind("<Button-1>", press_btn)



        self.btnadd = Button(self.calc_frame, bg="blue", text="+", bd=5, width=8, height=1,font=('arial',15))
        self.btnadd.grid(row=1, column=3, pady=2)
        self.btnadd.bind("<Button-1>", press_btn)
        ##
        self.btn1 = Button(self.calc_frame, bg="blue", text="6", bd=5, width=8, height=1, font=('arial', 15))
        self.btn1.grid(row=2, column=0, pady=2)
        self.btn1.bind("<Button-1>", press_btn)
        self.btn2 = Button(self.calc_frame, bg="blue", text="5", bd=5, width=8, height=1, font=('arial', 15))
        self.btn2.grid(row=2, column=1, pady=2)
        self.btn2.bind("<Button-1>", press_btn)
        self.btn3 = Button(self.calc_frame, bg="blue", text="4", bd=5, width=8, height=1, font=('arial', 15))
        self.btn3.grid(row=2, column=2, pady=2)
        self.btn3.bind("<Button-1>", press_btn)
        self.btnadd = Button(self.calc_frame, bg="blue", text="-", bd=5, width=8, height=1, font=('arial', 15))
        self.btnadd.grid(row=2, column=3, pady=2)
        self.btnadd.bind("<Button-1>", press_btn)

        ##
        self.btn1 = Button(self.calc_frame, bg="blue", text="3", bd=5, width=8, height=1, font=('arial', 15))
        self.btn1.grid(row=3, column=0, pady=2)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2 = Button(self.calc_frame, bg="blue", text="2", bd=5, width=8, height=1, font=('arial', 15))
        self.btn2.grid(row=3, column=1, pady=2)
        self.btn2.bind("<Button-1>", press_btn)

        self.btn3 = Button(self.calc_frame, bg="blue", text="1", bd=5, width=8, height=1, font=('arial', 15))
        self.btn3.grid(row=3, column=2, pady=2)
        self.btn3.bind("<Button-1>", press_btn)

        self.btnadd = Button(self.calc_frame, bg="blue", text="*", bd=5, width=8, height=1, font=('arial', 15))
        self.btnadd.grid(row=3, column=3, pady=2)
        self.btnadd.bind("<Button-1>", press_btn)

        ##
        self.btn1 = Button(self.calc_frame, bg="blue", text="0", bd=5, width=8, height=1, font=('arial', 15))
        self.btn1.grid(row=4, column=0, pady=2)
        self.btn1.bind("<Button-1>", press_btn)

        self.btn2 = Button(self.calc_frame, bg="blue", text="C", bd=5, width=8, height=1, font=('arial', 15))
        self.btn2.grid(row=4, column=1, pady=2)
        self.btn2.bind("<Button-1>", press_btn)

        self.btn3 = Button(self.calc_frame, bg="blue", text="=", bd=5, width=8, height=1, font=('arial', 15))
        self.btn3.grid(row=4, column=2, pady=2)
        self.btn3.bind("<Button-1>", press_btn)

        self.btnadd = Button(self.calc_frame, bg="blue", text="/", bd=5, width=8, height=1, font=('arial', 15))
        self.btnadd.grid(row=4, column=3, pady=2)
        self.btnadd.bind("<Button-1>", press_btn)

        #======================================================================================================================
        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=('arial',18),bg="cadetblue",bd=8,relief=GROOVE)
        self.bill_frame.place(x=650,y=360,width=650,height=380)
        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="cadetblue",font=('arial',10),yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=True)

        default_bill()

#============================================================================================================
class Window2:
    def __init__(self, root):
        self.root = root
        self.root.title("Store ")
        self.root.geometry("1350x750+0+0")

        self.root.configure(background='cadetblue')

        Change_Input = StringVar()
        Cash_Input  =StringVar()
        SubTotal_Input = StringVar()
        Tax_Input = StringVar()
        Item_Input = StringVar()
        Total_Input = StringVar()
        Qty_Input = StringVar()
        Amount_Input = StringVar()
        choice_Input = StringVar()

        self.Coffe1 = PhotoImage(file = "coffee-gif-tumblr-12.gif")
        self.Coffe2 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Coffe3 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Coffe4 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Coffe5 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Coffe6 = PhotoImage(file="coffee-gif-tumblr-12.gif")

        self.Drink1 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Drink2 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Drink3 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Drink4 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Drink5 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Drink6 = PhotoImage(file="coffee-gif-tumblr-12.gif")

        self.Cake1 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Cake2 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Cake3 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Cake4 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Cake5 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.Cake6 = PhotoImage(file="coffee-gif-tumblr-12.gif")

        self.IceCake1 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.IceCake2 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.IceCake3 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.IceCake4 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.IceCake5 = PhotoImage(file="coffee-gif-tumblr-12.gif")
        self.IceCake6 = PhotoImage(file="coffee-gif-tumblr-12.gif")

        self.FedBurger = PhotoImage(file = "coffee-gif-tumblr-12.gif")
        self.Fries = PhotoImage(file="holiday-food-gif-2.gif")
        self.FishBurger = PhotoImage(file = "holiday-food-gif-2.gif")
        self.BreadRoll = PhotoImage(file="holiday-food-gif-2.gif")
        self.ChickenNuggets = PhotoImage(file="holiday-food-gif-2.gif")
        self.MeatPie = PhotoImage(file="holiday-food-gif-2.gif")
        self.MeatBalls = PhotoImage(file="holiday-food-gif-2.gif")

        #====================================Function ab button ki ==============================

        def delete() :
            ItemCost=0.0
            Tax=2.5
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost )))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))
                selected_item = (self.POS_records.selection()[0])
                self.POS_records.delete(selected_item)

        def giveChange():
            ItemCost = 0.0
            Tax = 2.5
            CashInput = float(Cash_Input.get())
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                Change_Input.set(str('£%.2f' % (CashInput - ((ItemCost) + (( ItemCost *Tax)/100)))))
                if(Cash_Input.get() == "0"):
                    Change_Input.set("")
                    Method_of_Pay()

        def iExit():
            iExit = tk.messagebox.askyesno("Point of Sale", "Do You Want To quit")
            if iExit > 0:
                root.destroy()
                return

        def Method_of_Pay():
            if(choice_Input.get() == "Cash"):
                self.txtCash.focus()
                Cash_Input.set("")
            elif (choice_Input.get() == ""):
                 Cash_Input.set("0")
                 Change_Input.set("")

        def iPrint():
            q = self.txtReceipt.get("1.0", "end-1c")
            print(q)
            filename = tempfile.mktemp(".txt")
            open(filename, "w").write(q)
            os.startfile(filename, "print")








        #=============================================================================================

        MainFrame = Frame(self.root,bg='cadetblue')
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame = Frame(MainFrame, bg='cadetblue',bd=5,width=1348,height=160,padx=4,pady=4,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bg='cadetblue', bd=5, width=800, height=300, padx=4, pady=4, relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFTCOVER = LabelFrame(DataFrame, bg='cadetblue', bd=5, width=800, height=300, padx=4, pady=4,font =('arial',12,'bold'),text ="point of sale", relief=RIDGE)
        DataFrameLEFTCOVER.pack(side=LEFT)

        ChangeButtonFrame = Frame(DataFrameLEFTCOVER,  bd=5, width=300, height=460, pady=4, relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT,padx=4)

        ReceiptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, padx=5, pady=1, relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT,padx=4)

        FoodItemFrame = LabelFrame(DataFrame, bg='cadetblue', bd=5, width=450, height=300, padx=5, pady=2,
                                        font=('arial', 12, 'bold'), text="items", relief=RIDGE)
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame, bd=5, width=500, height=140,  relief=RIDGE)
        CalFrame.grid(row = 0,column=0,padx=5)

        ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140,pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column=1, padx=5)

        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140,pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0, column=2, padx=5)
        #########################################
      #  def iPrint():
       #     q = self.txtReciept.get("1.0", "end-1c")
        #    print(q)
        #    filename = tempfile.mktemp(".txt")
         #   open(filename, "w").write(q)
          #  os.startfile(filename, "print")


        ###############################Entry & Lebel Widget#====================================

        self.lblSubTotal = Label(CalFrame, font=('arial', 12, 'bold'),text="Sub Total",bd=5)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5)
        self.txtSubTotal = Entry(CalFrame, font=('arial', 12, 'bold'), textvariable=SubTotal_Input, bd=2,width=24)
        self.txtSubTotal.grid(row=0, column=1, sticky=W, padx=5)

        self.lblTax = Label(CalFrame, font=('arial', 12, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)
        self.txtTax = Entry(CalFrame, font=('arial', 12, 'bold'), textvariable=Tax_Input, bd=2, width=24)
        self.txtTax.grid(row=1, column=1, sticky=W, padx=5)

        self.lblTotal = Label(CalFrame, font=('arial', 12, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(CalFrame, font=('arial', 12, 'bold'), textvariable=Total_Input, bd=2, width=24)
        self.txtTotal.grid(row=2, column=1, sticky=W, padx=5)


        ###############################Entry & Lebel Widget#====================================

        self.lblMoP = Label(ChangeFrame, font=('arial', 12, 'bold'), text="Payment Method", bd=5)
        self.lblMoP.grid(row=0, column=0, sticky=W, padx=5)
        self.cboMoP = ttk.Combobox(ChangeFrame, font=('arial', 12, 'bold'),  width=34,state='readonly',
                                   textvariable=choice_Input,justify=RIGHT)
        self.cboMoP['value'] = ('','Cash','Master Card')
        self.cboMoP.current(0)
        self.cboMoP.grid(row=0, column=1)

        self.lblCash = Label(ChangeFrame, font=('arial', 12, 'bold'), text="Cash", bd=5)
        self.lblCash.grid(row=1, column=0, sticky=W, padx=5)
        self.txtCash = Entry(ChangeFrame, font=('arial', 12, 'bold'), textvariable=Cash_Input, bd=2, width=36,justify=RIGHT)
        self.txtCash.grid(row=1, column=1, sticky=W, padx=5)
        self.txtCash.insert(0,"0")

        self.lblChange = Label(ChangeFrame, font=('arial', 12, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2, column=0, sticky=W, padx=5)
        self.txtChange = Entry(ChangeFrame, font=('arial', 12, 'bold'), textvariable=Change_Input, bd=2, width=36,justify=RIGHT)
        self.txtChange.grid(row=2, column=1, sticky=W, padx=5)

        ###############################Entry & Lebel Widget#====================================

        self.btnPay = Button(RemoveFrame,padx=2, font=('arial', 12, 'bold'), text="Pay", width=10,height=1,bd=2,command=giveChange)
        self.btnPay.grid(row=0, column=0, pady=2,padx=7)

        self.btnExit = Button(RemoveFrame, padx=2, font=('arial', 12, 'bold'), text="Exit", width=10, height=1, bd=2,command=iExit)
        self.btnExit.grid(row=0, column=1, pady=2, padx=7)

        self.btnReset = Button(RemoveFrame, padx=2, font=('arial', 12, 'bold'), text="Reset", width=10, height=1, bd=2,command=iPrint)
        self.btnReset.grid(row=1, column=0, pady=2, padx=7)

        self.btnRemoveItem = Button(RemoveFrame, padx=2, font=('arial', 12, 'bold'), text="Remove Item", width=10, height=1, bd=2,command=delete)
        self.btnRemoveItem.grid(row=1, column=1, pady=2, padx=7)

        #=======================Function bnao ab button k===============

        def Coffe1():
            ItemCost = 2.3
            Tax = 2.5
            self.POS_records.insert("", tk.END , values = ("Coffe Capp","1","2.3"))
            for child in self.POS_records.get_children():
                ItemCost +=float(self.POS_records.item(child,"values")[2])
                SubTotal_Input.set(str('£%.2f' %(ItemCost-2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 2.3)*Tax)/100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 2.3) + ((ItemCost-2.3)*Tax)/100)))

        def Coffe2():
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Coffe Capp", "1", "1.90"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.90) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.90) + ((ItemCost - 1.90) * Tax) / 100)))

        def Coffe3():
            ItemCost = 3.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Coffe Capp", "1", "3.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 3.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 3.2) + ((ItemCost - 3.2) * Tax) / 100)))

        def Coffe4():
            ItemCost = 5.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Coffe Capp", "1", "5.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 5.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 5.2) + ((ItemCost - 5.2) * Tax) / 100)))

        def Coffe5():
            ItemCost = 2.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Coffe Capp", "1", "2.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 2.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 2.2) + ((ItemCost - 2.2) * Tax) / 100)))

        def Coffe6():
            ItemCost = 6.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Coffe Capp", "1", "6.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 6.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 6.2) + ((ItemCost - 6.2) * Tax) / 100)))

        def Drink1():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Drink Special", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Drink2():
            ItemCost = 5
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Drink Special", "1", "5"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 5) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 5) + ((ItemCost - 5) * Tax) / 100)))

        def Drink3():
            ItemCost = 6.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Drink Special", "1", "6.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 6.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 6.2) + ((ItemCost - 6.2) * Tax) / 100)))

        def Drink4():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Drink Special", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Drink5():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Drink Special", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Drink6():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Drink Special", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Cake1():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))


        def Cake2():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Cake3():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Cake4():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Cake5():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def Cake6():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def IceCake1():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("IceCakee ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def IceCake2():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Cake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def IceCake3():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("IceCake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def IceCake4():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("IceCake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def IceCake5():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("IceCake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        def IceCake6():
            ItemCost = 4.2
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("IceCake ", "1", "4.2"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 2.3)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 4.2) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 4.2) + ((ItemCost - 4.2) * Tax) / 100)))

        #==============================Treeview widget=====================================

        scroll_x = Scrollbar(ReceiptFrame,orient = HORIZONTAL)
        scroll_y = Scrollbar(ReceiptFrame, orient=VERTICAL)

        self.POS_records = ttk.Treeview(ReceiptFrame, height=20, columns=("Item", "Qty", "Amount"),
                                        xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_records.heading("Item",text="Item")
        self.POS_records.heading("Qty", text="Qty")
        self.POS_records.heading("Amount", text="Amount")

        self.POS_records['show'] = 'headings'

        self.POS_records.column("Item", width=120)
        self.POS_records.column("Qty", width=100)
        self.POS_records.column("Amount", width=100)

        self.POS_records.pack(fill=BOTH,expand=1)
        self.POS_records.bind("<ButtonRelease=1>")
        self.txtReceipt = Text(ReceiptFrame,width=79,height=1,font=('arial',5,'bold'))
        self.txtReceipt.pack()
        self.txtReceipt.insert(END,"item\t\t\t\t Qty\t\t\t Amount\t\n")



        ###############################Button  Wiget#====================================

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, image =self.FedBurger, width=104, height=104, bd=2)
        self.btnFedBurger.grid(row=0, column=0, pady=2, padx=4)

        self.btnFries = Button(ChangeButtonFrame, padx=2, image=self.Fries, width=104, height=104, bd=2)
        self.btnFries.grid(row=0, column=1, pady=2, padx=4)

        self.btnFishBurger = Button(ChangeButtonFrame, padx=2, image=self.FishBurger, width=104, height=104, bd=2)
        self.btnFishBurger.grid(row=1, column=0, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2)
        self.btnFedBurger.grid(row=1, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2)
        self.btnFedBurger.grid(row=2, column=0, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2)
        self.btnFedBurger.grid(row=2, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2)
        self.btnFedBurger.grid(row=3, column=0, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2)
        self.btnFedBurger.grid(row=3, column=1, pady=2, padx=4)

        ###############################Button  Widget#====================================

        self.btnCoffe1 = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Coffe1)
        self.btnCoffe1.grid(row=0, column=0, pady=2, padx=4)

        self.btnFries = Button(FoodItemFrame, padx=2, image=self.Fries, width=104, height=104, bd=2,command =Coffe2)
        self.btnFries.grid(row=0, column=1, pady=2, padx=4)

        self.btnFishBurger = Button(FoodItemFrame, padx=2, image=self.FishBurger, width=104, height=104, bd=2,command =Coffe3)
        self.btnFishBurger.grid(row=0, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command =Coffe4)
        self.btnFedBurger.grid(row=0, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command =Coffe5)
        self.btnFedBurger.grid(row=0, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command =Coffe6)
        self.btnFedBurger.grid(row=0, column=5, pady=2, padx=4)

        ###############################Button  Widget#====================================

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Drink1)
        self.btnFedBurger.grid(row=1, column=0, pady=2, padx=4)

        self.btnFries = Button(FoodItemFrame, padx=2, image=self.Fries, width=104, height=104, bd=2,command=Drink2)
        self.btnFries.grid(row=1, column=1, pady=2, padx=4)

        self.btnFishBurger = Button(FoodItemFrame, padx=2, image=self.FishBurger, width=104, height=104, bd=2,command=Drink3)
        self.btnFishBurger.grid(row=1, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Drink4)
        self.btnFedBurger.grid(row=1, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Drink5)
        self.btnFedBurger.grid(row=1, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Drink6)
        self.btnFedBurger.grid(row=1, column=5, pady=2, padx=4)

        ###############################Button  Widget#====================================

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Cake1)
        self.btnFedBurger.grid(row=2, column=0, pady=2, padx=4)

        self.btnFries = Button(FoodItemFrame, padx=2, image=self.Fries, width=104, height=104, bd=2,command=Cake2)
        self.btnFries.grid(row=2, column=1, pady=2, padx=4)

        self.btnFishBurger = Button(FoodItemFrame, padx=2, image=self.FishBurger, width=104, height=104, bd=2,command=Cake3)
        self.btnFishBurger.grid(row=2, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Cake4)
        self.btnFedBurger.grid(row=2, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Cake5)
        self.btnFedBurger.grid(row=2, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=Cake6)
        self.btnFedBurger.grid(row=2, column=5, pady=2, padx=4)

        ###############################Button  Widget#====================================

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=IceCake1)
        self.btnFedBurger.grid(row=3, column=0, pady=2, padx=4)

        self.btnFries = Button(FoodItemFrame, padx=2, image=self.Fries, width=104, height=104, bd=2,command=IceCake2)
        self.btnFries.grid(row=3, column=1, pady=2, padx=4)

        self.btnFishBurger = Button(FoodItemFrame, padx=2, image=self.FishBurger, width=104, height=104, bd=2,command=IceCake3)
        self.btnFishBurger.grid(row=3, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=IceCake4)
        self.btnFedBurger.grid(row=3, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=IceCake5)
        self.btnFedBurger.grid(row=3, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, image=self.FedBurger, width=104, height=104, bd=2,command=IceCake6)
        self.btnFedBurger.grid(row=3, column=5, pady=2, padx=4)


if __name__ == '__main__' :
    #root = Tk()
    #application = POS(root)
    #root.mainloop()

    main()
