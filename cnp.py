import pandas as pd

# Load the Excel file provided by the user
file_path = "C:\\Users\\lakshas\\Downloads\\ro_data.xlsx"
user_data = pd.read_excel(file_path)

# Function to generate CNP based on rules described
def generate_cnp(row, serial_number):
    # Extract data from the row
    gender = row['Gender']
    dob = row['Date of Birth']
    county_code = row['County Code']

    # Gender-based prefix (Gender and century of birth)
    if gender.lower() == 'male':
        prefix = 1 if dob.year < 2000 else 5
    elif gender.lower() == 'female':
        prefix = 2 if dob.year < 2000 else 6
    else:
        return None  # If gender is invalid

    # Birth year (last 2 digits)
    year = dob.year % 100
    month = f"{dob.month:02}"  # Ensure 2 digits for month
    day = f"{dob.day:02}"  # Ensure 2 digits for day

    # Concatenate CNP base string: Gender+DOB+County code
    cnp_base = f"{prefix}{year}{month}{day}{county_code:02}"

    # Add serial number (3 digits) to the CNP
    serial_number_str = f"{serial_number:03}"  # Ensure 3 digits for serial number
    cnp_with_serial = cnp_base + serial_number_str

    # Calculate checksum (simple placeholder logic)
    checksum = sum(int(x) for x in cnp_with_serial) % 11
    checksum = checksum if checksum != 10 else 1  # Special rule for checksum = 10

    # Return the complete CNP (13 digits)
    return f"{cnp_with_serial}{checksum}"

# Generate serial numbers for each row (this should be unique for each row)
user_data['Serial Number'] = range(1, len(user_data) + 1)

# Apply the function to generate CNP for each row
user_data['Generated CNP'] = user_data.apply(lambda row: generate_cnp(row, row['Serial Number']), axis=1)

# Save the updated DataFrame back to a new Excel file
output_path = 'C:/Users/lakshas/Downloads/User_Data_With_CNP_New.xlsx'
user_data.to_excel(output_path, index=False)
