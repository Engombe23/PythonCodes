#Assessed Task 4

print("Sales Report")
year = int(input("Input the year the sales report is for: "))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

sale_values = []

sales_total = 0

largestSale = 0

maxSale = 0

minSale = 0

for i in range(len(months)):
    sales = int(input("Input " + str(months[i]) + "'s sales amount: "))
    
    sale_values.append(sales)
    
    sales_total += sales
    
    if sales > largestSale:
        largestSale = sales
        
        maxSale = months[i]
        
    min1 = sale_values[0]
    
    for j in range(len(sale_values)):
        
        if(sale_values[j] < min1):
            min1 = sales
            
            minSale = months[j]
          

salesTotalTo2dp = "{:.2f}".format(sales_total)

print("The total sales for " + str(year) + " are £" + str(salesTotalTo2dp))

average = sales_total / len(months)

monthlySaleTo2dp = "{:.2f}".format(average)

print("The average monthly sales for " + str(year) + " was £" + str(monthlySaleTo2dp))

largestSaleTo2dp = "{:.2f}".format(largestSale)

print("The month with the maximum sales was " + str(maxSale) + " with £" + str(largestSaleTo2dp))

smallestSaleTo2dp = "{:.2f}".format(min1)

print("The month with the minimum sales was " + str(minSale) + " with £" + str(smallestSaleTo2dp))
