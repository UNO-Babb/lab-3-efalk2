#TempConvert.py
#Name: Ella Falk
#Date: 2/5/25
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = input("Provide a Fahrenheit temperature: ")
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempF = int(tempF)
  tempF = round(tempF, 1)
  #Output converted temperature.

  tempC = (tempF - 32) * (5/9)
  tempC = round(tempC, 1)

  print(tempF, "degrees Fahrenheit is ", tempC, "degrees Celsius.")


if __name__ == '__main__':
  main()
