class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle1 = Vehicle("ASD626", "Car", "Tyler Carlise")
vehicle2 = Vehicle("VSD513", "Motorcycle", "Joe Montana")

print(f"Vehicle 1 Owner: {vehicle1.owner}")
print(f"Vehicle 2 Owner: {vehicle2.owner}")

vehicle1.update_owner("Nolan Ryan")
vehicle2.update_owner("Michael Jordan")

print(f"Vehicle 1 New Owner: {vehicle1.owner}")
print(f"Vehicle 2 New Owner: {vehicle2.owner}")


#--------------------------------------------------------------------------#

# Question 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0  

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        return self.participants

event = Event("Music Festival", "10-03-2020")

event.add_participant()
event.add_participant()
event.add_participant()

print(f"Total Participants: {event.get_participant_count()}")