import Main  #importing Main as a method
#Making an object of class product in Main method
product = Main.product()

#event loop
while True:
    #Asking for user inputs for all the values
    try:
        product.code = int(input("Enter the product code: "))
        #Making sure user inputs the correct values
        if product.code >= 100 and product.code <= 1000:
            #If everything is good breaks of from loop
            break
        else:
            #if the input entered is not within above values makes an error
            raise TypeError
    except:
        #error prints this and goes back throught the loop until a valid input is entered
        print("INVALID! Input a value beween 100 and 1000")
while True:
    product.name = input("Enter the product name: ")
    break
while True:
    try:
        product.price = float(input("Enter the product price: "))
        if product.price > 0:
            break
        else:
            raise TypeError
    except:
        print("Enter a real number greater than zero!")
while True:
    try:
        product.manufacture_cost = float(input("Enter the manufacturing cost of the product: "))
        if product.manufacture_cost > 0:
            break
        else:
            raise TypeError
    except:
        print("Enter a real number greater than zero!")
while True:
    try:
        product.stock = int(input("Enter the existing stock level: "))
        if product.stock > 0:
            break
        else:
            raise TypeError
    except:
        print("Enter an integer number greater than zero!")
while True:
    try:
        product.EMUM = int(input("Enter the estimated monthly units manufactured: "))
        if product.EMUM >= 0:
            break
        else:
            raise TypeError
    except:
        print("Enter an integer number greater than or equal to zero!")
while True:
    try:
        product.sold = int(input("Enter the units sold per month: "))
        if product.sold > 0:
            break
        else:
            raise TypeError
    except:
        print("Enter an integer number greater than zero!")
#after all inputs have been entered directs it to the 12 month simulation function
product.simulation()


#For Testing
#********************************************************************************************
# product.code = 973
# product.name = "Computer"
# product.price = 2499.54
# product.manufacture_cost = 1200
# product.stock = 1
# product.EMUM = 2
# product.sold = 1
# product.simulation()