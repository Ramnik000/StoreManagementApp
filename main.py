from tkinter import*

root=Tk()
root.title('🏪 Store Application')
root.geometry('1200x600')
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

root.mainloop()