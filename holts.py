import tkinter as tk 
from tkinter import ttk
from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
  
LARGEFONT =("Verdana", 30)
TITLEFONT = ("Verdana", 20)
HEADING = ("Verdana", 15)
HEADING1 = ("Verdana", 10)
HEADING2 = ("Verdana", 8)
   
class holts(tk.Tk): 
      
    # __init__ function for class holts  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Holts Distributors')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
          
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1)
   
        # initializing frames to an empty array 
        self.frames = {}   
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (territories, sales_reps, customers, parts, vendors, orders, open_orders, invoices, reports): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row=0, column=0, sticky ="nsew") 
   
        self.show_frame(territories) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
   
# first window frame startpage 
   
class territories(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        
        label = Label(self, text ="TERRITORIES", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Search Territories', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = "Territory:", font = HEADING)
        label3.grid(row=3, column=1, columnspan = 5, sticky=W, pady=10)

        OPTIONS = ['North1', 'North2', 'South1', 'South2', 'East1', 'East2', 'East3', 'West1', 'West2', 'West3']

        variable = StringVar()
        variable.set('Choose a Territory')

        options = OptionMenu(self, variable, *OPTIONS)
        options.grid(row=4, column=1, columnspan=5, sticky=W, pady=10, ipadx=50)
    
        def getTerritories():
            con = mysql.connect(host='localhost', user='root', password='Helenli510', database='holts')
            cursor = con.cursor()
            
            cursor.execute(" SELECT TERRITORY.TERRITORY_NUM AS TERRITORY_NUMBER, \
                TERRITORY.TERRITORY_NAME AS TERRITORY_NAME, SALES_REP.SALES_REP_ID AS SALES_REP_NUMBER, \
                SALES_REP.SALES_REP_NAME AS SALES_REP_NAME, \
                CONCAT(SALES_REP.SALES_REP_ADDRESS, SALES_REP.SALES_REP_CITY, SALES_REP.SALES_REP_STATE, SALES_REP.SALES_REP_ZIP) AS SALES_REP_ADDRESS, \
                CUSTOMER.CUSTOMER_NUM AS CUSTOMER_NUMBER, CUSTOMER.CUSTOMER_NAME AS CUSTOMER_NAME, \
                CONCAT(CUSTOMER.CUSTOMER_ADDRESS1, CUSTOMER.CUSTOMER_ADDRESS2, CUSTOMER.CUSTOMER_CITY, CUSTOMER.CUSTOMER_STATE, CUSTOMER.CUSTOMER_ZIP) AS CUSTOMER_ADDRESS \
                \
                FROM TERRITORY, SALES_REP, CUSTOMER \
                \
                WHERE TERRITORY.TERRITORY_NAME='"+variable.get()+"'AND TERRITORY.TERRITORY_NUM = SALES_REP.TERRITORY_NUM \
                AND SALES_REP.SALES_REP_ID = CUSTOMER.SALES_REP_ID ORDER BY TERRITORY.TERRITORY_NUM ASC")
            
            
            records = cursor.fetchall()

            '''
            print_records = ''
            for record in records:
                print_records += str(record) +"\n"

            query_label = Label(self, text=print_records)
            query_label.grid(row=6, column=1, columnspan=8)
            '''

            w=tk.Tk()
            w.title('Territory List')
            w.geometry('1500x600')

            cols=['Territory Num', 'Territory Name', 'Sales Rep Num', 'Sales Rep Name', 'Sales Rep Address', 'Customer Num', 'Customer Name', 'Customer Address']

            for y in range(len(records)+1):
                for x in range(len(cols)):
                    if y==0:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y, padx = 1)
                        e.insert(0,cols[x])
                    else:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y, padx = 1)
                        e.insert(0,records[y-1][x])
            
            con.commit()
            con.close()

        button10 = Button(self, text ="Search", command=getTerritories)
        button10.grid(row = 5, column = 1, columnspan = 9, sticky = E, ipadx = 10, pady = 10)
    

class sales_reps(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="SALES REPS", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Add/Edit Sales Rep', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = "Name:", font = HEADING)
        label3.grid(row=3, column=1, columnspan = 4, sticky=W, pady=10)

        label4 = Label(self, text = "Address:", font = HEADING)
        label4.grid(row=5, column=1, columnspan = 4, sticky=W, pady=10)

        label5 = Label(self, text = "City:", font = HEADING)
        label5.grid(row=7, column=1, columnspan = 4, sticky=W, pady=10)

        label6 = Label(self, text = "State:", font = HEADING)
        label6.grid(row=9, column=1, columnspan = 4, sticky=W, pady=10)

        label7 = Label(self, text = "Zip:", font = HEADING)
        label7.grid(row=11, column=1, columnspan = 4, sticky=W, pady=10)

        label8 = Label(self, text = "MTD Sales:", font = HEADING)
        label8.grid(row=13, column=1, columnspan = 4, sticky=W, pady=10)

        label9 = Label(self, text = "YTD Sales:", font = HEADING)
        label9.grid(row=3, column=6, columnspan = 4, sticky=W, pady=10)

        label10 = Label(self, text = "MTD Commission:", font = HEADING)
        label10.grid(row=5, column=6, columnspan = 4, sticky=W, pady=10)

        label11 = Label(self, text = "YTD Commission:", font = HEADING)
        label11.grid(row=7, column=6, columnspan = 4, sticky=W, pady=10)

        label12 = Label(self, text = "Commission rate:", font = HEADING)
        label12.grid(row=9, column=6, columnspan = 4, sticky=W, pady=10)

        label13 = Label(self, text = "Territory:", font = HEADING)
        label13.grid(row=11, column=6, columnspan = 4, sticky=W, pady=10)

        s_name = Entry(self, width=30)
        s_name.grid(row=4, column=1, columnspan = 4, ipadx=50)

        s_add = Entry(self, width=30)
        s_add.grid(row=6, column=1, columnspan = 4, ipadx=50)

        s_city = Entry(self, width=30)
        s_city.grid(row=8, column=1,columnspan = 4,  ipadx=50)

        s_state = Entry(self, width=30)
        s_state.grid(row=10, column=1,columnspan = 4,  ipadx=50)

        s_zip = Entry(self, width=30)
        s_zip.grid(row=12, column=1, columnspan = 4, ipadx=50)

        s_mtdsales = Entry(self, width=30)
        s_mtdsales.grid(row=14, column=1,columnspan = 4,  ipadx=50)

        s_ytdsales = Entry(self, width=30)
        s_ytdsales.grid(row=4, column=6,columnspan = 4,  ipadx=50)

        s_mtdcom = Entry(self, width=30)
        s_mtdcom.grid(row=6, column=6,columnspan = 4,  ipadx=50)

        s_ytdcom = Entry(self, width=30)
        s_ytdcom.grid(row=8, column=6, columnspan = 4, ipadx=50)

        s_comrate = Entry(self, width=30)
        s_comrate.grid(row=10, column=6,columnspan = 4,  ipadx=50)

        OPTIONS = ['North1', 'North2', 'South1', 'South2', 'East1', 'East2', 'East3', 'West1', 'West2', 'West3']

        variable = StringVar()
        variable.set('Choose a Territory')

        options = OptionMenu(self, variable, *OPTIONS)
        options.grid(row=12, column=6, columnspan=4, sticky=W, pady=10, ipadx=50)

        button10 = Button(self, text ="Add")
        button10.grid(row = 14, column = 6, sticky ='', ipadx = 10, ipady = 7)

        button11 = Button(self, text ="Update")
        button11.grid(row = 14, column = 7, sticky ='', ipadx = 10, ipady = 7)

        button12 = Button(self, text ="Delete")
        button12.grid(row = 14, column = 8, sticky ='', ipadx = 10, ipady = 7)



        def getReps():
            con = mysql.connect(host='localhost', user='root', password='Helenli510', database='holts')
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM SALES_REP ORDER BY SALES_REP_ID ASC")
            
            records = cursor.fetchall()
 
            w=tk.Tk()
            w.title('Sales Rep List')
            w.geometry('1500x600')

            cols=['Sales Rep Num', 'Sales Rep Name', 'Address', 'City', 'State', 'Zip', 'MTD Sales', 'YTD Sales', 'MTD Commission', 'YTD Commission', 'Commission Rate', 'Territory Num']

            for y in range(len(records)+1):
                for x in range(len(cols)):
                    if y==0:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y, padx = 1)
                        e.insert(0,cols[x])
                    else:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y, padx = 1)
                        e.insert(0,records[y-1][x])
            
            con.commit()
            con.close()

        button13 = Button(self, text ="Show All", command = getReps)
        button13.grid(row = 14, column = 9, sticky ='', ipadx = 10, ipady = 7)

        """
        def getReps():
            con = mysql.connect(host='localhost', user='root', password='Helenli510', database='holts')
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM SALES_REP ORDER BY SALES_REP_IN ASC")
            
            records = cursor.fetchall()
            print_records = ''
            for record in records:
                print_records += str(record) +"\n"

            query_label = Label(self, text=print_records)
            query_label.grid(row=6, column=1, columnspan=8)
            
            con.commit()
            con.close()
        """



class customers(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="CUSTOMERS", font = TITLEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 6, ipady = 6) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 6, ipady = 6) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 6, ipady = 6) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 6, ipady = 6)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 6, ipady = 6) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 6, ipady = 6)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 6, ipady = 6) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 6, ipady = 6)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 6, pady = 6)

        label2 = Label(self, text = 'Add/Edit New Customer', font = HEADING)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 8)

        label3 = Label(self, text = "Name:", font = HEADING2)
        label3.grid(row=3, column=1, columnspan = 4, sticky=W, pady=8)

        label4 = Label(self, text = "Address 1:", font = HEADING2)
        label4.grid(row=5, column=1, columnspan = 4, sticky=W, pady=8)

        label14 = Label(self, text = "Address 2:", font = HEADING2)
        label14.grid(row=7, column=1, columnspan = 4, sticky=W, pady=8)

        label5 = Label(self, text = "City:", font = HEADING2)
        label5.grid(row=9, column=1, columnspan = 4, sticky=W, pady=8)

        label6 = Label(self, text = "State:", font = HEADING2)
        label6.grid(row=11, column=1, columnspan = 4, sticky=W, pady=8)

        label7 = Label(self, text = "Zip:", font = HEADING2)
        label7.grid(row=13, column=1, columnspan = 4, sticky=W, pady=8)

        label8 = Label(self, text = "MTD Sales:", font = HEADING2)
        label8.grid(row=15, column=1, columnspan = 4, sticky=W, pady=8)

        label9 = Label(self, text = "YTD Sales:", font = HEADING2)
        label9.grid(row=17, column=1, columnspan = 4, sticky=W, pady=8)

        label10 = Label(self, text = "Current Balance:", font = HEADING2)
        label10.grid(row=19, column=1, columnspan = 4, sticky=W, pady=8)

        label11 = Label(self, text = "Credit Limit:", font = HEADING2)
        label11.grid(row=21, column=1, columnspan = 4, sticky=W, pady=8)

        label25 = Label(self, text = "Territory:", font = HEADING2)
        label25.grid(row=23, column=1, columnspan = 4, sticky=W, pady=8)

        label15 = Label(self, text = "Shipping Name:", font = HEADING2)
        label15.grid(row=3, column=6, columnspan = 4, sticky=W, pady=8)

        label16 = Label(self, text = "Shipping Address 1:", font = HEADING2)
        label16.grid(row=5, column=6, columnspan = 4, sticky=W, pady=8)

        label17 = Label(self, text = "Shipping Address 2:", font = HEADING2)
        label17.grid(row=7, column=6, columnspan = 4, sticky=W, pady=8)

        label18 = Label(self, text = "Shipping City:", font = HEADING2)
        label18.grid(row=9, column=6, columnspan = 4, sticky=W, pady=8)

        label19 = Label(self, text = "Shipping State:", font = HEADING2)
        label19.grid(row=11, column=6, columnspan = 4, sticky=W, pady=8)

        label20 = Label(self, text = "Shipping Zip:", font = HEADING2)
        label20.grid(row=13, column=6, columnspan = 4, sticky=W, pady=8)

        label21 = Label(self, text = "Invoice Total:", font = HEADING2)
        label21.grid(row=15, column=6, columnspan = 4, sticky=W, pady=8)

        label22 = Label(self, text = "Payment Total:", font = HEADING2)
        label22.grid(row=17, column=6, columnspan = 4, sticky=W, pady=8)

        label23 = Label(self, text = "Current Amount:", font = HEADING2)
        label23.grid(row=19, column=6, columnspan = 4, sticky=W, pady=8)

        label24 = Label(self, text = "Previous Balance:", font = HEADING2)
        label24.grid(row=21, column=6, columnspan = 4, sticky=W, pady=8)


        c_name = Entry(self, width=25)
        c_name.grid(row=4, column=1, columnspan = 4, ipadx=50)

        c_add1 = Entry(self, width=25)
        c_add1.grid(row=6, column=1, columnspan = 4, ipadx=50)

        c_add2 = Entry(self, width=25)
        c_add2.grid(row=8, column=1, columnspan = 4, ipadx=50)
        
        c_city = Entry(self, width=25)
        c_city.grid(row=10, column=1,columnspan = 4,  ipadx=50)

        c_state = Entry(self, width=25)
        c_state.grid(row=12, column=1,columnspan = 4,  ipadx=50)

        c_zip = Entry(self, width=25)
        c_zip.grid(row=14, column=1, columnspan = 4, ipadx=50)

        c_mtdsales = Entry(self, width=25)
        c_mtdsales.grid(row=16, column=1,columnspan = 4,  ipadx=50)

        c_ytdsales = Entry(self, width=25)
        c_ytdsales.grid(row=18, column=1,columnspan = 4,  ipadx=50)

        c_currbal = Entry(self, width=25)
        c_currbal.grid(row=20, column=1,columnspan = 4,  ipadx=50)

        c_credlim = Entry(self, width=25)
        c_credlim.grid(row=22, column=1, columnspan = 4, ipadx=50)

        OPTIONS = ['North1', 'North2', 'South1', 'South2', 'East1', 'East2', 'East3', 'West1', 'West2', 'West3']

        variable = StringVar()
        variable.set('Choose a Territory')

        options = OptionMenu(self, variable, *OPTIONS)
        options.grid(row=24, column=1, columnspan=4, sticky=W, pady=8, ipadx=50)

        s_sname = Entry(self, width=25)
        s_sname.grid(row=4, column=6, columnspan = 4, ipadx=50)

        s_sadd1 = Entry(self, width=25)
        s_sadd1.grid(row=6, column=6, columnspan = 4, ipadx=50)

        s_sadd2 = Entry(self, width=25)
        s_sadd2.grid(row=8, column=6, columnspan = 4, ipadx=50)
        
        s_scity = Entry(self, width=25)
        s_scity.grid(row=10, column=6,columnspan = 4,  ipadx=50)

        s_sstate = Entry(self, width=25)
        s_sstate.grid(row=12, column=6,columnspan = 4,  ipadx=50)

        s_szip = Entry(self, width=25)
        s_szip.grid(row=14, column=6, columnspan = 4, ipadx=50)

        s_invoice = Entry(self, width=25)
        s_invoice.grid(row=16, column=6,columnspan = 4,  ipadx=50)

        s_payment = Entry(self, width=25)
        s_payment.grid(row=18, column=6,columnspan = 4,  ipadx=50)

        s_curramount = Entry(self, width=25)
        s_curramount.grid(row=20, column=6,columnspan = 4,  ipadx=50)

        s_prevbal = Entry(self, width=25)
        s_prevbal.grid(row=22, column=6, columnspan = 4, ipadx=50)

        def popup():
            MessageBox.showinfo("Error", "Name is required for adding a new customer")

        button10 = Button(self, text ="Add")
        button10.grid(row = 24, column = 6, sticky ='', ipadx = 10, ipady = 7)

        button11 = Button(self, text ="Update", command=popup)
        button11.grid(row = 24, column = 7, sticky ='', ipadx = 10, ipady = 7)

        button12 = Button(self, text ="Delete")
        button12.grid(row = 24, column = 8, sticky ='', ipadx = 10, ipady = 7)

        button13 = Button(self, text ="Show All")
        button13.grid(row = 24, column = 9, sticky ='', ipadx = 10, ipady = 7)

        

class parts(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="PARTS", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Add/Edit New Part', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = "Part Description:", font = HEADING)
        label3.grid(row=3, column=1, columnspan = 4, sticky=W, pady=10)

        label4 = Label(self, text = "Unit Price:", font = HEADING)
        label4.grid(row=5, column=1, columnspan = 4, sticky=W, pady=10)

        label5 = Label(self, text = "MTD Sales:", font = HEADING)
        label5.grid(row=7, column=1, columnspan = 4, sticky=W, pady=10)

        label6 = Label(self, text = "YTD Sales:", font = HEADING)
        label6.grid(row=9, column=1, columnspan = 4, sticky=W, pady=10)

        label7 = Label(self, text = "Units on Hand:", font = HEADING)
        label7.grid(row=3, column=6, columnspan = 4, sticky=W, pady=10)

        label8 = Label(self, text = "Units Allocated:", font = HEADING)
        label8.grid(row=5, column=6, columnspan = 4, sticky=W, pady=10)

        label9 = Label(self, text = "Reorder Point:", font = HEADING)
        label9.grid(row=7, column=6, columnspan = 4, sticky=W, pady=10)

        p_desc = Entry(self, width=30)
        p_desc.grid(row=4, column=1, columnspan = 4, ipadx=50)

        p_price = Entry(self, width=30)
        p_price.grid(row=6, column=1, columnspan = 4, ipadx=50)

        p_mtdsales = Entry(self, width=30)
        p_mtdsales.grid(row=8, column=1,columnspan = 4,  ipadx=50)

        p_ytdsales = Entry(self, width=30)
        p_ytdsales.grid(row=10, column=1,columnspan = 4,  ipadx=50)

        p_onhand = Entry(self, width=30)
        p_onhand.grid(row=4, column=6, columnspan = 4, ipadx=50)

        p_allocated = Entry(self, width=30)
        p_allocated.grid(row=6, column=6,columnspan = 4,  ipadx=50)

        p_reorder = Entry(self, width=30)
        p_reorder.grid(row=8, column=6,columnspan = 4,  ipadx=50)

        button10 = Button(self, text ="Add")
        button10.grid(row = 10, column = 6, sticky ='', ipadx = 10, ipady = 7)

        button11 = Button(self, text ="Update")
        button11.grid(row = 10, column = 7, sticky ='', ipadx = 10, ipady = 7)

        button12 = Button(self, text ="Delete")
        button12.grid(row = 10, column = 8, sticky ='', ipadx = 10, ipady = 7)


        def getParts():
            con = mysql.connect(host='localhost', user='root', password='Helenli510', database='holts')
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM PART ORDER BY PART_NUM ASC")
            
            records = cursor.fetchall()
 
            w=tk.Tk()
            w.title('Parts List')
            w.geometry('1500x600')

            cols=['Part Num', 'Part Description', 'Unit Price', 'MTD Sales', 'YTD Sales', 'Units On Hand', 'Units Allocated', 'Reorder Point', '']

            for y in range(len(records)+1):
                for x in range(len(cols)):
                    if y==0:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y, padx = 1)
                        e.insert(0,cols[x])
                    else:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y, padx = 1)
                        e.insert(0,records[y-1][x])
            
            con.commit()
            con.close()
            
        button13 = Button(self, text ="Show All", command=getParts)
        button13.grid(row = 10, column = 9, sticky ='', ipadx = 10, ipady = 7)


class vendors(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="VENDORS", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Add/Edit New Vendor', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = "Name:", font = HEADING)
        label3.grid(row=3, column=1, columnspan = 4, sticky=W, pady=10)

        label4 = Label(self, text = "Address:", font = HEADING)
        label4.grid(row=5, column=1, columnspan = 4, sticky=W, pady=10)

        label5 = Label(self, text = "City:", font = HEADING)
        label5.grid(row=7, column=1, columnspan = 4, sticky=W, pady=10)

        label6 = Label(self, text = "State:", font = HEADING)
        label6.grid(row=9, column=1, columnspan = 4, sticky=W, pady=10)

        label7 = Label(self, text = "Zip:", font = HEADING)
        label7.grid(row=11, column=1, columnspan = 4, sticky=W, pady=10)

        v_name = Entry(self, width=30)
        v_name.grid(row=4, column=1, columnspan = 4, ipadx=50)

        v_add = Entry(self, width=30)
        v_add.grid(row=6, column=1, columnspan = 4, ipadx=50)

        v_city = Entry(self, width=30)
        v_city.grid(row=8, column=1,columnspan = 4,  ipadx=50)

        v_state = Entry(self, width=30)
        v_state.grid(row=10, column=1,columnspan = 4,  ipadx=50)

        v_zip = Entry(self, width=30)
        v_zip.grid(row=12, column=1, columnspan = 4, ipadx=50)

        button10 = Button(self, text ="Add")
        button10.grid(row = 12, column = 6, sticky ='', ipadx = 10, ipady = 7)

        button11 = Button(self, text ="Update")
        button11.grid(row = 12, column = 7, sticky ='', ipadx = 10, ipady = 7)

        button12 = Button(self, text ="Delete")
        button12.grid(row = 12, column = 8, sticky ='', ipadx = 10, ipady = 7)

        button13 = Button(self, text ="Show All")
        button13.grid(row = 12, column = 9, sticky ='', ipadx = 10, ipady = 7)
 
class orders(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="ORDERS", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Add/Edit Orders', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = "Number:", font = HEADING)
        label3.grid(row=3, column=1, columnspan = 4, sticky=W, pady=10)

        label4 = Label(self, text = "Date:", font = HEADING)
        label4.grid(row=5, column=1, columnspan = 4, sticky=W, pady=10)

        label5 = Label(self, text = "Comments:", font = HEADING)
        label5.grid(row=7, column=1, columnspan = 4, sticky=W, pady=10)

        label6 = Label(self, text = "PO Number:", font = HEADING)
        label6.grid(row=9, column=1, columnspan = 4, sticky=W, pady=10)

        label7 = Label(self, text = "Customer Number:", font = HEADING)
        label7.grid(row=11, column=1, columnspan = 4, sticky=W, pady=10)

        label8 = Label(self, text = "Add Item:", font = HEADING)
        label8.grid(row=3, column=6, columnspan = 4, sticky=W, pady=10)

        label9 = Label(self, text = "Quantity:", font = HEADING)
        label9.grid(row=5, column=6, columnspan = 4, sticky=W, pady=10) 

        o_name = Entry(self, width=30)
        o_name.grid(row=4, column=1, columnspan = 4, ipadx=50)

        o_add = Entry(self, width=30)
        o_add.grid(row=6, column=1, columnspan = 4, ipadx=50)

        o_city = Entry(self, width=30)
        o_city.grid(row=8, column=1,columnspan = 4,  ipadx=50)

        o_state = Entry(self, width=30)
        o_state.grid(row=10, column=1,columnspan = 4,  ipadx=50)

        o_zip = Entry(self, width=30)
        o_zip.grid(row=12, column=1, columnspan = 4, ipadx=50)

        o_qty = Entry(self, width=30)
        o_qty.grid(row=6, column=6, columnspan = 4, ipadx=50)


        button10 = Button(self, text ="Add")
        button10.grid(row = 14, column = 6, sticky ='', ipadx = 10, ipady = 7)

        button11 = Button(self, text ="Update")
        button11.grid(row = 14, column = 7, sticky ='', ipadx = 10, ipady = 7)

        button12 = Button(self, text ="Delete")
        button12.grid(row = 14, column = 8, sticky ='', ipadx = 10, ipady = 7)

        button13 = Button(self, text ="Show All")
        button13.grid(row = 14, column = 9, sticky ='', ipadx = 10, ipady = 7)

        OPTIONS = ['T-Shirt', 'Sweatpant', 'Jacket', 'Coat', 'Jeans', 'Backpack', 'Wallet', 'Dress', 'Hoodie', 'Sneaker']

        variable = StringVar()
        variable.set('Choose an Item')

        options = OptionMenu(self, variable, *OPTIONS)
        options.grid(row=4, column=6, columnspan=4, sticky=W, pady=10, ipadx=50)

        def addItems():
            label10 = Label(self, text = "Add Item:", font = HEADING)
            label10.grid(row=7, column=6, columnspan = 4, sticky=W, pady=10) 

            OPTIONS = ['T-Shirt', 'Sweatpant', 'Jacket', 'Coat', 'Jeans', 'Backpack', 'Wallet', 'Dress', 'Hoodie', 'Sneaker']

            variable = StringVar()
            variable.set('Choose an Item')

            options = OptionMenu(self, variable, *OPTIONS)
            options.grid(row=8, column=6, columnspan=4, sticky=W, pady=10, ipadx=50)

            label11 = Label(self, text = "Quantity:", font = HEADING)
            label11.grid(row=9, column=6, columnspan = 4, sticky=W, pady=10)

            o_qty2 = Entry(self, width=30)
            o_qty2.grid(row=10, column=6, columnspan = 4, ipadx=50)

        button14 = Button(self, text ="Add More Items", command=addItems)
        button14.grid(row = 13, column = 9, sticky =W, ipadx = 10, ipady = 7)


class open_orders(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="OPEN ORDERS", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Open Orders', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)



        def openOrders():
            con = mysql.connect(host='localhost', user='root', password='Helenli510', database='holts')
            cursor = con.cursor()
                    
            cursor.execute("SELECT DISTINCT ORDERS.ORDER_NUM, ORDERS.ORDER_DATE, ORDERS.ORDER_COMMENTS, ORDERS.CUSTOMER_PO_NUM, ORDERS.CUSTOMER_NUM, ORDERS.SPECIAL_CHARGE_NUM \
                \
                FROM ORDERS, CUSTOMER, SPECIAL_CHARGES \
                \
                WHERE CUSTOMER.CUSTOMER_NUM = ORDERS.CUSTOMER_NUM AND ORDERS.ORDER_STATUS = 'OPEN' ORDER BY CUSTOMER.CUSTOMER_NUM ASC;")
                    
                    
            records = cursor.fetchall()

            cols=['Order Num', 'Order Date', 'Comments', 'PO Num', 'Customer Num', 'Special Charges']

            w=tk.Tk()
            w.title('Open Orders')
            w.geometry('1500x600')

            for y in range(len(records)+1):
                for x in range(len(cols)):
                    if y==0:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y+3, padx = 1)
                        e.insert(0,cols[x])
                    else:
                        e=tk.Entry(w, width = 17)
                        e.grid(column=x, row=y+3, padx = 1)
                        e.insert(0,records[y-1][x])
                    
            con.commit()
            con.close()

        button10 = Button(self, text ="Show Open Orders", 
        command = openOrders)
        button10.grid(row = 3, column = 1, columnspan = 9, sticky = '', padx = 10, pady = 10)

class invoices(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="INVOICES", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'Invoices', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = 'Select Invoice', font = HEADING)
        label3.grid(row = 3, column = 1, columnspan = 9, sticky='', pady = 10)


        OPTIONS = ['17', '18', '19', '20', '21', '22', '23', '24']

        variable = StringVar()
        variable.set('Choose an Invoice')

        options = OptionMenu(self, variable, *OPTIONS)
        options.grid(row=4, column=1, columnspan=9, sticky='', pady=10, ipadx=50)

        button10 = Button(self, text ="Show Invoice")
        button10.grid(row = 5, column = 7, sticky = '', padx = 10, pady = 10)


class reports(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = Label(self, text ="REPORTS", font = LARGEFONT)
        label.grid(row=0, column=1, columnspan = 9, sticky = '', padx=10, pady=10)

       
        button1 = Button(self, text ="Territories", 
        command = lambda : controller.show_frame(territories), bg='white') 
        button1.grid(row = 1, column = 1, sticky = '', ipadx = 10, ipady = 10) 
   
        button2 = Button(self, text ="Sales Reps", 
        command = lambda : controller.show_frame(sales_reps), bg='white') 
        button2.grid(row = 1, column = 2, sticky = '', ipadx = 10, ipady = 10) 
        
        button3 = Button(self, text ="Customers", 
        command = lambda : controller.show_frame(customers), bg='white')
        button3.grid(row = 1, column = 3, sticky = '', ipadx = 10, ipady = 10) 
    
        button4 = Button(self, text ="Parts", 
        command = lambda : controller.show_frame(parts), bg='white')
        button4.grid(row = 1, column = 4, sticky = '', ipadx = 10, ipady = 10)

        button5 = Button(self, text ="Vendors", 
        command = lambda : controller.show_frame(vendors), bg='white')
        button5.grid(row = 1, column = 5, sticky = '', ipadx = 10, ipady = 10) 

        button6 = Button(self, text ="Orders", 
        command = lambda : controller.show_frame(orders), bg='white')
        button6.grid(row = 1, column = 6, sticky = '', ipadx = 10, ipady = 10)    

        button7 = Button(self, text ="Open Orders", 
        command = lambda : controller.show_frame(open_orders), bg='white')
        button7.grid(row = 1, column = 7, sticky = '', ipadx = 10, ipady = 10) 

        button8 = Button(self, text ="Invoices", 
        command = lambda : controller.show_frame(invoices), bg='white')
        button8.grid(row = 1, column = 8, sticky = '', ipadx = 10, ipady = 10)

        button9 = Button(self, text ="Reports", 
        command = lambda : controller.show_frame(reports))
        button9.grid(row = 1, column = 9, sticky = '', padx = 10, pady = 10)

        label2 = Label(self, text = 'See Reports', font = TITLEFONT)
        label2.grid(row = 2, column = 1, columnspan = 9, sticky='', pady = 10)

        label3 = Label(self, text = 'Download Reports', font = HEADING)
        label3.grid(row = 3, column = 1, columnspan = 9, sticky='', pady = 10)

        button10 = Button(self, text ="Open Orders by Customers")
        button10.grid(row = 4, column = 1, columnspan = 9, sticky = '', padx = 10, pady = 10)

        button11 = Button(self, text ="Open Orders By Part")
        button11.grid(row = 5, column = 1, columnspan = 9, sticky = '', padx = 10, pady = 10)

        button12 = Button(self, text ="Daily Cash Reports")
        button12.grid(row = 6, column = 1, columnspan = 9, sticky = '', padx = 10, pady = 10)

        button13 = Button(self, text ="Daily Invoices")
        button13.grid(row = 7, column = 1, columnspan = 9, sticky = '', padx = 10, pady = 10)

        button14 = Button(self, text ="Customer Monthly Reports")
        button14.grid(row = 8, column = 1, columnspan = 9, sticky = '', padx = 10, pady = 10)
 

   
# Driver Code 
app = holts() 
app.mainloop() 
