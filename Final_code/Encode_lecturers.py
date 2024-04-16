import pandas as pd

# Sample input data
data = {
    'lecturer': ['Gopakumar G', 'Ameena A', 'Manju S Nair', 'Alka Vijay', 'Shyama Das', 'Shiny B', 'Sreelekshmi K R',
                 'Arathy U P', 'Angel Thankam Thomas', 'Rosy K Philp', 'Jithy John', 'Sabhana Mol S', 'Jyothirmayi Devi',
                 'Vishnu S Kumar', 'Leya G', 'Betty James', 'Sulaja Sanal', 'Nasseena N', 'Ajoy Thomas', 'Anjitha P',
                 'Neethu Treesa Jacob', 'Syeatha Merlin Thampy', 'Sheerna Thampi', 'Chinchu M Pillai', 'Sushitha Susan Jacob',
                 'Ahammed Siraj K K'],
    'position': ['Associate Professor', 'Assistant Professor', 'Associate Professor & Head Of the Department',
                 'Assistant Professor', 'Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Associate Professor'],
    'preferred_timeslot': ['NIL', 'NIL', 'Forenoon', 'NIL', 'Forenoon', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'Forenoon', 'NIL',
                           'Forenoon', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL']
}

# Create a DataFrame from the input data
df = pd.DataFrame(data)

# Generate codes based on the given rules
def generate_code(row):
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

# Apply the generate_code function to each row in the DataFrame
df['code'] = df.apply(generate_code, axis=1)

# Save the DataFrame with generated codes to a text file without the column header 'code'
output_file = 'encode_lecturers_output.txt'
df[['code']].to_csv(output_file, sep='\t', index=False, header=False)

print(f"Encoded data saved to '{output_file}'")
