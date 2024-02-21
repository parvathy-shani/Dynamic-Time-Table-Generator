def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line by space and consider the part after space
            line_parts = line.strip().split(' ', 1)
            if len(line_parts) > 1:
                data.append(line_parts[1])
    return data

def generate_events(lecturers_data, classes_data, students_data):
    events = []
    for lecturer in lecturers_data:
        for class_name in classes_data:
            for student_set in students_data:
                events.append((lecturer, class_name, student_set))
    return events

def main():
    # Read data from text files considering the part after space
    lecturers_data = read_file('lecturers.txt')
    classes_data = read_file('classes.txt')
    students_data = read_file('students.txt')

    # Generate events
    events = generate_events(lecturers_data, classes_data, students_data)

    # Write events to a new text file
    with open('events.txt', 'w') as f:
        f.write("Generated Events (lecturer, class, student set):\n")
        for event in events:
            f.write(f"{event[0]} {event[1]} {event[2]}\n")

    print("Events saved to 'events.txt' file.")

if __name__ == "__main__":
    main()
