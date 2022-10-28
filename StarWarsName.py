#Assessed Task 2 - Week 4

print("Star Wars name generator".center(35))

print()
first_name = input("Please enter your first name: ")
surname = input("Please enter your last name: ")
maiden_name = input("Please enter your Mother's maiden name ")
birth_place = input("Please enter the name of the city you were born in: ")

star_wars_name = first_name[:3] + surname[:2].lower() + " " + maiden_name[:2] + birth_place[:3].lower()

print("Your Star Wars name is " + star_wars_name)