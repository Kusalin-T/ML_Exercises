india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Please enter a city name: ")
print(f"City belongs to {'india' if city in india else ('pakistan' if city in pakistan else ('bangladesh' if city in bangladesh else 'Unknown'))}")

city1, city2 = input("Please input two city names as 'city1 city2': ").split(" ")
print(f"{'Same country' if (city1 in india and city2 in india or city1 in pakistan and city2 in pakistan or city1 in bangladesh and city2 in bangladesh)  else 'Not same country'}")

sugar = int(input("Please enter sugar level: "))
if sugar<80: 
    print("Low")
elif sugar>100:
    print("High")
else:
    print("OK")        