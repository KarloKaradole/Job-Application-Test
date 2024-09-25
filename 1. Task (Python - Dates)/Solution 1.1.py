from datetime import datetime

def transform_date_format(dates):
    transformed_dates = []
    
    for date_str in dates:
        if "p" == date_str[5] and "p" == date_str[9]:
            parts = date_str.split("p") # Making a list ["2 016","19","12"]
            year = parts[0].strip().replace(" ", "") # Removing all the blank spaces between characters in part year
            day = parts[1].strip()
            #month = parts[2].strip() # We know that month does not have "p" in its part, so we can include it or not in the answer
            transformed_date = f"{year}{day}{date_str[-2: :]}"
            transformed_dates.append(transformed_date)
        else:
            # Try different formats until one matches
            for fmt in ["%Y/%m/%d", "%m-%d-%Y", "%Yp %dp %m", #"%Y %m %d", #"%Y%m%d"
                        ]:
                        # We can play with different kinds of formats
                try:
                    # Parse the date
                    parsed_date = datetime.strptime(date_str, fmt)
                    # Format the date as YYYYDDMM
                    transformed_date = parsed_date.strftime("%Y%d%m")
                    transformed_dates.append(transformed_date)
                    break  # Exit after finding the correct format
                except ValueError:
                    continue  # Try the next format if this one fails
    
    return transformed_dates

# Test the function
dates = ["2010/02/20", "2 016p 19p 12", "11-18-2012", "2018 12 24", "20130720"]
print(transform_date_format(dates))
