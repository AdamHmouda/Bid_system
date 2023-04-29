## Simple Bid System

This code is a simple program that prompts the user to enter their name and bid amount. The program continues to prompt the user until they choose to stop. Once the user decides to stop, the program determines the highest bidder and displays their name and bid amount.

### How to Use
1. Run the program
2. Enter your name
3. Enter your bid amount
4. Decide if there is anyone else who wants to bid
5. Repeat steps 2-4 until all bidders have entered their bids
6. When finished, enter 'n' to stop bidding and the program will determine the highest bidder

### Code Explanation
The program uses a dictionary named `bider` to store the name and bid amount of each bidder. The `running` variable is set to `True` to start the loop that prompts the user to enter their information. The `find_highest_bidder()` function takes the `bider` dictionary and loops through it to find the highest bidder. The `winner` and `highest_ammount` variables are used to keep track of the highest bidder and their bid amount. Finally, the winner's name and bid amount are displayed.