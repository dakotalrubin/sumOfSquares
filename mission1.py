# File: mission1.py
# Author: Dakota Rubin
# Date: April 28 2025

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
def calculateSumOfSquares(userInputArray, numberOfIntegers, sum, index):
  # Check whether the index lies within bounds
  if index < numberOfIntegers:

    # Get the element at the current index in userInputArray
    element = userInputArray[index]

    # If the element at the current index is numeric, calculate a new sum
    try:
      number = int(element)

      # Check to make sure only negative integers between -100 and -1 are used
      if number >= -100 and number <= -1:
        sum += number ** 4

    # Skip non-numeric values
    except:
      pass

    # Increment the index and use recursion to calculate the sum of squares
    sum = calculateSumOfSquares(userInputArray, numberOfIntegers, sum, index+1)

  return sum

"""This method creates an array of calculated sums of squares."""
def createSumOfSquaresArray(sumOfSquaresArray, numberOfTestCases, index):
  # Check whether the index lies within bounds
  if index < numberOfTestCases:
    # Get the number of integers the user will enter for a test case
    numberOfIntegers = getNumber()

    # Get user input that should contain valid integers
    userInput = input()

    # Split user input using spaces and store elements in an array
    userInputArray = userInput.split()

    # Set the sum for a test case to -1 if the number of integers isn't equal
    # to the number of elements in the given user input array
    if numberOfIntegers != len(userInputArray):
      sum = -1
    else:
      # Calculate the sum of squares for a test case using the given
      # userInputArray, numberOfIntegers, an initial sum of zero and
      # starting from index 0
      sum = calculateSumOfSquares(userInputArray, numberOfIntegers, 0, 0)

    # Append the sum of squares for a test case to sumOfSquaresArray
    sumOfSquaresArray.append(sum)

    # Increment the index and use recursion to fill sumOfSquaresArray
    createSumOfSquaresArray(sumOfSquaresArray, numberOfTestCases, index+1)

  return sumOfSquaresArray

"""This method prints sumOfSquaresArray to standard output."""
def printSumOfSquaresArray(sumOfSquaresArray, index):
  # Ensure the index lies within bounds
  if index < len(sumOfSquaresArray):
    # Print the element at the current index in sumOfSquaresArray
    print(sumOfSquaresArray[index])

    # Increment the index and use recursion to print sumOfSquaresArray
    printSumOfSquaresArray(sumOfSquaresArray, index+1)

# ------------------------------------------------------------------------------
# MAIN PROGRAM -----------------------------------------------------------------
# ------------------------------------------------------------------------------

"""This method runs the main program."""
def main():
  # Get the number of test cases from user input
  numberOfTestCases = getNumber()

  # Create sumOfSquaresArray using an empty array, the number of test cases
  # given by the user and starting from index 0
  sumOfSquaresArray = createSumOfSquaresArray([], numberOfTestCases, 0)

  # Print sumOfSquaresArray to standard output starting from index 0
  printSumOfSquaresArray(sumOfSquaresArray, 0)

# This statement allows the user to run the main method as a script
if __name__ == "__main__":
  main()