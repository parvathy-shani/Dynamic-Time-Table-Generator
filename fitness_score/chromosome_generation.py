import random

# Function to read data from a text file
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()[1:]  # Skip the header line
    return data

# Function to generate a single gene
def generate_gene(day, time):
    rooms = ["303", "309"]
    lecturers = read_data('Event creation/lecturers.txt')
    classes = read_data('Event creation/classes.txt')
    students = read_data('Event creation/students.txt')

    room = random.choice(rooms)
    lecturer = random.choice(lecturers).strip().split(': ')[1]  # Extract only the lecturer name
    class_info = random.choice(classes).strip().split(': ')[1]  # Extract only the class info
    student_info = random.choice(students).strip().split(': ')[1]  # Extract only the student info

    return f"{time}-{day} {room} {lecturer} {class_info} {student_info}"

# Function to generate a single chromosome
def generate_chromosome():
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    timeslots = ["9AM", "10AM", "11AM", "1PM", "2PM", "3PM"]
    chromosome = []
    for day in days:
        for time in timeslots:
            gene = generate_gene(day, time)
            chromosome.append(gene)
    return chromosome

# Function to generate multiple chromosomes
def generate_chromosomes(num_chromosomes):
    chromosomes = []
    for _ in range(num_chromosomes):
        chromosome = generate_chromosome()
        chromosomes.append(chromosome)
    return chromosomes

# Main function to generate initial population and store it in a text file
def main():
    num_chromosomes = 50
    chromosomes = generate_chromosomes(num_chromosomes)

    # Store chromosomes in a text file
    with open('initial_population.txt', 'w') as file:
        for chromosome in chromosomes:
            for gene in chromosome:
                file.write(str(gene) + '\n')
            file.write('\n')

if __name__ == "__main__":
    main()
