import class_package.Person as Person

#create Customer Class
class Customer(Person.Person):
    def __init__(self, name, lastname, date, gender, customer_id, email):
        super().__init__(name, lastname, date, gender)
        self.customer_id = customer_id
        self.email = email


    def __str__(self):
        return super().__str__() + ' ' + self.customer_id + ' ' + self.email
    
    def say_hi_customer(self):
     print(f'Hello! My name is {self.name} {self.lastname} and my date is {self.date}. I am {self.gender}. My customer id is {self.customer_id} and my email is {self.email}')
    
    #setters and getters for ID
    def get_customer_id(self):
        return self.customer_id
   
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    # buy product method
    def buy_product(self):
        return "I'll buy this product"
    
    #add to favorite method
    def add_to_favorite(self):
        return "I'll add this product to my favorite list"



