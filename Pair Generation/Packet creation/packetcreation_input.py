# Function to create rooms text file
def create_rooms_file(rooms_data, filename):
    with open(filename, 'w') as f:
        for room, number in rooms_data.items():
            f.write(f"{room} {number}\n")

# Function to create timeslots text file
def create_timeslots_file(timeslots_data, filename):
    with open(filename, 'w') as f:
        for timeslot, number in timeslots_data.items():
            f.write(f"{timeslot} {number}\n")

# Data for rooms and timeslots
rooms_data = {
    "Room-no.303": 1,
    "Room-no.309": 2
}

timeslots_data = {
    "9AM-MONDAY": 1,
    "10AM-MONDAY": 2,
    "11AM-MONDAY": 3,
    "1PM-MONDAY": 4,
    "2PM-MONDAY": 5,
    "3PM-MONDAY": 6,
    "9AM-TUESDAY": 7,
    "10AM-TUESDAY": 8,
    "11AM-TUESDAY": 9,
    "1PM-TUESDAY": 10,
    "2PM-TUESDAY": 11,
    "3PM-TUESDAY": 12,
    "9AM-WEDNESDAY": 13,
    "10AM-WEDNESDAY": 14,
    "11AM-WEDNESDAY": 15,
    "1PM-WEDNESDAY": 16,
    "2PM-WEDNESDAY": 17,
    "3PM-WEDNESDAY": 18,
    "9AM-THURSDAY": 19,
    "10AM-THURSDAY": 20,
    "11AM-THURSDAY": 21,
    "1PM-THURSDAY": 22,
    "2PM-THURSDAY": 23,
    "3PM-THURSDAY": 24,
    "9AM-FRIDAY": 25,
    "9:50AM-FRIDAY": 26,
    "10:40AM-FRIDAY": 27,
    "11:30AM-FRIDAY": 28,
    "2PM-FRIDAY": 29,
    "3PM-FRIDAY": 30
}

# File paths
rooms_filename = "rooms.txt"
timeslots_filename = "timeslots.txt"

# Create rooms file
create_rooms_file(rooms_data, rooms_filename)

# Create timeslots file
create_timeslots_file(timeslots_data, timeslots_filename)

print("Rooms and timeslots files created successfully.")