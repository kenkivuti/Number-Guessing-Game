import random
# wgen using for loop you import so as to use count
# from itertools import count

class Game():

    def __init__(self) -> None:
        # initialization
        self.target_num : int


    def start_game(self) -> None:
        # starts the game and runs till the correct number is guessed
        self.target_num=random.randint(0,100)

        while True:
            guess = self._get_user_guess()
            if self._check_guess(guess):
                break

#  you can also use the for loop method and pass max_attempts
        # for attempt in count(1):
        #     if attempt > max_attempts:
        #         print(f"Game over! You've reached the maximum number of attempts ({max_attempts}).")
        #         break

    def _get_user_guess(self) -> int:
        # retrives int guess from player.
        # returns value of player's guess.
        if True:
           guess = input("please enter a positive integer between 0 and 100 : ")
           try:
            #   cause exception
              if float(guess).is_integer() and int(guess) >= 0 and int(guess) <= 100:
               return int(guess)
           except:
            #    run when exception is caused
               print("guess was not valid int.")

    def _check_guess(self,guess) -> bool:
        #  provides guess against the target value.prints 'higher' or 'lower'
         
         if guess < self.target_num:
             print(" guess a Higher number! ")
             return False
         if guess > self.target_num:
             print(" guess a Lower number!") 
             return False
         print(f"correct Guess! the number was : {self.target_num}")
         return True
    

if __name__ == '__main__':
    game_instance = Game()
    game_instance.start_game()
                   