#create an empty dictionary
empty_dictionary = {}

#adding a item into dictionary
empty_dictionary["Loop"] ="The action of doing something over and over again"

# #wipe or erase an existing dictionary
# empty_dictionary={}

#we can seperate the dictionary by adding comma
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Function"])

#Edit an item in the dictionary
programming_dictionary["Bug"] = "Sleep bro"
# print(programming_dictionary)

#Loop through a dictionary
for thing in programming_dictionary:
    print(thing)  #to print key
    print(programming_dictionary[thing])   #to print value

#Nest a list into a dictionary
travel_log = {
    "France":["Paris","lalie"],
    "Ronaldo":["lisbon","Portugal","Giorgina"]
}

#Nesting a dictionary in a dictionary
travel_log2 = {
    "France":{"cities_visited":["Paris","lalie"],"total visits":12},
    "Ronaldo":["lisbon","Portugal","Giorgina"]
}

print(travel_log2["France"])

#Nesting a dictionary inside a list
travel_log3 =[
    {
        "country":"France",
        "cities_visited":["Paris","lals","Pescara"],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":["Munich","Hitler","Dusseldrof"],
        "total_visits":5

    },
]
print("bruh")
print(travel_log3)
