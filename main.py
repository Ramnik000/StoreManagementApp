from tkinter import*

def show_food():
    
    foodLabel = Label(Contentlabel, text="Available Food: ", font=("Arial", 13))
    foodLabel.grid(row=0, column=0, pady=2, padx=10)

   
    foodItem1 = Label(Contentlabel, text="Momos", bg="#FFC0CB", fg="Black")
    foodItem1.grid(row=1, column=0, pady=2, padx=10)
    foodItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    foodItemEntry1.grid(row=1, column=1, pady=2, padx=10)
    foodItemEntry1.insert(0, "0")

    foodItem2 = Label(Contentlabel, text="Pizza", bg="#FFC0CB", fg="Black")
    foodItem2.grid(row=2, column=0, pady=2, padx=10)
    foodItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    foodItemEntry2.grid(row=2, column=1, pady=2, padx=10)
    foodItemEntry2.insert(0, "0")

    foodItem3 = Label(Contentlabel, text="Burger", bg="#FFC0CB", fg="Black")
    foodItem3.grid(row=3, column=0, pady=2, padx=10)
    foodItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    foodItemEntry3.grid(row=3, column=1, pady=2, padx=10)
    foodItemEntry3.insert(0, "0")

def show_beauty():
  
    beautyLabel = Label(Contentlabel, text="Available Beauty and Cosmetics: ", font=("Arial", 13))
    beautyLabel.grid(row=0, column=2, pady=2, padx=10)

    
    beautyItem1 = Label(Contentlabel, text="Shampoo", bg="#FFC0CB", fg="Black")
    beautyItem1.grid(row=1, column=2, pady=2, padx=10)
    beautyItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    beautyItemEntry1.grid(row=1, column=3, pady=2, padx=10)
    beautyItemEntry1.insert(0, "0")

    beautyItem2 = Label(Contentlabel, text="Lipstick", bg="#FFC0CB", fg="Black")
    beautyItem2.grid(row=2, column=2, pady=2, padx=10)
    beautyItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    beautyItemEntry2.grid(row=2, column=3, pady=2, padx=10)
    beautyItemEntry2.insert(0, "0")

    beautyItem3 = Label(Contentlabel, text="Nail Polish", bg="#FFC0CB", fg="Black")
    beautyItem3.grid(row=3, column=2, pady=2, padx=10)
    beautyItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    beautyItemEntry3.grid(row=3, column=3, pady=2, padx=10)
    beautyItemEntry3.insert(0, "0")

def show_fashion():
        
    fashionLabel = Label(Contentlabel, text="Available Fashion: ", font=("Arial", 13))
    fashionLabel.grid(row=0, column=4, pady=2, padx=10)

    fashionItem1 = Label(Contentlabel, text="Shoes", bg="#FFC0CB", fg="Black")
    fashionItem1.grid(row=1, column=4, pady=2, padx=10)
    fashionItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    fashionItemEntry1.grid(row=1, column=5, pady=2, padx=10)
    fashionItemEntry1.insert(0, "0")

    fashionItem2 = Label(Contentlabel, text="Hoodies", bg="#FFC0CB", fg="Black")
    fashionItem2.grid(row=2, column=4, pady=2, padx=10)
    fashionItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    fashionItemEntry2.grid(row=2, column=5, pady=2, padx=10)
    fashionItemEntry2.insert(0, "0")

    fashionItem3 = Label(Contentlabel, text="Coat", bg="#FFC0CB", fg="Black")
    fashionItem3.grid(row=3, column=4, pady=2, padx=10)
    fashionItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    fashionItemEntry3.grid(row=3, column=5, pady=2, padx=10)
    fashionItemEntry3.insert(0, "0")

def show_grocery():
    groceryLabel = Label(Contentlabel, text="Available Grocery: ", font=("Arial", 13))
    groceryLabel.grid(row=0, column=6, pady=2, padx=10)

    groceryItem1 = Label(Contentlabel, text="Banana", bg="#FFC0CB", fg="Black")
    groceryItem1.grid(row=1, column=6, pady=2, padx=10)
    groceryItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    groceryItemEntry1.grid(row=1, column=7, pady=2, padx=10)
    groceryItemEntry1.insert(0, "0")

    groceryItem2 = Label(Contentlabel, text="Kiwi", bg="#FFC0CB", fg="Black")
    groceryItem2.grid(row=2, column=6, pady=2, padx=10)
    groceryItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    groceryItemEntry2.grid(row=2, column=7, pady=2, padx=10)
    groceryItemEntry2.insert(0, "0")

    groceryItem3 = Label(Contentlabel, text="oranges", bg="#FFC0CB", fg="Black")
    groceryItem3.grid(row=3, column=6, pady=2, padx=10)
    groceryItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    groceryItemEntry3.grid(row=3, column=7, pady=2, padx=10)
    groceryItemEntry3.insert(0, "0")


root=Tk()
root.title('🏪 Store Application')
root.geometry('1100x800')
root.config(bg="#E9386D")
headingLabel = Label(root, text="Store Management", font=("Arial", 24, 'bold'), bg="#FFC0CB", fg="Black")
headingLabel.pack(pady=10,fill= X)


CustomerLabel = LabelFrame(root, text="Customer Details", font=("Arial", 15, 'bold'), bg="#FFC0CB", fg="Black")
CustomerLabel.pack()
customerNameLabel = Label(CustomerLabel, text="Name", font=("Arial", 13),bg="#FFC0CB", fg="Black")
customerNameLabel.grid(row=0,column=0, pady=2,padx=10)

customerNameEntry = Entry(CustomerLabel, font=("Arial", 13))
customerNameEntry.grid(row=0,column=1)

customerLoyalyCard = Label(CustomerLabel,text="Loyalty Card",font=("Arial", 13),bg="#FFC0CB", fg="Black")
customerLoyalyCard.grid(row=0,column=2, pady=2,padx=10)

customerLoyalyCardEntry = Entry(CustomerLabel,font=("Arial", 13))
customerLoyalyCardEntry.grid(row=0,column=3)

customeBillNumber = Label(CustomerLabel, text="Bill Number",font=("Arial", 13),bg="#FFC0CB", fg="Black")
customeBillNumber.grid(row=0,column=4, pady=2,padx=10)

customeBillNumberEntry = Entry(CustomerLabel,font=("Arial", 13))
customeBillNumberEntry.grid(row=0,column=5)

searchButton = Button(CustomerLabel, text="SEARCH",font=("Arial", 13))
searchButton.grid(row=0,column=6,pady=5,padx=10)

ButtonLabel = LabelFrame(root, text="Select your Interest !!", font=("Arial", 15, 'bold'), bg="#FFC0CB", fg="Black")
ButtonLabel.pack(pady=10)

foodButton = Button(ButtonLabel, text="FOOD 🍕",font=("Arial", 13), command=show_food)
foodButton.grid(row=1,column=0, pady=5,padx=10)

beautyButton = Button(ButtonLabel, text="Beauty & Cosmetics 💅🏻",font=("Arial", 13), command=show_beauty)
beautyButton.grid(row=1,column=1, pady=5,padx=10)

fashionButton = Button(ButtonLabel, text="FASHION 👠",font=("Arial", 13),  command=show_fashion)
fashionButton.grid(row=1,column=2, pady=5,padx=10)

groceryButton = Button(ButtonLabel, text="GROCERY 🥗",font=("Arial", 13), command=show_grocery)
groceryButton.grid(row=1,column=3, pady=5,padx=10)

Contentlabel = LabelFrame(root,bg="#FFC0CB", fg="Black")
Contentlabel.pack(pady=10, fill=BOTH)


prices = {
    "Momos": 5.00,
    "Pizza": 8.00,
    "Burger": 7.00,
    "Shampoo": 15.00,
    "Lipstick": 20.00,
    "Nail Polish": 12.00,
    "Shoes": 40.00,
    "Hoodies": 25.00,
    "Coat": 60.00
}

FinalBillLabel = LabelFrame(root, text="Total", font=("Arial", 15, 'bold'), bg="#FFC0CB", fg="Black")
FinalBillLabel.pack(fill=BOTH)

foodTotal = Label(FinalBillLabel, text="Food Total :", font=("Arial", 13),bg="#FFC0CB", fg="Black")
foodTotal.grid(row=0,column=0, pady=2,padx=10 )

foodTotalEntry = Entry(FinalBillLabel, font=("Arial", 13), width=10, bd=5)
foodTotalEntry.grid(row=0,column=1)

beautyTotal = Label(FinalBillLabel,text="Beauty Total :",font=("Arial", 13),bg="#FFC0CB", fg="Black")
beautyTotal.grid(row=0,column=2, pady=2,padx=10)

beautyTotalEntry = Entry(FinalBillLabel,font=("Arial", 13), width=10, bd=5)
beautyTotalEntry.grid(row=0,column=3)

fashionTotal = Label(FinalBillLabel, text="Fashion Total :",font=("Arial", 13),bg="#FFC0CB", fg="Black")
fashionTotal.grid(row=0,column=4, pady=2,padx=10)

fashionTotalEntry = Entry(FinalBillLabel,font=("Arial", 13), width=10, bd=5)
fashionTotalEntry.grid(row=0,column=5)

groceryTotal = Label(FinalBillLabel, text="Grocery Total :",font=("Arial", 13),bg="#FFC0CB", fg="Black")
groceryTotal.grid(row=0,column=6, pady=2,padx=10)

groceryTotalEntry = Entry(FinalBillLabel,font=("Arial", 13), width=10, bd=5)
groceryTotalEntry.grid(row=0,column=7)

totalBill = Label(FinalBillLabel, text="Total :",font=("Arial", 13),bg="#FFC0CB", fg="Black")
totalBill.grid(row=0,column=8, pady=2,padx=10)

totalBillEntry = Entry(FinalBillLabel,font=("Arial", 13), width=10, bd=5)
totalBillEntry.grid(row=0,column=9)

billFrame = LabelFrame(root,text="Bill Area", font=("Arial", 13, 'bold'), bg="#FFC0CB", fg="Black")
billFrame.pack(side="left",pady=10, fill=Y, padx=20)
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
billText = Text(billFrame, font=("Arial", 13), yscrollcommand=scrollbar.set, wrap=WORD, bd=5, relief=GROOVE, height=10, width=70)
billText.pack(fill=Y, expand=True)
scrollbar.config(command=billText.yview)


root.mainloop()