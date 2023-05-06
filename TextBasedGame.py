#Valerie Meiners

#show instructions for movement and collecting items
def main():
    print('*** Bedtime Adventure Text Game ***')
    print('*** Collect 6 Items Before Encountering the Baby ***\n')
    print('*** Move Commands: North, South, East, West ***')
    print('*** Take Item?: Yes, No ***\n')

if __name__ == "__main__":
    main()

    # create a dictionary linking rooms
    # villain in laundry room
    # create a dictionary linking items to rooms

    rooms = {'Living Room': {'South': 'Dining Room', 'West': 'Bedroom Two', 'East': 'Play Room', 'North': 'Bedroom One'},
             'Dining Room': {'North': 'Living Room', 'East': 'Kitchen', 'Item': 'Teddy Bear'}, 'Kitchen': {'West': 'Dining Room', 'Item': 'Bottle'},
             'Play Room': {'West': 'Living Room', 'North': 'Laundry Room', 'Item': 'Blanket'}, 'Laundry Room': {'South': 'Play Room'},
              'Bedroom One': {'South': 'Living Room', 'East': 'Bathroom', 'Item': 'Book'}, 'Bedroom Two': {'East': 'Living Room', 'Item': 'Pajamas'},
              'Bathroom': {'West': 'Bedroom One', 'Item': 'Pacifier'}}

    items = {'Living Room': {'No Item'}, 'Dining Room': {'Teddy Bear'}, 'Kitchen': {'Bottle'}, 'Play Room': {'Blanket'}, 'Laundry Room': {'Baby'},
             'Bedroom One': {'Book'}, 'Bedroom Two': {'Pajamas'}, 'Bathroom': {'Pacifier'}}

current_room = ('Living Room') # starting room
move = ''
inventory = [] # append the inventory if item acquired
acquire = ''

while move != 'Exit': # define how to exit game and what the program does if it is not exited
    print('\nYou are in the',current_room) # update user on position
    print('Inventory:',inventory,'\n') # update user of inventory
    move = input('Enter Move:') # prompt user for input
    for i in rooms.keys(): # define iteration through the rooms dictionary
        if i == current_room:
            if move in rooms[i]:
                current_room = rooms[current_room][move]
                print('\nYou are in the', current_room)
                if len(inventory) == 6 and current_room == 'Laundry Room': # define parameters of a win
                    print('The baby is comforted. You win!')
                    move = 'Exit' # define move for the user to end the program
                    break
                if len(inventory) != 6 and current_room == 'Laundry Room': # define parameters of a loss
                    print('The baby demands more! You lose!')
                    move = 'Exit' # define move for the user to end the program
                    break
                if current_room != 'Living Room' and items[current_room] not in inventory: # define item parameters when not in starting room
                    print('You see',items[current_room],'\n') # update user of items in room
                    acquire = input('Take Item?') # prompt user for input
                else:
                    print('No item here.')
                if acquire == 'Yes': # define parameters if user takes the item
                    acquire = '' #reset acquire
                    if items[current_room] in inventory: # define parameters if item already in inventory
                        print('You already have that item.','\n')
                    else: # append the inventory if the item has not been previously acquired
                        inventory.append(items[current_room])
                break
            else:
                print('Invalid Command.\n') # define parameters when user input is invalid
print("You have left the game. Goodbye.") # define exit from game


