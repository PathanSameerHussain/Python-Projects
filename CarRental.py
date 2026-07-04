print("======= CAR RENTAL SYSTEM =======")
car = {}
while True:

    print("1. Add Car, 2. Display All Cars, 3. Search Car, 4. Rent a Car, 5. Return a Car, 6. Update Car Details, 7. Delete Car, 8. Show Available Cars, 9. Show Rented Cars, 10. Show Total Cars, 11. Exit")
    choice = int(input(("choose from (1-11): ")))
    if choice == 1:
        cid = input("enter car id: ")
        if cid in car:
            print("the car id already exists")
        else:
            brand = input("enter brand name: ")
            model = input("enter car model: ")
            price = int(input("enter car price per day: "))

            car[cid] = {"brand": brand, "model": model, "price": price, "availability": True}
            print("new car is added succesfully")
    elif choice == 2:
        if len(car) == 0:
            print("there are no cars available")
        else:
            print(car)
    elif choice == 3:
        cid = input("enter car id to search: ")
        if cid in car:
            print(car[cid])
        else:
            print("invalid cid entered")
    elif choice == 4:
        cid = input("enter car id: ")
        if cid in car:
            days = int(input("enter rental days: "))
            print("the total amount would be ",days*car[cid]["price"])
            car[cid]["availability"] = False
            print("car is rented succesfully")
        else:
            print("invalid car id entered")
    elif choice == 5:
        #return a car
        cid = input("enter car id: ")
        if cid in car:
            if car[cid]["availability"] == False:
                car[cid]["availability"] = True
                print("car is returned succesfully")
            else:
                print("car was not rented")
        else:
            print("this car was not rented")
    elif choice == 6:
        #update car details
        cid = input("enter car id: ")
        if cid in car:
            print("what do you want to update please select from(1-3): ")
            choice1 = int(input(("1.brand 2.model 3.price: ")))
            if choice1 == 1:
                new_brand = input("enter new brand name: ")
                car[cid]["brand"] = new_brand
            elif choice1 == 2:
                new_model = input("enter new model name: ")
                car[cid]["model"] = new_model
            elif choice1 == 3:
                new_price = input("enter new price per day: ")
                car[cid]["price"] = new_price
        else:
            print("invalid car id entered")
    elif choice == 7:
        #delete car
        cid = input("enter car id: ")
        if cid in car:
            deleted_car = car.pop(cid) 
            print(f"{deleted_car} is deleted succesfully ")
        else:
            print("invalid car id entered")
    elif choice == 8:
        #Show Available Cars
        if car[cid]["availability"] == True:
            print(car[cid])
        else:
            print("there are no cars available")
    elif choice == 9:
        if car[cid]["availability"] == False:
            print(car[cid])
        else:
            print("there are no rented cars available")
    elif choice == 10:
        # Show Total Cars
        if len(car)==0:
            print("there are no cars")
        else:
            print(len(car))
    elif choice == 11:
        print("you have succesfully exited the car renting system")
        break
        

