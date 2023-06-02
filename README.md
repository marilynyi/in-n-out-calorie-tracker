# In-N-Out Burger Calorie Tracker
#### Video Demo: Available upon request
### Description: This is my final project submission to conclude the CS50's Introduction to Programming with Python course at HarvardX. The project is a basic calorie tracker specifically for the menu items at In-N-Out Burger.

## Overview

This repository contains a basic calorie tracking project for the [menu items](https://www.in-n-out.com/menu) at [In-N-Out Burger](https://www.in-n-out.com/). The project file ```project.py``` is an interactive program used to build a meal and determine the ```total number of calories``` for that meal. There are 57 unique items listed on the website. These have been bucketed into the following categories in the program's main input prompt for simplicity in item selection.

### Input Prompt
```
Add an item:
  1: 🍔 Burger
  2: 🍟 French Fries
  3: 🍨 Shake
  4: 🥤 Beverage
```

Depending on the item, the user will encounter additional prompts, e.g., ```burger style```, ```milkshake flavor```, or ```beverage size```.

As each item is successfully selected, the program will output a running receipt of the ```count```, ```name```, and specific ```total number of calories``` for each particular item. The program will terminate and output the total ```count``` and ```calories``` of all items when the user issues the termination command ```Control``` ```D``` with an example of the output shown below.

### Example Output
```
2 x 🍔 Cheeseburger (Protein style): 660 calories
1 x 🍟 French Fries: 370 calories
1 x 🥤 Dr Pepper® (Medium): 180 calories

Total Items: 4
Total Calories: 1210
```

## Supporting Files and Documentation
1. [backup_html.html](https://github.com/code50/131757384/blob/main/project/backup_html.html): A copy of the HTML code containing the full In-N-Out menu information. Should the website change, the project will continue to work when pulling from this file instead.

2. [project_menu.txt](https://github.com/code50/131757384/blob/main/project/project_menu.txt): An output of the primary list of formatted and regexed data for the main file ```project.py```. This serves to quickly validate index numbers and item information at a glance.

3. [regex_project.txt](https://github.com/code50/131757384/blob/main/project/regex_project.txt): The regex expression in unique parts created using the regex builder [regex101.com](https://regex101.com/) to capture all relevant menu information in the HTML code.

4. [requirements.txt](https://github.com/code50/131757384/blob/main/project/requirements.txt): Text file that contains a short list of installed libraries:
    - ```pyfiglet```
    - ```regex```
    - ```pytest```

5. [test_project.py](https://github.com/code50/131757384/blob/main/project/test_project.py): Test file to validate three stand-alone functions in ```project.py```, namely
    - ```burgerStyleValid```
    - ```shakeFlavorValid```
    - ```beverageSizeValid```

6. [CS50P Final Project Requirements](https://cs50.harvard.edu/python/2022/project/): Includes final project instructions

## Limitations
- For simplicity, ```class``` methods were not used.

    Due to variations in the data structure depending on the type of item as well as my personal desire to keep ```0``` as a way to return to the main menu, my primary goal was to get the program in working condition. I wanted to preserve the entire In-N-Out menu. With my current knowledge of Python and the complexity of the data structure, introducing ```class``` methods did not seem optimal.

-  Once a primary menu item (```Burger```, ```French Fries```, ```Shake```, or ```Beverage```) is selected and the user is then prompted for a specific item, the user has the option to cancel and go back to the main menu. Past the specific item menu, the user cannot back out of their item customization; valid non-zero integers must be provided.

    A demonstration of this limitation is shown in the Example Usage section.

- Some index references are hardcoded instead of formulated for simplicity.

    The formatted list used to pull indices from is not in the cleanest form. I wanted to preserve the original data as much as I could instead of manually cleaning up the formatted list itself.

- Adding a particular item prints itself in its own line rather than combining count and calories if there exists a previous line with the same type of item. This is due to my appending strings to the list used to print the items. While not optimal, the output displays correct values.
    ```
    1 x 🍓 Strawberry Shake: 590 calories
    1 x 🍟 French Fries: 370 calories
    3 x 🍓 Strawberry Shake: 1770 calories

    Total Items: 5
    Total Calories: 2730
    ```

## Example Usage

### Main menu
User is greeted with a welcome message and menu items at the start of the program.
```
 ___         _  _      ___       _     ___
|_ _|_ _ ___| \| |___ / _ \ _  _| |_  | _ )_  _ _ _ __ _ ___ _ _
 | || ' \___| .` |___| (_) | || |  _| | _ \ || | '_/ _` / -_) '_|
|___|_||_|  |_|\_|    \___/ \_,_|\__| |___/\_,_|_| \__, \___|_|
                                                   |___/

-----------------------------------------------------------------
This is a calorie tracker for items on the In-N-Out menu.
Start building your meal!
-----------------------------------------------------------------

Add an item:
  1: 🍔 Burger
  2: 🍟 French Fries
  3: 🍨 Shake
  4: 🥤 Beverage
  ```
User selects ```1: 🍔 Burger```.

### Burger menu
User is prompted for the type of burger. Note the option here to press ```0``` to return to the main menu.
```
Pick a burger:
 1: 🍔 Hamburger
 2: 🍔 Cheeseburger
 3: 🍔 Double-Double
Type 0 to cancel
 ```
 User selects ```2: 🍔 Cheeseburger```.

 ### Burger style menu
User is prompted for an optional burger style.
 ```
 Pick a style for 🍔 Cheeseburger:
  1: No additional style
  2: With mustard & ketchup instead of spread
  3: Protein style (bun replaced with lettuce)
```

User selects ```3: Protein style (bun replaced with lettuce)```.

### Burger quantity menu
User is prompted for burger quantity.
```
How many 🍔 Cheeseburger (Protein style)?
```
User types ```1``` for burger quantity.

### Return to main menu
User is shown their successful item addition and is prompted to add another item.
```
1 x 🍔 Cheeseburger (Protein style): 330 calories

Add an item:
  1: 🍔 Burger
  2: 🍟 French Fries
  3: 🍨 Shake
  4: 🥤 Beverage
  ```
User types ```Control``` ```D``` instead.

### Program termination
User is shown the output of total items and calories.
```
1 x 🍔 Cheeseburger (Protein style): 330 calories

Total Items: 1
Total Calories: 330
```