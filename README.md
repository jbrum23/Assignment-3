# Assignment-3

# Exercise 1: Retail Checkout Simulation
## Description
This program prompts the user to enter item prices until 0 is entered, stores the values in a list, and calculates the total purchase amount, average item cost, and number of items bought.
## Assumptions
* Prices are entered as numeric values.
* Input of 0 ends the program.
* Negative values are considered invalid and ignored.
* If no items are entered, the average cost is 0.

# Exercise 2: Market Survey Analyzer
## Description
This program analyzes a list of customer preferences, counts how many times each product appears using a dictionary, and prints a market share summary as percentages.
## Assumptions
* Preferences are stored in a list of strings.
* Each entry represents one customer's choice.
* Percentages are calculated based on total responses.
* Output is displayed in a simple text format.

# Exercise 3: Expense Report Categorizer
## Description
This program stores expenses by category in a dictionary, calculates totals for each category using nested loops, and prints a summary along with the grand total.
## Assumptions
* Expenses are stored as lists of numbers within each category.
* Each category contains at least one expense.
* Totals are calculated by summing values in each list.
* Output is displayed in a simple text format.

# Exercise 4: Sales Commission Calculator
## Description
This program calculates a 10% commission for each employee based on their sales, stores the results, and prints a leaderboard sorted from highest to lowest commission.
## Assumptions
* Sales data is stored in a dictionary with employee names and sales amounts.
* Commission is calculated as 10% of sales.
* Employees are ranked based on commission earned.
* Output is displayed in descending order.

# Exercise 5: Stock Portfolio Tracker
## Description
This program stores stock data in a nested dictionary, calculates the total value of the portfolio, and simulates a week of random daily price changes to print the updated total value each day.
## Assumptions
- Each stock has a defined number of shares and a price.
- Total value is calculated as shares × price for each stock.
- Daily price changes are random within a range of ±5%.
- Output includes the initial total and updated daily totals.

# Exercise 6: Bank Loan Repayment Simulator
## Description
This program simulates monthly loan repayment using a while loop, applying interest and subtracting payments each month until the balance is paid off, and prints the number of months required.
## Assumptions
* User inputs loan amount, interest rate, and monthly payment.
* Interest is applied monthly based on an annual rate.
* Payments are made once per month.
* The loop continues until the balance is zero or less.

# Exercise 7: Simple Supply Chain Tracker
## Description
This program models multiple warehouses with inventory data, uses nested loops to calculate the total stock of each product across all warehouses, and prints the results.
## Assumptions
* Warehouses are stored as a list of dictionaries.
* Each warehouse contains an inventory dictionary.
* Product quantities are numeric.
* Totals are calculated by summing across all warehouses.

# Exercise 8: Customer Loyalty Tiers
## Description
This program assigns customers to loyalty tiers based on their total purchase amount using conditional logic and counts how many customers fall into each tier.
## Assumptions
* Customer data is stored in a dictionary with purchase amounts.
* Tiers are defined as Bronze (<1000), Silver (1000–4999), and Gold (5000+).
* Each customer belongs to exactly one tier.
* Output displays the count for each tier.

# Exercise 9: Business Growth Projection
## Description
This program takes an initial revenue and growth rate, uses a loop to project revenue over 10 years, and prints the results in a year-by-year table.
## Assumptions
* User inputs revenue and growth rate.
* Growth rate is applied annually.
* Revenue increases each year based on the given percentage.
* Output is displayed in a simple table format.

# Exercise 10: Startup Pitch Deck Visualizer

## Description
This program uses a loop and string multiplication to simulate a simple bar chart using # symbols to represent projected growth over multiple years.
## Assumptions
* Number of years is predefined.
* Each year increases the number of # symbols.
* Bars are displayed in a simple text format.
* Output represents relative growth visually.
