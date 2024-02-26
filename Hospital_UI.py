from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
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
        Radiobutton(self.login_window,text='RECEPTIONIST',variable=self.radioButton,value='RECEPTIONIST',bg='#3daaf6').place(x=160,y=140)
        Radiobutton(self.login_window,text='SUPERVISOR',variable=self.radioButton,value='SUPERVISOR',bg='#3daaf6').place(x=320,y=140)
        Radiobutton(self.login_window,text='MANAGER',variable=self.radioButton,value='MANAGER',bg='#3daaf6').place(x=460,y=140)
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
        try:
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
            elif entered_designation=='SUPERVISOR' and result!=None:
                self.login_window.destroy()
                mydb.close()
                supervisor_ui=Tk()
                sui=SupervisorUI(supervisor_ui)
                supervisor_ui.mainloop()

            elif entered_designation=='MANAGER' and result!=None:
                self.login_window.destroy()
                mydb.close()
                manager_ui=Tk()
                mui=ManagerUI(manager_ui)
                manager_ui.mainloop()

            else:
                messagebox.showerror(title='Login Error',message='Invalid Username or Id or Password. ')


        except:
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
        photo_label= Label(self.employee_register_ui, text="Insert ID Photo              :", bg='#fee3fe',font=('Times New Roman', 14, 'bold')).place(x=15, y=410)
        permanent_address_label=Label(self.employee_register_ui,text='Permanent Address :',bg='#fee3fe',font=('Times New Roman',14,'bold')).place(x=15,y=460)

        name_entry= Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=25,textvariable=self.name)
        name_entry.place(x=230,y=210)
        d_o_b_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=15,textvariable=self.birth)
        d_o_b_entry.insert(0,'DD-MM-YYYY')
        d_o_b_entry.place(x=230,y=260)

        father_name_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=25,textvariable=self.father)
        father_name_entry.place(x=230,y=310)
        self.designation_combobox=ttk.Combobox(self.employee_register_ui,values=["DOCTOR",'SUPERVISOR','MANAGER','RECEPTIONIST'],font=('Times New Roman',14,'bold'))
        self.designation_combobox['state']='readonly'
        self.designation_combobox.place(x=230,y=360)
        permanent_address_entry=Entry(self.employee_register_ui,font=('Times New Roman',14,'bold'),width=40,textvariable=self.permanent)
        permanent_address_entry.place(x=38,y=500)



        account_confirm_button=Button(self.employee_register_ui,text='CREATE ACCOUNT',bg='pink',font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE,command=self.create_account)
        account_confirm_button.place(x=1130,y=380)
        modify_button=Button(self.employee_register_ui,text='MODIFY ACCOUNT',bg='pink',font=('Times New Roman',10,'bold'),bd=5,relief=RIDGE)
        modify_button.place(x=1130,y=450)
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
                mydb.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (self.name.get(),self.birth.get(),self.father.get(),self.permanent.get(),self.pass1.get(),self.phone.get(),self.email.get(),self.present.get(),self.number,self.designation_combobox.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo(title='SUCCESS',message='New employee has been created. If you want to modify anything.Please click modify account.')
                self.employee_register_ui.destroy()
            except:
                messagebox.showerror(title='DATABASE CONNECTION ERROR',message='Database Connection Error. Please Connect to Database Properly.')







class DoctorUI:
    def __init__(self,window):
        self.doctor_window=window
        self.doctor_window.title('DOCTOR USER INTERFACE')
        self.doctor_window.geometry('500x500')
        self.doctor_window.resizable(FALSE,FALSE)




class SupervisorUI:
    def __init__(self,window):
        self.supervisor_window=window
        self.supervisor_window.title('SUPERVISOR USER INTERFACE')
        self.supervisor_window.resizable(FALSE, FALSE)
        self.radio_button = IntVar()
        Radiobutton(self.supervisor_window, text='Patient Registration', variable=self.radio_button, value=1).pack()
        Radiobutton(self.supervisor_window, text='Patient Test Registration', variable=self.radio_button,
                    value=2).pack()
        open_button = Button(self.supervisor_window, command=self.open_option).pack()


class ManagerUI:
    def __init__(self,window):
        self.manager_window=window
        self.manager_window.title('MANAGER USER INTERFACE')

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
            patient_test = Patient_Registration(p_t_r)
            p_t_r.mainloop()

        elif self.radio_button.get()==3:
            v_r = Tk()
            v_patient = Patient_Registration(v_r)
            v_r.mainloop()

        else:
            messagebox.showerror(title='Selection Error',message='Please select any of the three option')


class Patient_Registration:
    def __init__(self,window):
        self.patient_registration=window
        self.patient_registration.state('zoomed')
        self.patient_registration.title('Register Patient')
        self.patient_registration.resizable(FALSE,FALSE)
        titile_label=Label(self.patient_registration,text='Register New Patient',font=('Times New Roman',20,'bold')).pack()
        frame1=LabelFrame(self.patient_registration,text='')



class Patient_Details:
    def __init__(self,window):
        self.patient_details=window

class Test_Registration:
    def __init__(self,window):
        self.test_registration=window

login_window=Tk()
a=LoginUI(login_window)
login_window.mainloop()


