from random import randint  #importing random to get a random number
import time  #impoting time
import sys   #importing sys
timeb = 0.009
timea = 0.5
#function to print characters 1 at a time smoothly
def word(i):
    for character in i:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(timeb)
    time.sleep(timea)
#making a class product
class product():
    #function to store all the values in self
    def __init__(self, code = 420, name = "Tesla", price = 69, manufacture_cost = 69, stock = 69, EMUM = 69, sold = 69) -> None:
        self.code = code
        self.name = name #maybe change this into separate class so that you can have like player_one like name_1 ykyk
        self.price = price
        self.manufacture_cost = manufacture_cost
        self.stock = stock
        self.EMUM = EMUM
        self.sold = sold
    #All setters and getters for the vallues above to use them throught different files
    #gets the said value using the return statement
    @property
    def code(self):
        return self._code
    #sets the value for the said value
    @code.setter
    def code(self, i:int):
            self._code = i
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, i:str):
        self._name = i

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, i:float):
        self._price = i

    @property
    def manufacture_cost(self):
        return self._manufacture_cost
    @manufacture_cost.setter
    def manufacture_cost(self, i:float):
        self._manufacture_cost = i

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, i:int):
        self._stock = i
    
    @property
    def EMUM(self):
        return self._EMUM
    @EMUM.setter
    def EMUM(self, i:int):
        self._EMUM = i

    @property
    def sold(self):
        return self._sold
    @sold.setter
    def sold(self, i:int):
            self._sold = i
    #function used to simulate 12 months of sales and track inventory and calculate net profit
    def simulation(self):
        word(f"╔{'═'*25}╗\n║Product Code: {self.code}\n║Product Name: {self.name}\n╠\n║Sale Price: {self.price}\n║Manifacture Cost: {self.manufacture_cost}\n║Existing Stock: {self.stock}\n║Monthly Production: {self.EMUM}\n║Sold per month: {self.sold}\n╚{'═'*25}╝")
        time.sleep(4)
        #assigning variables for needed values
        stock = self.stock
        totalSold = 0
        totalNotFilled = 0
        totalManufactured = 0
        sold1 = self.sold - 10
        sold2 = self.sold + 10
        #for loop runs 12 times and calcultes everything 12 times
        for i in range(1,13):
            #variables for needed variables
            notFilled = 0
            emum = self.EMUM
            emumRange = randint(-10,10)
            emum += emumRange
            #checking if emem goes in negative since its not possible to
            if emum < 0:
                emum = 0
                pass
            #generating a number of items sold
            sold = randint(sold1, sold2)
            #checking if sold goes in negative since its not possible
            if sold < 0:
                sold = 0
                pass
            #adding the emum to stock value
            stock = (stock + emum)
            #checking if items sold it higher than the available stock
            if sold > stock:
                #adding value to orders not filled
                notFilled = sold - stock
                sold = stock
                stock = 0
                pass
            #if sold is less than the stock it goes through here
            elif sold <= stock:
                stock -= sold
                pass
            #Printing 12 months of all the data
            word(f"\n\nMonth {i}:\n»{' '*5}Manufactured: {emum} Units\n»{' '*5}Units sold: {sold} units\n»{' '*5}Orders not filled: {notFilled} units\n»{' '*5}Current stock: {stock} units")
            time.sleep(0.8)
            #adding values to a total amount
            totalSold += sold
            totalManufactured += emum
            totalNotFilled += notFilled
        #calculating the total net profit using the following formula
        netProfit = (totalSold*self.price)-(totalManufactured * self.manufacture_cost)
        #making sure net profit stays at 2 decimal place since its money
        netProfit = round(netProfit,2)
        #Printing the final total values along side the net profit
        word(f"\n\nTotal units sold: {totalSold}\nTotal Orders not filled: {totalNotFilled}\nTotal net profit: {netProfit}")