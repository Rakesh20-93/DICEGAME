# create random numbers
import random

# Initialise scores to 0
P_1_SCORE = 0
P_2_SCORE = 0

# Repeat everything for 10 times
for i in range(10):

    # Generate random numbers between 1 and 6 .
    P_1_VALUE = random.randint(1, 6)
    P_2_VALUE = random.randint(1, 6)

    # Display the values
    print("Player 1 rolled: ", P_1_VALUE)
    print("Player 2 rolled: ", P_2_VALUE)

    # Selection:.
    if P_1_VALUE > P_2_VALUE:
        print("player 1 wins.")
        P_1_SCORE = P_1_SCORE + 1  # increment a variable
    elif P_2_VALUE > P_1_VALUE:
        print("player 2 wins")
        P_2_SCORE = P_2_SCORE + 1
    else:
        print("It's a Draw")

    input("Press Enter to Continue.")  # Wait for user .

print("*** GAME OVER***")
print("Player 1 score:", P_1_SCORE)
print("Player 2 score:", P_2_SCORE)