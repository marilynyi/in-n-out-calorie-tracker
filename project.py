import os
from pyfiglet import Figlet
import re
import sys
from urllib.request import urlopen


os.system("clear")

# Retrieve data from In N Out Nutrition Info
#
# In page source:
# Doctype = HTML
# Charset = "utf-8"
url = "https://www.in-n-out.com/menu/nutrition-info"
page = urlopen(url)
html = page.read().decode("utf-8")
html = html.replace("&reg", "").replace(";", "®").replace("\r", "")

# Uncomment to view html code
# print(html)


# Create regex for menu_item
menu_item = re.compile(
    r'(?:(?:<h3 class="js-accordion__header">(.*)<\/h3>.*\n\n\s*.*)|(?:<h3 class="js-accordion__header">(.*)<\/h3>.*\n\n\s*<div class="sf-Long-text" ><dl>\n\s*)|(?:<\/span>\n\s*(\w.*)(?:\n\s*)?<\/h2> <div class="js-accordion__panel">(?:.*)?.*\n\n\s*<div class="sf-Long-text" >(?:(?:\s)?<dl>\n\s*)?(?:.*)?)|(?:<h3 class="js-accordion__header">\n\s*(.*)\n\s*<\/h3>.*\n\n\s*<div class="sf-Long-text" ><dl>\n\s*))<dt>(Serving Size \(g\))<\/dt>(?:\n\s*)?<dd>(\d*(?: oz.)?)<\/dd>(?:\n\s*)?<dt>(Total Calories)<\/dt>(?:\n\s*)?<dd>(\d*)<\/dd>'
)

project_menu = []
project_menu = menu_item.findall(html)

# Function referenced from https://stackoverflow.com/questions/21391763/remove-empty-strings-from-tuples-inside-a-list
project_menu = [(tuple(int(x) if x.isdigit() else x for x in _ if x)) for _ in project_menu]

# Function referenced from https://stackoverflow.com/questions/34056301/how-to-add-sequential-numbers-to-a-list-of-tuples
project_menu = [tuple([index] + list(ref)) for index, ref in enumerate(project_menu)]


# Print all menu items in list format
def all():

    for i in project_menu:
        print(i)


# Print project header
def projectHeader():

    figlet = Figlet()

    header = "In-N-Out Burger"
    figlet.setFont(font = "small")
    print(figlet.renderText(header))

    print("-----------------------------------------------------------------")
    print("This is a calorie tracker for items on the In-N-Out menu.")
    print("Start building your meal!")
    #print("Type ALL to see the master list. 😀")
    print("-----------------------------------------------------------------\n")



def main():


    # Print ASCII project header and project description
    projectHeader()

    total_list = []
    total_calories = 0
    total_count = 0


    while True:
        try:

            calcExists = True

            # Print main menu
            menu_options = mainMenu()
            for i in menu_options:
                print(i)

            # Ask user to select a number pertaining to a menu item
            user_input = input().lower()

            # Print HTML code formatted and regexed to view data then exit program
            if user_input == "all":
                all()
                sys.exit()

            # If menu option is valid
            elif int(user_input) in range(1, len(menu_options) + 1):

                # Convert user input into an integer
                user_input = int(user_input)

                os.system("clear")

                # User selects burger (1), fries (2), shake (3), or beverage (4)
                try:
                    if user_input == 1:
                        count, name, calories = burger()

                    elif user_input == 2:
                        count, name, calories = fries()

                    elif user_input == 3:
                        count, name, calories = shake()

                    elif user_input == 4:
                        count, name, calories = beverage()

                    else:
                        calcExists = False
                        pass

                    # If function inputs are valid, proceed along to append and calculation
                        try:
                            if count == 0 and name == 0 and calories == 0:
                                calcExists = False
                                raise ValueError
                        except:
                            calcExists == False
                            pass

                except ValueError:
                    calcExists = False
                    pass

                # If user inputs are valid, append in receipt format to list and calculate total calories
                # Else skip append and calculation, then step out to main menu
                if calcExists == False or count == 0:
                    pass
                else:
                    total_list.append(f"{count} x {name.strip()}: {calories} calories")
                    total_calories += calories
                    total_count += count

            else:
                calcExists = False
                raise ValueError

        except ValueError:
            calcExists = False
            os.system("clear")
            pass

        except EOFError:
            break

        # Print running list of items successfully entered by user
        for i in total_list:
            print(i)
        print("")

    os.system("clear")

    # When user terminates program using Ctrl D, print all items, their corresponding calories, and total calories
    for i in total_list:
        print(i)
    print("")
    print(f"Total Items: {total_count}")
    print(f"Total Calories: {total_calories}")


# Print main menu
def mainMenu():
    item_number = 0
    menu = ["🍔 Burger", "🍟 French Fries", "🍨 Shake", "🥤 Beverage"]
    menu_options = []

    # Print list of menu options
    print("Add an item:")
    for i in menu:
        item_number += 1
        menu_options.append(f"  {item_number}: {i}")
    return menu_options


# If user selects Burger as a menu option
def burger():
    while True:
        try:
            item_number = 0
            burgers = ["🍔 Hamburger", "🍔 Cheeseburger", "🍔 Double-Double"]

            # Print burger menu options
            print("Pick a burger:")
            for i in burgers:
                item_number += 1
                print(f" {item_number}: {i}")
            print("Type 0 to cancel")

            # Ask user to select a burger option
            burger_input = int(input().strip())

            os.system("clear")

            burger_name = burgers[burger_input - 1]

            # If user inputs 0, go back to main menu
            if burger_input == 0:
                return 0, 0, 0

            # If burger input is valid
            if burger_input in range(1, len(burgers) + 1):
                break
            else:
                raise ValueError

        except (IndexError, ValueError):
            os.system("clear")
            pass

    # Ask user for burger style
    burger_name, burger_calories = burgerStyle(burger_name, burger_input)

    # Ask user for quantity to output total item count and calories
    burger_count, burger_name, burger_calories = quantity(burger_name, burger_calories)
    return burger_count, burger_name, burger_calories


# Customize burger name with selected style
def burgerStyle(burger_name, burger_input):
    while True:
        try:

            # Print burger style options
            print(f"Pick a style for {burger_name}:")
            print("  1: No additional style")
            print("  2: With mustard & ketchup instead of spread")
            print("  3: Protein style (bun replaced with lettuce)")

            # If burger style is valid, affix style to burger name and calculate calories for new burger
            burger_style = int(input().strip())

            os.system("clear")

            burger_name, burger_calories = burgerStyleValid(burger_input, burger_name, burger_style)

            break

        except ValueError:
            os.system("clear")
            pass

    return burger_name, burger_calories

# Calculate burger calories
def burgerStyleValid(burger_input, burger_name, burger_style):
    if burger_style == 1:  # Regular
        burger_name = f"{burger_name}"
        burger_calories = int(project_menu[(burger_input - 1) * 3][-1])
    elif burger_style == 2: # Replace spread with mustard & ketchup
        burger_name = f"{burger_name} (with mustard & ketchup)"
        burger_calories = int(project_menu[(burger_input - 1) * 3 + 1][-1])
    elif burger_style == 3: # Protein style
        burger_name = f"{burger_name} (Protein style)"
        burger_calories = int(project_menu[(burger_input - 1) * 3 + 2][-1])
    else:
        raise ValueError

    return burger_name, burger_calories


# If user selects French Fries as a menu option
def fries():

    fries_name = "🍟 French Fries"
    fries_calories = int(project_menu[9][-1])

    # Ask user for quantity to output total item count and calories
    return quantity(fries_name, fries_calories)


# If user selects shake as a menu option
def shake():
    while True:
        try:
            item_number = 0
            shake_calories = 0

            # Print shake options
            shake_names = ["🍫 Chocolate Shake", "🍦 Vanilla Shake", "🍓 Strawberry Shake"]
            print("Pick a flavor:")
            for i in shake_names:
                item_number += 1
                print(f"  {item_number}: {i}")
            print(f"Type 0 to cancel")

            # Ask user for type of shake
            shake_input = int(input().strip())

            os.system("clear")

            shake_name = shake_names[shake_input-1]

            # Go back to main menu
            if shake_input == 0:
                return 0, 0, 0

            shake_calories = shakeFlavorValid(shake_input, shake_names)

            break

        except (IndexError, ValueError):
            os.system("clear")
            pass


    # Ask user for quantity to output total item count and calories
    return quantity(shake_name, shake_calories)


# Calculate calories for selected shake
def shakeFlavorValid(shake_input, shake_names):
    # If shake input is valid
    if shake_input in range(1, len(shake_names)+1):
        shake_calories = int(project_menu[shake_input + 9][-1])

    else:
        raise ValueError

    return shake_calories


# If user selects a beverage as a menu option
def beverage():

    # List of all types of beverage_names (top-level)
    beverage_names = [
        "🥤 Coca-Cola®",
        "🥤 Diet Coke®",
        "🥤 7 Up®",
        "🥤 Dr Pepper®",
        "🥤 Barq's® Root Beer",
        "🥤 Barq's® Caffeine Free Root Beer",
        "🥤 Pink Lemonade",
        "🥤 Minute Maid® Zero Sugar Lemonade",
        "🥤 Iced Tea",
        "🥤 Sweet Tea",
        "☕️ Coffee (16 oz.)",
        "☕️ Hot Cocoa (8 oz.)",
        "🥛 Milk (10 oz.)",
    ]

    # Prompt user for beverage or go back to main menu
    while True:
        try:
            item_number = 0

            # Print beverage options
            print("Pick a beverage:")
            print("   Offered in Small (S), Medium (M), Large (L), and Extra Large (XL):")
            for i in beverage_names[0:10]:
                item_number += 1
                print(f"     {item_number}: {i}")
            print("  Other beverages")
            for i in beverage_names[10:]:
                item_number += 1
                print(f"     {item_number}: {i}")
            print("Type 0 to cancel")

            # Ask user to select a beverage
            beverage_input = int(input().strip())

            os.system("clear")

            # Go back to main menu
            if beverage_input == 0:
                os.system("clear")
                return 0, 0, 0

            # If beverage input is valid
            elif int(beverage_input) in range(1, len(beverage_names)+1):
                break

            else:
                raise ValueError

        except (IndexError, ValueError):
            os.system("clear")
            pass


    # If beverage with size option (not Coffee, Hot Cocoa, and Milk)
    if int(beverage_input) in range(1, len(beverage_names)-2):
        while True:
            try:
                beverage_input = int(beverage_input)
                beverage_name = beverage_names[beverage_input-1]

                # Ask user for desired beverage size
                size_input = input(f"What size for {beverage_name.strip()}? S, M, L, or XL\n").strip().lower()

                os.system("clear")

                beverage_name, beverage_calories = beverageSizeValid(beverage_input, beverage_name, size_input)

                break

            except ValueError:
                os.system("clear")
                pass


    # If beverage with no size option (Coffee, Hot Cocoa, and Milk)
    else:
        while True:
            try:
                os.system("clear")

                beverage_input = int(beverage_input)
                beverage_name = beverage_names[beverage_input-1]

                # Calculate calories
                if beverage_input == 11: # Coffee
                    beverage_calories = int(project_menu[53][-1])
                elif beverage_input == 12: # Hot cocoa
                    # Ask user if they want to add marshmallows to the Hot Cocoa
                    hot_cocoa_add_marshmallows = input(f"Add marshmallows to {beverage_name.strip()}? Y or N\n").strip().lower()
                    while True:
                        try:
                            os.system("clear")

                            if hot_cocoa_add_marshmallows in ["y","yes"]:
                                # Remove leading whitespace from name and affix with styled item
                                beverage_name = f"{beverage_name.strip()} with marshmallow"
                                beverage_calories = int(project_menu[55][-1])
                            # If user doesn't want Hot Cocoa
                            elif hot_cocoa_add_marshmallows in ["n","no"]:
                                beverage_calories = int(project_menu[54][-1])
                            else:
                                raise ValueError

                            break

                        except ValueError:
                            os.system("clear")
                            pass
                elif beverage_input == 13: # Milk
                    beverage_calories = int(project_menu[56][-1])
                else:
                    raise ValueError

                break

            except ValueError:
                os.system("clear")
                pass


    # Ask user for quantity to output total item count and calories
    return quantity(beverage_name, beverage_calories)


# Customize beverage name based on size and calculate calories
def beverageSizeValid(beverage_input, beverage_name, size_input):

    # If Small size
    if size_input in ["s","small", "sm"]:
        beverage_name = f"{beverage_name} (Small)"
        # idx 13 17 21 25 29 33 37 41 45 49
        # ipt 01 02 03 04 05 06 07 08 09 10
        # idx = 13 + 4*(ipt-1)
        beverage_calories = int(project_menu[13+4*(beverage_input-1)][-1])
    # If Medium size
    elif size_input in ["m","med","medium"]:
        beverage_name = f"{beverage_name} (Medium)"
        # idx of small + 1
        beverage_calories = int(project_menu[14+4*(beverage_input-1)][-1])
    # If Large size
    elif size_input in ["l","large"]:
        beverage_name = f"{beverage_name} (Large)"
        # idx of small + 2 or medium + 1
        beverage_calories = int(project_menu[15+4*(beverage_input-1)][-1])
    # If Extra Large size
    elif size_input in ["xl","xtra large","extra large","xlarge","x-l","extra-large"]:
        beverage_name = f"{beverage_name} (Extra Large)"
        # idx of small + 3 or medium + 2 or large + 1
        beverage_calories = int(project_menu[16+4*(beverage_input-1)][-1])
    else:
        raise ValueError

    return beverage_name, beverage_calories


# Multiply calories by count to get total calories
def quantity(name, calories):

    while True:
        try:
            print(f"How many {name.strip()}?")
            if name == "🍟 French Fries":
                print("Type 0 to cancel")

            count = int(input().strip())

            os.system("clear")

            # Go back to main menu
            if name == "🍟 French Fries" and count == 0:
                return 0, 0, 0

            if count and count > 0:
                calories *= count

            else:
                raise ValueError

            break

        except ValueError:
            os.system("clear")
            pass

    return count, name, calories


if __name__ == "__main__":
    main()