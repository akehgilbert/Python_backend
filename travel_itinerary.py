'''
Travel itinerary from Essen HBF to Berlin HBF
'''
from datetime import datetime

# Train details are stored in a list of dictionaries called train
trains = [
    {
        "train_id": "ICE100",
        "departure_time": "08:00",
        "arrival_time": "11:00",
        "stops": ["Essen"," " "Duisburg"," " "Düsseldorf"," " "Köln"," " "Berlin"],
        "price": 150
    },
    {
        "train_id": "RE2",
        "departure_time": "10:00",
        "arrival_time": "16:00",
        "stops": ["Essen"," " "Mülheim"," " "Duisburg"," " "Düsseldorf"," " "Köln"," " "Bonn"," " "Berlin"],
        "price": 80
    },
    {
        "train_id": "S_Bahn",
        "departure_time": "09:00",
        "arrival_time": "20:00",
        "stops": ["Essen"," " "Mülheim"," " "Duisburg"," " "Düsseldorf"," " "Leverkusen"," " "Köln"," " "Berlin"],
        "price": 50
    },
    {
        "train_id": "Flixtrain",
        "departure_time": "07:00",
        "arrival_time": "09:30",
        "stops": ["Essen"," " "Duisburg"," " "Düsseldorf"," " "Köln"," " "Berlin"],
        "price": 120
    }
]

# calculates the duration of the trip with every particular train
def calculate_travel_time(departure, arrival):
    time_format = "%H:%M"
    departure_time = datetime.strptime(departure, time_format)
    arrival_time = datetime.strptime(arrival, time_format)
    duration = arrival_time - departure_time
    return duration

# displays the train_id, departure time, arrival time, train stops, price and duration
def display_trains():
    for train in trains:
        print(f"Train ID: {train['train_id']}")
        print(f"Departure Time: {train['departure_time']}")
        print(f"Arrival Time: {train['arrival_time']}")
        print(f"Stops: {','.join(train['stops'])}")
        print(f"Price: €{train['price']}")  
        print(f"Duration: {calculate_travel_time(train['departure_time'], train['arrival_time'])}")
        print('_'*40) 
display_trains()
# filter trains by budget
def filter_trains_by_budget(max_price):
    print(f"Trains with a price below €{max_price}:")
    for train in trains:
        if train['price'] <= max_price:
            print(f"# {train['train_id']} (€{train['price']})")
filter_trains_by_budget(120)



