def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        next(f)  # Skip the first line (heading)
        for line in f:
            data.append(line.strip())
    return data

def generate_pairs(packets_data, events_data):
    pairs = []
    for packet in packets_data:
        for event in events_data:
            pairs.append((packet, event))
    return pairs

def main():
    # Read data from text files starting from the second line
    packets_data = read_file('packets.txt')
    events_data = read_file('events.txt')

    # Generate pairs
    pairs = generate_pairs(packets_data, events_data)

    # Write pairs to a new text file
    with open('pairs.txt', 'w') as f:
        f.write("Generated Pairs (packet, event):\n")
        for pair in pairs:
            f.write(f"{pair[0]} {pair[1]}\n")

    print("Pairs saved to 'pairs.txt' file.")

if __name__ == "__main__":
    main()
