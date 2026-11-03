#simple function 
def greet() :
    print("Hello, welcome to the 100 Days of Python challenge!")
    print("I hope you are enjoying the journey so far.")
    print("Keep up the great work and happy coding!")

greet()



#function with input
def greet_with_name(name): #name is a parameter
      print(f"Hello, welcome to the 100 Days of Python challenge with {name}!")
      print(f"I hope you are enjoying the journey so far.")
      print(f"Keep up the great work and happy coding with {name}!")

greet_with_name("snow") #snow is an argument



#function with multiple input
def greet_with(name, location):
     print(f"hello {name}")
     print(f"what is it like in {location}")

greet_with("Mr.snow", "Newyork")#positional arguments

greet_with(location="Germany", name="Mr.snow")#keyword arguments
