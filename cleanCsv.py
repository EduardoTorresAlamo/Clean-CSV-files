#
# EDUARDO TORRES ALAMO
# 2/20/2023
# This was made for a specific issue at my place of work
#

import pandas as pd

# Read in the .csv file
# Change 'original.csv' for the desired file to clean
df = pd.read_csv('original.csv')

# Remove extra spaces and set everything to lowercase
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

# Write the cleaned data to a new .csv file
# Change 'cleaned.csv' to desired filename.
df.to_csv('cleaned.csv', index=False)






