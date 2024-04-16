import json

# Load data from data.json
with open('combined_data.json', 'r') as json_file:
    data = json.load(json_file)

# Load teacher-course mapping from encode_events_output.txt
with open('encode_events_output.txt', 'r') as txt_file:
    teacher_course_mapping = [line.strip() for line in txt_file]

# Generate valid events
valid_events = []
invalid_events = []

for mapping in teacher_course_mapping:
    teacher_code, course_info = mapping.split()
    found = False
    for course in data:
        if course_info.startswith(course['Course code']):
            sem_code = course_info.split('-')[1]
            batch = course_info.split('-')[2]
            if any(teacher['teacher_code'] == teacher_code for teacher in course['lecturers']):
                valid_event = f"{teacher_code} {course['Course code']}-{sem_code}-{batch}"
                valid_events.append(valid_event)
                found = True
                break
    if not found:
        invalid_events.append(mapping)

# Write valid events to valid_events.txt
with open('format_events_output.txt', 'w') as output_file:
    for event in valid_events:
        output_file.write(f"{event}\n")

# Write invalid events to invalid_events.txt
#with open('invalid_events.txt', 'w') as output_file:
#   for event in invalid_events:
#       output_file.write(f"{event}\n")

print("Valid events have been stored in format_events_output.txt.")
#print("Invalid events have been stored in invalid_events.txt.")
