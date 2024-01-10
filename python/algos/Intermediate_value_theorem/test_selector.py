### import algorithms

import os
import ivt

def select_file():
  print ("Choose file: ")

  # print list of tests
  folder = os.path.join(os.path.dirname(__file__), 'tests')
  tests = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

  for i, test in enumerate(tests):
    print (i, test)

  # read selected test
  while True:
    try:
      index = int(input("Enter option: "))
      if index < 0 or index >= len(tests):
        print ("Invalid option, try again")
      break
    except ValueError:
      print ("Invalid option")
      
