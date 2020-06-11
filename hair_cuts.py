hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0

#Iterate through the prices list and add each price to the variable total_price.

for price in prices:
  total_price += price

#After your loop, create a variable called average_price that is the total_price divided by
#the number of prices.  You can get the number of prices by using the len() function.

average_price = total_price / len(prices)

#Print the value of average_price so the output looks like:
#Average Haircut Price:
#<average_price>

print("Average Price: ${0}".format(average_price))

#That average price is more expensive than Carly thought it would be! She wants to cut all
#prices by 5 dollars.  Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

new_prices = [price - 5 for price in prices]
print(new_prices)


#Create a variable called total_revenue and set it to 0.

total_revenue = 0

#Use a for loop to create a variable i that goes from 0 to len(hairstyles) Hint: You can use range() to do this!

for i in range(len(hairstyles)):
  #Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people
  #who got the haircut at position i) to total_revenue at each step.

    total_revenue += prices[i] * last_week[i]

    #After your loop, print the value of total_revenue, so the output looks like:
    #Total Revenue: <total_revenue>

    print("Total Revenue: ${0}".format(total_revenue))

    #Find the average daily revenue by dividing total_revenue by 7. Call this number
    #average_daily_revenue and print it out.

    average_daily_revenue=total_revenue / 7
    print("Average daily revenue: ${0}".format(average_price))


    cuts_under_30=[hairstyles[i]
    for i in range(len(hairstyles)) if new_prices[i] < 30]

    print(cuts_under_30)
