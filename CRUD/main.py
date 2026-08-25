from pathlib import Path
import os

def create_file():

    try:
     name = input("What is the file name?: ")
     path = Path(name)

     if not path.exists():
       with open(path, "w") as fs:
        data = input("what you want to write?: ")
        fs.write(data)
     else:
       print("File name already exists")
    except Exception as err:
       print(f"An error has occured as {err}")

def update_file():
   try:
    name = input("What is the name of the file?: ")
    path = Path(name)

    if path.exists():
      print("""
            1 : rename the file
            2 : appending the content
            3 : overwriting the file""")
      
      choice = int(input("what is your choice?: "))

      if choice == 1:
         new_name = input("what is the new name?: ")
         if not Path(new_name).exists():
          path.rename(new_name)
         else:
          print("This name already exists! Try another name")
      elif choice == 2:
         text = input("what you need to add?: ")
         with open(path, "a") as fs:
          fs.write(text)
      elif choice == 3:
          text = input("What do you want to overwrite this with?: ")
          with open(path, "w") as fs:
            fs.write(text)
      else:
          print('Enter a valid choice please!')
    else:
      print("File does not exist!")
   except Exception as err:
     print(f"An error has occured as {err}")

def read_file():
    try:
      name = input("What is the name of the file?: ")
      path = Path(name)

      if path.exists():
         with open(path, "r") as fs:
          read = fs.read()
          print(read)
      else:
       print("file name doesn't exist")

    except Exception as err:
       print(f"An error has occured as {err}")

def delete_file():
  try:
    name = input("Enter the filename you want to delete")
    path = Path(name)
    if path.exists():
      path.unlink()
    else:
      print("Path name does not exist")
  except Exception as err:
    print(f"An error has occured as {err}")

print("""1 : create a new file
2 : update the file
3 : read the file
4 : delete the file""")

try:
 option = int(input("select the option please: "))

 if option == 1:
    create_file()
 elif option == 2:
    update_file()
 elif option == 3:
    read_file()
 elif option == 4:
    delete_file()
 else:
    print("Enter a valid option please!")

except Exception as err:
    print(f"An error occured as {err}")
