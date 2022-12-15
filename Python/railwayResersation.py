"""
There are 10 stations in the Journey: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
There are 5 Seats: P1, P2, P3, P4, P5

P1 = [1, 2, 3, 4, 5]
P2 = [1, 2, 3, 4]
P3 = [1, 2, 3]
P4 = [2, 3, 4, 5]
P5 = [1, 2, 3, 4, 5]

Write a code to find seat for passenger traveling from x to y.
"""


class Reservation:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.P1 = [1, 2, 3, 4, 5]
        self.P2 = [1, 2, 3, 4]
        self.P3 = [1,2]
        self.P4 = [2, 3, 4, 5]
        self.P5 = [1, 2, 3, 4, 5]
        self.seats = {'P1':self.P1, 'P2':self.P2, 'P3':self.P3, 'P4':self.P4, 'P5':self.P5}
        self.stations()

    def stations(self):
        if self.stop - self.start > 1:
            staions = []
            for i in range(self.start+1, self.stop):
                staions.append(i)
            self.findSeat(staions)
        else:
            staions = [self.start, self.stop]
            self.findSeatOne(staions)

    def findSeatOne(self, stations):      #In case passenger travels only fro one stop(eg: 1-2 or 4-5)
        seats = set()
        for x in self.seats:
            if (self.stop not in self.seats[x]) or (self.start not in self.seats[x]):
                seats.add(x)
        print(seats)
        

    def findSeat(self, stations):
        seats = set()
        for x in self.seats:
            if not any(elem in stations  for elem in self.seats[x]):
                seats.add(x)
        
        print(seats)
a = Reservation(4,5)