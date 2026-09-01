## Cleaning function

import pandas as pd
import re



# Split Location into City and Country

airbnb[["BnB_Type", "Location"]] = airbnb["Title"].str.split(
    " in ",
    n=1,
    expand=True
)

airbnb[["City", "Country"]] = airbnb["Location"].str.split(
    ",",
    n=1,
    expand=True
)

# Remove extra spaces
airbnb["City"] = airbnb["City"].str.strip()
airbnb["Country"] = airbnb["Country"].str.strip()



split = airbnb["Title"].str.split(" in ", n=1, expand=True)

airbnb["BnB_Type"] = split[0]
airbnb["Location"] = split[1]
airbnb[["BnB_Type", "Location"]].isnull().sum()


# Split Location into City and Country

airbnb[["City", "Country"]] = airbnb["Location"].str.split(
    ",",
    n=1,
    expand=True
)

# Remove leading and trailing spaces
airbnb["City"] = airbnb["City"].str.strip()
airbnb["Country"] = airbnb["Country"].str.strip()


# Split Location into City and Country
airbnb[["City", "Country"]] = airbnb["Location"].str.split(
    ",",
    n=1,
    expand=True
)

# Remove leading and trailing spaces
airbnb["City"] = airbnb["City"].str.strip()
airbnb["Country"] = airbnb["Country"].str.strip()



# Extract the first month abbreviation
airbnb["Month"] = airbnb["Date"].str.extract(r"^([A-Za-z]{3})")[0]

# Convert to full month name
month_map = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

airbnb["Month"] = airbnb["Month"].map(month_map)

airbnb[["Date", "Month"]].head()



# Extract Rating
airbnb["Rating"] = airbnb["Review and rating"].str.extract(r'(\d+\.\d+|\d+)')

# Extract Number of Reviews
airbnb["Reviews"] = airbnb["Review and rating"].str.extract(r'\((\d+)\)')

# Convert both columns to numeric
airbnb["Rating"] = pd.to_numeric(airbnb["Rating"])
airbnb["Reviews"] = pd.to_numeric(airbnb["Reviews"])

# Display the result
airbnb[["Review and rating", "Rating", "Reviews"]].head(10)


# Get the list of columns
cols = airbnb.columns.tolist()

# Remove the Review and Rating columns
cols.remove("Reviews")
cols.remove("Rating")

# Find the position of the Detail column
detail_index = cols.index("Detail")

# Insert Rating and Reviews after Detail
cols.insert(detail_index + 1, "Rating")
cols.insert(detail_index + 2, "Reviews")

# Reorder the DataFrame
airbnb = airbnb[cols]

# Display the first few rows
airbnb.head()

# Remove rows with missing values in Country, Rating, or Reviews
airbnb = airbnb.dropna(subset=["Country", "Rating", "Reviews"])

# Reset the index
airbnb.reset_index(drop=True, inplace=True)

# Check the result
airbnb.info()

# Replace blank strings with NaN
airbnb[["Country", "Rating", "Reviews"]] = (
    airbnb[["Country", "Rating", "Reviews"]]
    .replace(r'^\s*$', pd.NA, regex=True)
)

# Remove rows with missing values
airbnb = airbnb.dropna(subset=["Country", "Rating", "Reviews"])

# Reset the index
airbnb.reset_index(drop=True, inplace=True)


# Remove duplicates based on specific columns
airbnb = airbnb.drop_duplicates(
    subset=[
        "Property Name",
        "Amenities",
        "Property Type",
        "City",
        "Country",
        "Month",
        "Price(in dollar)",
        "Rating",
        "Number of Reviews",
        "Rating Category"
    ]
).reset_index(drop=True)

print("Remaining rows:", len(airbnb))


# Clean Price column

airbnb["Price(in dollar)"] = (
    airbnb["Price(in dollar)"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("$", "", regex=False)
    .str.strip()
)

airbnb["Price(in dollar)"] = pd.to_numeric(
    airbnb["Price(in dollar)"],
    errors="coerce"