import json

# with open('info', 'r') as file:
#     info = file.read()


with open('info', 'r') as file:
    info_list = json.load(file)

# Now, info_list contains the list of dictionaries
print(info_list)