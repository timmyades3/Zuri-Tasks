import random

 
def play():

  while True:
    user_choice=input("what's your choice? 'r' for rock 'p' for paper 's' for scissors\n")
    user_choice=user_choice.lower()

    if user_choice not in ['r', 'p', 's']:
      print('Error: please input either r, p or s')
      continue
    
    computer_choice = random.choice(['r', 'p', 's'])
    if user_choice == computer_choice:
      print( "you and the computer have both chosen {}. it's a tie".format(computer_choice))
      print("Please try again")
      continue  
    
    # r > s, s > p, p > R
    if is_win(user_choice, computer_choice):
      print ("you have chosen {} and the computer have chosen {}. you won!".format(user_choice, computer_choice)) 
      return "Game Ended!"
    
    print("you have chosen {} and the computerhas chosen {}. you lost :(".format(user_choice, computer_choice))   
    print("Please try again")
 
def is_win(player, opponent):

  if (player == 'r' and opponent == 's') or (player =='s' and opponent =='p') or (player =='p' and opponent == 'r'):
    return True
  return False

if __name__ == '__main__':
  print(play())  


   
    
