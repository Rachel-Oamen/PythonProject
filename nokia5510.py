# NOKIA 5510 MENU FUNCTIONS

while True:
    print("\n====== NOKIA PHONE MENU ======")
    print("1. Contacts")
    print("2. Messages")
    print("3. Chat")
    print("4. Call Register")
    print("5. Tone Tones")
    print("6. Settings")
    print("7. Call Divert")
    print("8. Music")
    print("9. Games")
    print("10. Calculator")
    print("11. Reminders")
    print("12. Clock")
    print("13. Profiles")
    print("14. WAP Services")
    print("15. Call")
    print("16. Exit")

    choice = input("Select an option: ")

    
    if choice == "1":

        while True:
            print("\n===== CONTACTS =====")
            print("1. View Contacts")
            print("2. Add Contact")
            print("3. Search Contact")
            print("4. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("No contacts available.")

            elif choice == "2":
                name = input("Enter contact name: ")
                number = input("Enter phone number: ")
                print(name, "has been added successfully.")

            elif choice == "3":
                name = input("Enter name to search: ")
                print("Searching for", name)

            elif choice == "4":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "2":

        while True:
            print("\n===== MESSAGES =====")
            print("1. Inbox")
            print("2. Create Message")
            print("3. Sent Messages")
            print("4. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Your inbox is empty.")

            elif choice == "2":
                message = input("Enter your message: ")
                print("Message created:", message)

            elif choice == "3":
                print("No sent messages.")

            elif choice == "4":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "3":

        while True:
            print("\n===== CHAT =====")
            print("1. Start New Chat")
            print("2. View Chats")
            print("3. Back")

            choice = input("Select option: ")

            if choice == "1":
                name = input("Enter recipient name: ")
                message = input("Type your message: ")
                print("Message sent to", name)

            elif choice == "2":
                print("No chats available.")

            elif choice == "3":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "4":

        while True:
            print("\n===== CALL REGISTER =====")
            print("1. Missed Calls")
            print("2. Received Calls")
            print("3. Dialled Numbers")
            print("4. Delete Recent Calls")
            print("5. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("No missed calls.")

            elif choice == "2":
                print("No received calls.")

            elif choice == "3":
                print("No dialled numbers.")

            elif choice == "4":
                print("Recent calls deleted.")

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "5":

        while True:
            print("\n===== TONE TONES =====")
            print("1. Ringing Tone")
            print("2. Ringing Volume")
            print("3. Message Alert Tone")
            print("4. Keypad Tones")
            print("5. Warning Tones")
            print("6. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Ringing tone selected.")

            elif choice == "2":
                print("Adjusting ringing volume.")

            elif choice == "3":
                print("Message alert tone selected.")

            elif choice == "4":
                print("Keypad tones activated.")

            elif choice == "5":
                print("Warning tones activated.")

            elif choice == "6":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "6":

        while True:
            print("\n===== SETTINGS =====")
            print("1. Phone Settings")
            print("2. Display Settings")
            print("3. Call Settings")
            print("4. Security Settings")
            print("5. Restore Factory Settings")
            print("6. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Phone settings selected.")

            elif choice == "2":
                print("Display settings selected.")

            elif choice == "3":
                print("Call settings selected.")

            elif choice == "4":
                print("Security settings selected.")

            elif choice == "5":
                print("Factory settings restored.")

            elif choice == "6":
                break

            else:
                print("Invalid choice!")


    elif choice == "7":

        while True:
            print("\n===== CALL DIVERT =====")
            print("1. Divert All Voice Calls")
            print("2. Divert When Busy")
            print("3. Divert When Not Answered")
            print("4. Divert When Unreachable")
            print("5. Cancel All Diverts")
            print("6. Check Divert Status")
            print("7. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("All voice calls diverted.")

            elif choice == "2":
                print("Calls will be diverted when busy.")

            elif choice == "3":
                print("Calls will be diverted when not answered.")

            elif choice == "4":
                print("Calls will be diverted when unreachable.")

            elif choice == "5":
                print("All call diverts cancelled.")

            elif choice == "6":
                print("Checking call divert status.")

            elif choice == "7":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "8":

        while True:
            print("\n===== MUSIC =====")
            print("1. Music Player")
            print("2. Radio")
            print("3. Recorder")
            print("4. Stop Music")
            print("5. Track List")
            print("6. Previous Track")
            print("7. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Opening music player.")

            elif choice == "2":
                print("Radio.")

            elif choice == "3":
                print("Recorder.")

            elif choice == "4":
                print("Music stopped.")

            elif choice == "5":
                print("Playing next track.")

            elif choice == "6":
                print("Playing previous track.")

            elif choice == "7":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "9":

        while True:
            print("\n===== GAMES =====")
            print("1. Snake")
            print("2. Space Impact")
            print("3. Sudoku")
            print("4. Select Game")
            print("5. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Starting Snake game.")

            elif choice == "2":
                print("Starting Space Impact.")

            elif choice == "3":
                print("Starting Sudoku game.")

            elif choice == "4":
                print("Choose your favourite game.")

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "10":

        while True:
            print("\n===== CALCULATOR =====")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Back")

            choice = input("Select option: ")

            if choice == "1":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", num1 + num2)

            elif choice == "2":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", num1 - num2)

            elif choice == "3":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", num1 * num2)

            elif choice == "4":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if num2 == 0:
                    print("Error! Cannot divide by zero.")
                else:
                    print("Result:", num1 / num2)

            elif choice == "5":
                break

            else:
                print("Invalid choice!")


    elif choice == "11":

        while True:
            print("\n===== REMINDERS =====")
            print("1. Add Reminder")
            print("2. View Reminders")
            print("3. Delete Reminder")
            print("4. Delete All Reminders")
            print("5. Back")

            choice = input("Select option: ")

            if choice == "1":
                reminder = input("Enter your reminder: ")
                print("Reminder added:", reminder)

            elif choice == "2":
                print("Your reminders will appear here.")

            elif choice == "3":
                print("Reminder deleted.")

            elif choice == "4":
                print("All reminders deleted.")

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "12":

        while True:
            print("\n===== CLOCK =====")
            print("1. Show Time")
            print("2. Show Date")
            print("3. Stopwatch")
            print("4. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Current Time: 05:40")

            elif choice == "2":
                print("Current Date: Nov-14-2026")

            elif choice == "3":
                print("Stopwatch feature coming soon.")

            elif choice == "4":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "13":

        while True:
            print("\n===== PROFILES (ACTIVATION) =====")
            print("1. General")
            print("2. Silent")
            print("3. Meeting")
            print("4. Outdoor")
            print("5. Pager")
            print("6. Back")

            choice = input("Select profile: ")

            if choice == "1":
                print("General profile activated.")

            elif choice == "2":
                print("Silent profile activated.")

            elif choice == "3":
                print("Meeting profile activated.")

            elif choice == "4":
                print("Outdoor profile activated.")

            elif choice == "5":
                print("Pager profile activated.")

            elif choice == "6":
                break

            else:
                print("Invalid choice!")

    
    elif choice == "14":

        while True:
            print("\n===== WAP SERVICES =====")
            print("1. Home")
            print("2. Bookmarks")
            print("3. Go to Address")
            print("4. Service Inbox")
            print("5. Saved Pages")
            print("6. Settings")
            print("7. Back")

            choice = input("Select option: ")

            if choice == "1":
                print("Opening WAP homepage.")

            elif choice == "2":
                print("Opening bookmarks.")

            elif choice == "3":
                address = input("Enter website address: ")
                print("Website address:", address)

            elif choice == "4":
                print("Opening service inbox.")

            elif choice == "5":
                print("Opening saved pages.")

            elif choice == "6":
                print("Opening WAP settings.")

            elif choice == "7":
                break

            else:
                print("Invalid choice!")


    elif choice == "15":
        print("Calling...")


    elif choice == "16":
        print("Thank you for using Nokia!")
        break

    else:
        print("Invalid selection. Try again.")
