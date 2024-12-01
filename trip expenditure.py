def hotelcost(days):
    return 1500*days
def flightcost(city):
    if city=="visakhapatnam":
        return 8000
    elif city=="amravati":
        return 7200
    elif city=="tirupati":
        return 5000
    elif city=="vijaywada":
        return 7200
def rentalcar(days):
    if days >=7:
        return 8000*days - 2000
    elif days >=3:
        return 8000*days - 1000
    else:
        return 8000*days
def tripcost(city,days,extramoneyspent):
    return rentalcar(days)+flightcost(city)+hotelcost(days)+extramoneyspent



print(tripcost("tirupati",14,3000))
