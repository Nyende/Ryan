
from tkinter import*
import tkinter.messagebox
import libBksDatabase

class library:
    def __init__(self,root):
        self.root=root
        self.root.title('library Database Management system ')
        self.root.geometry('1350x750+0+0')

       #lets create my variables to be used in the program

        Mty = StringVar()
        Ref = StringVar()
        Til = StringVar()
        Fna = StringVar()
        Sna = StringVar()
        Adr1 = StringVar()
        Adr2 = StringVar()
        Pcd = StringVar()
        Mno = StringVar()
        BKid = StringVar()
        BKt = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        Spr = StringVar()
        Lrf = StringVar()
        Dod = StringVar()
        Dnol = StringVar()
        #===========================================function decl====================
        def iExit():
            iExit=tkinter.messagebox.askyesno('library Database Management system ','Are You Sure You want To Abort')
            if iExit > 0:
                root.destroy()
                return

        def delectData():
            if (len(Mty.get()) != 0):
                libBksDatabase.deleteRec(sd[0])
                displayData()
                cleardata()

        def UpdateData():
            if (len(Mty.get()) != 0):
                libBksDatabase.updateRec(sd[0],Mty.get(),Ref.get(),Fna.get(),Sna.get(),Adr1.get(),BKid.get(),BKt.get(),Dod.get(),Dnol.get(),Adr2.get(),Pcd.get(),Mno.get(),Til.get(),DBo.get(),Spr.get(),Atr.get(),Lrf.get(),Ddu.get()
                                          ,)





        def cleardata():
            self.txtMType.delete(0,END)
            self.txtBKt.delete(0,END)
            self.txtAdr1.delete(0,END)
            self.txtadr2.delete(0,END)
            self.txtAtr.delete(0,END)
            self.txtBKid.delete(0,END)
            self.txtDBo.delete(0,END)
            self.txtDdu.delete(0,END)
            self.txtDnol.delete(0,END)
            self.txtDod.delete(0,END)
            self.txtFna.delete(0,END)
            self.txtmno.delete(0,END)
            self.txtlrf.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtspr.delete(0,END)
            self.txtRef.delete(0,END)
            self.txtTil.delete(0,END)

        #if you want to add data to the program we are goning to use database system
        #libBksDatabase is the name of our database ,,addDataRec is the function of adding
        #items in the database and its in our class database

        def AddData():
            if(len(Mty.get()) !=0):
                libBksDatabase.addDataRec(Mty.get(),Ref.get(),Fna.get(),Sna.get(),Adr1.get()
                                          ,BKid.get(),BKt.get(),Dod.get(),Dnol.get(),Adr2.get()
                                          ,Pcd.get(),Mno.get(),Til.get(),DBo.get(),Spr.get(),Atr.get()
                                          ,Lrf.get(),Ddu.get())
                list1.delete(0,END)
                list1.insert(END,Mty.get(),Ref.get(),Fna.get(),Sna.get(),Adr1.get()
                                          ,BKid.get(),BKt.get(),Dod.get(),Dnol.get(),Adr2.get()
                                          ,Pcd.get(),Mno.get(),Til.get(),DBo.get(),Spr.get(),Atr.get()
                                          ,Lrf.get(),Ddu.get())
            tkinter.messagebox.showinfo('Adding Member','You have added Ref No.: ' + Ref.get())
        def searchData():
            list1.delete(0,END)
            for rows in libBksDatabase.searchdata(Mty.get(),Ref.get(),Fna.get(),Sna.get(),Adr1.get(),BKid.get(),BKt.get(),Dod.get(),Dnol.get(),Adr2.get(),Pcd.get(),Mno.get(),Til.get(),DBo,Spr.get(),Atr.get(),Lrf.get(),Ddu.get()):

                list1.insert(END,rows)



        def displayData():
            list1.delete(0,END)
            for row in libBksDatabase.viewData():
                list1.insert(END,row)
        #let add a functio which will allow us to click on the data in the lisbox
        # and it can also display back in our entrys in membertype labelframe ..
        # then we will call and bind it in our list1 as below

        def selectData(event):
            global sd
            # lets create a new variable selectbk to hold our curselection
            selectBk = list1.curselection()[0]
            sd=list1.get(selectBk)

            self.txtMType.delete(0, END)
            self.txtMType.insert(END,sd[1])
            self.txtBKt.delete(0, END)
            self.txtBKt.insert(END,sd[2])
            self.txtAdr1.delete(0, END)
            self.txtAdr1.insert(END,sd[3])
            self.txtadr2.delete(0, END)
            self.txtadr2.insert(END,sd[4])
            self.txtAtr.delete(0, END)
            self.txtAtr.insert(END, sd[5])
            self.txtBKid.delete(0, END)
            self.txtBKid.insert(END, sd[6])
            self.txtDBo.delete(0, END)
            self.txtDBo.insert(END, sd[7])
            self.txtDdu.delete(0, END)
            self.txtDdu.insert(END, sd[9])
            self.txtDnol.delete(0, END)
            self.txtDnol.insert(END, sd[10])
            self.txtDod.delete(0, END)
            self.txtDod.insert(END, sd[11])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[12])
            self.txtmno.delete(0, END)
            self.txtmno.insert(END, sd[13])
            self.txtlrf.delete(0, END)
            self.txtlrf.insert(END, sd[14])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[15])
            self.txtspr.delete(0, END)
            self.txtspr.insert(END, sd[16])
            self.txtRef.delete(0, END)
            self.txtRef.insert(END, sd[17])
            self.txtTil.delete(0, END)
            self.txtTil.insert(END, sd[18])




        #==============================================frame=================================
        #lets use oir main frame to be mainframe and our label

        Mainframe = Frame(self.root)
        Mainframe.grid()
        #lets create a title labelfor our library

        Titframe=Frame(Mainframe,bd=2,padx=40,pady=8,bg='cadet blue',relief=RIDGE)
        Titframe.pack(side=TOP)
        #lets also add a alabel for our Titframe

        self.lblTit=Label(Titframe,font=('arial',46,'bold'),text='locus Database Management system ')
        self.lblTit.grid(sticky=W)
        #lets also addd most fame to put our inform on buttonframe buttom,dataframe left,dataframe right and they labels

        Buttonframe = Frame(Mainframe, bd=2, padx=20, pady=20,width=1350,height=100, bg='cadet blue', relief=RIDGE)
        Buttonframe.pack(side=BOTTOM)

        FrameDetails = Frame(Mainframe, bd=0, padx=20,width=1350, height=50, relief=RIDGE)
        FrameDetails.pack(side=BOTTOM)

        Dataframe = Frame(Mainframe, bd=1, padx=20, pady=20, width=1300, height=400, relief=RIDGE)
        Dataframe.pack(side=BOTTOM)
        #let also add labels to the frames

        DataframeLeft = LabelFrame(Dataframe, bd=1, padx=20,width=800, height=300, bg='cadet blue', relief=RIDGE
                              ,font=('arial',12,'bold'),text='Library Membership info:')
        DataframeLeft.pack(side=LEFT)

        DataframeRight = LabelFrame(Dataframe, bd=2, padx=20, pady=20, width=450, height=300, bg='cadet blue', relief=RIDGE
                              , font=('arial', 12, 'bold'), text='Book Details:')
        DataframeRight.pack(side=RIGHT)

        #===============================labels and entry==================================

        self.lblMemberType=Label(DataframeLeft,font=('arial',12,'bold'),text='Member Type:',padx=2,pady=2,bg='cadet blue')
        self.lblMemberType.grid(row=0,column =0,sticky=W)
        self.txtMType = Entry(DataframeLeft, textvar=Mty,width=25,font=('arial',12,'bold'))
        self.txtMType.grid(row=0, column=1)

        self.lblReferenceType=Label(DataframeLeft,font=('arial',12,'bold'),text='Reference No.  :',padx=2,pady=2,bg='cadet blue')
        self.lblReferenceType.grid(row=1,column =0,sticky=W)
        self.txtRef = Entry(DataframeLeft, textvar=Ref,width=25,font=('arial',12,'bold'))
        self.txtRef.grid(row=1, column=1)

        self.lblBKidType = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Book ID :', padx=2, pady=2,
                                      bg='cadet blue')
        self.lblBKidType.grid(row=0, column=2, sticky=W)
        self.txtBKid = Entry(DataframeLeft, textvar=BKid, width=25, font=('arial', 12, 'bold'))
        self.txtBKid.grid(row=0, column=3)

        self.lblBKt = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Book Title :', padx=2, pady=2,
                                      bg='cadet blue')
        self.lblBKt.grid(row=1, column=2, sticky=W)
        self.txtBKt = Entry(DataframeLeft, textvar=BKt, width=25, font=('arial', 12, 'bold'))
        self.txtBKt.grid(row=1, column=3)

        self.lblTil = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Title :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblTil.grid(row=2, column=0, sticky=W)
        self.txtTil = Entry(DataframeLeft, textvar=Til, width=25, font=('arial', 12, 'bold'))
        self.txtTil.grid(row=2, column=1)

        self.lblAtr = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Author :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblAtr.grid(row=2, column=2, sticky=W)
        self.txtAtr = Entry(DataframeLeft, textvar=Atr, width=25, font=('arial', 12, 'bold'))
        self.txtAtr.grid(row=2, column=3)

        self.lblFna = Label(DataframeLeft, font=('arial', 12, 'bold'), text='FirstName :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblFna.grid(row=3, column=0, sticky=W)
        self.txtFna = Entry(DataframeLeft, textvar=Fna, width=25, font=('arial', 12, 'bold'))
        self.txtFna.grid(row=3, column=1)

        self.lblDBo = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Date Borrowed :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblDBo.grid(row=3, column=2, sticky=W)
        self.txtDBo = Entry(DataframeLeft, textvar=DBo, width=25, font=('arial', 12, 'bold'))
        self.txtDBo.grid(row=3, column=3)

        self.lblSna = Label(DataframeLeft, font=('arial', 12, 'bold'), text='SurName :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblSna.grid(row=4, column=0, sticky=W)
        self.txtSna = Entry(DataframeLeft, textvar=Sna, width=25, font=('arial', 12, 'bold'))
        self.txtSna.grid(row=4, column=1)

        self.lblDdu = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Date Due :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblDdu.grid(row=4, column=2, sticky=W)
        self.txtDdu = Entry(DataframeLeft, textvar=Ddu, width=25, font=('arial', 12, 'bold'))
        self.txtDdu.grid(row=4, column=3)

        self.lblAdr1 = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Address 1 :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblAdr1.grid(row=5, column=0, sticky=W)
        self.txtAdr1 = Entry(DataframeLeft, textvar=Adr1, width=25, font=('arial', 12, 'bold'))
        self.txtAdr1.grid(row=5, column=1)

        self.lblDnol = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Days of loan:', padx=2, pady=2,
                            bg='cadet blue')
        self.lblDnol.grid(row=5, column=2, sticky=W)
        self.txtDnol = Entry(DataframeLeft, textvar=Dnol, width=25, font=('arial', 12, 'bold'))
        self.txtDnol.grid(row=5, column=3)

        self.lbladr2 = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Address 2 :', padx=2, pady=2,
                            bg='cadet blue')
        self.lbladr2.grid(row=6, column=0, sticky=W)
        self.txtadr2 = Entry(DataframeLeft, textvar=Adr2, width=25, font=('arial', 12, 'bold'))
        self.txtadr2.grid(row=6, column=1)

        self.lbllrf = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Late Return Fine:', padx=2, pady=2,
                            bg='cadet blue')
        self.lbllrf.grid(row=6, column=2, sticky=W)
        self.txtlrf = Entry(DataframeLeft, textvar=Lrf, width=25, font=('arial', 12, 'bold'))
        self.txtlrf.grid(row=6, column=3)

        self.lblDdu = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Post Code  :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblDdu.grid(row=7, column=0, sticky=W)
        self.txtDdu = Entry(DataframeLeft, textvar=Pcd, width=25, font=('arial', 12, 'bold'))
        self.txtDdu.grid(row=7, column=1)

        self.lblDod = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Date Over Due :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblDod.grid(row=7, column=2, sticky=W)
        self.txtDod = Entry(DataframeLeft, textvar=Dod, width=25, font=('arial', 12, 'bold'))
        self.txtDod.grid(row=7, column=3)

        self.lblmno = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Mobile No. :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblmno.grid(row=8, column=0, sticky=W)
        self.txtmno = Entry(DataframeLeft, textvar=Mno, width=25, font=('arial', 12, 'bold'))
        self.txtmno.grid(row=8, column=1)

        self.lblspr = Label(DataframeLeft, font=('arial', 12, 'bold'), text='Selling Price :', padx=2, pady=2,
                            bg='cadet blue')
        self.lblspr.grid(row=8, column=2, sticky=W)
        self.txtspr = Entry(DataframeLeft, textvar=Spr, width=25, font=('arial', 12, 'bold'))
        self.txtspr.grid(row=8, column=3)
        #================================listbox===========================================

        scorllbar = Scrollbar(DataframeRight)
        scorllbar.grid(row =0 ,column=1,sticky='ns')

        list1 =Listbox(DataframeRight,font=('arial', 12, 'bold'),yscrollcommand=scorllbar.set)
        list1.grid(row =0 ,column=0,padx=8)
        list1.bind('<<ListboxSelect>>',selectData)
        scorllbar.config(command=list1.yview)
        #=========================================buttons ===========================

        self.btnaddata=Button(Buttonframe,text='Add Data',font=('arial', 14, 'bold'),height=2,width=13,
                              command=AddData,bd=4)
        self.btnaddata.grid(row=0,column=0)

        self.btndispdata = Button(Buttonframe, text='Display',command=displayData,font=('arial', 14, 'bold'),
                                  height=2, width=13, bd=4)
        self.btndispdata.grid(row=0, column=1)

        self.btnclrdata = Button(Buttonframe, text='Clear Data', command=cleardata,font=('arial', 14, 'bold'),
                                 height=2, width=13, bd=4)
        self.btnclrdata.grid(row=0, column=2)

        self.btndeldata = Button(Buttonframe, text='Delete Data',command=delectData,font=('arial', 14, 'bold'),
                                 height=2, width=13, bd=4)
        self.btndeldata.grid(row=0, column=3)

        self.btnupdata = Button(Buttonframe, text='Update Data', command=UpdateData,font=('arial', 14, 'bold'),
                                height=2, width=13, bd=4)
        self.btnupdata.grid(row=0, column=4)

        self.btnschdata = Button(Buttonframe, text='Search Data',command=searchData, font=('arial', 14, 'bold'),
                                 height=2, width=13, bd=4)
        self.btnschdata.grid(row=0, column=5)

        self.btnabrtdata = Button(Buttonframe, text='Abort',command=iExit, font=('arial', 14, 'bold'), height=2, width=13, bd=4)
        self.btnabrtdata.grid(row=0, column=6)




if __name__=='__main__':
    root = Tk()
    application = library(root)
    root.mainloop()










