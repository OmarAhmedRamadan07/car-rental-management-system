import json

def add_car_details():
    data = []

    file = open("car_data.json", "r")
    data = json.load(file)
    file.close()

    
    car_model = input("enter the car model: ").capitalize()
    reg_number = input("enter the reg number: ")
    price_per_day = float(input("enter the price: "))
    car_days = int(input("enter the car days: "))
    res_date = input("enter the reservation date (YYYY-MM-DD): ")
    
    new_car = {
        "car_model": car_model,
        "reg_number": reg_number,
        "price_per_day": price_per_day,
        "car_days": car_days,
        "reservation_date": res_date
    }
    
    data.append(new_car)
    
    file = open("car_data.json", "w")
    json.dump(data, file, indent=3)
    file.close()
    print(f"Car {car_model} added successfully.")

def book_car_delete(username):
    data = []
    history = []
    try:
        file = open("car_data.json", "r")
        data = json.load(file)
        file.close()
    except:
        pass
    
    try:
        file = open("rental_history.json", "r")
        history = json.load(file)
        file.close()
    except:
        pass
    
    for car in data:
        print("\n==================================================")
        for key, value in car.items():
            print(f"{key}: {value}")
    
    car_model_delete = input("enter the car name to book: ").capitalize()
    rental_days = float(input("enter the days to rent the car: "))
    
    for car in data:
        if car["car_model"] == car_model_delete:
            total_cost = car["price_per_day"] * rental_days
            history_entry = {
                "username": username,
                "car_model": car["car_model"],
                "reg_number": car["reg_number"],
                "rental_days": rental_days,
                "total_cost": total_cost,
                "reservation_date": car["reservation_date"]
            }
            history.append(history_entry)
            data.remove(car)
            
            file = open("car_data.json", "w")
            json.dump(data, file, indent=3)
            file.close()
            
            file = open("rental_history.json", "w")
            json.dump(history, file, indent=3)
            file.close()
            
            print(f"Car {car_model_delete} booked. Total cost: {total_cost}")
            return
    print(f"Car {car_model_delete} not found.")

def display_cars():
    data = []
    try:
        file = open("car_data.json", "r")
        data = json.load(file)
        file.close()
    except:
        pass
    
    choose = input("choose option \n 1.show all cars \n 2.show car using date: ")
    
    if choose == "1":
        print("========================== car data: =================================")
        for car in data:
            print("\n==================================================")
            for key, value in car.items():
                print(f"{key}: {value}")
    elif choose == "2":
        date_car = input("enter the reservation date (YYYY-MM-DD): ")
        found = False
        for car in data:
            if car["reservation_date"] == date_car:
                found = True
                for key, value in car.items():
                    print(f"{key}: {value}")
        if not found:
            print("No cars found for this date.")
    else:
        print("Invalid option, please try again.")

def update_car_data():
    data = []
    try:
        file = open("car_data.json", "r")
        data = json.load(file)
        file.close()
    except:
        pass
    
    car_name = input("enter the car name to update: ").capitalize()
    
    for car in data:
        if car["car_model"] == car_name:
            new_car_model = input("enter the new car name: ").capitalize()
            new_reg_number = input("enter the new registration number: ")
            new_price_per_day = float(input("enter the new price per day: "))
            new_car_days = int(input("enter the new car days number: "))
            new_res_date = input("enter the new reservation date (YYYY-MM-DD): ")
            
            car["car_model"] = new_car_model
            car["reg_number"] = new_reg_number
            car["price_per_day"] = new_price_per_day
            car["car_days"] = new_car_days
            car["reservation_date"] = new_res_date
            
            file = open("car_data.json", "w")
            json.dump(data, file, indent=3)
            file.close()
            
            print(f"Data updated for car {car_name}")
            return
    print(f"Car {car_name} not found.")

def display_rental_history(username, is_admin=False):
    history = []
    try:
        file = open("rental_history.json", "r")
        history = json.load(file)
        file.close()
    except:
        pass
    
    if is_admin:
        choose = input("choose option \n 1.show all rental history \n 2.show specific user's history: ")
        if choose == "1":
            print("========================== rental history: =================================")
            for entry in history:
                print("\n==================================================")
                for key, value in entry.items():
                    print(f"{key}: {value}")
        elif choose == "2":
            target_user = input("enter the username: ")
            found = False
            print(f"========================== {target_user}'s rental history: =================================")
            for entry in history:
                if entry["username"] == target_user:
                    found = True
                    print("\n==================================================")
                    for key, value in entry.items():
                        print(f"{key}: {value}")
            if not found:
                print(f"No rental history for {target_user}.")
        else:
            print("Invalid option.")
    else:
        print(f"========================== {username}'s rental history: =================================")
        found = False
        for entry in history:
            if entry["username"] == username:
                found = True
                print("\n==================================================")
                for key, value in entry.items():
                    print(f"{key}: {value}")
        if not found:
            print("No rental history found.")

def cancel_booking(username, is_admin=False):
    history = []
    cars = []
    try:
        file = open("rental_history.json", "r")
        history = json.load(file)
        file.close()
    except:
        pass
    
    try:
        file = open("car_data.json", "r")
        cars = json.load(file)
        file.close()
    except:
        pass
    
    if is_admin:
        target_user = input("enter the username of the booking to cancel: ")
        car_model = input("enter the car model to cancel: ").capitalize()
    else:
        target_user = username
        car_model = input("enter the car model to cancel: ").capitalize()
    
    for entry in history:
        if entry["username"] == target_user and entry["car_model"] == car_model:
            car_to_restore = {
                "car_model": entry["car_model"],
                "reg_number": entry["reg_number"],
                "price_per_day": entry["total_cost"] / entry["rental_days"],
                "car_days": int(entry["rental_days"]),
                "reservation_date": entry["reservation_date"]
            }
            cars.append(car_to_restore)
            history.remove(entry)
            
            file = open("car_data.json", "w")
            json.dump(cars, file, indent=3)
            file.close()
            
            file = open("rental_history.json", "w")
            json.dump(history, file, indent=3)
            file.close()
            
            print(f"Booking for {car_model} by {target_user} cancelled.")
            return
    print(f"No booking found for {car_model} by {target_user}.")

start1 = True

while start1:
    user_operation = input("choose option \n 1.Login \n 2.SignUp \n 3.exit: ")
    
    if user_operation == "1":
        user_data = []
        try:
            file = open("users_data.json", "r")
            user_data = json.load(file)
            file.close()
        except:
            pass
        
        user_name = input("enter the user name: ")
        password = input("enter the password: ")
        
        if user_name == "admin" and password == "12345":
            start1 = False
            start2 = True
            
            while start2:
                user_option = input("\nchoose option \n 1.add car \n 2.book car \n 3.update car \n 4.show cars \n 5.view rental history \n 6.cancel booking \n 7.exit: ")
                
                if user_option == "1":
                    add_car_details()
                elif user_option == "2":
                    book_car_delete("admin")
                elif user_option == "3":
                    update_car_data()
                elif user_option == "4":
                    display_cars()
                elif user_option == "5":
                    display_rental_history("admin", is_admin=True)
                elif user_option == "6":
                    cancel_booking("admin", is_admin=True)
                elif user_option == "7":
                    start2 = False
                    print("You have exited.")
                else:
                    print("Invalid option, try again.")
        
        else:
            for user in user_data:
                if user["user_name"] == user_name and user["password"] == password:
                    start1 = False
                    start3 = True
                    
                    while start3:
                        user_option = input("\nchoose option \n 1.book car \n 2.show cars \n 3.view rental history \n 4.cancel booking \n 5.exit: ")
                        
                        if user_option == "1":
                            book_car_delete(user_name)
                        elif user_option == "2":
                            display_cars()
                        elif user_option == "3":
                            display_rental_history(user_name)
                        elif user_option == "4":
                            cancel_booking(user_name)
                        elif user_option == "5":
                            start3 = False
                            print("You have exited.")
                        else:
                            print("Invalid option, try again.")
                    break
            else:
                print("Invalid username or password.")
    
    elif user_operation == "2":
        data = []
        try:
            file = open("users_data.json", "r")
            data = json.load(file)
            file.close()
        except:
            pass
        
        new_user_name = input("enter the user name: ")
        new_user_password = input("enter the password: ")
        
        new_user = {
            "user_name": new_user_name,
            "password": new_user_password
        }
        
        data.append(new_user)
        
        file = open("users_data.json", "w")
        json.dump(data, file, indent=3)
        file.close()
        
        print("User has been added.")
    
    elif user_operation == "3":
        print("You have exited.")
        break
    
    else:
        print("Invalid option, try again.")