"""
Model to aircraft flights
"""
from pprint import pprint as pp

class Flight:

    '''
    instance method for initializing new objects
    it is an initializer not a constructor
    self ~ this in java
    _number ? why
      - to avoid name clash with number()
      - by convention, implementation details start with underscore
     '''

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No Airline code in Flight '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid Airline code in Flight '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number in Flight '{number}'")

        self._number = number
        self._aircraft = aircraft

        # seat booking data structure will be list of dictionaries
        # list : number of rows
        # dict : mapping of seat to passenger
        rows, seats = self._aircraft.seating_plan()
        '''
        say xxx ---> {seat_letter: None for seat_letter in seats} is dictionary comprehension
        [ xxx for _ in rows ] list comprehension
        so, it is list of dictionaries
        
        [None,
         {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
         {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
         .
         .
          {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}]
        '''
        self._seating = [None] + [{seat_letter: None for seat_letter in seats} for _ in rows]

    def allocate_seat(self, seat, passenger_name):
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat Occupied {seat}")

        self._seating[row][letter] = passenger_name

    def reallocate_passenger(self, from_seat, to_seat):
        row_from, letter_from = self._parse_seat(from_seat)

        if self._seating[row_from][letter_from] is None:
            raise ValueError (f"No Passenger to relocate from seat {from_seat}")

        if self._seating[row_from][letter_from] is not None:
            raise ValueError (f"Already occupied Passenger seat {from_seat}")

        row_to, letter_to = self._parse_seat(from_seat)

        self._seating[row_to][letter_to] = self._seating[row_from][letter_from]
        self._seating[row_from][letter_from] = None

    def num_available_seats(self):
        return sum(sum (1 for s in row.values if s is None) # seat per row
                   for row in self._seating if row is not None) # each row

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        # get last character as seat letter
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {seat}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {seat}")

        if row not in rows:
            raise ValueError(f"Out of range row in seat {seat}")

        return row, letter

    def aircraft_model(self):
        return self._aircraft.model()

    # self basically holds the reference of the instance on which the method is called.
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def current_seating(self):
        return self._seating

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seat()):
            card_printer(passenger, seat, self._number, self.aircraft_model())

    def _passenger_seat(self):
        rows, seat_letters = self._aircraft.seating_plan()
        for r in rows:
            for sl in seat_letters:
                passenger = self._seating[r][sl]
                if passenger is not None:
                    yield passenger, f"{r} {sl}" #tuple


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def total_seats(self):
        r, sl = self.seating_plan()
        return len (r) * len(sl)


class A380 (Aircraft):
    def model(self):
        return "A-380"

    def seating_plan(self):
        return range(1, 30), "ABCDEF"


class Boeing777 (Aircraft):
    def model(self):
        return "Boeing-777"

    def seating_plan(self):
        return range(1, 20), "ABCDEF"


def console_card_printer(passenger, seat, flight, aircraft):
    output = f"| Name : {passenger} " \
             f" Seat : {seat}" \
             f" Flight : {flight}"   \
             f" Aircraft: {aircraft} |"

    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()

'''
class invariants:
Truths about an object that endure for its lifetime
'''

if __name__ == "__main__":
    f = Flight("AI3344", A380("D-WIVEDI"))
    f.allocate_seat("1A", "Chirag Nayak")
    f.allocate_seat("1B", "Saanvi Nayak")
    f.allocate_seat("1C", "Yamini Dwivedi")
    f.allocate_seat("2A", "SJV")
    pp(f.current_seating())
    pp(f._aircraft.total_seats())
    f.make_boarding_cards(console_card_printer)

    g = Flight("SD1234", Boeing777("N-AYAK"))
    g.allocate_seat("1A", "Chirag Nayak")
    g.allocate_seat("1B", "Saanvi Nayak")
    g.allocate_seat("1C", "Yamini Dwivedi")
    g.allocate_seat("2A", "SJV")
    pp(g.current_seating())
    pp(g._aircraft.total_seats())
    g.make_boarding_cards(console_card_printer)
 
