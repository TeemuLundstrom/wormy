from util import ask_settings, ask_command
from game import play

(size,update_time) = ask_settings()

while True:
    play(size,update_time)
    command = ask_command()

    # If command == "1" we play again with same settings

    if command == "2":
        (size,update_time) = ask_settings()

    elif command == "3":
        break

print()
print("Goodbye! Thank you for playing :) ")
print()
    

