
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
running =True
bider ={}
print(logo)

def find_highest_bidder(record):
    highest_ammount=0
    winner=""
    for bidder in record:
        highest_bider=record[bidder]
        if highest_bider >highest_ammount:
            highest_ammount=highest_bider
            winner=bidder
    print(f"Winner is {winner} with a bid of {highest_ammount}$")
while running:
    name=input("Enter your name : \n")
    price=int(input("Enter bid ammount : \n"))
    A=input("Is there anyone else ?(y/n) \n")
    bider[name]=price
    if A=="n":
        running = False
        find_highest_bidder(bider)