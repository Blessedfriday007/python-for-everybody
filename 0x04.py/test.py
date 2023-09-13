#create a function computepay      
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        #calculate pay with time and a half for extra hours.
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

# prompt the user for hours and rate per hour
hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

# Convert input to float/numbers
hours_worked = float(hours_input)
hourly_rate = float(rate_input)

# Calculate gross pay using the computepay function / call the function to compute Grosspay.
gross_pay = computepay(hours_worked, hourly_rate)

print("Gross Pay:", gross_pay)






