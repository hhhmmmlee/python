

def mycode202(num, all_cars):
    print(f"start 202")
    num = len(all_cars)//2
    in_cars = all_cars[0:num]
    out_cars = all_cars[num:]
    print(f"num is {num}")
    print(f"in_cars is {in_cars}")
    print(f"out_cars is {out_cars}")

    fast_map = []
    out_map = {}
    
    for j, car in enumerate(out_cars):
        out_map[hash(car)] = j

    for i, car in enumerate(in_cars):
        if out_map.get(hash(car)) > i :
           fast_map.append(car) 
    
    print(f"fast_map is {fast_map}")
        

def main(num):
    
    
    in_cars = []
    out_cars = []
    all_cars = ["Ford", "Volvo", "BMW", "Toyota", "Nissan", "Honda", "Ford", "BMW", "Toyota", "Nissan", "Honda", "Volvo"]

    
    if (num == 202) :
        mycode202(num, all_cars) 

    

    elif (num == 404) :
        print(f"num is 404")
    print(f"end of the program")


if __name__ == "__main__":
    main(202)