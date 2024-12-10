import pandas as pd

# List of cities/counties and their codes
city_data = [
    ("Bacau", "04"),
    ("Botosani", "07"),
    ("Arad", "02"),
    ("Iași", "24"),
    ("Botosani", "07"),
    ("Brasov", "08"),
    ("Constanta", "13"),
    ("Cluj-Napoca", "12"),
    ("Resita", "10"),
    ("Sibiu", "32"),
    ("Buzau", "10"),
    ("Bacau", "04"),
    ("Bacau", "04"),
    ("Resita", "10"),
    ("Ploiesti", "29"),
    ("Ramnicu Valcea", "39"),
    ("Galati", "18"),
    ("Bucharest", "40"),
    ("Bucharest", "40"),
    ("Bucharest", "40"),
    ("Pitesti", "03"),
    ("Slatina", "28"),
    ("Bucharest", "40"),
    ("Craiova", "17"),
    ("Galati", "18"),
    ("Slatina", "28"),
    ("Ploiesti", "29"),
    ("Cluj-Napoca", "12"),
    ("Cluj-Napoca", "12"),
    ("Timisoara", "37"),
    ("Ploiesti", "29"),
    ("Oradea", "05"),
    ("Botosani", "07"),
    ("Bacau", "04"),
    ("Iasi", "24"),
    ("Piatra Neamt", "27"),
    ("Ploiesti", "29"),
    ("Galati", "18"),
    ("Oradea", "05"),
    ("Brasov", "08"),
    ("Bucharest", "40"),
    ("Arad", "02"),
    ("Craiova", "17"),
    ("Timisoara", "37"),
    ("Cluj-Napoca", "12"),
    ("Suceava", "34"),
    ("Suceava", "34"),
    ("Iasi", "24"),
    ("Galati", "18"),
    ("Cluj-Napoca", "12"),
    ("Timisoara", "37"),
    ("Buzau", "10"),
    ("Timisoara", "37"),
    ("Suceava", "34"),
    ("Brasov", "08"),
    ("Constanța", "13"),
    ("Buzau", "10"),
    ("Cluj-Napoca", "12"),
    ("Slatina", "28"),
    ("Slatina", "28"),
    ("Cluj-Napoca", "12"),
    ("Suceava", "34"),
    ("Galati", "18"),
    ("Constanta", "13"),
    ("Ramnicu Valcea", "39"),
    ("Galati", "18"),
    ("Cluj-Napoca", "12"),
    ("Buzau", "10"),
    ("Iasi", "24"),
    ("Galati", "18"),
    ("Craiova", "17"),
    ("Buzau", "10"),
    ("Buzau", "10"),
    ("Cluj-Napoca", "12"),
    ("Deva", "21"),
    ("Oradea", "05"),
    ("Timisoara", "37"),
    ("Timisoara", "37"),
    ("Craiova", "17"),
    ("Slatina", "28"),
    ("Deva", "21"),
    ("Botosani", "07"),
    ("Botosani", "07"),
    ("Cluj-Napoca", "12"),
    ("Buzau", "10"),
    ("Craiova", "17"),
    ("Buzau", "10"),
    ("Brasov", "08"),
    ("Sibiu", "32"),
    ("Sibiu", "32"),
    ("Timișoara", "37"),
    ("Pitesti", "03"),
    ("Bucharest", "40"),
    ("Targoviste", "16"),
    ("Pitesti", "03"),
    ("Constanta", "13"),
    ("Suceava", "34"),
    ("Ploiesti", "29"),
    ("Bacau", "04"),
    ("Slatina", "28"),
    ("Iasi", "24"),
    ("Sibiu", "32"),
    ("Arad", "02"),
    ("Bacau", "04"),
    ("Constanta", "13"),
    ("Ploiesti", "29"),
    ("Brasov", "08"),
    ("Targoviste", "16"),
    ("Suceava", "34"),
    ("Sibiu", "32"),
    ("Pitesti", "03"),
    ("Iasi", "24"),
    ("Timisoara", "37"),
    ("Oradea", "05"),
    ("Brasov", "08"),
    ("Arad", "02"),
    ("Suceava", "34"),
    ("Craiova", "17"),
    ("Timisoara", "37"),
    ("Buzau", "10"),
    ("Pitesti", "03"),
    ("Brasov", "08"),
    ("Brasov", "08"),
    ("Ploiesti", "29"),
    ("Cluj-Napoca", "12")
]

# Create DataFrame
df = pd.DataFrame(city_data, columns=["City", "County Code"])

# Save to a CSV file
file_path = "C:/Users/lakshas/Downloads/cities_with_codes.csv"
df.to_csv(file_path, index=False)

file_path
