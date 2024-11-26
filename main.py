from tkinter import*

def show_food():
    
    foodLabel = Label(Contentlabel, text="Available Food: ", font=("Arial", 13))
    foodLabel.grid(row=0, column=0, pady=2, padx=10)

   
    foodItem1 = Label(Contentlabel, text="Momos", bg="#FFC0CB", fg="Black")
    foodItem1.grid(row=1, column=0, pady=2, padx=10)
    foodItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    foodItemEntry1.grid(row=1, column=1, pady=2, padx=10)

    foodItem2 = Label(Contentlabel, text="Pizza", bg="#FFC0CB", fg="Black")
    foodItem2.grid(row=2, column=0, pady=2, padx=10)
    foodItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    foodItemEntry2.grid(row=2, column=1, pady=2, padx=10)

    foodItem3 = Label(Contentlabel, text="Burger", bg="#FFC0CB", fg="Black")
    foodItem3.grid(row=3, column=0, pady=2, padx=10)
    foodItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    foodItemEntry3.grid(row=3, column=1, pady=2, padx=10)

def show_beauty():
  
    
    beautyLabel = Label(Contentlabel, text="Available Beauty and Cosmetics: ", font=("Arial", 13))
    beautyLabel.grid(row=0, column=2, pady=2, padx=10)

    
    beautyItem1 = Label(Contentlabel, text="Shampoo", bg="#FFC0CB", fg="Black")
    beautyItem1.grid(row=1, column=2, pady=2, padx=10)
    beautyItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    beautyItemEntry1.grid(row=1, column=3, pady=2, padx=10)

    beautyItem2 = Label(Contentlabel, text="Lipstick", bg="#FFC0CB", fg="Black")
    beautyItem2.grid(row=2, column=2, pady=2, padx=10)
    beautyItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    beautyItemEntry2.grid(row=2, column=3, pady=2, padx=10)

    beautyItem3 = Label(Contentlabel, text="Nail Polish", bg="#FFC0CB", fg="Black")
    beautyItem3.grid(row=3, column=2, pady=2, padx=10)
    beautyItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    beautyItemEntry3.grid(row=3, column=3, pady=2, padx=10)

def show_fashion():
        
    fashionLabel = Label(Contentlabel, text="Available Fashion: ", font=("Arial", 13))
    fashionLabel.grid(row=0, column=4, pady=2, padx=10)

    fashionItem1 = Label(Contentlabel, text="Shoes", bg="#FFC0CB", fg="Black")
    fashionItem1.grid(row=1, column=4, pady=2, padx=10)
    fashionItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    fashionItemEntry1.grid(row=1, column=5, pady=2, padx=10)

    fashionItem2 = Label(Contentlabel, text="Hoodies", bg="#FFC0CB", fg="Black")
    fashionItem2.grid(row=2, column=4, pady=2, padx=10)
    fashionItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    fashionItemEntry2.grid(row=2, column=5, pady=2, padx=10)

    fashionItem3 = Label(Contentlabel, text="Coat", bg="#FFC0CB", fg="Black")
    fashionItem3.grid(row=3, column=4, pady=2, padx=10)
    fashionItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    fashionItemEntry3.grid(row=3, column=5, pady=2, padx=10)

def show_grocery():
    groceryLabel = Label(Contentlabel, text="Available Grocery: ", font=("Arial", 13))
    groceryLabel.grid(row=0, column=6, pady=2, padx=10)

    groceryItem1 = Label(Contentlabel, text="Banana", bg="#FFC0CB", fg="Black")
    groceryItem1.grid(row=1, column=6, pady=2, padx=10)
    groceryItemEntry1 = Entry(Contentlabel, width=10, bd=5)
    groceryItemEntry1.grid(row=1, column=7, pady=2, padx=10)

    groceryItem2 = Label(Contentlabel, text="Kiwi", bg="#FFC0CB", fg="Black")
    groceryItem2.grid(row=2, column=6, pady=2, padx=10)
    groceryItemEntry2 = Entry(Contentlabel, width=10, bd=5)
    groceryItemEntry2.grid(row=2, column=7, pady=2, padx=10)

    groceryItem3 = Label(Contentlabel, text="oranges", bg="#FFC0CB", fg="Black")
    groceryItem3.grid(row=3, column=6, pady=2, padx=10)
    groceryItemEntry3 = Entry(Contentlabel, width=10, bd=5)
    groceryItemEntry3.grid(row=3, column=7, pady=2, padx=10)


root=Tk()
root.title('🏪 Store Application')
root.geometry('1100x650')
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

root.mainloop()