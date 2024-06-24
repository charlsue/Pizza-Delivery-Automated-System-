while True:
  print("Welcome to the Python Pizza Deliveries")
  import time
  time.sleep(1)
  print("\n\n")
  while True:
    size = input("What size pizza do you want? S, M, or L\n")
    bill = 0
    if size == "S":
      bill += 15
      break
    if size == "M":
      bill += 20
      break
    if size == "L":
      bill += 25
      break
    else: 
      print("Please enter a valid size")
    continue
    
  add_pepperoni = input("Do you want pepperoni? Y or N\n")
  extra_cheese = input("Do you want extra cheese? Y or N\n")
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1  
      
  print("\n")
  print("Thank you for choosing Python Pizza Deliveries")
  print(f"Your final bill is ${bill}")
  print("\n")
  new_customer = input("Is there another customer? Y or N ")
  if new_customer == "N":
    print("Have a good day!")
    break
    
  else:
    print("\n")
    
