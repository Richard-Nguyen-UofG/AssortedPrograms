#
# Richard Nguyen
# prints the first day of each week within a year (2022) with an indicator in between
#

days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Jan 1st 2022 is a Saturday

month = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
    
while day < sum(month_days):
        
    index = 0
    day_temp = day
    for x in month_days:
        if day_temp - x <= 0:
            break
        
        day_temp = day_temp - x
        index += 1
    
    day_num = str(day_temp)
    end = ""
    if day_num.endswith("1") and not day_num.startswith("1"):
        end = "st"
    elif day_num.endswith("2")and not day_num.startswith("1"):
        end = "nd"
    elif day_num.endswith("3")and not day_num.startswith("1"):
        end = "rd"
    else:
        end = "th"
        

    if day % 7 == 2:
        print(str(month[index]) + " " + str(day_temp) + end + ":")
        print("----")
        
    day += 1