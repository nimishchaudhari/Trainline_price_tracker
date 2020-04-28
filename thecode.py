# Code for Parsing
import trainline
import csv

def find_train(dept_stat,arr_stat,from_date,to_date):
    results = trainline.search(
	departure_station=dept_stat,
	arrival_station=arr_stat,
	from_date=from_date,
	to_date=to_date)
    x = results.csv()
    data = x.split("\n")
    data = [i.split(";") for i in data]
    return str(data)

def cheapest_ticket(dept_stat,arr_stat,from_date,to_date):
    results = trainline.search(
    departure_station=dept_stat,
    arrival_station=arr_stat,
    from_date=from_date,
    to_date=to_date)
    x = results.csv()
    data = x.split("\n")
    data = [i.split(";") for i in data]
    head = data.pop(0)
    data.pop(-1)
    prices = []
    for i in data:                      #To make all the euro values integer
        price = i[4].split(",")
        i[4] = int(price[0])            #Splitted the price into two, taken first part
        prices.append(i[4])
    min_prices = []
    min_val = min(prices)
    for i in range(0,len(prices)):
        if min_val == prices[i]:
            min_prices.append(i)

    print(min_prices) # Giving me the array locations ofthe minimum prices found

    cheapest_bookings = []
    for i in min_prices:
            cheapest_bookings.append(data[i])
    cheapest_bookings.insert(0,head)
    def print_op(list):
        x = ""
        for i in list:
            x = x + str(i) + '\n'
        return x
    return str(print_op(cheapest_bookings))

print("Cheapest Tickets:")
print(cheapest_ticket(
    "Paris","Nantes",
    "15/06/2020 10:00",
    "27/06/2020 08:00"
))