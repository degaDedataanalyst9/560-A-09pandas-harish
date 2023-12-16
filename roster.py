import pandas as pd

# Data for 10 UNC basketball players
players = {
    "First Name": ["Zayden", "Elliot", "Cormac", "RJ", "Armando", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
    "Last Name": ["High", "Cadeau", "Ryan", "Davis", "Bacot", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"],
    "Height": [6.9, 6.1, 6.5, 6.0, 6.11, 6.3, 6.5, 6.10, 6.1, 6.4],  # Height in feet and inches
    "Weight": [225, 180, 195, 180, 240, 195, 195, 230, 180, 190]  # Weight in pounds
}
data = pd.DataFrame(players)

# Function to calculate BMI
def calculate_bmi(height, weight):
    feet, inches = divmod(height, 1)
    height_meters = feet * 0.3048 + inches * 0.1 * 0.3048
    weight_kg = weight * 0.453592
    bmi = weight_kg / (height_meters ** 2)
    return bmi

# Calculating BMI for each player
data['BMI'] = data.apply(lambda row: calculate_bmi(row['Height'], row['Weight']), axis=1)

# Formatting BMI to display only the first two decimal places
data['BMI'] = data['BMI'].apply(lambda x: "{:.2f}".format(x))

print(data)
