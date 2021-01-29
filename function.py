import classobject

def choice():
    please_choose = input(f"Please choose the madlib you want to play: \n Press 1 for the ZOO. \n Press 2 for the park. \n Press 3 for the arcade. \n Enter choice: ")
    while please_choose:
        if please_choose == '1':
            classobject.madlib_at_the_zoo.at_the_zoo()
            try_again = input("Do you want to try again? Yes / No: ")
            if try_again == "Yes" or try_again == "yes":
                choice()
            elif try_again == "No" or try_again == "no":
                print("Exiting the game!")
                break
            else:
                while try_again:
                    try_again_conditional = input("Please enter Yes or No: ")
                    if try_again_conditional == "Yes" or try_again_conditional == "yes":
                        return choice()
                    elif try_again_conditional == "No" or try_again_conditional == "no":
                        print("Exiting the game. Thanks for playing!")
                        break
            break
        elif please_choose == '2':
            classobject.madlib_at_the_park.at_the_park()
            try_again = input("Do you want to try again? Yes / No: ")
            if try_again == "Yes" or try_again == "yes":
                choice()
            elif try_again == "No" or try_again == "no":
                print("Exiting the game!")
            else:
                while try_again:
                    try_again_conditional = input("Please enter Yes or No: ")
                    if try_again_conditional == "Yes" or try_again_conditional == "yes":
                        return choice()
                    elif try_again_conditional == "No" or try_again_conditional == "no":
                        print("Exiting the game. Thanks for playing!")
                        break
            break
        elif please_choose == '3':
            classobject.madlib_at_the_zoo.at_the_zoo()
            try_again = input("Do you want to try again? Yes / No: ")
            if try_again == "Yes" or try_again == "yes":
                choice()
            elif try_again == "No" or try_again == "no":
                print("Exiting the game!")
            else:
                while try_again:
                    try_again_conditional = input("Please enter Yes or No: ")
                    if try_again_conditional == "Yes" or try_again_conditional == "yes":
                        return choice()
                    elif try_again_conditional == "No" or try_again_conditional == "no":
                        print("Exiting the game. Thanks for playing!")
                        break
            break
        else:
            print("You've entered the wrong option. Try again! (1, 2 or 3)")
            choice()