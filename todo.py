# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp
# 

def add(list, item):
  if (len(list)>=10):
    print("error! Can't be more than 10 elements in the list")
  else:
    if (len(item)==0):
      print("error! Can't input blank text")
    elif (len(item)>=100):
      print("error! Can't input text more than 100 symbols")
    else:
      list.append(item)
  pass


def remove(list, index):
  # https://www.w3schools.com/python/python_lists_remove.asp
  list.pop(index)
  pass


def clear(list):
  # https://www.w3schools.com/python/python_lists_remove.asp
  list.clear()
  print("List is empty now, what you want to do?")
  pass


def print_list(list):
  # https://www.w3schools.com/python/python_lists_loop.asp
  if (list==[]):
    print("List is empty")
  else:
    print(list)
  pass


def show(list, index):
  # https://www.w3schools.com/python/python_lists_access.asp
  print(list[index])
  pass

list = []
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index\n6. Exit\n"))
  if choice == 1:
    item = input("What you want to add?\n")
    add(list, item)
    print_list(list)
  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    remove(list, index)
    print_list(list)
  elif choice == 3:
    clear(list)
    print_list(list)
  elif choice == 4:
    print_list(list)
  elif choice == 5:
    index = int(input("Which item would you like to see?\n"))
    show(list, index)
  elif choice == 6:
    print("Exiting...")
    break
  else:
    print("Invalid input")
