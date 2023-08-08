import datetime
import random

# greet user
print('Welcome to dog walking App\n')

date_time_list = [
    "20-05-2022 07:00",
    "21-05-2022 07:30",
    "22-05-2022 08:00",
    "23-05-2022 08:30",
    "24-05-2022 09:00"
]

dog_walker_name = [
    "Ben",
    "Sarah",
    "Mark",
    "Jane",
    "Musa"
]

while True:

    # ask person if they are a dog walker or user
    user_type = input("Are you a dog walker or a dog owner or (type 'exit' to quit)? \n")

    if user_type == "dog walker":
        dog_walker_id = []
        dog_walker_info = []

        while True:
            name = input("Enter your fullname (or type 'exit' to start again): ")
            if name == "exit":
                break
            if not name.replace(' ', '').isalpha():
                print("Please enter only letters for your name.")
                continue
            id_num = input("Enter your identification number (3 digits only): ")
            while not id_num.isdigit() or len(id_num) != 3:
                print("Please enter a 3-digit number.")
                id_num = input("Enter your identification number (3 digits only): ")

            while True:
                try:
                    date_time = datetime.datetime.strptime(
                        input("Enter your available date and time (format: DD-MM-YYYY HH:MM): "), '%d-%m-%Y %H:%M')
                    break
                except ValueError:
                    print("Invalid date/time format. Please enter in format: DD-MM-YYYY HH:MM")
                    continue
            date_time_str = datetime.datetime.strftime(date_time, '%d-%m-%Y %H:%M')

            dog_walker_name.append(name)
            dog_walker_id.append(id_num)
            date_time_list.append(date_time_str)
            dog_walker_dict = {"Name": name, "ID Number": id_num, "Available Date and Time": date_time_str}
            dog_walker_info.append(dog_walker_dict)

            print("Dog walker information:")
            for walker in dog_walker_info:
                print('Your information ' + str(walker) + ' has been added to the list.')
                print()



    # If a USER
    elif user_type == "dog owner":

        while True:
            # Print the list of available date and time options with numbers
            print('Date and time available')
            for i in range(len(date_time_list)):
                print(str(i + 1) + ". " + date_time_list[i])

            # Ask the user to input their selection
            selection = input("Select a date and time (enter the number): ")

            try:
                # Convert the selection to an integer and subtract 1 to get the index of the selected date and time
                index = int(selection) - 1

                # Check if the index is valid
                if index >= 0 and index < len(date_time_list):
                    # Get the selected date and time from the list and print it out
                    selected_date_time = date_time_list[index]
                    print(f"You selected {selected_date_time}\n")
                    break
                else:
                    print("Invalid selection. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        # ask user to select a durtion from a given list of duration
        duration_list = [
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00"]

        while True:
            print("Duration available:")
            for i in range(len(duration_list)):
                print(str(i + 1) + ". " + duration_list[i])

            selection = input('select the duration you want from the option(enter the number): ')

            if selection.isdigit():
                selection = int(selection)
                if selection >= 1 and selection <= len(duration_list):
                    selected_duration = duration_list[selection - 1]
                    print("You selected a duration of " + selected_duration + " for dog walking.\n")
                    break
            print("Invalid selection. Please try again.\n")

        # ask user to select a breed from a given list of breeds
        breed_list = [
            "Siberian Husky",
            "Poodles",
            "Rottweilers",
            "German Shepherd",
            "Golden Retrievers",
            "Chow Chow",
            "Goldendoodle"]

        while True:
            print("Available dog breeds:")
            for i in range(len(breed_list)):
                print(str(i + 1) + ". " + breed_list[i])

            selection = input('Select the breed of the dog you want to walk (enter the number): ')

            if selection.isdigit():
                selection = int(selection)
                if selection >= 1 and selection <= len(breed_list):
                    selected_breed = breed_list[selection - 1]
                    print("You selected the breed: " + selected_breed + '\n')
                    break

            print("Invalid selection. Please try again.\n")

        # ask user to select the number of dogs they have to be walked from a given list of dog numbers
        number_of_dogs = [
            'I have 1 dog',
            'I have 2 dogs',
            'I have 3 dogs',
            'I have 4 dogs',
            'I have 5 dogs']

        while True:
            print('number of dogs that can be walked at once:')

            for i in range(len(number_of_dogs)):
                print(str(i + 1) + '. ' + number_of_dogs[i])

            selection = input('Select the number of dogs you want to be walked at once (pick from the option above): ')

            try:
                selection = int(selection)

                if selection >= 1 and selection <= len(number_of_dogs):

                    selected_no_of_dogs = number_of_dogs[selection - 1]
                    print("You selected " + selected_no_of_dogs + " to be walked.\n")
                    break
                else:
                    print('Invalid selection. Try again.\n')

            except ValueError:
                print('Invalid selection. Try again\n')

        fee_per_dog_per_hour = 15
        selected_duration_hours = int(selected_duration.split(":")[0])
        selected_no_of_dogs_num = int(selected_no_of_dogs.split()[2])
        total_fee = selected_duration_hours * selected_no_of_dogs_num * fee_per_dog_per_hour

        print(f"The total fee for walking {selected_no_of_dogs} for {selected_duration} is ${total_fee}.")

        assign = random.choice(dog_walker_name)
        print("Your assigned dog walker is: ", assign)
        print()

    else:
        user_type == "exit"
        print('Bye, thanks.')
        break
