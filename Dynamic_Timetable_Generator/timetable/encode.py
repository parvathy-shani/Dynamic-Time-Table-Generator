import pandas as pd 
def encode_timeslots(data: dict) -> str:
    gene_positions = {}
    gene_count = 1
    for day, slots in data.items():
        for slot in slots:
            gene_positions["G"+str(gene_count)] = f'{day} {slot}'
            gene_count+=1

    return gene_positions

def generate_code(room_name, allotted_batch, purpose):
    # Extract first three letters of room name
    room_code = room_name[:3]
    # Extract first three letters of allotted batch
    batch_code = allotted_batch[:3]
    # Generate purpose code 'l' for lecture, 'o' for other purposes
    purpose_code = 'l' if purpose.lower() == 'lecture' else 'o'
    # Combine codes to form 7-character code
    code = f"{room_code}-{batch_code}-{purpose_code}"
    return code

def room(data: dict) -> dict:
    # Generate codes for each classroom
    codes = []
    for classroom in data:
        code = generate_code(classroom["room_name"], classroom["allotted_batch"], classroom["purpose"])
        codes.append(code)

    return codes

def lectures(data):
    df = pd.DataFrame(data)
    # Apply the generate_code function to each row in the DataFrame

    return df.apply(generate_codez, axis=1).to_string(index=False)

# Generate codes based on the given rules
def generate_codez(row):
    department_code = 'CS'
    position_mapping = {
        'Professor': 'PP',
        'Associate Professor': 'AP',
        'Assistant Professor': 'AA'
    }
    position_code = position_mapping.get(row['position'], 'AA')  # Default to Assistant Professor if position not found
    order_code = str(row.name + 1).zfill(2)  # Adding 1 to index since index starts from 0, and then zero padding
    preference_mapping = {
        'Forenoon': 'f',
        'Afternoon': 'a',
        'NIL': 'n'  # Assuming 'n' for NIL preference
    }
    preference_code = preference_mapping.get(row['preferred_timeslot'], 'n')  # Default to 'n' if preference not found
    return f"{department_code}{position_code}{order_code}{preference_code}"


# Function to convert course data into code
def convert_course_to_code(course_data):
    course_code, sem_code, batch = course_data['course_code'], course_data['section'], course_data['batch']
    sem_code = "m" if sem_code == "Minor" else "h" if sem_code == "Honours" else sem_code[0]
    return f"{course_code.replace(' ', '')}-{sem_code}-{batch}"

def courses(data):
    course_codes = [convert_course_to_code(course) for course in data]
    return course_codes

def extract_timeslot(line):
    return line[0][0]

def extract_room_batch(line):
    room_parts = line[0][1].split('-')
    return room_parts[1]  # Extract the batch from the room part

def extract_course_batch(line):
    course_parts = line[1][1].split('-')
    return course_parts[2]  # Extract the batch from the course part

def check_batch_match(room_batch, course_batch):
    return room_batch == course_batch

def formatted_pairs(data):
    # Read data from the file and perform batch matching validation
    valid_lines = []
    for line in data:
        print(line)
        timeslot = extract_timeslot(line)
        room_batch = extract_room_batch(line)
        course_batch = extract_course_batch(line)

        if check_batch_match(room_batch, course_batch):
            valid_lines.append(line)  # Store valid lines

    return valid_lines

def generate_gene(data_line, gene_number):
    # Split the data line into relevant attributes
    attributes = data_line.strip().split()
    event = f"G{gene_number} {attributes[1]} {attributes[2]} {attributes[3]}"
    return event

def generate_chromosome(input_data, batch):
    chromosome = []
    gene_number = 1
    for line in input_data:
        gene = generate_gene(line, gene_number)
        # Extract batch information from the room code
        room_code = line.split()[1]
        if batch in room_code:
            chromosome.append(gene)
            gene_number += 1
            if gene_number > 30:  # Stop at G30
                break
    return chromosome

def chromosome_generation(data):
    batches = ['S2C', 'S2D', 'S4C', 'S4D', 'S6C', 'S6D', 'S8C', 'S8D']  # Names of the batches
    num_chromosomes_per_batch = 50  # Number of chromosomes for each batch

    for batch in batches:
        chromosomes = []
        for _ in range(num_chromosomes_per_batch):
            chromosome = generate_chromosome(data, batch)
            chromosomes.append(chromosome)
    return chromosomes