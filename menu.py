from class_package.Customer import Customer

#Instance a Customer
#object and print its details
#using the instance method __str__().
customer1 = Customer("José", "Carrizo", "24/09/192", "male", "0001", "carrizoja@gmail.com")  #Creating an object of type
print(customer1)  #Printing the object
customer1.say_hi_customer()
print(customer1.buy_product())
print(customer1.add_to_favorite())
print(customer1.get_customer_id())

