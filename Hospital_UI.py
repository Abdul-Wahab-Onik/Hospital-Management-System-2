from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import date


import mysql.connector
class LoginUI:
    def __init__(self,login_window):
        self.login_window=login_window
        self.login_window.title('LOGIN USER INTERFACE')
        self.login_window.geometry('600x500')
        self.login_window.resizable(FALSE,FALSE)
        self.login_window.config(bg='#3daaf6')
        title_label=Label(self.login_window,text='HEALTH CARE PRIVATE HOSPITAL',font=('Times New Roman',20,'bold'),bg='#3daaf6').pack()
        login_frame=LabelFrame(self.login_window,text='Please Choose Your Designation Before Login',font=('Times New Roman',15,'bold'),bd=5,relief=RIDGE,bg='#3daaf6',fg='red')
        login_frame.place(x=12,y=100,width=570,height=250)
        self.radioButton=StringVar()
        self.user_name=StringVar()
        self.id_num=StringVar()
        self.password=StringVar()
        Radiobutton(self.login_window,text='DOCTOR',variable=self.radioButton,value='DOCTOR',bg='#3daaf6').place(x=30,y=140)
        Radiobutton(self.login_window,text='RECEPTIONIST',variable=self.radioButton,value='RECEPTIONIST',bg='#3daaf6').place(x=150,y=140)
        Radiobutton(self.login_window,text='PHARMACIST',variable=self.radioButton,value='PHARMACIST',bg='#3daaf6').place(x=320,y=140)
        Radiobutton(self.login_window,text='MANAGER',variable=self.radioButton,value='MANAGER',bg='#3daaf6').place(x=480,y=140)
        UserName_label=Label(self.login_window, text='Enter USER_NAME :',font=('Times New Roman',11,'bold'),bg='#3daaf6').place(x=40,y=200)
        Id_label=Label(self.login_window, text='Enter ID                    :',font=('Times New Roman',11,'bold'),bg='#3daaf6').place(x=40,y=250)
        Password_label=Label(self.login_window, text='Enter PASSWORD   :',font=('Times New Roman',11,'bold'),bg='#3daaf6').place(x=40,y=300)
        UserName_entry=Entry(self.login_window,font=('Times New Roman',11,'bold'),width=30,textvariable=self.user_name)
        UserName_entry.place(x=200,y=200)
        Id_entry=Entry(self.login_window,font=('Times New Roman',11,'bold'),width=30,textvariable=self.id_num)
        Id_entry.place(x=200,y=250)
        Password_entry=Entry(self.login_window,font=('Times New Roman',11,'bold'),width=30,show='*',textvariable=self.password)
        Password_entry.place(x=200,y=300)
        LoginButton=Button(self.login_window,text='LOGIN',bg='orange',font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,command=self.login)
        LoginButton.place(x=270,y=380)
        RegisterButton=Button(self.login_window,text='REGISTER NEW EMPLOYEE',bg='green',font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,command=self.registration)
        RegisterButton.place(x=218,y=440)
    def registration(self):
        self.login_window.destroy()
        employee_register=Tk()

        er=EmployeeRegistrationUI(employee_register)
        employee_register.mainloop()

    def login(self):
        entered_name=self.user_name.get()
        entered_id=self.id_num.get()
        entered_password=self.password.get()
        entered_designation=self.radioButton.get()

        mydb=mysql.connector.connect(host='localhost',username='root',password='1234',database='employee_db')
        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM employee_details WHERE ID=%s AND Name=%s AND Password=%s  AND Designation=%s',(entered_id,entered_name,entered_password,entered_designation))
        result=mycursor.fetchone()
        if entered_designation=='DOCTOR' and result!=None:

            self.login_window.destroy()
            mydb.close()
            doctor_ui=Tk()
            dui=DoctorUI(doctor_ui)
            doctor_ui.mainloop()
        elif entered_designation=='RECEPTIONIST' and result!=None:
            self.login_window.destroy()
            mydb.close()
            receptionist_ui=Tk()
            rui=ReceptionistUI(receptionist_ui)
            receptionist_ui.mainloop()
        elif entered_designation=='PHARMACIST' and result!=None:
            self.login_window.destroy()
            mydb.close()
            supervisor_ui=Tk()
            sui=PharmacistUI(supervisor_ui)
            supervisor_ui.mainloop()
        elif entered_designation=='MANAGER' and result!=None:
            self.login_window.destroy()
            mydb.close()
            manager_ui=Tk()
            mui=ManagerUI(manager_ui)
            manager_ui.mainloop()


        else:
            messagebox.showerror(title='Login Error',message='Invalid Username or Id or Password. ')



            messagebox.showerror(title='DATABASE ERROR',message='Database connection not established yet. Please handle database error first.')



class EmployeeRegistrationUI:

    def __init__(self,employee_register):
        self.employee_register_ui=employee_register
        self.employee_register_ui.title('EMPLOYEE REGISTRATION USER INTERFACE')
        self.employee_register_ui.geometry('1300x720')
        self.employee_register_ui.resizable(FALSE,FALSE)
        self.number=random.randint(0000,9999)
        self.employee_register_ui.config(bg='#a4f8fa')
        # IMPORTANT VARIABLES NEEDED FOR DATABASES
        self.name = StringVar()
        self.birth = StringVar()
        self.father = StringVar()
        self.pass1 = StringVar()
        self.pass2 = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.present = StringVar()
        self.permanent=StringVar()
        title_label=Label(self.employee_register_ui,text='HEALTH CARE PRIVATE HOSPITAL EMPLOYEE REGISTRATION SYSTEM',font=('Times New Roman',20,'bold'),bg='#a4f8fa').pack()
        id_label=Label(self.employee_register_ui,text=f'UNIQUE ID: {self.number}',font=('Times New Roman',15,'bold'),bg='#a4f8fa').place(x=30,y=100)
        personal_details_label=LabelFrame(self.employee_register_ui,text='PERSONAL DETAILS',font=('Times New Roman',15,'bold'),bg='#fee3fe',bd=5,relief=RIDGE)
        personal_details_label.place(x=10,y=170,width=500,height=470)
        login_details_label=LabelFrame(self.employee_register_ui,text='LOGIN DETAILS',bg='#dbd5fd',font=('Times New Roman',15,'bold'),bd=5,relief=RIDGE)
        login_details_label.place(x=560,y=170,width=550,height=170)
        contact_label=LabelFrame(self.employee_register_ui,text='CONTACT INFORMATION',bg='#dbd5fd',font=('Times New Roman',15,'bold'),bd=5,relief=RIDGE)
        contact_label.place(x=560,y=400,width=550,height=270)
        phone_label=Label(self.employee_register_ui,text='Personal Phone Number  :',bg='#dbd5fd',font=('Times New Roman',14,'bold')).place(x=570,y=445)
        email_label=Label(self.employee_register_ui,text='Personal Email                 :',bg='#dbd5fd',font=('Times New Roman',14,'bold')).place(x=570,y=495)
        present_address_label=Label(self.employee_register_ui,text='Present Address               :',bg='#dbd5fd',font=('Times New Roman',14,'bold')).place(x=570,y=545)
        passw_label=Label(self.employee_register_ui,text='Enter Password      :',bg='#dbd5fd',font=('Times New Roman',14,'bold')).place(x=570,y=210)
        passw_confirm=Label(self.employee_register_ui,text='Confirm Password  :',bg='#dbd5fd',font=('Times New Roman',14,'bold')).place(x=570,y=270)
        password_entry =Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=22,textvariable=self.pass1)
        password_entry.place(x=760,y=210)
        confirm_entry =Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=22,show='*',textvariable=self.pass2)
        confirm_entry.place(x=760,y=270)
        phone_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=20,textvariable=self.phone)
        phone_entry.place(x=790,y=445)
        email_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=28,textvariable=self.email)
        email_entry.place(x=790,y=495)
        present_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=28,textvariable=self.present)
        present_entry.place(x=790,y=540)


        name_label=Label(self.employee_register_ui,text='Name of the Employee  :',bg='#fee3fe',font=('Times New Roman',14,'bold')).place(x=15,y=210)
        d_o_b_label=Label(self.employee_register_ui,text='Date of Birth                  :',bg='#fee3fe',font=('Times New Roman',14,'bold')).place(x=15,y=260)
        father_name_label=Label(self.employee_register_ui,text="Father's Name               :",bg='#fee3fe',font=('Times New Roman',14,'bold')).place(x=15,y=310)
        designation_label = Label(self.employee_register_ui, text='Designation                    :', bg='#fee3fe',font=('Times New Roman', 14, 'bold')).place(x=15, y=360)
        doctor_label= Label(self.employee_register_ui, text="Specialist(for doctor only):", bg='#fee3fe',font=('Times New Roman', 14, 'bold')).place(x=15, y=410)
        permanent_address_label=Label(self.employee_register_ui,text='Permanent Address :',bg='#fee3fe',font=('Times New Roman',14,'bold')).place(x=15,y=460)

        name_entry= Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=25,textvariable=self.name)
        name_entry.place(x=230,y=210)
        d_o_b_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=15,textvariable=self.birth)
        d_o_b_entry.insert(0,'DD-MM-YYYY')
        d_o_b_entry.place(x=230,y=260)

        father_name_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=25,textvariable=self.father)
        father_name_entry.place(x=230,y=310)
        self.designation_combobox=ttk.Combobox(self.employee_register_ui,values=["DOCTOR",'PHARMACIST','RECEPTIONIST','MANAGER'],font=('Times New Roman',14,'bold'))
        self.designation_combobox['state']='readonly'
        self.designation_combobox.place(x=230,y=360)
        self.specilization_combobox=ttk.Combobox(self.employee_register_ui,values=['N/A','Cardiologist','Nephrologist','General Medicine','Gynecologist'],font=('Times New Roman',14,'bold'))
        self.specilization_combobox['state']='readonly'
        self.specilization_combobox.place(x=230,y=410)

        permanent_address_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=40,textvariable=self.permanent)
        permanent_address_entry.place(x=38,y=500)



        account_confirm_button=Button(self.employee_register_ui,text='CREATE ACCOUNT',bg='pink',font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,command=self.create_account)
        account_confirm_button.place(x=1130,y=370)

    def create_account(self):
        if self.name.get()=='':
            messagebox.showerror(title='NAME ERROR',message='Please Enter Name of the Employee.')
        elif self.birth.get()=='':
            messagebox.showerror(title='BIRTH ERROR', message='Please Enter Birth Date of the Employee.')
        elif self.father.get()=='':
            messagebox.showerror(title="FATHER'S ERROR", message="Father's Name is Blank.")
        elif self.permanent.get()=='':
            messagebox.showerror(title='PERMANENT ADDRESS ERROR', message='Please Enter Permanent Address of the Employee.')
        elif self.pass1.get()=='':
            messagebox.showerror(title='PASSWORD ERROR', message='Please Enter Password.')
        elif self.pass2.get()=='':
            messagebox.showerror(title='PASSWORD ERROR', message='Please Confirm your Password.')
        elif self.pass1.get()!=self.pass2.get():
            messagebox.showerror(title='NOT MATCHING', message='Passwords are not matching.')
        elif self.phone.get()=='':
            messagebox.showerror(title='PHONE ERROR', message='Enter your phone number correctly.')
        elif self.email.get()=='':
            messagebox.showerror(title='EMAIL ERROR', message='Please Enter Email of the Employee.')
        elif self.present.get()=='':
            messagebox.showerror(title='PRESENT ADDRESS ERROR', message='Please Enter Present Address of the Employee.')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='employee_db')
                mydb=conn.cursor()
                mydb.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (self.name.get(),self.birth.get(),self.father.get(),self.permanent.get(),self.pass1.get(),self.phone.get(),self.email.get(),self.present.get(),self.number,self.designation_combobox.get(),self.specilization_combobox.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo(title='SUCCESS',message='New employee has been created. If you want to modify anything.Please click modify account.')
                self.employee_register_ui.destroy()
            except:
                messagebox.showerror(title='DATABASE CONNECTION ERROR',message='Database Connection Error. Please Connect to Database Properly.')





class DoctorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Interface")

        # Database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="doctor_db"
        )
        self.cursor = self.conn.cursor()

        # Create Treeview
        self.tree = ttk.Treeview(root, columns=('Patient Name', 'Prescribed Doctor'), show='headings')
        self.tree.heading('Patient Name', text='Patient Name')
        self.tree.heading('Prescribed Doctor', text='Prescribed Doctor')
        self.tree.pack(fill=BOTH, expand=True)

        # Populate Treeview
        self.populate_treeview()

        # Double click event
        self.tree.bind('<Double-1>', self.on_double_click)

        # Button to delete patient
        delete_button = Button(root, text="Delete Patient", command=self.delete_patient)
        delete_button.pack()

    def populate_treeview(self):
        # Clear existing data
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Fetch data from database and insert into Treeview
        self.cursor.execute("SELECT * FROM patients")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert('', 'end', values=(row[0], row[1]))

    def on_double_click(self, event):
        item = self.tree.selection()[0]
        patient_name = self.tree.item(item, 'values')[0]
        doctor_name = self.tree.item(item, 'values')[1]
        self.open_prescription_window(patient_name, doctor_name)

    def open_prescription_window(self, patient_name, doctor_name):
        prescription_window = Toplevel(self.root)
        prescription_window.title("Write Prescription")

        # Label and Entry for prescription
        Label(prescription_window, text="Prescription for " + patient_name).pack()
        prescription_entry = Text(prescription_window, width=100)
        prescription_entry.pack()

        # Button to save prescription
        save_button = Button(prescription_window, text="Save Prescription",
                                command=lambda: self.save_prescription(prescription_window, patient_name,
                                                                       prescription_entry.get(1.0,END)))
        save_button.pack()

    def save_prescription(self, prescription_window, patient_name, prescription):
        r=open('prescription.txt','w')
        r.write(f"Patient's Name: {patient_name}\n")
        r.write(prescription)
        r.close()

    def delete_patient(self):
        item = self.tree.selection()[0]
        patient_name = self.tree.item(item, 'values')[0]
        self.cursor.execute("DELETE FROM patients WHERE patient_name = %s", (patient_name,))
        self.conn.commit()
        self.populate_treeview()


class ManagerUI:
    def __init__(self,window):
        self.manager_window=window
        self.manager_window.title('MANAGER USER INTERFACE')
        self.manager_window.geometry('800x600')
        self.manager_window.resizable(FALSE,FALSE)
        self.option_frame=Frame(self.manager_window,bg='#74f58b')
        self.option_frame.pack(side=LEFT)
        self.option_frame.pack_propagate(FALSE)
        self.option_frame.configure(width=250,height=600)
        self.main_frame = Frame(self.manager_window, highlightbackground='yellow', highlightthickness=3,bg='#ddf9b3')
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(FALSE)
        self.main_frame.configure(width=550, height=600)
        financial_button=Button(self.option_frame,text='Financial Calculations',font=('Times New Roman',12,'bold'),command=self.financial_statement)
        financial_button.place(x=25,y=150)
        food_supervising=Button(self.option_frame,text='Food Supervising',font=('Times New Roman',12,'bold'),command=self.food_supervsior)
        food_supervising.place(x=25,y=300)

    def delete_frames(self):
        for frames in self.main_frame.winfo_children():
            frames.destroy()
    def food_supervsior(self):
        self.delete_frames()
        def slip_print():
            r = open('patient_food.txt', 'w')
            r.write(f"Date: {date.today()}\n")
            r.write(f"Patient's Name: {patient_name_entry.get()}\n")
            r.write(f"Patient's ID: {patient_id_entry.get()}\n")
            r.write(f"Patient's Room Number: {room_number_entry.get()}\n")
            r.write(f'Food for the patient:{food_list.get()}')
            r.close()
            messagebox.showinfo(title='Patient food',message='Patient food successfully updated.')
        title=Label(self.main_frame,text='Food Management For Patients',font=('Times New Roman',20,'bold'),bg='#ddf9b3').pack()
        patient_name=Label(self.main_frame,text='Patient Name :',font=('Times New Roman',12,'bold'),bg='#ddf9b3').place(x=10,y=200)
        patient_id=Label(self.main_frame,text='Patient ID :',font=('Times New Roman',12,'bold'),bg='#ddf9b3').place(x=10,y=250)
        room_number=Label(self.main_frame,text='Room Number :',font=('Times New Roman',12,'bold'),bg='#ddf9b3').place(x=10,y=300)
        food=Label(self.main_frame,text='Select food for Patient:',font=('Times New Roman',12,'bold'),bg='#ddf9b3').place(x=10,y=350)
        patient_name_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        patient_name_entry.place(x=170,y=200)
        patient_id_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        patient_id_entry.place(x=170,y=250)
        room_number_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        room_number_entry.place(x=170,y=300)

        food_list=ttk.Combobox(self.main_frame,values=['2 bread with jam and 1 boiled egg','Vegetable Oats','soya chunks with plain rice','1 bowl rice with chicken curry','1bowl rice with fish curry'],width=50)
        food_list['state']='readonly'
        food_list.place(x=170,y=350)

        button=Button(self.main_frame,text='Print',command=slip_print)
        button.place(x=400,y=500)


    def financial_statement(self):
        self.delete_frames()

        def calculate_method():
            if cost_entry1.get() == '' or cost_entry2.get() == '' or cost_entry3.get() == '' or profit_entry1.get() == '' or profit_entry2.get() == '' or profit_entry3.get() == '':
                messagebox.showerror(title='Error',
                                     message='Please fill all blank boxes with Numbers only and input month name')
            else:
                total=(int(profit_entry1.get())+int(profit_entry2.get())+int(profit_entry3.get()))-(int(cost_entry1.get())+int(cost_entry2.get())+int(cost_entry3.get()))
                l=Label(self.main_frame,text=total,font=('Times New Roman',12,'bold')).place(x=300,y=150)

        title=Label(self.main_frame,text='Check Financial Status of the Hospital',font=('Times New Roman',20,'bold'),bg='#ddf9b3').pack()
        month=Label(self.main_frame,text='Month:',font=('Times New Roman',14,'bold'),bg='#ddf9b3').place(x=10,y=60)
        recieved_title=Label(self.main_frame,text='Total Amount Recieved :',font=('Times New Roman',14,'bold'),bg='#ddf9b3').place(x=10,y=120)
        recieved_1=Label(self.main_frame,text='Patient Registration :',font=('Times New Roman',10,'bold'),bg='#ddf9b3').place(x=10,y=160)
        recieved_2=Label(self.main_frame,text='Patient Tests Registration:',font=('Times New Roman',10,'bold'),bg='#ddf9b3').place(x=10,y=200)
        recieved_3=Label(self.main_frame,text='Food Service: ',font=('Times New Roman',10,'bold'),bg='#ddf9b3').place(x=10,y=240)
        cost_title=Label(self.main_frame,text='Total Amount Spend :',font=('Times New Roman',14,'bold'),bg='#ddf9b3').place(x=10,y=300)
        cost_1=Label(self.main_frame,text='Electricity Bills:',font=('Times New Roman',10,'bold'),bg='#ddf9b3').place(x=10,y=360)
        cost_2=Label(self.main_frame,text='Employee Salaries:',font=('Times New Roman',10,'bold'),bg='#ddf9b3').place(x=10,y=400)
        cost_3=Label(self.main_frame,text='Others Servicing costs',font=('Times New Roman',10,'bold'),bg='#ddf9b3').place(x=10,y=440)
        calculate=Label(self.main_frame,text='Calculate Total=',font=('Times New Roman',12,'bold'),bg='#ddf9b3').place(x=300,y=120)
        month_ccb=ttk.Combobox(self.main_frame,values=['JAN-01','FEB-02','MAR-03','APR-04','MAY-05','JUN-06','JUL-07','AUG-08','SEP-09','OCT-10','NOV-11','DEC-12'],font=('Times New Roman',14,'bold'),width=10)
        month_ccb['state']='readonly'
        month_ccb.place(x=100,y=60)
        profit_entry1=Entry(self.main_frame,width=10,font=('Times New Roman',10,'bold'))
        profit_entry1.place(x=160,y=160)
        profit_entry2=Entry(self.main_frame,width=10,font=('Times New Roman',10,'bold'))
        profit_entry2.place(x=160,y=200)
        profit_entry3=Entry(self.main_frame,width=10,font=('Times New Roman',10,'bold'))
        profit_entry3.place(x=160,y=240)
        cost_entry1=Entry(self.main_frame,width=10,font=('Times New Roman',10,'bold'))
        cost_entry1.place(x=160,y=360)
        cost_entry2=Entry(self.main_frame,width=10,font=('Times New Roman',10,'bold'))
        cost_entry2.place(x=160, y=400)
        cost_entry3=Entry(self.main_frame,width=10,font=('Times New Roman',10,'bold'))
        cost_entry3.place(x=160, y=440)

        def insert_db():
            if cost_entry1.get() == '' or cost_entry2.get() == '' or cost_entry3.get() == '' or profit_entry1.get() == '' or profit_entry2.get() == '' or profit_entry3.get() == '':
                messagebox.showerror(title='Error',
                                     message='Please fill all blank boxes with Numbers only and input month name')
            elif month_ccb.get() == '':
                messagebox.showerror(title='Month Error', message='Please input month.')
            else:
                earned = int(profit_entry1.get()) + int(profit_entry2.get()) + int(profit_entry3.get())
                spend = int(cost_entry1.get()) + int(cost_entry2.get()) + int(cost_entry3.get())
                remaining = earned - spend

                try:
                    # Establish connection to the MySQL server
                    db_connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="manager"
                    )
                    cursor = db_connection.cursor()

                    # SQL query to insert data into the table
                    sql_query = "INSERT INTO monthly_financial_status (months, earned, expenditure, remaining) VALUES (%s, %s, %s, %s)"
                    values = (month_ccb.get(), earned, spend, remaining)

                    # Execute the query
                    cursor.execute(sql_query, values)

                    # Commit the transaction
                    db_connection.commit()

                    # Close the cursor and database connection
                    cursor.close()
                    db_connection.close()

                    messagebox.showinfo(title='Info Saved', message='Saved Info Successfully')
                except mysql.connector.Error as error:
                    messagebox.showerror(title='Database Error', message=f'Error: {error}')
        db_button=Button(self.main_frame,text='SAVE INFO',font=('Times New Roman',12,'bold'),command=insert_db)
        db_button.place(x=360,y=550)
        calc_button=Button(self.main_frame,text='CALCULATE ALL',font=('Times New Roman',12,'bold'),command=calculate_method)
        calc_button.place(x=120,y=550)
class PharmacistUI:
    def __init__(self,window):
        self.pharmacist_window=window
        self.pharmacist_window.title('PHARMACIST USER INTERFACE')
        self.pharmacist_window.geometry('1200x600')
        self.pharmacist_window.resizable(FALSE, FALSE)
        self.option_frame=Frame(self.pharmacist_window,bg='yellow')
        self.option_frame.pack(side=LEFT)
        self.option_frame.pack_propagate(FALSE)
        self.option_frame.configure(width=250,height=600)

        self.main_frame=Frame(self.pharmacist_window,highlightbackground='green',highlightthickness=3)
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(FALSE)
        self.main_frame.configure(width=1190,height=600)
        sale_button=Button(self.option_frame,text='Sales Management',font=('Times New Roman',15,'bold'),command=self.sale_management)
        sale_button.place(x=10,y=100)
        medicine_stored_button=Button(self.option_frame,text='View Medicine Database',font=('Times New Roman',15,'bold'),command=self.stored_medicine)
        medicine_stored_button.place(x=10, y=300)
        update_button=Button(self.option_frame,text='Update Medicine Storage',font=('Times New Roman',15,'bold'),command=self.update_medicine)
        update_button.place(x=10,y=500)

    def delete_pages(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def sale_management(self):
        self.delete_pages()

        def search():
            a = medicne_entry.get()  # Assuming medicne_entry is a tkinter Entry widget
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='medicine_db')
            mydb = conn.cursor()
            mydb.execute("SELECT quantity FROM medicines WHERE medicine_name = %s", (a,))
            result = mydb.fetchone()  # Assuming you expect only one result
            conn.close()

            if result:
                quantity = result[0]  # Extracting quantity from the result tuple
                messagebox.showinfo(title='Medicine Info', message=f"The quantity of {a} is {quantity}.")
            else:
                messagebox.showinfo(title='Medicine Info', message=f"{a} not found in the database.")

        def add_medicine():
            l = Label(self.main_frame,
                      text=f'Medicine Name:{medicne_entry.get()},Quantity:{quantity_entry.get()},Unit Price{unit_price_entry.get()}').pack(
                side=BOTTOM)

        def insert_customer(customer_name, contact_number, invoice_id, paid_amount):
            try:
                # Establish a connection to the MySQL database
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='1234',
                    database='customer_db'
                )
                


                # Create a cursor object to execute SQL queries
                cursor = conn.cursor()

                # SQL query to insert data into the customers table
                insert_query = "INSERT INTO customers (customer_name, contact_number, invoice_id, paid_amount) VALUES (%s, %s, %s, %s)"

                # Data to be inserted
                customer_data = (customer_name, contact_number, invoice_id, paid_amount)

                # Execute the insert query
                cursor.execute(insert_query, customer_data)

                # Commit the transaction
                conn.commit()

                messagebox.showinfo(title='Upadate Message',message='Database updated successfully.')


            except mysql.connector.Error as error:
                messagebox.showerror(title='Update failed',message='Database connection unsuccessful')


        title_l1 = Label(self.main_frame, text='SALES MANAGEMENT PAGE', font=('Times New Roman', 15, 'bold')).pack()
        cd = Label(self.main_frame, text=date.today(), font=('Times New Roman', 15, 'bold')).pack()
        name_label = Label(self.main_frame, text='Customer Name     :', font=('Times New Roman', 12, 'bold')).place(
            x=10, y=100)
        contact_label = Label(self.main_frame, text='Contact Number     :', font=('Times New Roman', 12, 'bold')).place(
            x=10, y=150)
        invoice_label = Label(self.main_frame, text='Invoice ID            :',
                              font=('Times New Roman', 12, 'bold')).place(x=10, y=200)
        product_name = Label(self.main_frame, text='Medicine Name      :', font=('Times New Roman', 12, 'bold')).place(x=10, y=250)
        name_entry = Entry(self.main_frame, width=25, font=('Times New Roman', 12, 'bold'))
        name_entry.place(x=158, y=100)
        contact_entry = Entry(self.main_frame, width=25, font=('Times New Roman', 12, 'bold'))
        contact_entry.place(x=158, y=150)
        invoice_id=random.randint(0000000000, 9999999999)
        invoice_label2 = Label(self.main_frame, text=invoice_id,
                               font=('Times New Roman', 12, 'bold')).place(x=158, y=200)
        medicne_entry = Entry(self.main_frame, width=25, font=('Times New Roman', 12, 'bold'))
        medicne_entry.place(x=158, y=250)
        search_button = Button(self.main_frame, text='Search medicine', command=search).place(x=315, y=250)
        quantity_label = Label(self.main_frame, text='Quantity', font=('Times New Roman', 12, 'bold')).place(x=10,
                                                                                                             y=300)
        quantity_entry = Entry(self.main_frame, font=('Times New Roman', 12, 'bold'), width=5)
        quantity_entry.place(x=158, y=300)
        unit_price_l = Label(self.main_frame, text='Unit Price :', font=('TImes New Roman', 12, 'bold')).place(x=210,
                                                                                                               y=300)
        unit_price_entry = Entry(self.main_frame, width=5)
        unit_price_entry.place(x=290, y=300)
        total_l=Label(self.main_frame,text='Total Amount to be Paid:',font=('Times New Roman',12,'bold')).place(x=400,y=150)
        total_e=Entry(self.main_frame,width=7,font=('Times New Roman',12,'bold'))
        total_e.place(x=600,y=150)
        add_medicine = Button(self.main_frame, text='Add Medicine', command=add_medicine).place(x=10, y=350)
        insert_button = Button(self.main_frame,text='Insert into Database',command=lambda :insert_customer(name_entry.get(),contact_entry.get(),invoice_id,int(total_e.get()))).place(x=190,y=350)

    def stored_medicine(self):
        self.delete_pages()
        title_l1=Label(self.main_frame,text='STORED MEDICINE PAGE',font=('Times New Roman',15,'bold')).pack()

        def load_data():
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="medicine_db"
                )
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT medicine_name, provider_name, mg_quantity, batch_number, manufacture_date, expiry_date, quantity FROM medicines")
                rows = cursor.fetchall()
                for row in rows:
                    trv1.insert("", "end", values=row)
                connection.close()
            except mysql.connector.Error as error:
                print("Failed to fetch data from MySQL table:", error)
        trv1=ttk.Treeview(self.main_frame)
        trv1.pack(fill='both',expand=TRUE)
        trv1['columns']= ("Medicine Name", "Provider Name", "MG Quantity", "Batch Number", "Manufacture Date", "Expiry Date", "Quantity")
        trv1.column("#0", width=0, stretch=NO)
        for column in trv1["columns"]:
            trv1.heading(column, text=column)

        load_data()

    def update_medicine(self):
        self.delete_pages()
        def update():
            a=int(mg_entry.get())
            if name_entry.get()=='' or provider_entry.get()==''  or type(a)!=int or a=='' or batch_entry.get()=='' or manufac_entry.get()=='' or expiry_entry.get()=='' or quantity_entry.get()=='':
                messagebox.showerror(title='Update error', message='Please provide all information correctly. Make sure mg_entry must be numbers.')
            else:
                conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='medicine_db')
                mydb = conn.cursor()
                mydb.execute("insert into medicines values (%s,%s,%s,%s,%s,%s,%s)", (
                name_entry.get(), provider_entry.get(), a, batch_entry.get(), manufac_entry.get(), expiry_entry.get(),
                quantity_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo(title='Updated',message='Medicine updated successfully.')
                name_entry.delete(0,END)
                provider_entry.delete(0,END)
                mg_entry.delete(0,END)
                batch_entry.delete(0,END)
                manufac_entry.delete(0,END)
                expiry_entry.delete(0,END)
                quantity_entry.delete(0,END)

        title_l1=Label(self.main_frame,text='UPDATE MEDICINE PAGE',font=('Times New Roman',15,'bold')).pack()
        medicine_name_lb=Label(self.main_frame,text='Name of the Medicine :',font=('Times New Roman',12,'bold')).place(x=10,y=60)
        medicine_code_lb=Label(self.main_frame,text='Provider Company :',font=('Times New Roman',12,'bold')).place(x=10,y=120)
        mg_label=Label(self.main_frame,text='Containing Mg      :',font=('Times New Roman',12,'bold')).place(x=10,y=180)
        type_m_label=Label(self.main_frame,text='Medicine Type    :',font=('Times New Roman',12,'bold')).place(x=10,y=240)
        batch_label=Label(self.main_frame,text='Batch Number     :',font=('Times New Roman',12,'bold')).place(x=10,y=300)
        manufac_label=Label(self.main_frame,text='Manufacture Date  :',font=('Times New Roman',12,'bold')).place(x=10,y=360)
        expire_label=Label(self.main_frame,text='Expiry Date     :',font=('Times New Roman',12,'bold')).place(x=10,y=420)
        quantity=Label(self.main_frame,text='Quantity of the Medicine:',font=('Times New Roman',12,'bold')).place(x=10,y=480)
        name_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        name_entry.place(x=205,y=60)
        provider_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        provider_entry.place(x=205,y=120)
        mg_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        mg_entry.place(x=205,y=180)
        type_medicine=ttk.Combobox(self.main_frame,font=('Times New Roman',12,'bold'),values=['Syrup','Capsule','Tablet','Supositor'])
        type_medicine['state']='readonly'
        type_medicine.place(x=205,y=240)
        batch_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        batch_entry.place(x=205,y=300)
        manufac_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        manufac_entry.place(x=205,y=360)
        expiry_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        expiry_entry.place(x=205,y=420)
        quantity_entry=Entry(self.main_frame,font=('Times New Roman',12,'bold'))
        quantity_entry.place(x=205,y=480)
        button=Button(self.main_frame,text='UPDATE MEDICINE',font=('Times New Roman',12,'bold'),bg='#8ad5f6',command=update)
        button.place(x=205,y=540)








class ReceptionistUI:
    def __init__(self,receptionist_ui):
        self.receptionist_window = receptionist_ui
        self.receptionist_window.title('RECEPTIONIST INTERFACE')
        self.receptionist_window.geometry('300x300')
        self.receptionist_window.resizable(FALSE,FALSE)
        self.radio_button=IntVar()
        Radiobutton(self.receptionist_window,text='Patient Registration',variable=self.radio_button,value=1,font=('Times New Roman',13,'bold')).place(x=40,y=20)
        Radiobutton(self.receptionist_window,text='Patient Test Registration',variable=self.radio_button,value=2,font=('Times New Roman',13,'bold')).place(x=40,y=60)
        Radiobutton(self.receptionist_window,text='View Patient Database',variable=self.radio_button,value=3,font=('Times New Roman',13,'bold')).place(x=40,y=100)
        open_button=Button(self.receptionist_window,text='Open Current Option',command=self.open_option,font=('Times New Roman',13,'bold')).place(x=60,y=200)

    def open_option(self):
        if self.radio_button.get()==1:

            p_r=Tk()
            patient_regi=Patient_Registration(p_r)
            p_r.mainloop()
        elif self.radio_button.get()==2:
            p_t_r = Tk()
            patient_test = Test_Registration(p_t_r)
            p_t_r.mainloop()

        elif self.radio_button.get()==3:
            v_r = Tk()
            v_patient = Patient_Details(v_r)
            v_r.mainloop()

        else:
            messagebox.showerror(title='Selection Error',message='Please select any of the three option')


class Patient_Registration:
    def __init__(self,window):
        self.patient_registration=window
        self.patient_registration.geometry('1300x700')
        self.patient_registration.title('Register Patient')
        self.patient_registration.resizable(FALSE,FALSE)
        self.number = random.randint(0000, 9999)
        titile_label=Label(self.patient_registration,text='Register New Patient',font=('Times New Roman',20,'bold'),relief=RIDGE,bd=10).pack()
        frame1=LabelFrame(self.patient_registration,text='Bio Details of Patient',font=('Times New Roman',20,'bold'),relief=RIDGE,bd=10)
        frame1.place(x=40,y=80,width=1220,height=300)
        frame2=LabelFrame(self.patient_registration,text='Payment Details',font=('Times New Roman',20,'bold'),relief=RIDGE,bd=10)
        frame2.place(x=40,y=400,width=1220,height=200)
        update_button=Button(self.patient_registration,text='Register Patient Information',font=('Times New Roman',13,'bold'),command=self.register)
        update_button.place(x=600,y=640)
        name_label=Label(self.patient_registration,text='Name of the Patient                  :',font=('Times New Roman',13,'bold')).place(x=65,y=110)
        age_label=Label(self.patient_registration,text='Age of the Patient                    :',font=('Times New Roman',13,'bold')).place(x=65,y=150)
        y=Label(self.patient_registration,text='years',font=('Times New Roman',13,'bold')).place(x=400,y=150)
        blood_group=Label(self.patient_registration,text='Blood Group of the Patient     :',font=('Times New Roman',13,'bold')).place(x=65,y=190)
        blood_pressure_label=Label(self.patient_registration,text='Blood Pressure of the Patient :',font=('Times New Roman',13,'bold')).place(x=65,y=230)
        gender_label=Label(self.patient_registration,text='Gender of the Patient              :',font=('Times New Roman',13,'bold')).place(x=65,y=270)
        diabetic_label=Label(self.patient_registration,text='Diabetics of the Patient              :',font=('Times New Roman',13,'bold')).place(x=65,y=310)
        medical_issue_label=Label(self.patient_registration,text='Medical Issue :',font=('Times New Roman',13,'bold')).place(x=900,y=120)
        amount_label=Label(self.patient_registration,text='Amount to be paid :',font=('Times New Roman',13,'bold')).place(x=65,y=450)
        paid_through=Label(self.patient_registration,text='Paid Through :',font=('Times New Roman',13,'bold')).place(x=700,y=450)
        acc_number=Label(self.patient_registration,text='Account Number  :',font=('Times New Roman',13,'bold')).place(x=700,y=500)
        ref_number=Label(self.patient_registration,text='Reference Number :',font=('Times New Roman',13,'bold')).place(x=700,y=550)
        self.amount=Entry(self.patient_registration,font=('Times New Roman',12,'bold'))
        self.amount.place(x=250,y=450)
        self.acc_number_entry=Entry(self.patient_registration,font=('Times New Roman',12,'bold'))
        self.acc_number_entry.place(x=855,y=500)
        self.ref_entry=Entry(self.patient_registration,font=('Times New Roman',12,'bold'))
        self.ref_entry.place(x=855,y=550)
        self.paid_media=ttk.Combobox(self.patient_registration,values=['Cash','Bkash','Nagad'],font=('Times New Roman',13,'bold'))
        self.paid_media['state']='readonly'
        self.paid_media.place(x=820,y=450)
        self.name_entry=Entry(self.patient_registration,width=30,font=('Times New Roman',13,'bold'))
        self.name_entry.place(x=340,y=110)
        self.age_entry=Entry(self.patient_registration,width=5,font=('Times New Roman',13,'bold'))
        self.age_entry.place(x=340,y=150)
        patient_id=Label(self.patient_registration,text=f'Patient ID :     {self.number}',font=('Times New Roman',13,'bold')).place(x=65,y=500)
        self.doctor_specialization = ttk.Combobox(self.patient_registration,
                                             values=['Cardiologist [heart]', 'Nephrologist[kidney]', 'General Medicine[general]',
                                                     'Gynecologist[pregnant]'])
        self.doctor_specialization['state']='readonly'
        self.doctor_specialization.place(x=900, y=280)
        self.blood_group_cb=ttk.Combobox(self.patient_registration,values=['A+','B+','O+','AB+','A-','B-','O-','AB-'],font=('Times New Roman',13,'bold'))
        self.blood_group_cb['state']='readonly'
        self.blood_group_cb.place(x=340,y=190)
        self.blood_pressure_cb=ttk.Combobox(self.patient_registration,values=['HIGH','NORMAL','LOW'],font=('Times New Roman',13,'bold'))
        self.blood_pressure_cb['state']='readonly'
        self.blood_pressure_cb.place(x=340,y=230)
        self.diabetic_cb=ttk.Combobox(self.patient_registration,values=['N/A','TYPE-1','TYPE-2'],font=('Times New Roman',13,'bold'))
        self.diabetic_cb['state']='readonly'
        self.diabetic_cb.place(x=340,y=310)
        self.gender_combo=ttk.Combobox(self.patient_registration,values=['Male','Female'],font=('Times New Roman',13,'bold'))
        self.gender_combo['state']='readonly'
        self.gender_combo.place(x=340,y=270)
        self.text_box=Text(self.patient_registration,width=30,height=5)
        self.text_box.place(x=900,y=190)

        suggest_button=Button(self.patient_registration,text='SUGGEST',font=('Times New Roman',12,'bold'),command=self.suggest).place(x=1160,y=200)

    def register(self):
        if self.name_entry.get()=='':
            messagebox.showerror(title='NameError',message='Please Enter Patient Name.')
        if self.age_entry.get()=='' or len(self.age_entry.get())>=3:
            messagebox.showerror(title='NameError',message='Please Enter Patient Age.')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='patient_db')
                mydb=conn.cursor()
                mydb.execute("insert into patient_details values(%s,%s,%s,%s,%s,%s,%s)",
                         (self.name_entry.get(), self.age_entry.get(),
                          self.blood_group_cb.get(),self.blood_pressure_cb.get(),
                          self.gender_combo.get(), self.diabetic_cb.get(),self.number))
                conn.commit()
                conn.close()

                conn1=mysql.connector.connect(host='localhost', username='root', password='1234', database='payemnt')
                mydb2=conn1.cursor()
                mydb2.execute("insert into payment_details values(%s,%s,%s,%s,%s)",
                         (self.number,self.amount.get(),self.paid_media.get(),self.acc_number_entry.get(),self.ref_entry.get()))
                conn1.commit()
                conn1.close()
                self.patient_registration.destroy()
                messagebox.showinfo(title='Patient Database', message='Patient Database has been updated')

            except:
                messagebox.showerror(title='DATABASE CONNECTION ERROR',message='Database Connection Error. Please Connect to Database Properly.')

    def suggest(self):

        phrases = {
            'heart_diseases': ['sweating', 'shortness of breath', 'chest pain', 'high blood pressure'],
            'pregnancy_related': ['nausea', 'weight gain', 'bloating', 'fatigue', 'heart burn', 'missed period',
                                  'frequent urination', 'vomiting'],
            'kidney_diseases': ['very little', 'too much urine', 'cloudy urine', 'blood in urine', 'fever',
                                'swelling in the hands and feet', 'fatigue', 'shortness of breath', 'loss of appetite',
                                'nausea', 'vomiting'],
            'general_diseases': ['fever', 'cold', 'vomiting', 'blood pressure']
        }
        others = ['is', 'are', 'she', 'he', 'the', 'patient', 'has', 'have', 'feeling']

        writings = self.text_box.get(1.0, END).lower()
        found = False

        # Check for specific phrases in the input
        for phrase, symptoms in phrases.items():
            symptom_count = sum(1 for symptom in symptoms if f'{symptom}' in writings)
            if symptom_count > 1:
                messagebox.showinfo(title='Doctor Consultation',
                                    message=f"Consult a {phrase.replace('_', ' ').title()} for {', '.join(symptoms)}-related concerns")

                found = True
                break

        p_window=Tk()
        p_window.geometry('50x50')
        def doctor():
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='doctor_db')
            mydb = conn.cursor()
            mydb.execute("INSERT INTO patients (patient_name, prescribed_doctor) VALUES (%s, %s)",(self.name_entry.get(),suggest.get()))
            conn.commit()
            conn.close()
        suggest=Entry(p_window)
        suggest.pack()
        suggest_button=Button(p_window,text='SuggestDoctor',command=doctor).pack()
        p_window.mainloop()

        if not found:
            messagebox.showinfo(title='Doctor Consultation',
                                message="No specific suggestion based on the provided symptoms")



class Patient_Details:
    def __init__(self, window):
        self.patient_details = window
        self.patient_details.title('Patient Details')
        self.patient_details.geometry('1300x600')
        self.patient_details.resizable(False, False)
        title_label = Label(self.patient_details, text='Patient Details', font=('Times New Roman', 20, 'bold'),relief=RIDGE, bd=10).pack()
        search_id_label = Label(self.patient_details, text='Search by ID :', font=('Times New Roman', 13, 'bold')).place(x=10, y=100)
        search_name_label = Label(self.patient_details, text='Search by Name :', font=('Times New Roman', 13, 'bold')).place(x=10, y=150)
        self.search_id_entry = Entry(self.patient_details, font=('Times New Roman', 13, 'bold'))
        self.search_id_entry.place(x=180, y=100)
        self.search_name_entry = Entry(self.patient_details, font=('Times New Roman', 13, 'bold'))
        self.search_name_entry.place(x=180, y=150)
        search_button = Button(self.patient_details, text='Search', font=('Times New Roman', 13, 'bold'), command=self.search)
        search_button.place(x=380, y=100)
        all_button = Button(self.patient_details, text='View All', font=('Times New Roman ', 13, 'bold'), command=self.view)
        all_button.place(x=380, y=170)
        cols = ('ID', 'NAME', 'GENDER', 'AGE', 'BLOOD GROUP', 'BLOOD PRESSURE', 'DIABETICS')
        self.trv = ttk.Treeview(self.patient_details, columns=cols, show='headings')
        for col in cols:
            self.trv.heading(col, text=col)
        self.trv.place(x=1, y=230)

    

    def search(self):
        if self.search_id_entry.get()=='' and self.search_name_entry.get()=='':
            messagebox.showerror(title='Empty',message='Please enter id or name.')
        # Get the search term from the entry widgets
        search_term_id = self.search_id_entry.get()
        search_term_name = self.search_name_entry.get()

        # Clear the Treeview
        for row in self.trv.get_children():
            self.trv.delete(row)

        # Connect to the database
        conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='patient_db')
        mydb = conn.cursor()

        # Execute the query based on the search term
        if search_term_id:
            mydb.execute(
                "SELECT ID, Name, Gender, Age, BloodGroup, BloodPressure, Diabetics FROM patient_details WHERE ID = %s",
                (search_term_id,))
        elif search_term_name:
            mydb.execute(
                "SELECT ID, Name, Gender, Age, BloodGroup, BloodPressure, Diabetics FROM patient_details WHERE Name LIKE %s",
                (f'%{search_term_name}%',))

        records = mydb.fetchall()

        # Insert records into the Treeview
        for record in records:
            self.trv.insert('', 'end', values=record)

        # Close the database connection
        mydb.close()
        conn.close()



    def view(self):
        for row in self.trv.get_children():
            self.trv.delete(row)
        conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='patient_db')
        mydb = conn.cursor()
        mydb.execute("SELECT ID, Name, Gender, Age, BloodGroup, BloodPressure, Diabetics FROM patient_details")
        records = mydb.fetchall()
        for i, (ID, Name, Gender, Age, BloodGroup, BloodPressure, Diabetics) in enumerate(records, start=1):
            self.trv.insert('', 'end', values=(ID, Name, Gender, Age, BloodGroup, BloodPressure, Diabetics))


class Test_Registration:
    def __init__(self, window):
        self.test_registration = window
        self.test_registration.title('Patient Test Registration')
        self.test_registration.geometry('600x600')
        self.test_registration.resizable(False, False)

        title_label = Label(self.test_registration, text='Patient Test Registration', font=('Times New Roman', 13, 'bold'))
        title_label.pack()

        frame1 = LabelFrame(self.test_registration, text='Patient Details', font=('Times New Roman', 10, 'bold'), relief=RIDGE, bd=10)
        frame1.place(x=20, y=100, width=300, height=110)
        frame2 = LabelFrame(self.test_registration, text='Dates', font=('Times New Roman', 10, 'bold'), relief=RIDGE, bd=10)
        frame2.place(x=350, y=100, width=220, height=110)

        name_label = Label(frame1, text='Name:', font=('Times New Roman', 10, 'bold'))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.entry_name = Entry(frame1, font=('Times New Roman', 10, 'bold'))
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        id_label = Label(frame1, text='ID:', font=('Times New Roman', 10, 'bold'))
        id_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.entry_id = Entry(frame1, font=('Times New Roman', 10, 'bold'))
        self.entry_id.grid(row=1, column=1, padx=5, pady=5)

        issue_label = Label(frame2, text='Issue Date:', font=('Times New Roman', 10, 'bold'))
        issue_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.issue = Entry(frame2, font=('Times New Roman', 10, 'bold'))
        self.issue.grid(row=0, column=1, padx=5, pady=5)

        delivery_label = Label(frame2, text='Delivery Date:', font=('Times New Roman', 10, 'bold'))
        delivery_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.delivery = Entry(frame2, font=('Times New Roman', 10, 'bold'))
        self.delivery.grid(row=1, column=1, padx=5, pady=5)

        self.test = ttk.Combobox(self.test_registration, values=['X-ray', 'Ultrsonography', 'Blood Test', 'Urology Test Package', 'Dengue Test'])
        self.test['state'] = 'readonly'
        self.test.place(x=25, y=250)

        self.add_button = Button(self.test_registration, text='Add', command=self.add)
        self.add_button.place(x=200, y=250)

        # Create a Treeview widget
        self.tree = ttk.Treeview(self.test_registration, columns=('Test Name', 'Cost'))
        self.tree.heading('Test Name', text='Test Name')
        self.tree.heading('Cost', text='Cost')
        self.tree.place(x=20, y=300)
        total_label=Label(self.test_registration,text='Total Cost=').place(x=100,y=560)
        self.total_entry=Entry(self.test_registration)
        self.total_entry.place(x=180,y=560)
        button2=Button(self.test_registration,text='PRINT',command=self.print)
        button2.place(x=400,y=560)
    def print(self):
        if self.entry_name.get()=='':
            messagebox.showerror(title="Error",message="Please enter patient name")
        elif self.entry_id.get()=='':
            messagebox.showerror(title="Error",message="Please enter patient id")
        elif self.issue.get()=='':
            messagebox.showerror(title="Error",message="Please enter issue date")
        elif self.delivery.get() == '':
            messagebox.showerror(title="Error", message="Please enter delivery date")

        elif self.total_entry.get()=='':
            messagebox.showerror(title="Error",message="Please enter total costs")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='Patient_Test_Registration')
            mydb = conn.cursor()
            mydb.execute("insert into PatientTests values(%s,%s,%s,%s,%s)",
                     (self.entry_name.get(), self.entry_id.get(),
                      self.issue.get(), self.delivery.get(),
                      self.total_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo(title='Patient Tests',message='Patient Test Report Successfully updated')


    def add(self):
        test_costs = {
            'X-ray': 300,
            'Ultrsonography': 2500,
            'Blood Test': 100,
            'Urology Test Package': 1500,
            'Dengue Test': 500
        }
        selected_tests = self.test.get().split(',')  # Split selected tests by comma
        print(selected_tests)
        total_cost = 0
        dummy_list = []

        # Iterate over selected test names
        for test_name in selected_tests:
            test_name = test_name.strip()  # Remove leading/trailing spaces
            if test_name in test_costs:
                total_cost += test_costs[test_name]  # Add cost of each selected test
                dummy_list.append(test_name)  # Add selected test to dummy list

        # Insert selected test and its cost into the Treeview widget
        self.tree.insert('', 'end', text='', values=(' , '.join(dummy_list), total_cost))
        print(dummy_list)
login_window=Tk()
a=LoginUI(login_window)
login_window.mainloop()


