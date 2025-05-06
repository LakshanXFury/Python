import pandas as pd
import random

# Sample French first and last names without special characters
male_first_names = [
    "Jean", "Louis", "Pierre", "Paul", "Jacques", "Michel", "Henri", "Luc", "Marc", "Alain",
    "Nicolas", "Julien", "Antoine", "Gerard", "Laurent", "Etienne", "Damien", "Vincent", "Andre", "Francois"
]

female_first_names = [
    "Marie", "Claire", "Sophie", "Julie", "Camille", "Isabelle", "Helene", "Anne", "Nathalie", "Valerie",
    "Celine", "Sandrine", "Martine", "Lucie", "Caroline", "Elise", "Veronique", "Aline", "Nicole", "Laure"
]

last_names = [
    "Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau",
    "Simon", "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier"
]

# Generate 200 unique names (mix of male and female)
names = []
used_combinations = set()
while len(names) < 200:
    """
    If True is selected → it picks a male name and sets:
    If False is selected → it picks a female name and sets:
    """
    if random.choice([True, False]):
        salutation = "SAL_MR"
        first = random.choice(male_first_names)
    else:
        salutation = "SAL_MS"
        first = random.choice(female_first_names)
    last = random.choice(last_names)
    combo = (salutation, first, last)
    if combo not in used_combinations:
        used_combinations.add(combo)
        names.append(combo)

# Create DataFrame
df = pd.DataFrame(names, columns=["Salutation", "FirstName", "LastName"])

# Save to Excel
excel_path = "*/Downloads/French_Names_List.xlsx"
df.to_excel(excel_path, index=False)
