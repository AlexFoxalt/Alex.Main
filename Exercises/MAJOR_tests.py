from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    direct_flight = []
    not_direct_flights = []
    for x, y, price in costs:
        if x in a and y in b or x in b and y in a:
            direct_flight.append(price)
        elif x in a and y not in b or x in b and y not in a:
            not_direct_flights.append(price)
        elif x not in a and y in b or x not in b and y in a:
            not_direct_flights.append(price)
    if not direct_flight:
        return sum(not_direct_flights)
    if not not_direct_flights:
        return direct_flight[0]
    if not direct_flight and not not_direct_flights:
        return 0
    print(not_direct_flights)
    return direct_flight[0] if sum(not_direct_flights) > direct_flight[0] else sum(not_direct_flights)


print(cheapest_flight([['A', 'C', 40],
                       ['A', 'B', 20],
                       ['A', 'D', 20],
                       ['B', 'C', 50],
                       ['D', 'C', 70]],
                      'D',
                      'C'))
