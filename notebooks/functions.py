import pandas as pd
import importlib # to refresh functions imported from functions.py file
#import functions #updates re to be made in functions.py
import matplotlib.pyplot as plt
import seaborn as sns

#=============================================================================
#Split the category colinto several categories
#=============================================================================


def clean_category_col(df):
    """
    input: raw df
    slit the main category into 2 sub_categories
    output: df1 = df with 2 more columns (sub_cat1/2)
    """
    df1 = df.copy()
    
    #split the category colinto several categories
    cat1 = df1["category"].apply(
                                 lambda x : str(x).split("|")[0]
                                            .strip()
                                            .replace("&", "_")
                                 )
    cat2 = df1["category"].apply(
                                 lambda x : str(x).split("|")[1]
                                            .strip()
                                            
                                            .replace(",", "_")
                                            .replace("&", "_")
                                 )
    
    df1.insert(3, "sub_cat1", cat1)
    df1.insert(4, "sub_cat2", cat2)
    
    return df1

#=============================================================================
#Clean the discounted_price column
#=============================================================================

def disc_price_col_clean(df):
    """
    input: raw df
    Clean the column discount_price and cast it to float
    output: df1 = df 
    """

    df1 = df.copy()
    df1["discounted_price"] = (
                                df1["discounted_price"]
                                .astype(str)
                                .str.replace("₹", "", regex= False)
                                .str.replace(",", "", regex = False)
                                .astype(float)
                                .round(2)
                                #.apply(lambda x : f"{x : .2f}")
                              )
    
    return df1

#=============================================================================
#Clean the actual_price column
#=============================================================================

def actual_price_col_clean(df):
    """
    input: raw df
    Clean the column actual_price and cast it to float
    output: df1 = df 
    """

    df1 = df.copy()
    df1["actual_price"] = (
                                df1["actual_price"]
                                .astype(str)
                                .str.replace("₹", "", regex= False)
                                .str.replace(",", "", regex = False)
                                
                                .astype(float)
                                .round(2)
                                #.apply(lambda x : f"{x : .2f}")
                              )
    
    return df1

#============================================================================#
#Clean the discount_percentage column                                        #
#============================================================================#

def discount_percent_clean(df):
    """
    input: raw df
    Clean the column discount_percentage and cast it to integer: remove % sign
    output: df1
    """

    df1 = df.copy()
    df1["discount_percentage"] = (
                                df1["discount_percentage"]
                                .astype(str)
                                .str.replace("%", "", regex= False)
                                .astype(int)
                              )
    return df1

#============================================================================#
#convert the 2 columns: rating rating & rating_count to floats                                    #
#============================================================================#

def rating_cols_clean(df):
    """
    input: raw df
    convert the 2 columns: rating to float  & rating_count to in
    output: df1
    """

    df1 = df.copy()

    #delete 2  NaN rows based on column: "rating_count": 2/1464 = 0.14%
    df1 = df1.dropna(subset = "rating_count")
    #convert the column rating to int
    df1["rating"] = (
                     df1["rating"]
                     .astype(str)
                     
                     .str.replace("|", "1", regex= False)
                     .str.strip()
                     .astype(float)
                     
                     )
   #convert the column rating_count to int
    df1["rating_count"] = (
                     df1["rating_count"]
                     .astype(str)
                     
                     .str.replace(",", "", regex= False)
                     .astype(int)
                     )
    
    return df1  

def clean_split_reviews_ids(df):
    """
    input raw df
    split all columns containing multiple values into lists for indexing
    output
    """
    df1=df.copy()
    
    df1.review_id = df1.review_id.str.split(',')
    df1.user_id = df1.user_id.str.split(',')
    df1.review_title = df1.review_title.str.split(',')
    df1.review_content = df1.review_content.str.split(',')
    return df1


def remove_product_id_dupl(df):
    """
    input raw df
    order by the number of product reviews
    remove any duplicates, as identified by identical product names or product ids
    """
    df1 = df.copy()
    sorted_df1 = df1.sort_values(by='rating_count', ascending=False)
    df1 = sorted_df1.drop_duplicates(subset='product_id', keep='first')
    df1 = sorted_df1.drop_duplicates(subset='product_name', keep='first')
    df1.reset_index(drop=True, inplace=True)
    return df1
##############################################################################
# Categorizes price and ratings
##############################################################################
def categorize_price_rating(df):
    df1 = df.copy()
    df1["price_segment"] = pd.cut(
                                    df1["discounted_price"],
                                    bins = [0, 500, 5000, 100000],
                                    labels = ["Budget [0-500]", "Mid-Range[500-5000]", "Premium[5000-100000]"]
                                  )
    
    df1["rating_segment"] = pd.cut(
                                    df1["rating"],
                                    bins = [0, 3, 4.2, 5],
                                    labels = ["Poor[0 - 3]", "Mid-value[3.1 - 4.2]", "Excellent[4.3 - 5]"]
                                  )
                                
    return df1   

#=============================================================================
# PLOTS
#=============================================================================

##############################################################################
# Plot1: Zidene ==>PRICE SEGMENTS VS RATING BARCHART
##############################################################################
def price_seg_rating_plot(df):
    df1 = df.copy()
    
    plt.figure(figsize = (10, 6))
    #Plot background
    plt.gca().set_facecolor("#f5f5f5")
    
    my_plot = sns.countplot(
                            data = df1,
                            x = "price_segment",
                            hue = "rating_segment",
                            palette = ["red", "orange", "green"]
                          )
    plt.xlabel("Price Segment", fontsize = 16)
    plt.ylabel("Rating", fontsize = 16)
    plt.title("Rating / Price Segments Relationship", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    for container in my_plot.containers:
        perc = my_plot.bar_label(container)
        my_plot.bar_label(container)
    
    plt.show()

##############################################################################
# Plot2: Zidene ==>PRICE SEGMENTS VS RATING
##############################################################################
def rating_vs_categ_plot(df):
    """
    Bubble graph that shows how products are related to ratings
    """
    df1 = df.copy()

    #Definition of plot characteristics
    plt.figure(figsize = (12,6))
    # Background inside chart
    plt.gca().set_facecolor("#f5f5f5")
    
    my_plot = sns.boxplot(
                            data = df1,
                            y = "sub_cat1",
                            x = "rating",
                            color = "green"
                         )
    #
    #plt.xscale("log")
    plt.xlabel("Rating", fontsize = 16)
    plt.ylabel("Category", fontsize = 16)
    plt.title("Categories Rating", fontsize = 20)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    #plt.legend()
    
    # Transparent grid
    plt.grid(
            True,
            linestyle="--",
            alpha=0.3
            )
    
    plt.show()
#=============================================================================
# Plot3: Zidene ==>PRICE SEGMENTS VS RATING BARCHART: Stacked bar chart
#=============================================================================
def price_seg_rating_plot(df):
    df1 = df.copy()
    
    plt.figure(figsize = (10, 6))
    #Plot background
    plt.gca().set_facecolor("#f5f5f5")

    # Cross table
    table = pd.crosstab(
                        
                        df["rating_segment"],
                        df["price_segment"]
                        )

    #plt.figure(figsize=(8,5))

    sns.heatmap(
                table,
                annot=True,
                fmt="d",
                cmap="YlGnBu"
                )
    
    #plt.xlabel("Price Segment", fontsize = 16)
    #plt.ylabel("Rating", fontsize = 16)
    plt.title("Rating / Price Segments Relationship", fontsize = 20)
    #plt.xticks(fontsize = 14)
    #plt.yticks(fontsize = 14)
    #plt.grid(axis='y', linestyle='--', alpha=0.3)
    #for container in my_plot.containers:
        #perc = my_plot.bar_label(container)
        #my_plot.bar_label(container)
    
    print("figure displayed")

