import calendar

current_year=2024
final_year=int(input("Enter the final year:"))

leap_years = []

for year in range(current_year,final_year + 1):
     if calendar.isleap(year):
         leap_years.append(year)
         
print(f"Leap years from {current_year} to {final_year}:")

for year in leap_years:
    print(year)

