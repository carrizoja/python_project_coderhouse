#Montaje de la unidad de Google Drive

#from google.colab import drive
#drive.mount('/drive/')

#Ruta donde se va a guardar el archivo que simula la base de datos

path = '/drive/MyDrive/coderhouse/python/primera_entrega/'

# Reseteo para el archivo Json

#Importo las funciones de json
import json
with open("/drive/MyDrive/coderhouse/python/primera_entrega/database.json", "w") as f:
 json.dump({}, f)

userdata = {}
userdata['users'] = []
with open(path + "/database.json", "w") as file:
  json.dump(userdata, file, indent=4)

#Módulo de Registro de usuario

def user_register():
  #diccionario que se usará para agregar los datos ingresados al Json
  userdata = {}
  while True:
    username = input("Enter an username (at least 4 characters):\n")
    if len(username) < 4:
      print("Username must have at least 4 characters\n")
    else:
      break
  while True:
    password = input("Enter a password (at least 8 numeric and alphabet characters):\n")
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
      print("Password must have at least 8 characters and contain both numeric and alphabet characters\n")
    else:
      break
  userdata['username'] = username
  userdata['password'] = password

  with open(path + "/database.json") as file:
    read_data = json.load(file)
    read_data['users'].append(userdata)
  with open(path + "/database.json", "w") as file:
    try:
      json.dump(read_data, file, indent=4)
      print("User registered successfully!\n")
    except:
      print("Something was wrong with the register. Please, try again.")

#Módulo de Listado de usuarios

def user_list():
  try:
    with open(path + "/database.json") as file:
      read_data = json.load(file)
      for user in read_data['users']:
        print('Username:', user['username'])
        print('Password:', user['password'])
        print('')
  except:
    print("Something was wrong loading the user's list. Please, try again")

# Módulo de Login

def login():
  #diccionario que se usará para comparar los ingresos del usuario con lo existente en el Json
  userdata = {}
  while True:
    username = input("Enter the username:\n")
    password = input("Enter the password:\n")
    userdata['username'] = username
    userdata['password'] = password
    with open(path + "/database.json") as file:
      data = json.load(file)
      for user in data['users']:
        if user['username'] == username and user['password'] == password:
          print("Login successful!\n")
          return
      print("Invalid username or password.")
      return

#Módulo del Programa principal

print("WELCOME TO OUR REGISTER SYSTEM:\n")
print("---------------------- MENU -------------------------\n")

while True:
  print("CHOOSE AN OPTION")
  option = input("1 - REGISTER. 2 - LIST. 3 - LOGIN. 4 - EXIT\n")
  if option.isdigit():
    option = int(option)
    if option == 1:
      user_register()
    elif option == 2:
      print("The Users list:\n")
      user_list()
    elif option == 3:
      login()
    elif option == 4:
      print("Thank you for choose us. Bye!")
      break
    else:
      print("Invalid option. Please, select it again\n")
  else:
    print("Invalid option. Please, select it again\n")
