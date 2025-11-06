def main():
  # Get an odometer value in U.S. miles from the user.
  start_miles = float(input("Enter the starting odometer reading (miles): "))
  # Get another odometer value in U.S. miles from the user.
  end_miles = float(input("Enter the ending odometer reading (miles): "))
  # Get a fuel amount in U.S. gallons from the user.
  amount_gallons = float(input("Enter the amount of fuel used (gallons): "))
  mpg = end_miles - start_miles / amount_gallons
  # Call the miles_per_gallon function and store
  miles_per_gallon(start_miles, end_miles, amount_gallons)
  lp100k_from_mpg(mpg)
  print(f"The start miles is: {start_miles}")
  print(f"The end miles is: {end_miles}")
  print(f"The amount in gallons is: {amount_gallons}")
  
  # the result in a variable named mpg.
  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  # Display the results for the user to see.
  pass
def miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  Return: Fuel efficiency in miles per gallon.
  """
  mpg = (end_miles - start_miles / amount_gallons)
  print(f"The miles per gallon is: {mpg}")
  return
def lp100k_from_mpg(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  lp100k = 235.215 / mpg
  print(f"The liters per 100 kilometers is: {lp100k:.2f}")
  return
# Call the main function so that
# this program will start executing.
main()
