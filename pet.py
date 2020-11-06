import os
import pandas as pd
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('petshopnew.db')
cur=con.cursor()
from tkinter import *
from tkcalendar import Calendar, DateEntry

window=Tk()
window.geometry('1080x540')
window.title('Start Window')

C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file = "images\\mainbg_1080x540.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


Label(window).place(x=1,y=0)


def start():
    window=Toplevel()
    window.geometry('540x140')
    window.title('Login Window')
    Label(window,text='Username  ',font=("Times New",20)).grid(row=1,column=1)
    user=Entry(window,width=25,font=("Times New",18),bd=5,bg="light grey")
    user.grid(row=1,column=2)
    Label(window,text='Password  ',font=("Times n=New",20)).grid(row=2,column=1)
    pwd=Entry(window,show='*',width=25,font=("Times New",18),bd=5,bg="light grey")
    pwd.grid(row=2,column=2)

    def login():
        if(((int(user.get())!=123) or (int(pwd.get())!=123))):
            showwarning('Login Failed','Incorrect Id Or Password Used Or Mode Not Selected')
        else:
            menu = Toplevel()
            menu.geometry('540x540')
            menu.title('Menu Window')
            C = Canvas(menu, bg="blue", height=250, width=300)
            filename = PhotoImage(file="images\\registerbg_540x540.png")
            background_label = Label(menu, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            background_label.image = filename  # reference to the image
            C.grid(row=0, column=0, rowspan=5, columnspan=3)

            l=Label(menu,text='Dashboard :',font='Times 20 bold',fg='white',bg='black')
            l.grid(row=0,column=0)
            Label(menu).grid(row=1,column=100,rowspan=30)
            # def register():
            #     root=Toplevel()
            #     root.geometry("540x540")
            #     root.title("register details")


            def ownerdetails():
                ownerdetails.service = ""
                ownerdetails.service_number = 0

                def allotservice(*args):
                    ownerdetails.service = q.get()

                    if ownerdetails.service == "GROOMING":
                        ownerdetails.service_number = 2
                    elif ownerdetails.service == "VET CARE":
                        ownerdetails.service_number = 3
                    elif ownerdetails.service == "PET HOTEL":
                        ownerdetails.service_number = 4
                    elif ownerdetails.service == "DAY CAMP":
                        ownerdetails.service_number = 5
                    elif ownerdetails.service == "TRAINING CAMP":
                        ownerdetails.service_number = 6
                    elif ownerdetails.service == "ADOPTION":
                        ownerdetails.service_number = 1

                root = Toplevel()
                root.geometry('540x540')
                root.title('OWNER DETAILS')
                C = Canvas(root, bg="blue", height=250, width=300)
                filename = PhotoImage(file="images\\owner .png")
                background_label = Label(root, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                background_label.image = filename
                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                l = Label(root, text='Register owner details:', font='Times 20 bold')
                l.grid(row=0, column=0)

                l = Label(root, text=' ')
                l.grid(row=1, column=0)

                l = Label(root, text='Owner name: ')
                l.grid(row=2, column=0)
                g = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                g.grid(row=2, column=1)

                l = Label(root, text='Contact Number :').grid(row=3, column=0)
                h = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                h.grid(row=3, column=1)

                l = Label(root, text='Email address :').grid(row=4, column=0)
                i = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                i.grid(row=4, column=1)

                l = Label(root, text='Service Required :').grid(row=5, column=0)

                q = StringVar(root)
                q.set("Select Service")
                q.trace("w", allotservice)
                w = OptionMenu(root, q, "GROOMING", "VET CARE", "PET HOTEL", "DAY CAMP", "TRAINING CAMP","ADOPTION")
                w.grid(row=5, column=1)

                cur.execute("create table if not exists owner(owner_id integer primary key AUTOINCREMENT ,owner_name varchar(20),contact number(10),email varchar(20),service_required varchar(20))")

                def insertowner():
                    cur.execute("insert into owner(owner_name , contact , email , service_required) values(?,?,?,?)", (g.get(), h.get(), i.get(), q.get()))
                    con.commit()
                    showinfo("Owner Details Inserted")

                Button(root, text='Insert Data Of owner', command=insertowner, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=6, column=1, sticky=N + S + E + W)

                def adoption():
                    adoption.speciesreq=""
                    adoption.cost=0
                    def allotspecies(*args):
                        adoption.speciesreq = q.get()
                        if adoption.speciesreq == "dog":
                            adoption.cost = 20000
                        elif adoption.speciesreq == "cat":
                            adoption.cost = 25000
                        elif adoption.speciesreq == "hamster":
                            adoption.cost = 3000
                        elif adoption.speciesreq == "parrot":
                            adoption.cost = 2000
                    root = Toplevel()
                    root.geometry('540x540')
                    root.title('ADOPTION')
                    l = Label(root, text='Register Details :', font='Times 20 bold')
                    l.grid(row=0, column=0)

                    l = Label(root, text=' ')
                    l.grid(row=1, column=0)

                    q = StringVar(root)
                    q.set("Select Species")
                    q.trace("w", allotspecies)
                    w = OptionMenu(root, q, "dog", "cat", "hamster", "parrot")
                    w.grid(row=2, column=1)

                    print(adoption.cost)

                    Label(root, text='Desired Age : ').grid(row=3, column=0)
                    age = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    age.grid(row=3, column=1)

                    cur.execute("select max(owner_id) from owner")
                    currownidtup = cur.fetchone()
                    print(currownidtup)

                    currownid=currownidtup[0]

                    cur.execute("create table if not exists adoption(adpt_id integer primary key AUTOINCREMENT , species_req varchar(20) , desired_age integer , pet_cost integer , owner_id integer , foreign key (owner_id) references owner(owner_id))")

                    def insertadoption():
                        cur.execute("insert into adoption( species_req , desired_age , pet_cost, owner_id ) values(?,?,?,?)", (adoption.speciesreq , age.get(), adoption.cost, currownid))
                        con.commit()
                        showinfo("adoption booked successfully")

                    Button(root, text='book adoption', command=insertadoption, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=4, column=1, sticky=N + S + E + W)

                def petdetails():
                    petdetails.ownerid=0
                    f=ownerdetails.service
                    root = Toplevel()
                    root.geometry('540x540')
                    root.title('PET DETAILS')
                    C = Canvas(root, bg="blue", height=250, width=300)
                    filename = PhotoImage(file="images\\petdetailsbg_540x540.png")
                    background_label = Label(root, image=filename)
                    background_label.place(x=0, y=0, relwidth=1, relheight=1)

                    background_label.image = filename  # reference to the image
                    C.grid(row=0, column=0, rowspan=5, columnspan=3)

                    l = Label(root, text='Register Pet details:', font='Times 20 bold')
                    l.grid(row=0, column=0)

                    l = Label(root, text=' ')
                    l.grid(row=1, column=0)

                    l = Label(root, text='Pet name: ')
                    l.grid(row=2, column=0)

                    c = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    c.grid(row=2, column=1)
                    # xp=c.get()

                    l = Label(root, text='Gender :')
                    l.grid(row=3, column=0)
                    d = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    d.grid(row=3, column=1)
                    l = Label(root, text='Species :')
                    l.grid(row=4, column=0)
                    e = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                    e.grid(row=4, column=1)
                    l = Label(root, text='Service Required :')
                    l.grid(row=5, column=0)

                    l = Label(root, text=f)
                    l.grid(row=5, column=1)

                    cur.execute("select max(owner_id) from owner")
                    currowneridtup = cur.fetchone()
                    print(currowneridtup)

                    petdetails.ownerid = currowneridtup[0]


                    cur.execute("create table if not exists pet(pet_id integer primary key AUTOINCREMENT ,petname varchar(20),species_type varchar(20),gender varchar(6),service_required varchar(20),owner_id number(3),foreign key(owner_id) references owner(owner_id))")

                    def insertpet():
                        cur.execute("insert into pet(petname ,species_type ,gender ,service_required,owner_id) values(?,?,?,?,?)",(c.get(), e.get(), d.get(), f, petdetails.ownerid))
                        con.commit()
                        showinfo("Pet Details Inserted")

                    Button(root, text='Insert Data Of pet', command=insertpet, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=6, column=1, sticky=N + S + E + W)

                    def service():
                        service.currpetid=0
                        def groomingdetails():
                            groomingdetails.cost=0
                            groomingdetails.cal=0
                            groomingdetails.slot=0
                            def groomingcost(*args):
                                groomingservice=f.get()
                                if groomingservice=="HAIR WASH":
                                    groomingdetails.cost=2000
                                elif groomingservice=="FULL BATH":
                                    groomingdetails.cost=4000
                                elif groomingservice=="HAIRCUT":
                                    groomingdetails.cost=3000
                                elif groomingservice=="SPA":
                                    groomingdetails.cost=7000

                            def allotcal(t):
                                groomingdetails.cal=cal.get_date()

                            def groomingslot(*args):
                                groomingdetails.slot=o.get()

                            root = Toplevel()
                            root.geometry('540x540')
                            root.title('GROOMING:')
                            l = Label(root, text='Register Grooming Details :', font='Times 20 bold')
                            l.grid(row=0, column=0)
                            C = Canvas(root, bg="blue", height=250, width=300)
                            filename = PhotoImage(file="images\\grooming.png")
                            background_label = Label(root, image=filename)
                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                            background_label.image = filename
                            C.grid(row=0, column=0, rowspan=5, columnspan=3)

                            l = Label(root, text='Register Grooming details:', font='Times 20 bold')
                            l.grid(row=0, column=0)

                            l = Label(root, text=' ')
                            l.grid(row=1, column=0)

                            l = Label(root, text='Age of Pet: ').grid(row=2, column=0)
                            g = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                            g.grid(row=2,column=1)

                            l = Label(root, text='Salon Menu: ').grid(row=3, column=0)
                            f = StringVar(root)
                            f.set("Select Service")
                            f.trace("w", groomingcost)
                            w = OptionMenu(root, f, "HAIR WASH", "FULL BATH", "HAIRCUT", "SPA")
                            w.grid(row=3, column=1)

                            Label(root, text='date of appointment :').grid(row=4, column=0)
                            cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
                            cal.grid(row=4, column=1)
                            cal.bind("<<DateEntrySelected>>", allotcal)

                            l = Label(root, text='timing slot:').grid(row=5, column=0)
                            o = StringVar(root)
                            o.set("SLOT")
                            o.trace("w", groomingslot)
                            w = OptionMenu(root, o, "9-11", "11-1", "3-5", "5-7")
                            w.grid(row=5, column=1)

                            cur.execute("select max(pet_id) from pet")
                            currpetidtup = cur.fetchone()
                            print(currpetidtup)

                            service.currpetid = currpetidtup[0]

                            cur.execute("create table if not exists grooming(groom_id integer primary key AUTOINCREMENT ,pet_age number(2),salon_menu varchar(20),dateofappointment date,slot varchar(20),cost number(5), pet_id number (3), foreign key(pet_id) references pet(pet_id))")

                            def insertgrooming():
                                cur.execute("insert into grooming( pet_age , salon_menu , dateofappointment , slot , cost , pet_id  ) values( ? , ? , ? , ? , ? , ? )", ( g.get() , f.get() , groomingdetails.cal , groomingdetails.slot , groomingdetails.cost , service.currpetid ))
                                con.commit()
                                showinfo("grooming appointment placed")

                            def showdetails():
                                root = Toplevel()
                                root.geometry('540x540')
                                root.title('GROOMING:')

                                C = Canvas(root, bg="blue", height=250, width=300)
                                filename = PhotoImage(file="images\\details_540x540.png")
                                background_label = Label(root, image=filename)
                                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                background_label.image = filename
                                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                                l = Label(root, text='Grooming Appointment Details :', font='Times 20 bold')
                                l.grid(row=1, column=0)

                                # l = Label(root, text=' ')
                                # l.grid(row=1, column=0)

                                w=int(service.currpetid)

                                # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                                # pet_id = cur.fetchone()

                                cur.execute("select petname from pet where pet_id=?",(w,))
                                pet_name = cur.fetchone()

                                cur.execute("select gender from pet where pet_id=?",(w,))
                                pet_gender = cur.fetchone()

                                cur.execute("select species_type from pet where pet_id=?",(w,))
                                pet_species = cur.fetchone()

                                cur.execute("select service_required from pet where pet_id=?",(w,))
                                pet_service = cur.fetchone()

                                cur.execute("select max(groom_id) from grooming ")
                                currgroomidtup = cur.fetchone()
                                currgroomid=currgroomidtup[0]
                                x=int(currgroomid)

                                cur.execute("select pet_age from grooming where groom_id=?", (x,))
                                grooming_petage= cur.fetchone()

                                cur.execute("select salon_menu from grooming where groom_id=?", (x,))
                                grooming_menu = cur.fetchone()

                                cur.execute("select dateofappointment from grooming where groom_id=?", (x,))
                                grooming_date = cur.fetchone()

                                cur.execute("select slot from grooming where groom_id=?", (x,))
                                grooming_slot = cur.fetchone()

                                cur.execute("select cost from grooming where groom_id=?", (x,))
                                grooming_cost = cur.fetchone()

                                l = Label(root, text='Pet ID :').grid(row=2, column=0)
                                l = Label(root, text=service.currpetid).grid(row=2, column=1)

                                l = Label(root, text='Pet Name').grid(row=3, column=0)
                                l = Label(root, text=pet_name).grid(row=3, column=1)

                                l = Label(root, text='Gender : ').grid(row=4, column=0)
                                l = Label(root, text=pet_gender).grid(row=4, column=1)

                                l = Label(root, text='species : ').grid(row=5, column=0)
                                l = Label(root, text=pet_species).grid(row=5, column=1)

                                l = Label(root, text='Service Opted : ').grid(row=6, column=0)
                                l = Label(root, text=pet_service).grid(row=6, column=1)

                                l = Label(root, text='Grooming ID : ').grid(row=7, column=0)
                                l = Label(root, text=currgroomid).grid(row=7, column=1)

                                l = Label(root, text='Age of Pet : ').grid(row=8, column=0)
                                l = Label(root, text=grooming_petage).grid(row=8, column=1)

                                l = Label(root, text='Salon Menu Opted : ').grid(row=9, column=0)
                                l = Label(root, text=grooming_menu).grid(row=9, column=1)

                                l = Label(root, text='Date of Appointment : ').grid(row=10, column=0)
                                l = Label(root, text=grooming_date).grid(row=10, column=1)

                                l = Label(root, text='Slot Opted : ').grid(row=11, column=0)
                                l = Label(root, text=grooming_slot).grid(row=11, column=1)

                                l = Label(root, text='Estimated Cost : ').grid(row=12, column=0)
                                l = Label(root, text=grooming_cost).grid(row=12, column=1)

                                Button(root, text="Print", command=print_canvas).grid(row=13, column=0)

                            Button(root, text='book grooming appointment', command=insertgrooming, width=25,font=("Times New", 10), bd=5, bg="light grey").grid(row=6, column=1,sticky=N + S + E + W)
                            Button(root, text='Proceed', command=showdetails, width=25,font=("Times New", 10), bd=5, bg="light grey").grid(row=8, column=1,sticky=N + S + E + W)

                        def vetcaredetails():
                            vetcaredetails.cost=0
                            vetcaredetails.dob=0
                            vetcaredetails.vaccinedate=0
                            def allotvetcost(*args):
                                c=aa.get()
                                if c == "VACCINE":
                                    vetcaredetails.cost = 5000
                                elif c == "ROUTINE CHECK-UP":
                                    vetcaredetails.cost = 4000
                                elif c == "FULL CHECK-UP":
                                    vetcaredetails.cost = 8000
                                print(vetcaredetails.cost)
                            def allotdob(d):
                                vetcaredetails.dob=dob.get_date()
                                print(vetcaredetails.dob)
                            def allotvaccine(v):
                                vetcaredetails.vaccinedate=lastvaccine.get_date()
                                print(vetcaredetails.vaccinedate)
                            root = Toplevel()
                            root.geometry('540x540')
                            root.title('VET CARE:')
                            C = Canvas(root, bg="blue", height=250, width=300)
                            filename = PhotoImage(file="images\\vetcare.png")
                            background_label = Label(root, image=filename)
                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                            background_label.image = filename
                            C.grid(row=0, column=0, rowspan=5, columnspan=3)

                            l = Label(root, text='Register Vet Details :', font='Times 20 bold')
                            l.grid(row=0, column=0)

                            l = Label(root, text=' ')
                            l.grid(row=1, column=0)

                            l = Label(root, text='Select Service Required : ')
                            l.grid(row=2, column=0)

                            aa = StringVar(root)
                            aa.set("Select Service")
                            aa.trace("w", allotvetcost)
                            w = OptionMenu(root, aa, "VACCINE", "ROUTINE CHECK-UP", "FULL CHECK-UP")
                            w.grid(row=2, column=1)

                            l = Label(root, text='date of birth of pet :').grid(row=3, column=0)
                            dob = DateEntry(root, date_pattern='yyyy/mm/dd' , width=12, background='darkblue', foreground='white',borderwidth=2)
                            dob.grid(row=3, column=1)
                            dob.bind("<<DateEntrySelected>>", allotdob)

                            l = Label(root, text='latest vaccine :').grid(row=4, column=0)
                            lastvaccine = DateEntry(root, date_pattern='yyyy/mm/dd' ,width=12, background='darkblue', foreground='white',borderwidth=2)
                            lastvaccine.grid(row=4, column=1)
                            lastvaccine.bind("<<DateEntrySelected>>", allotvaccine)

                            Label(root, text='date of appointment :').grid(row=5, column=0)
                            cal = DateEntry(root, width=12, background='darkblue', foreground='white',borderwidth=2)
                            cal.grid(row=5, column=1)

                            cur.execute("select max(pet_id) from pet")
                            currpetidtup = cur.fetchone()
                            print(currpetidtup)

                            service.currpetid = currpetidtup[0]

                            cur.execute("create table if not exists vet_care(vet_id integer primary key AUTOINCREMENT ,medical_care varchar(20) , dob date , latest_vaccine date , dateofappointment date , cost_approx number(6), pet_id number (3), foreign key(pet_id) references pet(pet_id))")

                            def insertvetcare():
                                cur.execute("insert into vet_care( medical_care , dob , latest_vaccine , dateofappointment , cost_approx , pet_id ) values(?,?,?,?,?,?)", ( aa.get(), vetcaredetails.dob , vetcaredetails.vaccinedate , cal.get_date() , vetcaredetails.cost, service.currpetid))
                                con.commit()
                                showinfo("veterinary appointment placed")

                            def showdetails():
                                root = Toplevel()
                                root.geometry('540x540')
                                root.title('VET CARE:')

                                C = Canvas(root, bg="blue", height=250, width=300)
                                filename = PhotoImage(file="images\\details_540x540.png")
                                background_label = Label(root, image=filename)
                                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                background_label.image = filename
                                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                                l = Label(root, text='Vet Care Appointment Details :', font='Times 20 bold')
                                l.grid(row=1, column=0)

                                w=int(service.currpetid)

                                # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                                # pet_id = cur.fetchone()

                                cur.execute("select petname from pet where pet_id=?",(w,))
                                pet_name = cur.fetchone()

                                cur.execute("select gender from pet where pet_id=?",(w,))
                                pet_gender = cur.fetchone()

                                cur.execute("select species_type from pet where pet_id=?",(w,))
                                pet_species = cur.fetchone()

                                cur.execute("select service_required from pet where pet_id=?",(w,))
                                pet_service = cur.fetchone()

                                cur.execute("select max(vet_id) from vet_care ")
                                currvetidtup = cur.fetchone()
                                currvetid=currvetidtup[0]
                                x=int(currvetid)

                                cur.execute("select medical_care from vet_care where vet_id=?", (x,))
                                vet_medical_care= cur.fetchone()

                                cur.execute("select dob from vet_care where vet_id=?", (x,))
                                vet_pet_dob = cur.fetchone()

                                cur.execute("select latest_vaccine from vet_care where vet_id=?", (x,))
                                vet_lastest_vaccine_date = cur.fetchone()

                                cur.execute("select dateofappointment from vet_care where vet_id=?", (x,))
                                vet_dateofappointment = cur.fetchone()

                                cur.execute("select cost_approx from vet_care where vet_id=?", (x,))
                                vet_cost = cur.fetchone()

                                l = Label(root, text='Pet ID :').grid(row=2, column=0)
                                l = Label(root, text=service.currpetid).grid(row=2, column=1)

                                l = Label(root, text='Pet Name').grid(row=3, column=0)
                                l = Label(root, text=pet_name).grid(row=3, column=1)

                                l = Label(root, text='Gender : ').grid(row=4, column=0)
                                l = Label(root, text=pet_gender).grid(row=4, column=1)

                                l = Label(root, text='species : ').grid(row=5, column=0)
                                l = Label(root, text=pet_species).grid(row=5, column=1)

                                l = Label(root, text='Service Opted : ').grid(row=6, column=0)
                                l = Label(root, text=pet_service).grid(row=6, column=1)

                                l = Label(root, text='Vet ID : ').grid(row=7, column=0)
                                l = Label(root, text=currvetid).grid(row=7, column=1)

                                l = Label(root, text='Medical Care : ').grid(row=8, column=0)
                                l = Label(root, text=vet_medical_care).grid(row=8, column=1)

                                l = Label(root, text='Date of Birth').grid(row=9, column=0)
                                l = Label(root, text=vet_pet_dob).grid(row=9, column=1)

                                l = Label(root, text='Latest Vaccine : ').grid(row=10, column=0)
                                l = Label(root, text=vet_lastest_vaccine_date).grid(row=10, column=1)

                                l = Label(root, text='Date of Appointment : ').grid(row=11, column=0)
                                l = Label(root, text=vet_dateofappointment).grid(row=11, column=1)

                                l = Label(root, text='Estimated Cost : ').grid(row=12, column=0)
                                l = Label(root, text=vet_cost).grid(row=12, column=1)

                            Button(root, text='book veterinary appointment', command=insertvetcare, width=25,font=("Times New", 10), bd=5, bg="light grey").grid(row=6, column=1,sticky=N + S + E + W)
                            Button(root, text='Proceed', command=showdetails, width=25,font=("Times New", 10), bd=5, bg="light grey").grid(row=7, column=1,sticky=N + S + E + W)

                        def pethoteldetails():
                            pethoteldetails.accomodation=""
                            pethoteldetails.checkin=0
                            pethoteldetails.checkout=0
                            pethoteldetails.cost=0
                            def allotacco(*args):
                                pethoteldetails.accomodation=acco.get()
                                print(pethoteldetails.accomodation)
                            def allotcheckin(x):
                                pethoteldetails.checkin=checkin.get_date()
                                print(pethoteldetails.checkin)
                            def allotcheckout(y):
                                pethoteldetails.checkout=checkout.get_date()
                                print(pethoteldetails.checkout)
                            # def allotprice():
                            #     days=pethoteldetails.checkout - pethoteldetails.checkin
                            #     pethoteldetails.cost=days*1500
                            #     print(pethoteldetails.cost)
                            root = Toplevel()
                            root.geometry('540x540')
                            root.title('PET HOTEL')
                            C = Canvas(root, bg="blue", height=250, width=300)
                            filename = PhotoImage(file="images\\pethotel_540x540.png")
                            background_label = Label(root, image=filename)
                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                            background_label.image = filename
                            C.grid(row=0, column=0, rowspan=5, columnspan=3)

                            l = Label(root, text='Register Details :', font='Times 20 bold')
                            l.grid(row=0, column=0)

                            l = Label(root, text=' ')
                            l.grid(row=1, column=0)

                            l = Label(root, text='Accomodation :').grid(row=2, column=0)
                            acco = StringVar(root)
                            acco.set("SLOT")
                            acco.trace("w", allotacco)
                            w = OptionMenu(root, acco, "DELUXE", "SUITE", "PRESIDENTIAL SUITE")
                            w.grid(row=2, column=1)

                            l = Label(root, text='check-in-date : ').grid(row=3, column=0)
                            checkin = DateEntry(root, date_pattern='yyyy/mm/dd' , width=12, background='darkblue', foreground='white',borderwidth=2)
                            checkin.grid(row=3, column=1)
                            checkin.bind("<<DateEntrySelected>>", allotcheckin)

                            l = Label(root, text='check-out-date :').grid(row=4, column=0)
                            checkout = DateEntry(root, date_pattern='yyyy/mm/dd' , width=12, background='darkblue', foreground='white',borderwidth=2)
                            checkout.grid(row=4, column=1)
                            checkout.bind("<<DateEntrySelected>>", allotcheckout)

                            Label(root, text='duration of stay :').grid(row=5, column=0)
                            days = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                            days.grid(row=5,column=1)

                            # no_of_days=int(float(days.get()))
                            # pethoteldetails.cost=no_of_days

                            cur.execute("select max(pet_id) from pet")
                            currpetidtup = cur.fetchone()
                            print(currpetidtup)

                            service.currpetid = currpetidtup[0]

                            cur.execute("create table if not exists pet_hotel(resident_id integer primary key AUTOINCREMENT , accomodation varchar(20), check_in date , check_out date , cost_of_stay number(6), pet_id number(3) , foreign key(pet_id) references pet(pet_id))")

                            def insertpethotel():
                                daystup = days.get()
                                days1 = daystup[0]
                                daysnum = int(days1)
                                cost = daysnum * 1500
                                print(cost)
                                cur.execute("insert into pet_hotel(accomodation , check_in , check_out , cost_of_stay , pet_id ) values(?,?,?,?,?)",(pethoteldetails.accomodation , pethoteldetails.checkin , pethoteldetails.checkout , cost , service.currpetid ))
                                con.commit()
                                showinfo("pet hotel booked successfully")

                            def showdetails():
                                root = Toplevel()
                                root.geometry('540x540')
                                root.title('PET HOTEL : ')

                                C = Canvas(root, bg="blue", height=250, width=300)
                                filename = PhotoImage(file="images\\details_540x540.png")
                                background_label = Label(root, image=filename)
                                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                background_label.image = filename
                                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                                l = Label(root, text='Pet Hotel Details :', font='Times 20 bold')
                                l.grid(row=1, column=0)

                                w=int(service.currpetid)

                                # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                                # pet_id = cur.fetchone()

                                cur.execute("select petname from pet where pet_id=?",(w,))
                                pet_name = cur.fetchone()

                                cur.execute("select gender from pet where pet_id=?",(w,))
                                pet_gender = cur.fetchone()

                                cur.execute("select species_type from pet where pet_id=?",(w,))
                                pet_species = cur.fetchone()

                                cur.execute("select service_required from pet where pet_id=?",(w,))
                                pet_service = cur.fetchone()

                                cur.execute("select max(resident_id) from pet_hotel ")
                                currresidentidtup = cur.fetchone()
                                currresidentid=currresidentidtup[0]
                                x=int(currresidentid)

                                cur.execute("select accomodation from pet_hotel where resident_id=?", (x,))
                                pethotel_acco= cur.fetchone()

                                cur.execute("select check_in from pet_hotel where resident_id=?", (x,))
                                pethotel_checkin = cur.fetchone()

                                cur.execute("select check_out from pet_hotel where resident_id=?", (x,))
                                pethotel_checkout = cur.fetchone()

                                cur.execute("select cost_of_stay from pet_hotel where resident_id=?", (x,))
                                pethotel_cost = cur.fetchone()

                                l = Label(root, text='Pet ID :').grid(row=2, column=0)
                                l = Label(root, text=service.currpetid).grid(row=2, column=1)

                                l = Label(root, text='Pet Name').grid(row=3, column=0)
                                l = Label(root, text=pet_name).grid(row=3, column=1)

                                l = Label(root, text='Gender : ').grid(row=4, column=0)
                                l = Label(root, text=pet_gender).grid(row=4, column=1)

                                l = Label(root, text='species : ').grid(row=5, column=0)
                                l = Label(root, text=pet_species).grid(row=5, column=1)

                                l = Label(root, text='Service Opted : ').grid(row=6, column=0)
                                l = Label(root, text=pet_service).grid(row=6, column=1)

                                l = Label(root, text='Resident ID : ').grid(row=7, column=0)
                                l = Label(root, text=currresidentid).grid(row=7, column=1)

                                l = Label(root, text='Accomodation : ').grid(row=8, column=0)
                                l = Label(root, text=pethotel_acco).grid(row=8, column=1)

                                l = Label(root, text='Check-In Date : ').grid(row=9, column=0)
                                l = Label(root, text=pethotel_checkin).grid(row=9, column=1)

                                l = Label(root, text='Check-Out Date : ').grid(row=10, column=0)
                                l = Label(root, text=pethotel_checkout).grid(row=10, column=1)

                                l = Label(root, text='Cost of Stay : ').grid(row=11, column=0)
                                l = Label(root, text=pethotel_cost).grid(row=11, column=1)

                            Button(root, text='book pet hotel', command=insertpethotel, width=25,font=("Times New", 10), bd=5, bg="light grey").grid(row=6, column=1,sticky=N + S + E + W)
                            Button(root, text='proceed', command=showdetails, width=25,font=("Times New", 10), bd=5, bg="light grey").grid(row=8, column=1,sticky=N + S + E + W)

                        def daycampdetails():
                            root = Toplevel()
                            root.geometry('540x540')
                            root.title('DAY CAMP')
                            C = Canvas(root, bg="blue", height=250, width=300)
                            filename = PhotoImage(file="images\\daycamp.png")
                            background_label = Label(root, image=filename)
                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                            background_label.image = filename
                            C.grid(row=0, column=0, rowspan=5, columnspan=3)

                            l = Label(root, text='Register Details :', font='Times 20 bold')
                            l.grid(row=0, column=0)

                            l = Label(root, text=' ')
                            l.grid(row=1, column=0)

                            l = Label(root, text='Activity : ').grid(row=2, column=0)
                            act = StringVar(root)
                            act.set("SLOT")
                            w = OptionMenu(root, act, "PLAY", "SPA", "RECREATION")
                            w.grid(row=2, column=1)

                            Label(root, text='Duration(in hrs) : ').grid(row=3, column=0)
                            dura = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                            dura.grid(row=3,column=1)

                            cost_camp=0
                            # hrs = dura.get()
                            # cost_camp = int(hrs) * 1500

                            cur.execute("select max(pet_id) from pet")
                            currpetidtup = cur.fetchone()
                            print(currpetidtup)

                            service.currpetid = currpetidtup[0]

                            cur.execute("create table if not exists day_camp(daycare_id integer primary key AUTOINCREMENT , activity varchar(20) , duration number(2) , cost number(6) , pet_id number(3) , foreign key(pet_id) references pet(pet_id))")

                            def insertdaycamp():
                                cost=0
                                duratup = dura.get()
                                dura1 = duratup[0]
                                duranum = int(dura1)
                                a=act.get()
                                if a =="PLAY":
                                    cost=duranum*500
                                elif a=="SPA":
                                    cost=duranum*1500
                                elif a=="RECREATION":
                                    cost=duranum*2000
                                cur.execute("insert into day_camp( activity , duration , cost , pet_id ) values(?,?,?,?)", ( act.get() , dura.get() , cost , service.currpetid ))
                                con.commit()
                                showinfo("day camp booked successfully")

                            def showdetails():
                                root = Toplevel()
                                root.geometry('540x540')
                                root.title('DAY CAMP : ')

                                C = Canvas(root, bg="blue", height=250, width=300)
                                filename = PhotoImage(file="images\\details_540x540.png")
                                background_label = Label(root, image=filename)
                                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                background_label.image = filename
                                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                                l = Label(root, text='Day Camp Details :', font='Times 20 bold')
                                l.grid(row=1, column=0)

                                w=int(service.currpetid)

                                # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                                # pet_id = cur.fetchone()

                                cur.execute("select petname from pet where pet_id=?",(w,))
                                pet_name = cur.fetchone()

                                cur.execute("select gender from pet where pet_id=?",(w,))
                                pet_gender = cur.fetchone()

                                cur.execute("select species_type from pet where pet_id=?",(w,))
                                pet_species = cur.fetchone()

                                cur.execute("select service_required from pet where pet_id=?",(w,))
                                pet_service = cur.fetchone()

                                cur.execute("select max(daycare_id) from day_camp ")
                                currdaycampidtup = cur.fetchone()
                                currdaycampid=currdaycampidtup[0]
                                x=int(currdaycampid)

                                cur.execute("select activity from day_camp where daycare_id=?", (x,))
                                daycamp_activity = cur.fetchone()

                                cur.execute("select duration from day_camp where daycare_id=?", (x,))
                                daycamp_duration = cur.fetchone()

                                cur.execute("select cost from day_camp where daycare_id=?", (x,))
                                daycamp_cost = cur.fetchone()

                                l = Label(root, text='Pet ID :').grid(row=2, column=0)
                                l = Label(root, text=service.currpetid).grid(row=2, column=1)

                                l = Label(root, text='Pet Name').grid(row=3, column=0)
                                l = Label(root, text=pet_name).grid(row=3, column=1)

                                l = Label(root, text='Gender : ').grid(row=4, column=0)
                                l = Label(root, text=pet_gender).grid(row=4, column=1)

                                l = Label(root, text='species : ').grid(row=5, column=0)
                                l = Label(root, text=pet_species).grid(row=5, column=1)

                                l = Label(root, text='Service Opted : ').grid(row=6, column=0)
                                l = Label(root, text=pet_service).grid(row=6, column=1)

                                l = Label(root, text='Day Camp ID : ').grid(row=7, column=0)
                                l = Label(root, text=currdaycampid).grid(row=7, column=1)

                                l = Label(root, text='Activity : ').grid(row=8, column=0)
                                l = Label(root, text=daycamp_activity).grid(row=8, column=1)

                                l = Label(root, text='Duration : ').grid(row=9, column=0)
                                l = Label(root, text=daycamp_duration).grid(row=9, column=1)

                                l = Label(root, text='Cost : ').grid(row=10, column=0)
                                l = Label(root, text=daycamp_cost).grid(row=10, column=1)

                            Button(root, text='book day camp', command=insertdaycamp, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=4, column=1, sticky=N + S + E + W)
                            Button(root, text='Proceed', command=showdetails, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=5, column=1, sticky=N + S + E + W)


                        def trainingcampdetails():
                            trainingcampdetails.date=0
                            def allottrainingdate(*args):
                                trainingcampdetails.date=traindate.get_date()
                            root = Toplevel()
                            root.geometry('540x540')
                            root.title('TRAINING CAMP')
                            C = Canvas(root, bg="blue", height=250, width=300)
                            filename = PhotoImage(file="images\\training.png")
                            background_label = Label(root, image=filename)
                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                            background_label.image = filename
                            C.grid(row=0, column=0, rowspan=5, columnspan=3)

                            l = Label(root, text='Register Details :', font='Times 20 bold')
                            l.grid(row=0, column=0)

                            l = Label(root, text=' ')
                            l.grid(row=1, column=0)

                            l = Label(root, text='Package').grid(row=2, column=0)
                            pack = StringVar(root)
                            pack.set("SLOT")
                            w = OptionMenu(root, pack, "FULL TRAINING", "COMMAND TRAINING", "COMPLETE TRAINING")
                            w.grid(row=2, column=1)

                            l = Label(root, text='Date Slot :').grid(row=3, column=0)
                            traindate = DateEntry(root, width=12, background='darkblue', foreground='white',borderwidth=2)
                            traindate.grid(row=3, column=1)
                            traindate.bind("<<DateEntrySelected>>", allottrainingdate())

                            cur.execute("select max(pet_id) from pet")
                            currpetidtup = cur.fetchone()
                            print(currpetidtup)

                            service.currpetid = currpetidtup[0]

                            #
                            # if pack == "FULL TRAINING" :
                            #     traincost=50000
                            # elif pack == "COMMAND TRAINING" :
                            #     traincost=30000
                            # elif pack == "COMPLETE TRAINING" :
                            #     traincost=70000
                            #

                            cur.execute("create table if not exists training_camp(training_id integer primary key AUTOINCREMENT , package varchar(20) , train_date date , cost number(5) , trainer_id integer , pet_id number(3) , foreign key(pet_id) references pet(pet_id))")

                            def inserttrainingcamp():
                                cost=0
                                ttid=0
                                o=""
                                o=pack.get()
                                print(o)
                                if o =="FULL TRAINING":
                                    cost=20000
                                    ttid=1
                                elif o =="COMMAND TRAINING":
                                    cost=30000
                                    ttid=2
                                elif o =="COMPLETE TRAINING":
                                    cost=50000
                                    ttid=3
                                cur.execute("insert into training_camp( package , train_date , cost , trainer_id , pet_id ) values(?,?,?,?,?)", (pack.get() , trainingcampdetails.date , cost , ttid , service.currpetid ))
                                con.commit()
                                showinfo("training camp booked successfully")

                            def showdetails():
                                root = Toplevel()
                                root.geometry('540x540')
                                root.title('TRAINING CAMP : ')

                                C = Canvas(root, bg="blue", height=250, width=300)
                                filename = PhotoImage(file="images\\details_540x540.png")
                                background_label = Label(root, image=filename)
                                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                background_label.image = filename
                                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                                l = Label(root, text='Training Camp Appointment Details :', font='Times 20 bold')
                                l.grid(row=1, column=0)

                                w=int(service.currpetid)

                                # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                                # pet_id = cur.fetchone()

                                cur.execute("select petname from pet where pet_id=?",(w,))
                                pet_name = cur.fetchone()

                                cur.execute("select gender from pet where pet_id=?",(w,))
                                pet_gender = cur.fetchone()

                                cur.execute("select species_type from pet where pet_id=?",(w,))
                                pet_species = cur.fetchone()

                                cur.execute("select service_required from pet where pet_id=?",(w,))
                                pet_service = cur.fetchone()

                                cur.execute("select max(training_id) from training_camp")
                                currtrainingcampidtup = cur.fetchone()
                                currtrainingcampid=currtrainingcampidtup[0]
                                x=int(currtrainingcampid)

                                cur.execute("select package from training_camp where training_id=?", (x,))
                                trainingcamp_activity = cur.fetchone()

                                cur.execute("select train_date from training_camp where training_id=?", (x,))
                                trainingcamp_date = cur.fetchone()

                                cur.execute("select cost from training_camp where training_id=?", (x,))
                                trainingcamp_cost = cur.fetchone()

                                l = Label(root, text='Pet ID :').grid(row=2, column=0)
                                l = Label(root, text=service.currpetid).grid(row=2, column=1)

                                l = Label(root, text='Pet Name').grid(row=3, column=0)
                                l = Label(root, text=pet_name).grid(row=3, column=1)

                                l = Label(root, text='Gender : ').grid(row=4, column=0)
                                l = Label(root, text=pet_gender).grid(row=4, column=1)

                                l = Label(root, text='species : ').grid(row=5, column=0)
                                l = Label(root, text=pet_species).grid(row=5, column=1)

                                l = Label(root, text='Service Opted : ').grid(row=6, column=0)
                                l = Label(root, text=pet_service).grid(row=6, column=1)

                                l = Label(root, text='Training ID : ').grid(row=7, column=0)
                                l = Label(root, text=currtrainingcampid).grid(row=7, column=1)

                                l = Label(root, text='Activity : ').grid(row=8, column=0)
                                l = Label(root, text=trainingcamp_activity).grid(row=8, column=1)

                                l = Label(root, text='Date Slot : ').grid(row=9, column=0)
                                l = Label(root, text=trainingcamp_date).grid(row=9, column=1)

                                l = Label(root, text='Cost : ').grid(row=10, column=0)
                                l = Label(root, text=trainingcamp_cost).grid(row=10, column=1)
                            Button(root, text='book training camp', command=inserttrainingcamp, width=20, height=1, font=("Times New", 10),bd=5, bg="light grey").grid(row=4, column=1, sticky=N + S + E + W)
                            Button(root, text='Proceed', command=showdetails, width=20, height=1, font=("Times New", 10),bd=5, bg="light grey").grid(row=5, column=1, sticky=N + S + E + W)

                        if ownerdetails.service_number == 2 :
                            groomingdetails()
                        elif ownerdetails.service_number == 3 :
                            vetcaredetails()
                        elif ownerdetails.service_number == 4 :
                            pethoteldetails()
                        elif ownerdetails.service_number == 5 :
                            daycampdetails()
                        elif ownerdetails.service_number == 6 :
                            trainingcampdetails()

                    Button(root, text='proceed to service details', command=service, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=7, column=1, sticky=N + S + E + W)

                Button(root, text='proceed to enter more data', command=lambda:[adoption() if ownerdetails.service_number==1 else petdetails()], width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=7, column=1, sticky=N + S + E + W)

            def checkdetails():
                root = Toplevel()
                root.geometry('720x540')
                root.title('CHECK DETAILS')

                # C = Canvas(root, bg="blue", height=250, width=300)
                # filename = PhotoImage(file="images\\details_2_720x540.png.png")
                # background_label = Label(root, image=filename)
                # background_label.place(x=0, y=0, relwidth=1, relheight=1)
                #
                # background_label.image = filename
                # C.grid(row=0, column=0, rowspan=5, columnspan=3)

                l = Label(root, text='Check Appointment Details : ', font='Times 20 bold')
                l.grid(row=2, column=0)

                l = Label(root, text='Enter Pet ID : ', font='Times 20 bold')
                l.grid(row=3, column=0)
                c = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                c.grid(row=3, column=1)

                def showdetails():
                    showdetails.service=""
                    showdetails.i = c.get()
                    cur.execute("select service_required from pet where pet_id=?", (showdetails.i,))
                    servicetup = cur.fetchone()
                    showdetails.service=servicetup[0]



                    def groomingdetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('GROOMING:')
                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\details_540x540.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Grooming Appointment Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = showdetails.i

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        cur.execute("select owner_id from pet where pet_id=?", (w,))
                        owneridtup = cur.fetchone()
                        ownerid = owneridtup[0]
                        y = int(ownerid)

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select groom_id from grooming where pet_id=?",(w,))
                        petidtup = cur.fetchone()
                        petid = petidtup[0]
                        x = petid

                        cur.execute("select pet_age from grooming where groom_id=?", (x,))
                        grooming_petage = cur.fetchone()

                        cur.execute("select salon_menu from grooming where groom_id=?", (x,))
                        grooming_menu = cur.fetchone()

                        cur.execute("select dateofappointment from grooming where groom_id=?", (x,))
                        grooming_date = cur.fetchone()

                        cur.execute("select slot from grooming where groom_id=?", (x,))
                        grooming_slot = cur.fetchone()

                        cur.execute("select cost from grooming where groom_id=?", (x,))
                        grooming_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Grooming ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Age of Pet : ').grid(row=12, column=0)
                        l = Label(root, text=grooming_petage).grid(row=12, column=1)

                        l = Label(root, text='Salon Menu Opted : ').grid(row=13, column=0)
                        l = Label(root, text=grooming_menu).grid(row=13, column=1)

                        l = Label(root, text='Date of Appointment : ').grid(row=14, column=0)
                        l = Label(root, text=grooming_date).grid(row=14, column=1)

                        l = Label(root, text='Slot Opted : ').grid(row=15, column=0)
                        l = Label(root, text=grooming_slot).grid(row=15, column=1)

                        l = Label(root, text='Estimated Cost : ').grid(row=16, column=0)
                        l = Label(root, text=grooming_cost).grid(row=16, column=1)

                    def vetcaredetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('VET CARE:')

                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\details_540x540.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Vet Care Appointment Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = showdetails.i

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        cur.execute("select owner_id from pet where pet_id=?", (w,))
                        owneridtup = cur.fetchone()
                        ownerid = owneridtup[0]
                        y = int(ownerid)

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select vet_id from vet_care where pet_id=?",(w,))
                        vetidtup = cur.fetchone()
                        vetid = vetidtup[0]
                        x = vetid

                        cur.execute("select medical_care from vet_care where vet_id=?", (x,))
                        vet_medical_care = cur.fetchone()

                        cur.execute("select dob from vet_care where vet_id=?", (x,))
                        vet_pet_dob = cur.fetchone()

                        cur.execute("select latest_vaccine from vet_care where vet_id=?", (x,))
                        vet_lastest_vaccine_date = cur.fetchone()

                        cur.execute("select dateofappointment from vet_care where vet_id=?", (x,))
                        vet_dateofappointment = cur.fetchone()

                        cur.execute("select cost_approx from vet_care where vet_id=?", (x,))
                        vet_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Vet ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Medical Care : ').grid(row=12, column=0)
                        l = Label(root, text=vet_medical_care).grid(row=12, column=1)

                        l = Label(root, text='Date of Birth').grid(row=13, column=0)
                        l = Label(root, text=vet_pet_dob).grid(row=13, column=1)

                        l = Label(root, text='Latest Vaccine : ').grid(row=14, column=0)
                        l = Label(root, text=vet_lastest_vaccine_date).grid(row=14, column=1)

                        l = Label(root, text='Date of Appointment : ').grid(row=15, column=0)
                        l = Label(root, text=vet_dateofappointment).grid(row=15, column=1)

                        l = Label(root, text='Estimated Cost : ').grid(row=16, column=0)
                        l = Label(root, text=vet_cost).grid(row=16, column=1)

                    def pethoteldetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('PET HOTEL : ')

                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\details_540x540.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Pet Hotel Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = showdetails.i

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        cur.execute("select owner_id from pet where pet_id=?", (w,))
                        owneridtup = cur.fetchone()
                        ownerid = owneridtup[0]
                        y = int(ownerid)

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select resident_id from pet_hotel where pet_id=?",(w,))
                        residentidtup = cur.fetchone()
                        residentid = residentidtup[0]
                        x = residentid

                        cur.execute("select accomodation from pet_hotel where resident_id=?", (x,))
                        pethotel_acco = cur.fetchone()

                        cur.execute("select check_in from pet_hotel where resident_id=?", (x,))
                        pethotel_checkin = cur.fetchone()

                        cur.execute("select check_out from pet_hotel where resident_id=?", (x,))
                        pethotel_checkout = cur.fetchone()

                        cur.execute("select cost_of_stay from pet_hotel where resident_id=?", (x,))
                        pethotel_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Resident ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Accomodation : ').grid(row=12, column=0)
                        l = Label(root, text=pethotel_acco).grid(row=12, column=1)

                        l = Label(root, text='Check-In Date : ').grid(row=13, column=0)
                        l = Label(root, text=pethotel_checkin).grid(row=13, column=1)

                        l = Label(root, text='Check-Out Date : ').grid(row=14, column=0)
                        l = Label(root, text=pethotel_checkout).grid(row=14, column=1)

                        l = Label(root, text='Cost of Stay : ').grid(row=15, column=0)
                        l = Label(root, text=pethotel_cost).grid(row=15, column=1)

                    def daycampdetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('DAY CAMP : ')

                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\details_540x540.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Day Camp Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = showdetails.i

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        cur.execute("select owner_id from pet where pet_id=?", (w,))
                        owneridtup = cur.fetchone()
                        ownerid = owneridtup[0]
                        y = int(ownerid)

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select daycare_id from day_camp where pet_id=?",(w,))
                        daycampidtup = cur.fetchone()
                        daycampid = daycampidtup[0]
                        x = daycampid

                        cur.execute("select activity from day_camp where daycare_id=?", (x,))
                        daycamp_activity = cur.fetchone()

                        cur.execute("select duration from day_camp where daycare_id=?", (x,))
                        daycamp_duration = cur.fetchone()

                        cur.execute("select cost from day_camp where daycare_id=?", (x,))
                        daycamp_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Day Camp ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Activity : ').grid(row=12, column=0)
                        l = Label(root, text=daycamp_activity).grid(row=12, column=1)

                        l = Label(root, text='Duration : ').grid(row=13, column=0)
                        l = Label(root, text=daycamp_duration).grid(row=13, column=1)

                        l = Label(root, text='Cost : ').grid(row=14, column=0)
                        l = Label(root, text=daycamp_cost).grid(row=14, column=1)

                    def trainingcampdetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('TRAINING CAMP : ')

                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\details_540x540.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Training Camp Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = showdetails.i

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        cur.execute("select owner_id from pet where pet_id=?", (w,))
                        owneridtup = cur.fetchone()
                        ownerid = owneridtup[0]
                        y = int(ownerid)

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select training_id from training_camp where pet_id=?",(w,))
                        trainingcampidtup = cur.fetchone()
                        trainingcampid = trainingcampidtup[0]
                        x = trainingcampid

                        cur.execute("select package from training_camp where training_id=?", (x,))
                        trainingcamp_activity = cur.fetchone()

                        cur.execute("select train_date from training_camp where training_id=?", (x,))
                        trainingcamp_date = cur.fetchone()

                        cur.execute("select cost from training_camp where training_id=?", (x,))
                        trainingcamp_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Training ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Activity : ').grid(row=12, column=0)
                        l = Label(root, text=trainingcamp_activity).grid(row=12, column=1)

                        l = Label(root, text='Date Slot : ').grid(row=13, column=0)
                        l = Label(root, text=trainingcamp_date).grid(row=13, column=1)

                        l = Label(root, text='Cost : ').grid(row=14, column=0)
                        l = Label(root, text=trainingcamp_cost).grid(row=14, column=1)

                    if showdetails.service=='GROOMING':
                        groomingdetails()
                    elif showdetails.service=='VET CARE':
                        vetcaredetails()
                    elif showdetails.service=='PET HOTEL':
                        pethoteldetails()
                    elif showdetails.service=='DAY CAMP':
                        daycampdetails()
                    elif showdetails.service=='TRAINING CAMP':
                        trainingcampdetails()
                Button(root, text='Proceed', command=showdetails, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=7, column=1, sticky=N + S + E + W)

            def updatedetails():
                updatedetails.service =''
                updatedetails.petid=0
                updatedetails.oid=''
                root = Toplevel()
                root.geometry('540x540')
                root.title('UPDATE DETAILS')

                C = Canvas(root, bg="blue", height=250, width=300)
                filename = PhotoImage(file="images\\details_540x540.png")
                background_label = Label(root, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                background_label.image = filename
                C.grid(row=0, column=0, rowspan=5, columnspan=3)

                l = Label(root, text='UPDATE DETAILS :', font='Times 20 bold')
                l.grid(row=1, column=0)

                l = Label(root, text='Enter Pet_id : ')
                l.grid(row=2, column=0)
                zz = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                zz.grid(row=2, column=1)
                def updatede():
                    updatedetails.petid = zz.get()
                    cur.execute("select service_required from pet where pet_id=?", (updatedetails.petid,))
                    servicetup = cur.fetchone()
                    updatedetails.service = servicetup[0]
                    cur.execute("select owner_id from pet where pet_id=?", (updatedetails.petid,))
                    owneridtup = cur.fetchone()
                    ownerid = owneridtup[0]
                    updatedetails.oid = int(ownerid)

                    def changeowner_name():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('OOWNER NAME')
                        l = Label(root, text='Enter New Owner Name : ')
                        l.grid(row=2, column=0)
                        oname = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        oname.grid(row=2, column=1)

                        def updateoname():
                            print(updatedetails.oid)
                            oname1=oname.get()
                            print(oname1)
                            cur.execute("update owner set owner_name=? where owner_id=?",(oname1, updatedetails.oid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updateoname, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changeowner_number():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('OOWNER CONTACT NUMBER')
                        l = Label(root, text='Enter New Owner Contact Number : ')
                        l.grid(row=2, column=0)
                        onumber = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        onumber.grid(row=2, column=1)

                        def updateonumber():
                            cur.execute("update owner set contact=? where owner_id=?",(onumber.get(), updatedetails.oid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updateonumber, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changeowner_email():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('OWNER EMAIL')
                        l = Label(root, text='Enter New Owner Email : ')
                        l.grid(row=2, column=0)
                        oemail = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        oemail.grid(row=2, column=1)

                        def updateoemail():
                            cur.execute("update owner set email=? where owner_id=?", (oemail.get(), updatedetails.oid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updateoemail, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changepet_name():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('PET NAME')
                        l = Label(root, text='Enter New Pet Name : ')
                        l.grid(row=2, column=0)
                        pname = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        pname.grid(row=2, column=1)

                        def updatepname():
                            cur.execute("update pet set petname=? where owner_id=?", (pname.get(), updatedetails.oid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatepname, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changepet_species():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('PET SPECIES')
                        l = Label(root, text='Enter New Pet Species : ')
                        l.grid(row=2, column=0)
                        pspecies = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        pspecies.grid(row=2, column=1)

                        def updatepspecies():
                            cur.execute("update pet set species_type=? where owner_id=?",(pspecies.get(), updatedetails.oid,))
                            con.commit()
                        Button(root, text='Confirm Changes', command=updatepspecies, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changepet_gender():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('GENDER')
                        l = Label(root, text='Enter New Gender : ')
                        l.grid(row=2, column=0)
                        pgender = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        pgender.grid(row=2, column=1)

                        def updatepgender():
                            cur.execute("update pet set gender=? where owner_id=?", (pgender.get(), updatedetails.oid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatepgender, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changegrooming_age():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('PET AGE')
                        l = Label(root, text='Enter New Pet Age : ')
                        l.grid(row=2, column=0)
                        gage = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        gage.grid(row=2, column=1)

                        def updategage():
                            cur.execute("update grooming set pet_age=? where pet_id=?",(gage.get(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updategage, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changegrooming_salon():
                        changegrooming_age.cost = 0

                        def groomingcost_change(*args):
                            groomingservice = gmenu.get()
                            if groomingservice == "HAIR WASH":
                                changegrooming_age.cost = 2000
                            elif groomingservice == "FULL BATH":
                                changegrooming_age.cost = 4000
                            elif groomingservice == "HAIRCUT":
                                changegrooming_age.cost = 3000
                            elif groomingservice == "SPA":
                                changegrooming_age.cost = 7000

                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('SALON MENU')
                        l = Label(root, text='Enter New Salon Menu : ')
                        l.grid(row=2, column=0)
                        gmenu = StringVar(root)
                        gmenu.set("Select Service")
                        gmenu.trace("w", groomingcost_change)
                        w = OptionMenu(root, gmenu, "HAIR WASH", "FULL BATH", "HAIRCUT", "SPA")
                        w.grid(row=2, column=1)

                        def updategmenu():
                            cur.execute("update grooming set salon_menu=? , cost=? where pet_id=?",(gmenu.get(), changegrooming_age.cost, updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updategmenu, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changegrooming_date():
                        changegrooming_date.date = 0

                        def changegroomingdslot(t):
                            changegrooming_date.date = gdate.get_date()
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('DATE OF APPOINTMENT')
                        l = Label(root, text='Enter New Appointment Date : ')
                        l.grid(row=2, column=0)
                        Label(root, text='date of appointment :').grid(row=4, column=0)
                        gdate = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
                        gdate.grid(row=4, column=1)
                        gdate.bind("<<DateEntrySelected>>", changegroomingdslot)

                        def updategdate():
                            cur.execute("update grooming set dateofappointment=? where pet_id=?",(changegrooming_date.date, updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updategdate, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changegrooming_slot():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('SLOT')
                        l = Label(root, text='Enter New Slot : ')
                        l.grid(row=2, column=0)
                        l = Label(root, text='timing slot').grid(row=3, column=0)
                        gslot = StringVar(root)
                        gslot.set("SLOT")
                        w = OptionMenu(root, gslot, "9AM-11AM", "11AM-1PM", "3PM-5PM", "5PM-7PM")
                        w.grid(row=3, column=1)

                        def updategslot():
                            cur.execute("update grooming set slot=? where pet_id=?",(gslot.get(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updategslot, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changevetcare_medical():
                        changevetcare_medical.cost = 0
                        def vetcostchange(*args):
                            c = vcare.get()
                            if c == "VACCINE":
                                changevetcare_medical.cost = 5000
                            elif c == "ROUTINE CHECK-UP":
                                changevetcare_medical.cost = 4000
                            elif c == "FULL CHECK-UP":
                                changevetcare_medical.cost = 8000

                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('MEDICAL CARE')
                        l = Label(root, text='Enter New Medical Care : ')
                        l.grid(row=2, column=0)
                        vcare = StringVar(root)
                        vcare.set("Select Service")
                        vcare.trace("w", vetcostchange)
                        w = OptionMenu(root, vcare, "VACCINE", "ROUTINE CHECK-UP", "FULL CHECK-UP")
                        w.grid(row=2, column=1)

                        def updatevcare():
                            cur.execute("update vet_care set medical_care=?,cost_approx=? where pet_id=?",(vcare.get(), changevetcare_medical.cost, updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatevcare, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changevetcare_dob():
                        changevetcare_dob.dob = 0
                        def vdobchange(d):
                            changevetcare_dob.dob = vdob.get_date()
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('DATE OF BIRTH')
                        l = Label(root, text='Enter New DOB : ')
                        l.grid(row=2, column=0)
                        vdob = DateEntry(root, date_pattern='yyyy/mm/dd', width=12, background='darkblue',foreground='white', borderwidth=2)
                        vdob.grid(row=2, column=1)
                        vdob.bind("<<DateEntrySelected>>", vdobchange)

                        def updatevdob():
                            cur.execute("update vet_care set dob=? where pet_id=?",(changevetcare_dob.dob, updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatevdob, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changevetcare_lastvaccine():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('LATEST VACCINE')
                        l = Label(root, text='Enter New Latest Vaccine : ')
                        l.grid(row=2, column=0)
                        vvaccine = DateEntry(root, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                                             foreground='white', borderwidth=2)
                        vvaccine.grid(row=4, column=1)

                        def updatevvaccine():
                            cur.execute("update vet_care set latest_vaccine=? where pet_id=?",(vvaccine.get_date(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatevvaccine, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changevetcare_appointment():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('DATE OF APPOINTMENT')
                        l = Label(root, text='Enter New Appointment Date : ')
                        l.grid(row=2, column=0)
                        vappoint = DateEntry(root, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                                             foreground='white', borderwidth=2)
                        vappoint.grid(row=4, column=1)

                        def updatevappoint():
                            cur.execute("update vet_care set dateofappointment=? where pet_id=?",(vappoint.get_date(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatevappoint, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changepethotel_acco():
                        changepethotel_acco.acco = ""

                        def allotaccoupdate(*args):
                            changepethotel_acco.acco = phacco.get()

                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('ACCOMODATION')
                        l = Label(root, text='Enter New Accomodation : ')
                        l.grid(row=2, column=0)
                        phacco = StringVar(root)
                        phacco.set("SLOT")
                        phacco.trace("w", allotaccoupdate)
                        w = OptionMenu(root, phacco, "DELUXE", "SUITE", "PRESIDENTIAL SUITE")
                        w.grid(row=2, column=1)

                        def updatephacco():
                            cur.execute("update pet_hotel set accomodation=? where pet_id=?",(changepethotel_acco.acco, updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatephacco, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changepethotel_cin():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('CHECK-IN DATE')
                        l = Label(root, text='Enter New Check-In Date : ')
                        l.grid(row=2, column=0)
                        phcheckin = DateEntry(root, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                                              foreground='white', borderwidth=2)
                        phcheckin.grid(row=2, column=1)

                        def updatepcin():
                            cur.execute("update pet_hotel set check_in=? where pet_id=?",(phcheckin.get_date(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatepcin, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changepethotel_cout():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('CHECK-OUT DATE')
                        l = Label(root, text='Enter New Check-Out Date : ')
                        l.grid(row=2, column=0)
                        phcheckout = DateEntry(root, date_pattern='yyyy/mm/dd', width=12, background='darkblue',foreground='white', borderwidth=2)
                        phcheckout.grid(row=2, column=1)

                        def updatepcout():
                            cur.execute("update pet_hotel set check_out=? where pet_id=?",(phcheckout.get_date(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatepcout, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changedaycamp_duration():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('DURATION')
                        l = Label(root, text='Enter New Duration : ')
                        l.grid(row=2, column=0)
                        dcdura = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light grey")
                        dcdura.grid(row=2, column=1)

                        def updatedcdura():
                            cost = 0
                            duratup = dura.get()
                            dura1 = duratup[0]
                            duranum = int(dura1)
                            cur.execute("select duration from day_camp where daycare_id=?", (x,))
                            daycamp_dura = cur.fetchone()
                            a = daycamp_dura
                            if a == "PLAY":
                                cost = duranum * 500
                            elif a == "SPA":
                                cost = duranum * 1500
                            elif a == "RECREATION":
                                cost = duranum * 2000
                            cur.execute("update day_camp set duration=?,cost=? where pet_id=?",(dcdura.get(), cost, updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatedcdura, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def changetrainingcamp_date():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('TRAIN DATE')
                        l = Label(root, text='Enter New Train Date : ')
                        l.grid(row=2, column=0)
                        tcdate = DateEntry(root, date_pattern='yyyy/mm/dd', width=12, background='darkblue',foreground='white', borderwidth=2)
                        tcdate.grid(row=2, column=1)

                        def updatetcdate():
                            cur.execute("update training_camp set train_date=? where pet_id=?",(tcdate.get_date(), updatedetails.petid,))
                            con.commit()

                        Button(root, text='Confirm Changes', command=updatetcdate, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

                    def groomingdetails():
                        print(updatedetails.petid)
                        root = Toplevel()
                        root.geometry('720x720')
                        root.title('GROOMING:')

                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\grooming_720x720.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Grooming Appointment Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = updatedetails.petid

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        y=updatedetails.oid

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select groom_id from grooming where pet_id=?",(w,))
                        petidtup = cur.fetchone()
                        petid = petidtup[0]
                        x = petid

                        cur.execute("select pet_age from grooming where groom_id=?", (x,))
                        grooming_petage = cur.fetchone()

                        cur.execute("select salon_menu from grooming where groom_id=?", (x,))
                        grooming_menu = cur.fetchone()

                        cur.execute("select dateofappointment from grooming where groom_id=?", (x,))
                        grooming_date = cur.fetchone()

                        cur.execute("select slot from grooming where groom_id=?", (x,))
                        grooming_slot = cur.fetchone()

                        cur.execute("select cost from grooming where groom_id=?", (x,))
                        grooming_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)
                        Button(root, text='Change',command=changeowner_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)
                        Button(root, text='Change',command=changeowner_number, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=4, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)
                        Button(root, text='Change',command=changeowner_email, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=5, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)
                        Button(root, text='Change',command=changepet_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=7, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)
                        Button(root, text='Change',command=changepet_gender, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=8, column=2, sticky=N + S + E + W)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)
                        Button(root, text='Change',command=changepet_species, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=9, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Grooming ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Age of Pet : ').grid(row=12, column=0)
                        l = Label(root, text=grooming_petage).grid(row=12, column=1)
                        Button(root, text='Change',command=changegrooming_age, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=12, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Salon Menu Opted : ').grid(row=13, column=0)
                        l = Label(root, text=grooming_menu).grid(row=13, column=1)
                        Button(root, text='Change',command=changegrooming_salon, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=13, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Date of Appointment : ').grid(row=14, column=0)
                        l = Label(root, text=grooming_date).grid(row=14, column=1)
                        Button(root, text='Change',command=changegrooming_date, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=14, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Slot Opted : ').grid(row=15, column=0)
                        l = Label(root, text=grooming_slot).grid(row=15, column=1)
                        Button(root, text='Change',command=changegrooming_slot, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=15, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Estimated Cost : ').grid(row=16, column=0)
                        l = Label(root, text=grooming_cost).grid(row=16, column=1)

                    def vetcaredetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('VET CARE:')

                        C = Canvas(root, bg="blue", height=250, width=300)
                        filename = PhotoImage(file="images\\grooming_720x720.png")
                        background_label = Label(root, image=filename)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        background_label.image = filename
                        C.grid(row=0, column=0, rowspan=5, columnspan=3)

                        l = Label(root, text='Vet Care Appointment Details :', font='Times 20 bold')
                        l.grid(row=1, column=0)

                        w = updatedetails.petid

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        y=updatedetails.oid

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select vet_id from vet_care where pet_id=?",(w,))
                        vetidtup = cur.fetchone()
                        vetid = vetidtup[0]
                        x = vetid

                        cur.execute("select medical_care from vet_care where vet_id=?", (x,))
                        vet_medical_care = cur.fetchone()

                        cur.execute("select dob from vet_care where vet_id=?", (x,))
                        vet_pet_dob = cur.fetchone()

                        cur.execute("select latest_vaccine from vet_care where vet_id=?", (x,))
                        vet_lastest_vaccine_date = cur.fetchone()

                        cur.execute("select dateofappointment from vet_care where vet_id=?", (x,))
                        vet_dateofappointment = cur.fetchone()

                        cur.execute("select cost_approx from vet_care where vet_id=?", (x,))
                        vet_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)
                        Button(root, text='Change', command=changeowner_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)
                        Button(root, text='Change', command=changeowner_number, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=4, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)
                        Button(root, text='Change', command=changeowner_email, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=5, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)
                        Button(root, text='Change', command=changepet_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=7, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)
                        Button(root, text='Change', command=changepet_gender, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=8, column=2, sticky=N + S + E + W)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)
                        Button(root, text='Change', command=changepet_species, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=9, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Vet ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Medical Care : ').grid(row=12, column=0)
                        l = Label(root, text=vet_medical_care).grid(row=12, column=1)
                        Button(root, text='Change',command=changevetcare_medical, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=12, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Date of Birth').grid(row=13, column=0)
                        l = Label(root, text=vet_pet_dob).grid(row=13, column=1)
                        Button(root, text='Change',command=changevetcare_dob, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=13, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Latest Vaccine : ').grid(row=14, column=0)
                        l = Label(root, text=vet_lastest_vaccine_date).grid(row=14, column=1)
                        Button(root, text='Change', command=changevetcare_lastvaccine, width=25, font=("Times New", 10), bd=5, bg="light grey").grid(row=14, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Date of Appointment : ').grid(row=15, column=0)
                        l = Label(root, text=vet_dateofappointment).grid(row=15, column=1)
                        Button(root, text='Change', command=changevetcare_appointment, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=15, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Estimated Cost : ').grid(row=16, column=0)
                        l = Label(root, text=vet_cost).grid(row=16, column=1)

                    def pethoteldetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('PET HOTEL : ')
                        l = Label(root, text='Vet Care Appointment Details :', font='Times 20 bold')
                        l.grid(row=0, column=0)

                        l = Label(root, text=' ')
                        l.grid(row=1, column=0)

                        w = updatedetails.petid

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        y=updatedetails.oid

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select resident_id from pet_hotel where pet_id=?",(w,))
                        residentidtup = cur.fetchone()
                        residentid = residentidtup[0]
                        x = residentid

                        cur.execute("select accomodation from pet_hotel where resident_id=?", (x,))
                        pethotel_acco = cur.fetchone()

                        cur.execute("select check_in from pet_hotel where resident_id=?", (x,))
                        pethotel_checkin = cur.fetchone()

                        cur.execute("select check_out from pet_hotel where resident_id=?", (x,))
                        pethotel_checkout = cur.fetchone()

                        cur.execute("select cost_of_stay from pet_hotel where resident_id=?", (x,))
                        pethotel_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)
                        Button(root, text='Change', command=changeowner_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)
                        Button(root, text='Change', command=changeowner_number, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=4, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)
                        Button(root, text='Change', command=changeowner_email, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=5, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)
                        Button(root, text='Change', command=changepet_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=7, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)
                        Button(root, text='Change', command=changepet_gender, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=8, column=2, sticky=N + S + E + W)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)
                        Button(root, text='Change', command=changepet_species, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=9, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Resident ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Accomodation : ').grid(row=12, column=0)
                        l = Label(root, text=pethotel_acco).grid(row=12, column=1)
                        Button(root, text='Change', command=changepethotel_acco, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=12, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Check-In Date : ').grid(row=13, column=0)
                        l = Label(root, text=pethotel_checkin).grid(row=13, column=1)
                        Button(root, text='Change', command=changepethotel_cin, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=13, column=2, sticky=N + S + E + W)


                        l = Label(root, text='Check-Out Date : ').grid(row=14, column=0)
                        l = Label(root, text=pethotel_checkout).grid(row=14, column=1)
                        Button(root, text='Change', command=changepethotel_cout, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=14, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Cost of Stay : ').grid(row=15, column=0)
                        l = Label(root, text=pethotel_cost).grid(row=15, column=1)

                    def daycampdetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('DAY CAMP : ')
                        l = Label(root, text='Vet Care Appointment Details :', font='Times 20 bold')
                        l.grid(row=0, column=0)

                        l = Label(root, text=' ')
                        l.grid(row=1, column=0)

                        w = updatedetails.petid

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        y=updatedetails.oid

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select daycare_id from day_camp where pet_id=?",(w,))
                        daycampidtup = cur.fetchone()
                        daycampid = daycampidtup[0]
                        x = daycampid

                        cur.execute("select activity from day_camp where daycare_id=?", (x,))
                        daycamp_activity = cur.fetchone()

                        cur.execute("select duration from day_camp where daycare_id=?", (x,))
                        daycamp_duration = cur.fetchone()

                        cur.execute("select cost from day_camp where daycare_id=?", (x,))
                        daycamp_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)
                        Button(root, text='Change', command=changeowner_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)
                        Button(root, text='Change', command=changeowner_number, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=4, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)
                        Button(root, text='Change', command=changeowner_email, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=5, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)
                        Button(root, text='Change', command=changepet_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=7, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)
                        Button(root, text='Change', command=changepet_gender, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=8, column=2, sticky=N + S + E + W)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)
                        Button(root, text='Change', command=changepet_species, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=9, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Day Camp ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Activity : ').grid(row=12, column=0)
                        l = Label(root, text=daycamp_activity).grid(row=12, column=1)

                        l = Label(root, text='Duration : ').grid(row=13, column=0)
                        l = Label(root, text=daycamp_duration).grid(row=13, column=1)
                        Button(root, text='Change', command=changedaycamp_duration, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=13, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Cost : ').grid(row=14, column=0)
                        l = Label(root, text=daycamp_cost).grid(row=14, column=1)

                    def trainingcampdetails():
                        root = Toplevel()
                        root.geometry('540x540')
                        root.title('TRAINING CAMP : ')
                        l = Label(root, text='Training Camp Appointment Details :', font='Times 20 bold')
                        l.grid(row=0, column=0)

                        l = Label(root, text=' ')
                        l.grid(row=1, column=0)

                        w = updatedetails.petid

                        # cur.execute("select pet_id from pet where pet_id=?",service.currpetid)
                        # pet_id = cur.fetchone()

                        y=updatedetails.oid

                        cur.execute("select owner_name from owner where owner_id=?", (y,))
                        owner_name = cur.fetchone()

                        cur.execute("select contact from owner where owner_id=?", (y,))
                        owner_contact = cur.fetchone()

                        cur.execute("select email from owner where owner_id=?", (y,))
                        owner_email = cur.fetchone()

                        cur.execute("select petname from pet where pet_id=?", (w,))
                        pet_name = cur.fetchone()

                        cur.execute("select gender from pet where pet_id=?", (w,))
                        pet_gender = cur.fetchone()

                        cur.execute("select species_type from pet where pet_id=?", (w,))
                        pet_species = cur.fetchone()

                        cur.execute("select service_required from pet where pet_id=?", (w,))
                        pet_service = cur.fetchone()

                        cur.execute("select training_id from training_camp where pet_id=?",(w,))
                        trainingcampidtup = cur.fetchone()
                        trainingcampid = trainingcampidtup[0]
                        x = trainingcampid

                        cur.execute("select package from training_camp where training_id=?", (x,))
                        trainingcamp_activity = cur.fetchone()

                        cur.execute("select train_date from training_camp where training_id=?", (x,))
                        trainingcamp_date = cur.fetchone()

                        cur.execute("select cost from training_camp where training_id=?", (x,))
                        trainingcamp_cost = cur.fetchone()

                        l = Label(root, text='Owner ID : ').grid(row=2, column=0)
                        l = Label(root, text=y).grid(row=2, column=1)

                        l = Label(root, text='Owner Name : ').grid(row=3, column=0)
                        l = Label(root, text=owner_name).grid(row=3, column=1)
                        Button(root, text='Change', command=changeowner_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=3, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Contact : ').grid(row=4, column=0)
                        l = Label(root, text=owner_contact).grid(row=4, column=1)
                        Button(root, text='Change', command=changeowner_number, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=4, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Email : ').grid(row=5, column=0)
                        l = Label(root, text=owner_email).grid(row=5, column=1)
                        Button(root, text='Change', command=changeowner_email, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=5, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Pet ID :').grid(row=6, column=0)
                        l = Label(root, text=w).grid(row=6, column=1)

                        l = Label(root, text='Pet Name').grid(row=7, column=0)
                        l = Label(root, text=pet_name).grid(row=7, column=1)
                        Button(root, text='Change', command=changepet_name, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=7, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Gender : ').grid(row=8, column=0)
                        l = Label(root, text=pet_gender).grid(row=8, column=1)
                        Button(root, text='Change', command=changepet_gender, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=8, column=2, sticky=N + S + E + W)

                        l = Label(root, text='species : ').grid(row=9, column=0)
                        l = Label(root, text=pet_species).grid(row=9, column=1)
                        Button(root, text='Change', command=changepet_species, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=9, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Service Opted : ').grid(row=10, column=0)
                        l = Label(root, text=pet_service).grid(row=10, column=1)

                        l = Label(root, text='Training ID : ').grid(row=11, column=0)
                        l = Label(root, text=x).grid(row=11, column=1)

                        l = Label(root, text='Activity : ').grid(row=12, column=0)
                        l = Label(root, text=trainingcamp_activity).grid(row=12, column=1)

                        l = Label(root, text='Date Slot : ').grid(row=13, column=0)
                        l = Label(root, text=trainingcamp_date).grid(row=13, column=1)
                        Button(root, text='Change', command=changetrainingcamp_date, width=25, font=("Times New", 10), bd=5,bg="light grey").grid(row=13, column=2, sticky=N + S + E + W)

                        l = Label(root, text='Cost : ').grid(row=14, column=0)
                        l = Label(root, text=trainingcamp_cost).grid(row=14, column=1)

                    if updatedetails.service=='GROOMING':
                        groomingdetails()
                    elif updatedetails.service=='VET CARE':
                        vetcaredetails()
                    elif updatedetails.service=='PET HOTEL':
                        pethoteldetails()
                    elif updatedetails.service=='DAY CAMP':
                        daycampdetails()
                    elif updatedetails.service=='TRAINING CAMP':
                        trainingcampdetails()


                Button(root, text='Proceed', command=updatede, width=25, font=("Times New", 10),bd=5, bg="light grey").grid(row=3, column=1, sticky=N + S + E + W)

            Button(menu,text='Register details',command=ownerdetails,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=1,column=0,sticky=N+S+E+W)
            Button(menu,text='Check Booked Details',command=checkdetails,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=0,sticky=N+S+E+W)
            Button(menu,text='Update Booked Details',command=updatedetails,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=3,column=0,sticky=N+S+E+W)

    Button(window,text='Login',command=login,width=20,font=("Times New",15),bd=5,bg="light grey").grid(row=3,column=2,sticky=N+S+E+W)

    window.mainloop()

Button(window,command=start,text ='Log In',width=10,font=("Helvetica Neue bold",15),bd=4,bg="white",fg="red").place(x=420,y=390)

window.mainloop()
