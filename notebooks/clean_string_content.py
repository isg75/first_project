# Add all the imports needed by the functions in the project here
#================================================================
import pandas as pd
import re
#================================================================

# Remember to modify your functions to use the template shown below
      
    # Your function code here
def clean_strings(text: str) -> str:
    """
    This functions uses a REGEX to clean the text on the rows, like especial characters, spaces, etc. 
     But in this case it's applied to text, leaving the 
    """
   
    if pd.isna(text):
        return text
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s.]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text
    

