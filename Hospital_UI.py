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
        doctor_label= Label(self.employee_register_ui, text="Specialist on                   :", bg='#fee3fe',font=('Times New Roman', 14, 'bold')).place(x=15, y=410)
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
        self.specilization_combobox=ttk.Combobox(self.employee_register_ui,values=['N/A','Cardiologist','Nephrologist','General Medicine','Gynecologist'],font=('Times New Roman',14,'bold'))
        self.specilization_combobox['state']='readonly'
        self.specilization_combobox.place(x=230,y=410)

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
                mydb.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (self.name.get(),self.birth.get(),self.father.get(),self.permanent.get(),self.pass1.get(),self.phone.get(),self.email.get(),self.present.get(),self.number,self.designation_combobox.get(),self.specilization_combobox.get()))
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




class PharmacistUI:
    def __init__(self,window):
        self.supervisor_window=window
        self.supervisor_window.title('SUPERVISOR USER INTERFACE')
        self.supervisor_window.resizable(FALSE, FALSE)
        self.radio_button = IntVar()



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
    def __init__(self,window):
        self.test_registration=window
        self.test_registration.title('Patient Test Registration')
        self.test_registration.geometry('600x600')
        self.test_registration.resizable(FALSE,FALSE)
        title_label=

login_window=Tk()
a=LoginUI(login_window)
login_window.mainloop()


