## Visualization Functions

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



#RQ01. "Distribution of Airbnb Listings by Rating Category"

plt.figure(figsize=(8, 6))

ax = sns.barplot(
    x=rating_distribution.index,
    y=rating_distribution.values,
    hue=rating_distribution.index,
    palette={
        "Low": "#d9534f",
        "Average": "#f0ad4e",
        "High": "#5cb85c"
    },
    legend=False
)

plt.title("Distribution of Airbnb Listings by Rating Category")
plt.xlabel("Rating Category")
plt.ylabel("Number of Listings")

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()



#RQ02. "Price Comparison Between Low and High Rated Airbnb Listings"

rq2_data = airbnb[
    airbnb["Rating Category"].isin(["Low", "High"])
]

price_limit = rq2_data["Price(in dollar)"].quantile(0.95)

plt.figure(figsize=(8, 6))

sns.boxplot(
    data=rq2_data,
    x="Rating Category",
    y="Price(in dollar)",
    order=["Low", "High"],
    hue="Rating Category",
    palette={
        "Low": "#d9534f",
        "High": "#5cb85c"
    },
    legend=False
)

plt.ylim(0, price_limit)

plt.title(
    "Price Comparison Between Low and High Rated Airbnb Listings"
)
plt.xlabel("Rating Category")
plt.ylabel("Price in Dollars")

plt.tight_layout()
plt.show()



#RQ03. "Property Types Most Likely to Receive Poor Guest Ratings"

top_poor_types = property_summary.head(10)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    data=top_poor_types.reset_index(),
    x="Low_Rating_Percentage",
    y="Property Type",
    color="#d9534f"
)

plt.title("Property Types Most Likely to Receive Poor Guest Ratings")
plt.xlabel("Percentage of Low Rated Listings")
plt.ylabel("Property Type")

plt.tight_layout()
plt.show()


#RQ04. "Airbnb Price by Number of Amenities Mentioned" (with price limit)

price_limit = airbnb["Price(in dollar)"].quantile(0.95)

plt.figure(figsize=(9, 6))

sns.boxplot(
    data=airbnb,
    x="Amenity Count",
    y="Price(in dollar)",
    color="steelblue"
)

plt.ylim(0, price_limit)

plt.title("Airbnb Price by Number of Amenities Mentioned")
plt.xlabel("Number of Amenities Mentioned")
plt.ylabel("Price in Dollars")

plt.tight_layout()
plt.show()


#RQ05. "Airbnb Ratings by Number of Amenities Mentioned"

plt.figure(figsize=(9, 6))

sns.boxplot(
    data=airbnb,
    x="Amenity Count",
    y="Rating",
    color="seagreen"
)

plt.title("Airbnb Ratings by Number of Amenities Mentioned")
plt.xlabel("Number of Amenities Mentioned")
plt.ylabel("Rating")

plt.tight_layout()
plt.show()



#RQ06. "Airbnb Guest Ratings Across Top Listing Countries"

top_countries = (
    airbnb["Country"]
    .value_counts()
    .head(10)
    .index
)

rq6_plot = airbnb[
    airbnb["Country"].isin(top_countries)
]

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=rq6_plot,
    x="Country",
    y="Rating",
    color="steelblue"
)

plt.title("Airbnb Guest Ratings Across Top Listing Countries")
plt.xlabel("Country")
plt.ylabel("Guest Rating")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#RQ07. "Airbnb Prices Across Top Listing Locations"

top_locations = (
    airbnb["Country"]
    .value_counts()
    .head(10)
    .index
)

rq7_plot = airbnb[
    airbnb["Country"].isin(top_locations)
]

price_limit = rq7_plot["Price(in dollar)"].quantile(0.95)

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=rq7_plot,
    x="Country",
    y="Price(in dollar)",
    color="steelblue"
)

plt.ylim(0, price_limit)

plt.title("Airbnb Prices Across Top Listing Locations")
plt.xlabel("Location")
plt.ylabel("Price in Dollars")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


#RQ08. "Median Airbnb Price by Location"

top_locations = (
    airbnb["Country"]
    .value_counts()
    .head(10)
    .index
)

median_price_location = (
    airbnb[airbnb["Country"].isin(top_locations)]
    .groupby("Country")["Price(in dollar)"]
    .median()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=median_price_location.values,
    y=median_price_location.index,
    color="steelblue"
)

plt.title("Median Airbnb Price by Location")
plt.xlabel("Median Price in Dollars")
plt.ylabel("Location")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="$%.0f",
        padding=3
    )

plt.tight_layout()
plt.show()



#RQ09. "Relationship Between Number of Reviews and Airbnb Ratings"

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=rq8_data,
    x="Number of Reviews",
    y="Rating",
    alpha=0.6,
    color="steelblue"
)

plt.title("Relationship Between Number of Reviews and Airbnb Ratings")
plt.xlabel("Number of Reviews")
plt.ylabel("Airbnb Rating")

plt.tight_layout()
plt.show()


#RQ10. "Regression Analysis: Number of Reviews vs Airbnb Ratings"

plt.figure(figsize=(10, 6))

sns.regplot(
    data=rq8_data,
    x="Number of Reviews",
    y="Rating",
    scatter_kws={
        "alpha": 0.4,
        "color": "steelblue"
    },
    line_kws={
        "color": "red"
    }
)

plt.title("Number of Reviews vs Airbnb Rating")
plt.xlabel("Number of Reviews")
plt.ylabel("Airbnb Rating")

plt.tight_layout()
plt.show()


#RQ11. "Total Airbnb Reviews by Month"

plt.figure(figsize=(11, 6))

ax = sns.barplot(
    data=monthly_summary.reset_index(),
    x="Month",
    y="Total_Reviews",
    color="steelblue"
)

plt.title("Total Airbnb Reviews by Month")
plt.xlabel("Month")
plt.ylabel("Total Number of Reviews")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



#RQ12. "Average Airbnb Rating by Month"

plt.figure(figsize=(11, 6))

sns.lineplot(
    data=monthly_summary.reset_index(),
    x="Month",
    y="Average_Rating",
    marker="o",
    color="seagreen"
)

plt.title("Average Airbnb Rating by Month")
plt.xlabel("Month")
plt.ylabel("Average Rating")

plt.ylim(
    monthly_summary["Average_Rating"].min() - 0.02,
    5
)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



#RQ13. "Property Types Most Associated with Poor Ratings"

plt.figure(figsize=(10, 6))

plot_data = (
    poor_property_types
    .head(10)
    .sort_values("Poor_Rating_Percentage")
)

sns.barplot(
    data=plot_data.reset_index(),
    x="Poor_Rating_Percentage",
    y="Property Type",
    color="steelblue"
)

plt.title("Property Types Most Associated with Poor Ratings")
plt.xlabel("Poor Rated Listings in Percent")
plt.ylabel("Property Type")

plt.tight_layout()
plt.show()


