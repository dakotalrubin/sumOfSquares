# File: sumOfSquares.py
# Author: Dakota Rubin
# Date: May 29, 2024

# ------------------------------------------------------------------------------
# HELPER METHODS ---------------------------------------------------------------
# ------------------------------------------------------------------------------

"""This method gets the number of test cases to run from user input.
The default number of test cases for invalid input is 1."""
def getNumberOfTestCases():
  # Parse standard input for a valid number of test cases to run
  try:
    numberOfTestCases = int(input("Enter the number of test cases " +
      "(1 to 100): "))
  except:
    print("Please enter a number next time! Now using the default number 1.")
    numberOfTestCases = 1

  # Ensure the specified number of test cases lies within appropriate bounds
  if numberOfTestCases < 1 or numberOfTestCases > 100:
    print("Please enter a number between 1 and 100 next time! Now using the " +
      "default number 1.")
    numberOfTestCases = 1

  return numberOfTestCases

"""This method calculates the sum of squares for a given array of values."""
def calculateSumOfSquares(index, sum, inputValues):
  # Ensure the index stays within appropriate bounds
  if index < len(inputValues):
    # Attempt to convert the current value from a string to an integer
    if inputValues[index].isnumeric():
      currentValue = int(inputValues[index])

      # Check to make sure only positive integers are used in the calculation
      if currentValue > 0:
        sum += currentValue * currentValue
    else:
      # Remove the current value from the inputValues array and reset the index
      inputValues.remove(inputValues[index])
      index -= 1

    # Increment the index for each recursive method call
    index += 1

    # Use recursion to calculate the sum of squares
    sum = calculateSumOfSquares(index, sum, inputValues)

  return sum

"""This method builds an array for the computed sum-of-squares values.
The default number of integers for a given test case for invalid input is 1."""
def getSumOfSquaresArray(index, numberOfTestCases, sumOfSquaresArray):
  # Ensure the index stays within appropriate bounds
  if index < numberOfTestCases:
    # Get the number of integers the user will enter for this test case
    try:
      numberOfIntegers = int(input("Enter the number of integers " +
        "for this test case (1 to 100): "))
    except:
      print("Please enter a number next time! Now using the default number 1.")
      numberOfIntegers = 1

    # Ensure the number of integers lies within appropriate bounds
    if numberOfIntegers < 1 or numberOfIntegers > 100:
      print("Please enter a number between 1 and 100 next time! " +
        "Now using the default number 1.")
      numberOfIntegers = 1

    # Store an input string from the user that should contain valid integers
    inputString = input(f"Enter {numberOfIntegers} integer(s) for this " + 
      "test case separated by spaces (use values of -100 to 100): ")

    # Split the user's input string by spaces
    inputValues = inputString.split()

    # If the length of the array of input values exceeds numberOfIntegers,
    # truncate the array of input values to the specified numberOfIntegers
    if len(inputValues) > numberOfIntegers:
      del inputValues[numberOfIntegers:]

    # Calculate the sum of squares for the given test case starting with
    # an index of 0, an initial sum of 0, and an array of input integers
    sum = calculateSumOfSquares(0, 0, inputValues)

    # Append the sum of squares for this test case to the sumOfSquares array
    sumOfSquaresArray.append(sum)

    # Increment the index for each recursive method call
    index += 1

    # Use recursion to fill the sumOfSquares array
    getSumOfSquaresArray(index, numberOfTestCases, sumOfSquaresArray)

  return sumOfSquaresArray

"""This method prints the sumOfSquares array to standard output."""
def printSumOfSquaresArray(index, numberOfTestCases, sumOfSquaresArray):
    # Ensure the index stays within appropriate bounds
  if index < numberOfTestCases:
    # Print the element at the current index in the sumOfSquares array
    print(sumOfSquaresArray[index])

    # Increment the index for each recursive method call
    index += 1

    # Use recursion to print the sumOfSquares array
    printSumOfSquaresArray(index, numberOfTestCases, sumOfSquaresArray)

# ------------------------------------------------------------------------------
# MAIN PROGRAM -----------------------------------------------------------------
# ------------------------------------------------------------------------------

"""This method runs the main program."""
def main():
  # Get the number of test cases to run from user input
  numberOfTestCases = getNumberOfTestCases()

  # Build the sumOfSquares array starting with an index of 0, the number of
  # test cases specified by the user, and an empty sumOfSquares array
  sumOfSquaresArray = getSumOfSquaresArray(0, numberOfTestCases, [])

  # Print the sumOfSquares array to standard output starting with an index of 0,
  # the number of test cases specificed by the user, and the fully-populated
  # sumOfSquares array
  printSumOfSquaresArray(0, numberOfTestCases, sumOfSquaresArray)

# This statement allows the user to run the main method as a script
if __name__ == "__main__":
  main()