title="=====================Welcome to Cup And Kitaab===================="
print(title)
print("Enter 1 for library section")
print("Enter 2 for coffee section")
n=int(input())
if n==1:
    print('''===Welcome to the Library Section===''')
    print('''===Commands===
            View Book List        Press 2
            No need of a book     Press 3''')
    m=int(input("Give your Command: "))
    if m==2:
        print('''===Available Books are===
            1.Harry Potter and the goblet of fire
            2.War and Peace
            3.Rich Dad Poor Dad
            4.Startup Vs Girlfriend
            5.Mind Fucked
            6.The strange of dr jekyl and Mr Hyde
            7.Atlas
            8.Encyclopedia
            9.Today's Newspaper
            10.Canterville ghost
            11.The invisible man
            12.Canterburry tales
            13.Pride and prejudice
            14 Enola holmes
            15 Emma
            16.Wings of fire
            17.Ignited minds
            18.Midnights childrem
            19.Discovery of india
            20.The kite flyer
            21.Untouchables
            22 King leer
            23 Breathe
            24.Welcome to The Fires
            25.DO EPIC SHIT''')
        h=int(input("Enter the Number of Book"))
        if h==1:
            print("You have been issued Harry potter and the goblet of fire. Enjoy")
        elif h==2:
            print("You have been issued War and Peace. Enjoy")
        elif h==3:
            print("You have been issued Rich Dad Poor Dad. Enjoy")
        elif h==4:
            print("You have been issued Startup Vs Girlfriend. Enjoy")
        elif h==5:
            print("You have been issued Mind Fucked. Enjoy")
        elif h==6:
            print("You have been issued the strange case of dr jekyl and mr hyde.Enjoy ")
        elif h==7:
            print("You have been issued Atlas.Enjoy")
        elif h==8:
            print("You have been issued Encyclopedia.Enjoy")
        elif h==9:
            print("You have been issued today's newspaper")
        elif h==10:
            print("You have been issued canterville ghost.Enjoy")
        elif h==11:
            print("You have been issued The invisible man.Enjoy")
        elif h==12:
            print("You have been issued Canterburry tales.Enjoy")
        elif h==13:
            print("You have been issued Pride and prejudice.Enjoy")
        elif h==14:
            print("You have been issued Enola holmes.Enjoy ")
        elif h==15:
            print("You have been issued Emma .Enjoy")
        elif h==16:
            print("You have been issued Wings of fire .Enjoy")
        elif h==17:
            print("You have been issued Ignited minds .Enjoy")
        elif h==18:
            print("You have been issued midnight children.Enjoy")
        elif h==19:
            print("You have been issued Discovery of india.Enjoy")
        elif h==20:
            print("You have been issued The Kite Flier")
        elif h==21:
            print("You have been issued Untouchables")
        elif h==22:
            print("You have been issued King Leer")
        elif h==23:
            print("You have been issued Breathe")
        elif h==24:
            print("You have been issued Welcome to the fires")
        elif h==25:
            print("You have been issued Do the Epic Shit")
        else:
            print("Invalid Selection!!")
    z=int(input("Press 3 to enter Cofee Section"))    
    if m==3 or z==3:
        print("Coffee Section Appears on the TaskBar Click on the new icon appeared")
        from tkinter import*
        from tkinter import messagebox
        import random
        import time
        import datetime
        root=Tk()
        root.geometry("1350x750+0+0")
        root.title("Cup and Kitaab")
        root.configure(background='red')

        Tops=Frame(root, width=1800, height=100,bd=20,relief="raise")
        Tops.pack(side=TOP)

        f1=Frame(root, width=900, height=650,bd=8,relief="raise")
        f1.pack(side=LEFT)
        f2=Frame(root, width=440, height=650,bd=8,relief="raise")
        f2.pack(side=RIGHT)

        ft2=Frame(f2, width=440, height=450,bd=12,relief="raise")
        ft2.pack(side=TOP)
        fb2=Frame(f2, width=440, height=250,bd=16,relief="raise")
        fb2.pack(side=BOTTOM)

        f1a=Frame(f1, width=900, height=330,bd=8,relief="raise")
        f1a.pack(side=TOP)
        f2a=Frame(f1, width=900, height=320,bd=6,relief="raise")
        f2a.pack(side=BOTTOM)

        f1aa=Frame(f1a, width=600, height=330, bd=16, relief="raise")
        f1aa.pack(side=LEFT)
        f1ab=Frame(f1a,width=400, height=330, bd=16, relief="raise")
        f1ab.pack(side=LEFT)

        f2aa=Frame(f2a, width=450, height=330, bd=14, relief="raise")
        f2aa.pack(side=LEFT)
        f2ab=Frame(f2a, width=450, height=600, bd=14, relief="raise")
        f2ab.pack(side=RIGHT)

        Tops.configure(background='black')
        f1.configure(background='black')
        f2.configure(background='black')

        lblInfo= Label(Tops, font=('arial',70,'bold'), text="  Cup and Kitaab Coffee Section  ", bd=10)
        lblInfo.grid(row=0, column=0)
#===============================================Methods=======================================================================
        def qExit():
            qExit= messagebox.askyesno("Quit System","Do you Want to quit?")
            if qExit>0:
                root.destroy()
                return

        def Reset():
            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            CostOfDrinks.set("")
            CostOfCakes.set("")
            ServiceCharge.set("")
            txtReceipt.delete("1.0",END)

            E_Latta.set("0")
            E_Espresso.set("0")
            E_Americano.set("0")
            E_Cortado.set("0")
            E_Mocha.set("0")
            E_Macchiato.set("0")
            E_FlatWhite.set("0")
            E_IrishCoffee.set("0")

            E_Bourbon.set("0")
            E_Oreo.set("0")
            E_C_K.set("0")
            E_CoffeeCake.set("0")
            E_Red_Velvet.set("0")
            E_Silk.set("0")
            E_XXL.set("0")
            E_Baker.set("0")
        #=============================CHECKbUTTONN======================================================================
        def chkbutton_value():
            if(var1.get()==1):
                txtLatta.configure(state=NORMAL)
            elif(var1.get()==0):
                txtLatta.configure(state=DISABLED)
                E_Latta.set("0")
            if(var2.get()==1):
                txtEspresso.configure(state=NORMAL)
            elif(var2.get()==0):
                txtEspresso.configure(state=DISABLED)
                E_Espresso.set("0")

            if(var3.get()==1):
                txtAmericano.configure(state=NORMAL)
            elif(var3.get()==0):
                txtAmericano.configure(state=DISABLED)
                E_Americano.set("0")

            if(var4.get()==1):
                txtCortado.configure(state=NORMAL)
            elif(var4.get()==0):
                txtCortado.configure(state=DISABLED)
                E_Cortado.set("0")

            if(var5.get()==1):
                txtMocha.configure(state=NORMAL)
            elif(var5.get()==0):
                txtMocha.configure(state=DISABLED)
                E_Mocha.set("0")

            if(var6.get()==1):
                txtMacchiato.configure(state=NORMAL)
            elif(var6.get()==0):
                txtMacchiato.configure(state=DISABLED)
                E_Macchiato.set("0")

            if(var7.get()==1):
                txtFlatWhite.configure(state=NORMAL)
            elif(var7.get()==0):
                txtFlatWhite.configure(state=DISABLED)
                E_FlatWhite.set("0")

            if(var8.get()==1):
                txtIrishCoffee.configure(state=NORMAL)
            elif(var8.get()==0):
                txtIrishCoffee.configure(state=DISABLED)
                E_IrishCoffee.set("0")

            if(var9.get()==1):
                txtBourbon.configure(state=NORMAL)
            elif(var9.get()==0):
                txtBourbon.configure(state=DISABLED)
                E_Bourbon.set("0")

            if(var10.get()==1):
                txtOreo.configure(state=NORMAL)
            elif(var10.get()==0):
                txtOreo.configure(state=DISABLED)
                E_Oreo.set("0")

            if(var11.get()==1):
                txtC_K.configure(state=NORMAL)
            elif(var11.get()==0):
                txtC_K.configure(state=DISABLED)
                E_C_K.set("0")

            if(var12.get()==1):
                txtCoffeeCake.configure(state=NORMAL)
            elif(var12.get()==0):
                txtCoffeeCake.configure(state=DISABLED)
                E_CoffeeCake.set("0")

            if(var13.get()==1):
                txtRed_Velvet.configure(state=NORMAL)
            elif(var13.get()==0):
                txtRed_Velvet.configure(state=DISABLED)
                E_Red_Velvet.set("0")

            if(var14.get()==1):
                txtSilk.configure(state=NORMAL)
            elif(var14.get()==0):
                txtSilk.configure(state=DISABLED)
                E_Silk.set("0")

            if(var15.get()==1):
                txtXXL.configure(state=NORMAL)
            elif(var15.get()==0):
                txtXXL.configure(state=DISABLED)
                E_XXL.set("0")

            if(var16.get()==1):
                txtBaker.configure(state=NORMAL)
            elif(var16.get()==0):
                txtBaker.configure(state=DISABLED)
                E_Baker.set("0")
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)

            txtLatta.configure(state=DISABLED)
            txtEspresso.configure(state=NORMAL)
            txtAmericano.configure(state=NORMAL)
            txtCortado.configure(state=NORMAL)
            txtMocha.configure(state=NORMAL)
            txtMacchiato.configure(state=NORMAL)
            txtFlatWhite.configure(state=NORMAL)
            txtIrishCoffee.configure(state=NORMAL)
            txtBourbon.configure(state=NORMAL)
            txtOreo.configure(state=NORMAL)
            txtC_K.configure(state=NORMAL)
            txtCoffeeCake.configure(state=NORMAL)
            txtRed_Velvet.configure(state=NORMAL)
            txtSilk.configure(state=NORMAL)
            txtXXL.configure(state=NORMAL)
            txtBaker.configure(state=NORMAL)

        def CostOfItem():
            Item1=float(E_Latta.get())
            Item2=float(E_Espresso.get())
            Item3=float(E_Americano.get())
            Item4=float(E_Cortado.get())
            Item5=float(E_Mocha.get())
            Item6=float(E_Macchiato.get())
            Item7=float(E_FlatWhite.get())
            Item8=float(E_IrishCoffee.get())
            
            
            Item9=float(E_Bourbon.get())
            Item10=float(E_Oreo.get())
            Item11=float(E_C_K.get())
            Item12=float(E_CoffeeCake.get())
            Item13=float(E_Red_Velvet.get())
            Item14=float(E_Silk.get())
            Item15=float(E_XXL.get())
            Item16=float(E_Baker.get())

            PriceofDrinks=(Item1 * 100) + (Item2 * 80) + (Item3 * 105) + (Item4 * 110) + (Item5 * 75) + (Item6 * 95) + (Item7 * 45) + (Item8 * 120)
            PriceOfCookies=(Item9 * 20) + (Item10 * 40) + (Item11 * 90) + (Item12 * 30) + (Item13 * 60) + (Item14 * 85) + (Item15 * 70) + (Item16 * 90)
            DrinksPrice="₹", str('%.2f'%(PriceofDrinks))
            CakesPrice="₹",str('%.2f'%(PriceOfCookies))
            CostOfCakes.set(CakesPrice)
            CostOfDrinks.set(DrinksPrice)
            SC="₹", str('%.2f'%(19.75))
            ServiceCharge.set(SC)

            SubTotalofITEMS="₹", str('%.2f'%(PriceofDrinks + PriceOfCookies + 19.75))
            SubTotal.set(SubTotalofITEMS)

            Tax="₹", str('%.2f'%((PriceofDrinks + PriceOfCookies + 19.75)*0.05))
            PaidTax.set(Tax)
            TT=((PriceofDrinks + PriceOfCookies + 1.59)*0.05)
            TC="₹", str('%.2f'%(PriceofDrinks + PriceOfCookies + 19.75+TT))
            TotalCost.set(TC)
            

        def Receipt():
            txtReceipt.delete("1.0",END)
            x=random.randint(10908, 500876)
            randomRef = str(x)
            Receipt_Ref.set("BILL"+ randomRef)

            txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n")
            txtReceipt.insert(END,'Items\t\t\t\t\t'+ "Cost Of Items \n\n")
            txtReceipt.insert(END,'Latta: \t\t\t\t\t'+ E_Latta.get()+"\n")
            txtReceipt.insert(END,'Espresso: \t\t\t\t\t'+ E_Espresso.get()+"\n")
            txtReceipt.insert(END,'Americano: \t\t\t\t\t'+ E_Americano.get()+"\n")
            txtReceipt.insert(END,'Cortado: \t\t\t\t\t'+ E_Cortado.get()+"\n")
            txtReceipt.insert(END,'Mocha: \t\t\t\t\t'+ E_Mocha.get()+"\n")
            txtReceipt.insert(END,'Macchiato: \t\t\t\t\t'+ E_Macchiato.get()+"\n")
            txtReceipt.insert(END,'Flat White: \t\t\t\t\t'+ E_FlatWhite.get()+"\n")
            txtReceipt.insert(END,'Irish Coffee: \t\t\t\t\t'+ E_IrishCoffee.get()+"\n")
            txtReceipt.insert(END,'Bourbon: \t\t\t\t\t'+ E_Bourbon.get()+"\n")
            txtReceipt.insert(END,'Oreo: \t\t\t\t\t'+ E_Oreo.get()+"\n")
            txtReceipt.insert(END,'C&K Special: \t\t\t\t\t'+ E_C_K.get()+"\n")
            txtReceipt.insert(END,'Coffee cake: \t\t\t\t\t'+ E_CoffeeCake.get()+"\n")
            txtReceipt.insert(END,'Red Velvet: \t\t\t\t\t'+ E_Red_Velvet.get()+"\n")
            txtReceipt.insert(END,'Silk: \t\t\t\t\t'+ E_Silk.get()+"\n")
            txtReceipt.insert(END,'XXL: \t\t\t\t\t'+ E_XXL.get()+"\n")
            txtReceipt.insert(END,'Baker Special: \t\t\t\t\t'+ E_Baker.get()+"\n")
            txtReceipt.insert(END,'Cost Of Drinks:\t\t'+ CostOfDrinks.get()+'\tTax Paid:\t\t' + PaidTax.get()+"\n")
            txtReceipt.insert(END,'Cost Of Cookies: \t\t' + CostOfCakes.get()+'\tSubTotal:\t\t'+SubTotal.get()+ "\n")
            txtReceipt.insert(END,'Service Charge: \t\t' + ServiceCharge.get()+'\tTotal Cost:\t\t'+TotalCost.get()+ "\n")





#===============================================Variables=======================================================================
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()


        DateofOrder=StringVar()
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()
        CostOfCakes=StringVar()
        CostOfDrinks=StringVar()
        ServiceCharge=StringVar()

        E_Latta=StringVar()
        E_Espresso=StringVar()
        E_Americano=StringVar()
        E_Cortado=StringVar()
        E_Mocha=StringVar()
        E_Macchiato=StringVar()
        E_FlatWhite=StringVar()
        E_IrishCoffee=StringVar()

        E_Bourbon=StringVar()
        E_Oreo=StringVar()
        E_C_K=StringVar()
        E_CoffeeCake=StringVar()
        E_Red_Velvet=StringVar()
        E_Silk=StringVar()
        E_XXL=StringVar()
        E_Baker=StringVar()

        E_Latta.set("0")
        E_Espresso.set("0")
        E_Americano.set("0")
        E_Cortado.set("0")
        E_Mocha.set("0")
        E_Macchiato.set("0")
        E_FlatWhite.set("0")
        E_IrishCoffee.set("0")

        E_Bourbon.set("0")
        E_Oreo.set("0")
        E_C_K.set("0")
        E_CoffeeCake.set("0")
        E_Red_Velvet.set("0")
        E_Silk.set("0")
        E_XXL.set("0")
        E_Baker.set("0")

        DateofOrder.set(time.strftime("%d/%m/%Y"))


        #==================Coffees==========================
        Latta=       Checkbutton(f1aa, text="Latte \t", variable= var1, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=0,sticky=W)
        Espresso=    Checkbutton(f1aa, text="Espresso \t", variable= var2, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=1,sticky=W)
        Americano=   Checkbutton(f1aa, text="Americano \t", variable= var3, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=2,sticky=W)
        Cortado=     Checkbutton(f1aa, text="Cortado \t", variable= var4, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=3,sticky=W)
        Mocha=       Checkbutton(f1aa, text="Mocha \t", variable= var5, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=4,sticky=W)
        Macchiato=   Checkbutton(f1aa, text="Macchiato \t", variable= var6, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=5,sticky=W)
        FlatWhite=   Checkbutton(f1aa, text="Flat White \t", variable= var7, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=6,sticky=W)
        IrishCoffee= Checkbutton(f1aa, text="Irish Coffee \t", variable= var8, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=7,sticky=W)

        #======================Cookies======================
        Bourbon= Checkbutton(f1ab, text="Bourbon \t", variable= var9, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=0,sticky=W)
        Oreo= Checkbutton(f1ab, text="Oreo \t", variable= var10, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=1,sticky=W)
        C_K= Checkbutton(f1ab, text="C&K Special \t", variable= var11, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=2,sticky=W)
        CoffeeCake= Checkbutton(f1ab, text="Coffee Cake \t", variable= var12, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=3,sticky=W)
        Red_Velvet= Checkbutton(f1ab, text="Red Velvet Cake \t", variable= var13, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=4,sticky=W)
        Silk= Checkbutton(f1ab, text="Silk \t", variable= var14, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=5,sticky=W)
        XXL= Checkbutton(f1ab, text="XXL Cookie \t", variable= var15, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=6,sticky=W)
        Baker= Checkbutton(f1ab, text="Baker Cookie \t", variable= var16, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=7,sticky=W)
        #====================Enter Widget For Drinks===========================
        txtLatta= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Latta,state=NORMAL)
        txtLatta.grid(row=0, column=1)
        txtEspresso= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Espresso, state=NORMAL)
        txtEspresso.grid(row=1, column=1)
        txtAmericano= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Americano, state=NORMAL)
        txtAmericano.grid(row=2, column=1)
        txtCortado= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Cortado, state=NORMAL)
        txtCortado.grid(row=3, column=1)
        txtMocha= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Mocha, state=NORMAL)
        txtMocha.grid(row=4, column=1)
        txtMacchiato= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Macchiato, state=NORMAL)
        txtMacchiato.grid(row=5, column=1)
        txtFlatWhite= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_FlatWhite, state=NORMAL)
        txtFlatWhite.grid(row=6, column=1)
        txtIrishCoffee= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_IrishCoffee, state=NORMAL)
        txtIrishCoffee.grid(row=7, column=1)
        #====================Enter Widget For Cookies===========================
        txtBourbon= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Bourbon,state=NORMAL)
        txtBourbon.grid(row=0, column=1)
        txtOreo= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Oreo,state=NORMAL)
        txtOreo.grid(row=1, column=1)
        txtC_K= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_C_K,state=NORMAL)
        txtC_K.grid(row=2, column=1)
        txtCoffeeCake= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_CoffeeCake,state=NORMAL)
        txtCoffeeCake.grid(row=3, column=1)
        txtRed_Velvet= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Red_Velvet,state=NORMAL)
        txtRed_Velvet.grid(row=4, column=1)
        txtSilk= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Silk,state=NORMAL)
        txtSilk.grid(row=5, column=1)
        txtXXL= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_XXL,state=NORMAL)
        txtXXL.grid(row=6, column=1)
        txtBaker= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Baker, state=NORMAL)
        txtBaker.grid(row=7, column=1)
        #====================Informations===========================
        lblReceipt=Label(ft2, font=('arial',12,'bold'), text="Reciept: ",bd=2, anchor='w')
        lblReceipt.grid(row=0,column=0,sticky=W)
        txtReceipt=Text(ft2, width=59, height=22, bg="White",bd=8, font=('arial',11,'bold'))
        txtReceipt.grid(row=1, column=0)
        #====================Cost Items Information===========================
        lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'),text="Cost Of Drinks",bd=8)
        lblCostofDrinks.grid(row=0, column=0, sticky=W)
        txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left', textvariable=CostOfDrinks)
        txtCostofDrinks.grid(row=0, column=1, sticky=W)

        lblCostofCookies=Label(f2aa,font=('arial',16,'bold'),text="Cost Of Cookies",bd=8)
        lblCostofCookies.grid(row=1, column=0, sticky=W)
        txtCostofCookies=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left', textvariable=CostOfCakes)
        txtCostofCookies.grid(row=1, column=1, sticky=W)


        lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text="Service Charge",bd=8)
        lblServiceCharge.grid(row=2, column=0, sticky=W)
        txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left')
        txtServiceCharge.grid(row=2, column=1, sticky=W)

        #====================Payment Information==============================
        lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text="Paid Tax",bd=8)
        lblPaidTax.grid(row=0, column=0, sticky=W)
        txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=PaidTax)
        txtPaidTax.grid(row=0, column=1, sticky=W)

        lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text="Sub Total",bd=8)
        lblSubTotal.grid(row=1, column=0, sticky=W)
        txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=SubTotal)
        txtSubTotal.grid(row=1, column=1, sticky=W)


        lblTotal=Label(f2ab,font=('arial',16,'bold'),text="Total",bd=8)
        lblTotal.grid(row=2, column=0, sticky=W)
        txtTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=TotalCost)
        txtTotal.grid(row=2, column=1, sticky=W)


        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostOfDrinks.set("")
        CostOfCakes.set("")

        #====================Buttons===========================
        btnTotal=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Total",command=CostOfItem).grid(row=0, column=0)
        btnReceipt=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Receipt",command=Receipt).grid(row=0, column=1)
        btnReset=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Reset", command= Reset).grid(row=0, column=2)
        btnExit=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Exit", command= qExit).grid(row=0, column=3)

        root.mainloop()


if n==2:
            from tkinter import*
            from tkinter import messagebox
            import random
            import time
            import datetime
            root=Tk()
            root.geometry("1350x750+0+0")
            root.title("Cup and Kitaab")
            root.configure(background='red')

            Tops=Frame(root, width=1800, height=100,bd=20,relief="raise")
            Tops.pack(side=TOP)

            f1=Frame(root, width=900, height=650,bd=8,relief="raise")
            f1.pack(side=LEFT)
            f2=Frame(root, width=440, height=650,bd=8,relief="raise")
            f2.pack(side=RIGHT)

            ft2=Frame(f2, width=440, height=450,bd=12,relief="raise")
            ft2.pack(side=TOP)
            fb2=Frame(f2, width=440, height=250,bd=16,relief="raise")
            fb2.pack(side=BOTTOM)

            f1a=Frame(f1, width=900, height=330,bd=8,relief="raise")
            f1a.pack(side=TOP)
            f2a=Frame(f1, width=900, height=320,bd=6,relief="raise")
            f2a.pack(side=BOTTOM)

            f1aa=Frame(f1a, width=600, height=330, bd=16, relief="raise")
            f1aa.pack(side=LEFT)
            f1ab=Frame(f1a,width=400, height=330, bd=16, relief="raise")
            f1ab.pack(side=LEFT)

            f2aa=Frame(f2a, width=450, height=330, bd=14, relief="raise")
            f2aa.pack(side=LEFT)
            f2ab=Frame(f2a, width=450, height=600, bd=14, relief="raise")
            f2ab.pack(side=RIGHT)

            Tops.configure(background='black')
            f1.configure(background='black')
            f2.configure(background='black')

            lblInfo= Label(Tops, font=('arial',70,'bold'), text="  Cup and Kitaab Coffee Section  ", bd=10)
            lblInfo.grid(row=0, column=0)
            #===============================================Methods=======================================================================
            def qExit():
                qExit= messagebox.askyesno("Quit System","Do you Want to quit?")
                if qExit>0:
                    root.destroy()
                    return

            def Reset():
                PaidTax.set("")
                SubTotal.set("")
                TotalCost.set("")
                CostOfDrinks.set("")
                CostOfCakes.set("")
                ServiceCharge.set("")
                txtReceipt.delete("1.0",END)

                E_Latta.set("0")
                E_Espresso.set("0")
                E_Americano.set("0")
                E_Cortado.set("0")
                E_Mocha.set("0")
                E_Macchiato.set("0")
                E_FlatWhite.set("0")
                E_IrishCoffee.set("0")

                E_Bourbon.set("0")
                E_Oreo.set("0")
                E_C_K.set("0")
                E_CoffeeCake.set("0")
                E_Red_Velvet.set("0")
                E_Silk.set("0")
                E_XXL.set("0")
                E_Baker.set("0")
            #=============================CHECKbUTTONN======================================================================
            def chkbutton_value():
                if(var1.get()==1):
                    txtLatta.configure(state=NORMAL)
                elif(var1.get()==0):
                    txtLatta.configure(state=DISABLED)
                    E_Latta.set("0")
                if(var2.get()==1):
                    txtEspresso.configure(state=NORMAL)
                elif(var2.get()==0):
                    txtEspresso.configure(state=DISABLED)
                    E_Espresso.set("0")

                if(var3.get()==1):
                    txtAmericano.configure(state=NORMAL)
                elif(var3.get()==0):
                    txtAmericano.configure(state=DISABLED)
                    E_Americano.set("0")

                if(var4.get()==1):
                    txtCortado.configure(state=NORMAL)
                elif(var4.get()==0):
                    txtCortado.configure(state=DISABLED)
                    E_Cortado.set("0")

                if(var5.get()==1):
                    txtMocha.configure(state=NORMAL)
                elif(var5.get()==0):
                    txtMocha.configure(state=DISABLED)
                    E_Mocha.set("0")

                if(var6.get()==1):
                    txtMacchiato.configure(state=NORMAL)
                elif(var6.get()==0):
                    txtMacchiato.configure(state=DISABLED)
                    E_Macchiato.set("0")

                if(var7.get()==1):
                    txtFlatWhite.configure(state=NORMAL)
                elif(var7.get()==0):
                    txtFlatWhite.configure(state=DISABLED)
                    E_FlatWhite.set("0")

                if(var8.get()==1):
                    txtIrishCoffee.configure(state=NORMAL)
                elif(var8.get()==0):
                    txtIrishCoffee.configure(state=DISABLED)
                    E_IrishCoffee.set("0")

                if(var9.get()==1):
                    txtBourbon.configure(state=NORMAL)
                elif(var9.get()==0):
                    txtBourbon.configure(state=DISABLED)
                    E_Bourbon.set("0")

                if(var10.get()==1):
                    txtOreo.configure(state=NORMAL)
                elif(var10.get()==0):
                    txtOreo.configure(state=DISABLED)
                    E_Oreo.set("0")

                if(var11.get()==1):
                    txtC_K.configure(state=NORMAL)
                elif(var11.get()==0):
                    txtC_K.configure(state=DISABLED)
                    E_C_K.set("0")

                if(var12.get()==1):
                    txtCoffeeCake.configure(state=NORMAL)
                elif(var12.get()==0):
                    txtCoffeeCake.configure(state=DISABLED)
                    E_CoffeeCake.set("0")

                if(var13.get()==1):
                    txtRed_Velvet.configure(state=NORMAL)
                elif(var13.get()==0):
                    txtRed_Velvet.configure(state=DISABLED)
                    E_Red_Velvet.set("0")

                if(var14.get()==1):
                    txtSilk.configure(state=NORMAL)
                elif(var14.get()==0):
                    txtSilk.configure(state=DISABLED)
                    E_Silk.set("0")

                if(var15.get()==1):
                    txtXXL.configure(state=NORMAL)
                elif(var15.get()==0):
                    txtXXL.configure(state=DISABLED)
                    E_XXL.set("0")

                if(var16.get()==1):
                    txtBaker.configure(state=NORMAL)
                elif(var16.get()==0):
                    txtBaker.configure(state=DISABLED)
                    E_Baker.set("0")
                var1.set(0)
                var2.set(0)
                var3.set(0)
                var4.set(0)
                var5.set(0)
                var6.set(0)
                var7.set(0)
                var8.set(0)
                var9.set(0)
                var10.set(0)
                var11.set(0)
                var12.set(0)
                var13.set(0)
                var14.set(0)
                var15.set(0)
                var16.set(0)

                txtLatta.configure(state=DISABLED)
                txtEspresso.configure(state=NORMAL)
                txtAmericano.configure(state=NORMAL)
                txtCortado.configure(state=NORMAL)
                txtMocha.configure(state=NORMAL)
                txtMacchiato.configure(state=NORMAL)
                txtFlatWhite.configure(state=NORMAL)
                txtIrishCoffee.configure(state=NORMAL)
                txtBourbon.configure(state=NORMAL)
                txtOreo.configure(state=NORMAL)
                txtC_K.configure(state=NORMAL)
                txtCoffeeCake.configure(state=NORMAL)
                txtRed_Velvet.configure(state=NORMAL)
                txtSilk.configure(state=NORMAL)
                txtXXL.configure(state=NORMAL)
                txtBaker.configure(state=NORMAL)

            def CostOfItem():
                Item1=float(E_Latta.get())
                Item2=float(E_Espresso.get())
                Item3=float(E_Americano.get())
                Item4=float(E_Cortado.get())
                Item5=float(E_Mocha.get())
                Item6=float(E_Macchiato.get())
                Item7=float(E_FlatWhite.get())
                Item8=float(E_IrishCoffee.get())
                
                
                Item9=float(E_Bourbon.get())
                Item10=float(E_Oreo.get())
                Item11=float(E_C_K.get())
                Item12=float(E_CoffeeCake.get())
                Item13=float(E_Red_Velvet.get())
                Item14=float(E_Silk.get())
                Item15=float(E_XXL.get())
                Item16=float(E_Baker.get())

                PriceofDrinks=(Item1 * 100) + (Item2 * 80) + (Item3 * 105) + (Item4 * 110) + (Item5 * 75) + (Item6 * 95) + (Item7 * 45) + (Item8 * 120)
                PriceOfCookies=(Item9 * 20) + (Item10 * 40) + (Item11 * 90) + (Item12 * 30) + (Item13 * 60) + (Item14 * 85) + (Item15 * 70) + (Item16 * 90)
                DrinksPrice="₹", str('%.2f'%(PriceofDrinks))
                CakesPrice="₹",str('%.2f'%(PriceOfCookies))
                CostOfCakes.set(CakesPrice)
                CostOfDrinks.set(DrinksPrice)
                SC="₹", str('%.2f'%(19.75))
                ServiceCharge.set(SC)

                SubTotalofITEMS="₹", str('%.2f'%(PriceofDrinks + PriceOfCookies + 19.75))
                SubTotal.set(SubTotalofITEMS)

                Tax="₹", str('%.2f'%((PriceofDrinks + PriceOfCookies + 19.75)*0.05))
                PaidTax.set(Tax)
                TT=((PriceofDrinks + PriceOfCookies + 1.59)*0.05)
                TC="₹", str('%.2f'%(PriceofDrinks + PriceOfCookies + 19.75+TT))
                TotalCost.set(TC)
                

            def Receipt():
                txtReceipt.delete("1.0",END)
                x=random.randint(10908, 500876)
                randomRef = str(x)
                Receipt_Ref.set("BILL"+ randomRef)

                txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n")
                txtReceipt.insert(END,'Items\t\t\t\t\t'+ "Cost Of Items \n\n")
                txtReceipt.insert(END,'Latta: \t\t\t\t\t'+ E_Latta.get()+"\n")
                txtReceipt.insert(END,'Espresso: \t\t\t\t\t'+ E_Espresso.get()+"\n")
                txtReceipt.insert(END,'Americano: \t\t\t\t\t'+ E_Americano.get()+"\n")
                txtReceipt.insert(END,'Cortado: \t\t\t\t\t'+ E_Cortado.get()+"\n")
                txtReceipt.insert(END,'Mocha: \t\t\t\t\t'+ E_Mocha.get()+"\n")
                txtReceipt.insert(END,'Macchiato: \t\t\t\t\t'+ E_Macchiato.get()+"\n")
                txtReceipt.insert(END,'Flat White: \t\t\t\t\t'+ E_FlatWhite.get()+"\n")
                txtReceipt.insert(END,'Irish Coffee: \t\t\t\t\t'+ E_IrishCoffee.get()+"\n")
                txtReceipt.insert(END,'Bourbon: \t\t\t\t\t'+ E_Bourbon.get()+"\n")
                txtReceipt.insert(END,'Oreo: \t\t\t\t\t'+ E_Oreo.get()+"\n")
                txtReceipt.insert(END,'C&K Special: \t\t\t\t\t'+ E_C_K.get()+"\n")
                txtReceipt.insert(END,'Coffee cake: \t\t\t\t\t'+ E_CoffeeCake.get()+"\n")
                txtReceipt.insert(END,'Red Velvet: \t\t\t\t\t'+ E_Red_Velvet.get()+"\n")
                txtReceipt.insert(END,'Silk: \t\t\t\t\t'+ E_Silk.get()+"\n")
                txtReceipt.insert(END,'XXL: \t\t\t\t\t'+ E_XXL.get()+"\n")
                txtReceipt.insert(END,'Baker Special: \t\t\t\t\t'+ E_Baker.get()+"\n")
                txtReceipt.insert(END,'Cost Of Drinks:\t\t'+ CostOfDrinks.get()+'\tTax Paid:\t\t' + PaidTax.get()+"\n")
                txtReceipt.insert(END,'Cost Of Cookies: \t\t' + CostOfCakes.get()+'\tSubTotal:\t\t'+SubTotal.get()+ "\n")
                txtReceipt.insert(END,'Service Charge: \t\t' + ServiceCharge.get()+'\tTotal Cost:\t\t'+TotalCost.get()+ "\n")





            #===============================================Variables=======================================================================
            var1=IntVar()
            var2=IntVar()
            var3=IntVar()
            var4=IntVar()
            var5=IntVar()
            var6=IntVar()
            var7=IntVar()
            var8=IntVar()
            var9=IntVar()
            var10=IntVar()
            var11=IntVar()
            var12=IntVar()
            var13=IntVar()
            var14=IntVar()
            var15=IntVar()
            var16=IntVar()


            DateofOrder=StringVar()
            Receipt_Ref=StringVar()
            PaidTax=StringVar()
            SubTotal=StringVar()
            TotalCost=StringVar()
            CostOfCakes=StringVar()
            CostOfDrinks=StringVar()
            ServiceCharge=StringVar()

            E_Latta=StringVar()
            E_Espresso=StringVar()
            E_Americano=StringVar()
            E_Cortado=StringVar()
            E_Mocha=StringVar()
            E_Macchiato=StringVar()
            E_FlatWhite=StringVar()
            E_IrishCoffee=StringVar()

            E_Bourbon=StringVar()
            E_Oreo=StringVar()
            E_C_K=StringVar()
            E_CoffeeCake=StringVar()
            E_Red_Velvet=StringVar()
            E_Silk=StringVar()
            E_XXL=StringVar()
            E_Baker=StringVar()

            E_Latta.set("0")
            E_Espresso.set("0")
            E_Americano.set("0")
            E_Cortado.set("0")
            E_Mocha.set("0")
            E_Macchiato.set("0")
            E_FlatWhite.set("0")
            E_IrishCoffee.set("0")

            E_Bourbon.set("0")
            E_Oreo.set("0")
            E_C_K.set("0")
            E_CoffeeCake.set("0")
            E_Red_Velvet.set("0")
            E_Silk.set("0")
            E_XXL.set("0")
            E_Baker.set("0")

            DateofOrder.set(time.strftime("%d/%m/%Y"))


            #==================Coffees==========================
            Latta=       Checkbutton(f1aa, text="Latte \t", variable= var1, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=0,sticky=W)
            Espresso=    Checkbutton(f1aa, text="Espresso \t", variable= var2, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=1,sticky=W)
            Americano=   Checkbutton(f1aa, text="Americano \t", variable= var3, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=2,sticky=W)
            Cortado=     Checkbutton(f1aa, text="Cortado \t", variable= var4, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=3,sticky=W)
            Mocha=       Checkbutton(f1aa, text="Mocha \t", variable= var5, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=4,sticky=W)
            Macchiato=   Checkbutton(f1aa, text="Macchiato \t", variable= var6, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=5,sticky=W)
            FlatWhite=   Checkbutton(f1aa, text="Flat White \t", variable= var7, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=6,sticky=W)
            IrishCoffee= Checkbutton(f1aa, text="Irish Coffee \t", variable= var8, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=7,sticky=W)

            #======================Cookies======================
            Bourbon= Checkbutton(f1ab, text="Bourbon \t", variable= var9, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=0,sticky=W)
            Oreo= Checkbutton(f1ab, text="Oreo \t", variable= var10, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=1,sticky=W)
            C_K= Checkbutton(f1ab, text="C&K Special \t", variable= var11, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=2,sticky=W)
            CoffeeCake= Checkbutton(f1ab, text="Coffee Cake \t", variable= var12, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=3,sticky=W)
            Red_Velvet= Checkbutton(f1ab, text="Red Velvet Cake \t", variable= var13, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=4,sticky=W)
            Silk= Checkbutton(f1ab, text="Silk \t", variable= var14, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=5,sticky=W)
            XXL= Checkbutton(f1ab, text="XXL Cookie \t", variable= var15, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=6,sticky=W)
            Baker= Checkbutton(f1ab, text="Baker Cookie \t", variable= var16, onvalue=1, offvalue=0, font=('arial',18,'bold')).grid(row=7,sticky=W)
            #====================Enter Widget For Drinks===========================
            txtLatta= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Latta,state=NORMAL)
            txtLatta.grid(row=0, column=1)
            txtEspresso= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Espresso, state=NORMAL)
            txtEspresso.grid(row=1, column=1)
            txtAmericano= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Americano, state=NORMAL)
            txtAmericano.grid(row=2, column=1)
            txtCortado= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Cortado, state=NORMAL)
            txtCortado.grid(row=3, column=1)
            txtMocha= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Mocha, state=NORMAL)
            txtMocha.grid(row=4, column=1)
            txtMacchiato= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Macchiato, state=NORMAL)
            txtMacchiato.grid(row=5, column=1)
            txtFlatWhite= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_FlatWhite, state=NORMAL)
            txtFlatWhite.grid(row=6, column=1)
            txtIrishCoffee= Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_IrishCoffee, state=NORMAL)
            txtIrishCoffee.grid(row=7, column=1)
            #====================Enter Widget For Cookies===========================
            txtBourbon= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Bourbon,state=NORMAL)
            txtBourbon.grid(row=0, column=1)
            txtOreo= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Oreo,state=NORMAL)
            txtOreo.grid(row=1, column=1)
            txtC_K= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_C_K,state=NORMAL)
            txtC_K.grid(row=2, column=1)
            txtCoffeeCake= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_CoffeeCake,state=NORMAL)
            txtCoffeeCake.grid(row=3, column=1)
            txtRed_Velvet= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Red_Velvet,state=NORMAL)
            txtRed_Velvet.grid(row=4, column=1)
            txtSilk= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_Silk,state=NORMAL)
            txtSilk.grid(row=5, column=1)
            txtXXL= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left', textvariable=E_XXL,state=NORMAL)
            txtXXL.grid(row=6, column=1)
            txtBaker= Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Baker, state=NORMAL)
            txtBaker.grid(row=7, column=1)
            #====================Informations===========================
            lblReceipt=Label(ft2, font=('arial',12,'bold'), text="Reciept: ",bd=2, anchor='w')
            lblReceipt.grid(row=0,column=0,sticky=W)
            txtReceipt=Text(ft2, width=59, height=22, bg="White",bd=8, font=('arial',11,'bold'))
            txtReceipt.grid(row=1, column=0)
            #====================Cost Items Information===========================
            lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'),text="Cost Of Drinks",bd=8)
            lblCostofDrinks.grid(row=0, column=0, sticky=W)
            txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left', textvariable=CostOfDrinks)
            txtCostofDrinks.grid(row=0, column=1, sticky=W)

            lblCostofCookies=Label(f2aa,font=('arial',16,'bold'),text="Cost Of Cookies",bd=8)
            lblCostofCookies.grid(row=1, column=0, sticky=W)
            txtCostofCookies=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left', textvariable=CostOfCakes)
            txtCostofCookies.grid(row=1, column=1, sticky=W)


            lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text="Service Charge",bd=8)
            lblServiceCharge.grid(row=2, column=0, sticky=W)
            txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left')
            txtServiceCharge.grid(row=2, column=1, sticky=W)

            #====================Payment Information==============================
            lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text="Paid Tax",bd=8)
            lblPaidTax.grid(row=0, column=0, sticky=W)
            txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=PaidTax)
            txtPaidTax.grid(row=0, column=1, sticky=W)

            lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text="Sub Total",bd=8)
            lblSubTotal.grid(row=1, column=0, sticky=W)
            txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=SubTotal)
            txtSubTotal.grid(row=1, column=1, sticky=W)


            lblTotal=Label(f2ab,font=('arial',16,'bold'),text="Total",bd=8)
            lblTotal.grid(row=2, column=0, sticky=W)
            txtTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left', textvariable=TotalCost)
            txtTotal.grid(row=2, column=1, sticky=W)


            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            CostOfDrinks.set("")
            CostOfCakes.set("")

            #====================Buttons===========================
            btnTotal=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Total",command=CostOfItem).grid(row=0, column=0)
            btnReceipt=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Receipt",command=Receipt).grid(row=0, column=1)
            btnReset=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Reset", command= Reset).grid(row=0, column=2)
            btnExit=Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Exit", command= qExit).grid(row=0, column=3)

            root.mainloop()
