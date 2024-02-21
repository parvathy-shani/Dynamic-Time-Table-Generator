def read_file(filename):
    data = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split()
            data[line[0]] = int(line[1])
    return data

def generate_packets(timeslots_data, rooms_data):
    packets = []
    for time_slot, time_slot_number in timeslots_data.items():
        for room, room_number in rooms_data.items():
            packets.append((time_slot_number, room_number))
    return packets

def main():
    # Read timeslots and rooms data from text files
    timeslots_data = read_file('timeslots.txt')
    rooms_data = read_file('rooms.txt')

    # Generate packets
    packets = generate_packets(timeslots_data, rooms_data)

    # Write packets to a new text file
    with open('packets.txt', 'w') as f:
        f.write("Generated Packets (time slot, room):\n")
        for packet in packets:
            f.write(f"{packet[0]} {packet[1]}\n")

    print("Packets saved to 'packets.txt' file.")

if __name__ == "__main__":
    main()
