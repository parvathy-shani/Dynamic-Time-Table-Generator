def extract_timeslot(line):
    return line.split()[0]

def extract_room_batch(line):
    room_parts = line.split()[1].split('-')
    return room_parts[1]  # Extract the batch from the room part

def extract_course_batch(line):
    course_parts = line.split()[3].split('-')
    return course_parts[2]  # Extract the batch from the course part

def check_batch_match(room_batch, course_batch):
    return room_batch == course_batch

# Read data from the file and perform batch matching validation
valid_lines = []

with open("encode_pairs_output.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        timeslot = extract_timeslot(line)
        room_batch = extract_room_batch(line)
        course_batch = extract_course_batch(line)

        if check_batch_match(room_batch, course_batch):
            valid_lines.append(line.strip())  # Store valid lines

# Write valid lines to the output file
with open("format_pairs_output.txt", "w") as output_file:
    for valid_line in valid_lines:
        output_file.write(valid_line + '\n')
