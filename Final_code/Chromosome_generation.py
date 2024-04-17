import random


# Function to read data from the input file
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data


# Function to generate a single gene based on input data
def generate_gene(data_line, gene_number):
    # Split the data line into relevant attributes
    attributes = data_line.strip().split()
    event = f"G{gene_number} {attributes[1]} {attributes[2]} {attributes[3]}"
    return event


# Function to generate a single chromosome based on input data and batch
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


# Main function to generate initial population and store it in text files
def main():
    input_data = read_data('format_pairs_output.txt')
    batches = ['S2C', 'S2D', 'S4C', 'S4D', 'S6C', 'S6D', 'S8C', 'S8D']  # Names of the batches
    num_chromosomes_per_batch = 50  # Number of chromosomes for each batch

    for batch in batches:
        chromosomes = []
        for _ in range(num_chromosomes_per_batch):
            chromosome = generate_chromosome(input_data, batch)
            chromosomes.append(chromosome)

        # Store chromosomes in a text file
        output_file = f'initial_population_{batch}.txt'
        with open(output_file, 'w') as file:
            for chromosome in chromosomes:
                for gene in chromosome:
                    file.write(str(gene) + '\n')
                file.write('\n')


if __name__ == "__main__":
    main()
