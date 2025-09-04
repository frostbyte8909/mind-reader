#importing and setting up dependencies
import time
import pwinput
import pyfiglet

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

ascii_welcome_text = r""".___  ___.  __  .__   __.  _______     .______       _______     ___       _______   _______ .______      
|   \/   | |  | |  \ |  | |       \    |   _  \     |   ____|   /   \     |       \ |   ____||   _  \     
|  \  /  | |  | |   \|  | |  .--.  |   |  |_)  |    |  |__     /  ^  \    |  .--.  ||  |__   |  |_)  |    
|  |\/|  | |  | |  . `  | |  |  |  |   |      /     |   __|   /  /_\  \   |  |  |  ||   __|  |      /     
|  |  |  | |  | |  |\   | |  '--'  |   |  |\  \----.|  |____ /  _____  \  |  '--'  ||  |____ |  |\  \----.
|__|  |__| |__| |__| \__| |_______/    | _| `._____||_______/__/     \__\ |_______/ |_______|| _| `._____|
                                                                                                          """

#creating the mind reading game
print(ascii_welcome_text)
print("\nWelcome to the mind reading game\n I will guess the number that you have thought of\n but be careful, it may take some time\n")
num_guessed = pwinput.pwinput(prompt="Enter the number you thought of: ", mask='*')

#making the user wait using a progress bar
items = list(range(0, 5))
l = len(items)

printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    time.sleep(0.1)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

#concluding the game and printing the answer
text = num_guessed
ascii_art = pyfiglet.figlet_format(text)

print("The number you guessed was:")
print(ascii_art)
