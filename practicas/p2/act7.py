# Amigo invisible = Secret Santa

import random

print()
print(" Bienvenido al asignador de amigos invisibles ".center(80, "*"))
print("\nEsto sirve cuando hay al menos tres nombres, y no están repetidos\n")


# Input situation
while True:
    friends_names = input("Ingrese los participantes (separados por coma): ").split(",")
    friends_list = [friend.strip().title() for friend in friends_names]

    if len(friends_list) != len(set(friends_list)):
        print("Ingresó nombres repetidos. Vuelva a intentar")
    elif len(friends_list) < 3:
        print("Debe ingresar al menos tres nombres")
    else:
        break


while True:
    # Perform the random assignment by creating another list with the same elements but shuffled.
    shuffled = friends_list.copy()
    random.shuffle(shuffled)
    # Check that no one has assigned themselves
    if all(a != b for a, b in zip(friends_list, shuffled)):
        # A dictionary is created with the list of friends and their secret santa
        secret_santas = dict(zip(friends_list, shuffled))
        break


print("Sorteo de amigo invisible:")
for someone, ss in secret_santas.items():
    print(f"{someone} --> {ss}")



# # My first solution was:
# 
# secret_santas = {}    
# keep_trying = True
# 
# # We will make the assignments until everyone has their secret friend
# while keep_trying:
# 
#     copy_friends_list = friends_list.copy()
# 
#     for friend in friends_list:
#         while True:
#             random_friend = random.choice(copy_friends_list)
#             if friend != random_friend:
#                 # Someone is assigned an invisible friend
#                 secret_santas[friend] = random_friend
#                 copy_friends_list.remove(random_friend)
#                 break
#             elif len(copy_friends_list) == 1:
#                 # The last friend to be assigned has no one but himself,
#                 # so we reset the lists and try again from scratch
#                 secret_santas = {}
#                 break
#     if len(friends_list) == len(secret_santas):
#         keep_trying = False