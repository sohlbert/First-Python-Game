#Making a game

#Dictionary
player = {'name': 'Robert', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name': 'Chuthlu', 'attack': 12, 'health': 150}
game_running = True

while game_running = True:

print("Please select action")
print("1) Attack")
print("2) Heal")

player_choice = input()

if player_choice == '1':
    monster['health'] = monster['health'] - player['attack']
    player['health'] = player['health'] - monster['attack']
    print(monster['health'])
    print(player['health'])


elif player_choice == '2':
    print("Healing")
else:
    print('Invalid Input')