# Importing the pandas library
import pandas

# Reading data from a CSV file into a pandas DataFrame
data = pandas.read_csv("weather_data.csv")

# Extracting a specific column ("temp") from the DataFrame and converting it to a list
temp_list = data["temp"].to_list()

# Function to convert temperature from Celsius to Fahrenheit
def c_to_f(value):
    value = 1.8 * value + 32  # Conversion formula from Celsius to Fahrenheit
    return value

# Applying the conversion function to each value in the "temp" column (commented out in this code)
# data["temp"] = c_to_f(data["temp"])

# Creating a dictionary with student names and scores
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# Creating a new DataFrame from the dictionary
data = pandas.DataFrame(data_dict)

# Saving the new DataFrame to a CSV file named "new_data.csv"
data.to_csv("new_data.csv")