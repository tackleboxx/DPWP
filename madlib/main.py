'''

Class: Design Patterns for Web Programming - Online
Assignment: MadLib
Name: Danny Dunn


'''


print "This is my MadLib Assignment by Danny Dunn"

# First Question

first_place = raw_input(" Enter A Place ")

# Second Question

second_place = raw_input(" Enter Another Place ")

# Third Question

third_place = raw_input(" Enter A Place You Never Been ")

# First Number

first_number = raw_input(" Enter A Number Between 1 and 5 ")

# Second Number

second_number = raw_input(" Enter Another Number Between 1 and 5 ")

# Third Number

third_number = raw_input(" Enter A Different Number ")




# my array of friends

friends = ["Reed", "Izzy", "Chandra"]

#----------------------------------------------------------------------------


# Create Dictionary object

dog_toys = dict()
dog_toys = {"Walmart":"Chew Toy", "Petsmart":"Obedience School"}

#-----------------------------------------------------------------------------



#------------------------------------------------------------------------------

# mathematical operators for assignment

weeks = int(first_number) * int(second_number)
food_hours = second_number + third_number
# This is the section for the Story

print " Going Out "

print "Today I was thinking about taking my dog out for a walk."
print "Should I take my dog to the", first_place ,"?"
print "Do you think he would have a better time at the", second_place, "?"
print "I have not taken Archie out in " + str(weeks) + " days."
print "He may want to eat because he has not eaten in " + str(food_hours) + " hours."
print "OH NO! Archie ran by the street. Get back here!"

# adding my for loop
i = 0
for i in range(1,4):
    print i, "!"
    i = i + 1

print "That's a bad dog!, Oh I can't stay mad at you."
print "Well, my mind has been made up I will take him to the" ,third_place , "and see what happens there."
print "I wonder what the weather is going to be like? Hmm... Looks like I will"
# Conditional Statement for weather ---------------------------------------
weather = "sunny"

if weather == "sunny":
    print "go to the" , third_place,"."
elif weather != "sunny":
    print "go to the" , second_place, "."
else:
    print "go home"

print "After the long and treacherous trip to", third_place , "my dog and I were ecstatic that we made the trip."
print "I thought after the trip Archie was good we could go to Walmart and get a"

good_dog = dog_toys["Walmart"]
bad_dog = dog_toys["Petsmart"]

behavior = "good"

if behavior == "good":
    print good_dog,"."
else:
    print bad_dog,"."
    pass

print "We didn't realize that " + friends[0] + "," + friends[1] + ", and " + friends[2] + " Like to go to the", second_place, " too."
