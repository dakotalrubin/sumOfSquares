# File: mission1.py
# Author: Dakota Rubin
# Date: April 27, 2025

# ------------------------------------------------------------------------------
# HELPER METHODS ---------------------------------------------------------------
# ------------------------------------------------------------------------------

"""This method gets a number from user input."""
def getNumber():
  # Get user input
  userInput = input()

  # Check whether user input is valid
  try:
    # Attempt to convert user input into a number
    number = int(userInput)

    # Check whether the number lies within bounds
    if number >= 1 and number <= 100:
        return number

  # End the program for invalid user input
  except:
    exit()

"""This method calculates the sum of squares for a given user input array."""
def calculateSumOfSquares(index, sum, numberOfIntegers, userInputArray):
  # Check whether the index lies within bounds
  if index < numberOfIntegers:

    # Check whether the element at the current index in userInputArray exists
    try:
      element = userInputArray[index]

    # If there's an index error, all elements in userInputArray have been used
    except:
      return sum

    # If the element at the current index is numeric, calculate a new sum
    if element.isnumeric():
      number = int(element)

      # Check to make sure only positive integers between 1 and 100 are used
      if number >= 1 and number <= 100:
        sum += number * number

    # Increment the index and use recursion to calculate the sum of squares
    sum = calculateSumOfSquares(index+1, sum, numberOfIntegers, userInputArray)

  return sum

"""This method creates an array of calculated sums of squares."""
def createSumOfSquaresArray(index, numberOfTestCases, sumOfSquaresArray):
  # Check whether the index lies within bounds
  if index < numberOfTestCases:
    # Get the number of integers the user will enter for a test case
    numberOfIntegers = getNumber()

    # Get user input that should contain valid integers
    userInput = input()

    # Split user input using spaces and store elements in an array
    userInputArray = userInput.split()

    # Calculate the sum of squares for a test case starting with index 0,
    # an initial sum of 0, and the given userInputArray
    sum = calculateSumOfSquares(0, 0, numberOfIntegers, userInputArray)

    # Append the sum of squares for a test case to sumOfSquaresArray
    sumOfSquaresArray.append(sum)

    # Increment the index and use recursion to fill sumOfSquaresArray
    createSumOfSquaresArray(index+1, numberOfTestCases, sumOfSquaresArray)

  return sumOfSquaresArray

"""This method prints sumOfSquaresArray to standard output."""
def printSumOfSquaresArray(index, numberOfTestCases, sumOfSquaresArray):
  # Ensure the index lies within bounds
  if index < numberOfTestCases:
    # Print the element at the current index in sumOfSquaresArray
    print(sumOfSquaresArray[index])

    # Increment the index and use recursion to print sumOfSquaresArray
    printSumOfSquaresArray(index+1, numberOfTestCases, sumOfSquaresArray)

# ------------------------------------------------------------------------------
# MAIN PROGRAM -----------------------------------------------------------------
# ------------------------------------------------------------------------------

"""This method runs the main program."""
def main():
  # Get the number of test cases from user input
  numberOfTestCases = getNumber()

  # Create sumOfSquaresArray starting with index 0, the number of test cases
  # given by the user, and an empty array
  sumOfSquaresArray = createSumOfSquaresArray(0, numberOfTestCases, [])

  # Print sumOfSquaresArray to standard output starting with index 0,
  # the number of test cases given by the user, and the generated
  # sumOfSquaresArray
  printSumOfSquaresArray(0, numberOfTestCases, sumOfSquaresArray)

# This statement allows the user to run the main method as a script
if __name__ == "__main__":
  main()