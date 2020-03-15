#SPER Set 1 Homework
#By Nathan Ngo

#1: Write a program that prints your name and address. Each line of the address will be printed on a separate line.

    print('15550 Harbor Way')
    print('San Leandro, CA 94579-2776')

#2: Ask the user what their favorite place is. Once the user enters their favorite place, the computer should print:

##{favorite place} is a great place. I also want to go to {favorite place}.

##Obviously, {favorite place} will be replaced by the actual name of the place.

    print("What is your favorite place?")
    place = input()
    print(place, "is a great place. I also want to go to", place, ".")

#3: Write a program that will ask the user the following questions:

##What is your name?

##What is your age?

##What is your phone number?

##Once you have this information from the user, the program needs to print output in this format:

##Great to know you, Joe. You seem to be very smart for a 10-year-old. Thanks for sharing your phone number 8889990000. Will stay in touch.

    print("Hello! What is your name?")
    name = input()
    print("What is your age?")
    age = input()
    print("What is your phone number?")
    number = input()
    print("Great to know you," , name, ". You seem to be very smart for a", age , "year-old. Thanks for sharing your phone number", number , ". Will stay in touch.")

#4: Write down the output for the following statements in the Python shell:

3==4 - False
3!=2 - True
3==2 - False
'Bob'=='Bob' - True
"Bob"=='Bob' - True
Bob='Bob' - False
10+2==6+6 - True

A=10
B=10
A==B - True
A!=B - False

    ##15%3 - 0
    ##17%3 - 2
    ##1122>1121 - True
    ##1122>1124 - False
    ##1122>1122 - False
    ##1122>=1122 - True
    ##1122<1122 - False
    ##1122<=1122 - True
    ##1111=="1111" - False
    ##'111222'=111222 - False
    ##type(111222) - <class 'int'>
    ##type('111222') - <class 'str'>
    ##len('111222') - 6
    ##len('Vishal') - 6

#5: Write a program asking the school administrator the following questions.

##Approximately how many students are there in each grade?

##How many grades are going for the field trip?

##What is the maximum capacity of each bus?

##After the program has the above information, the program should write how many buses are needed. Output should be in this format:

##A total of 100 students will be going for the field trip. 5 buses will be needed.

    print("Approximately how many students are there in each grade?")
    students = input()
    print("How many grades are going for the field trip?")
    grades = input()
    print("What is the maximum capacity of each bus?")
    capacity = input()
    totalstudents = students * grades
    busesneededexactly = totalstudents / capacity
    busesneededestimate = totalstudents // capacity
    if busesneededexactly > busesneededestimate:
        busesneededestimate = busesneededestimate+1
        print("A total of", totalstudents , "will be going for the fieldtrip.", busesneededestimate , "buses will be needed.")
    else:
        print("A total of", totalstudents , "will be going for the fieldtrip.", busesneededestimate , "buses will be needed.")

#6: Ask the user if they like music. If they like music, ask them what kind of instrument they prefer. If they don't like music, ask what do they listen to when they are travelling in a car.

##The program should share output in this format:

##Name: Joe Johnson

##Likes Music: Yes

##Instrument Preference: Guitar

##or

##Name: Joe Johnson

##Likes Music: No

##Activity During Travelling: Listening to Audio Books
    print("What's your name?")
    name = input()
    print("Do you like music? Type Y or y for Yes and N or n for No.")
    musicchoice = input()
    if musicchoice == "y" or musicchoice == "Y":
        musicchoice = "Yes"
        print("Ooh! What insturment do you like!?")
        insturmentchoice = input()
        print("Name:", Name,
              "Likes Music:", musicchoice,
              "Instrument Preference:", insturmentchoice)
    elif musicchoice = "N" or musicchoice = "n":
        musicchoice == "No"
        musicchoice = "Yes"
        print("Oh!? Ok. Uhh, what do you like to do when travelling?")
        activitychoice = input()
        print("Name:", Name,
              "Likes Music:", musicchoice,
              "Activity Preference:", activitychoice)
    else:
        print("That's not a choice! >:( Try again!")

#7: Write a program asking the user his or her name. After that, ask if they like soccer or football. If they answer soccer, ask if they like Lionel Messi and if they answer football, ask if they like Tom Brady.

##Once the users enters the above information, the program should share output in the following format:

##Name: Joe Johnson

##Likes: Football

##Likes Tom Brady: Yes

    print("What's your name?")
    name = input()
    print("Do you like soccer or football? S for soccer and f for football!")
    choice = input()
    if choice == "S" or choice == "s":
        choice = "Soccer"
        print("Ooh! Do you like Lionel Messi? Yes or no?")
        soccerlike = input()
        if soccerlike == "Yes" or soccerlike == "yes":
            soccerlike = "Yes"
            print("Cool!")
            print("Name:", name,
                  "Choice:", choice,
                  "Likes Lionel Messi:", soccerlike)
        elif soccerlike == "No" or soccerlike == "no":
            soccerlike = "No"
            print("I agree.")
            print("Name:", name,
                  "Choice:", choice,
                  "Likes Lionel Messi:", soccerlike)
        else:
            print("Um, that's not a choice! Try again!")
    elif choice == "F" or choice == "f"
        choice == "Football"
        print("Hmmm...Just asking. Do you like Tom Brady?")
        footballlike = input()
        if footballlike == "Yes" or footballlike == "yes":
            footballlike = "Yes"
            print("Very nice!")
            print("Name:", name,
                  "Choice:", choice,
                  "Likes Tom Brady:", footballlike)
        elif footballlike == "No" or footballlike == "no":
            footballlike == "No"
            print("Excellent!")
            print("Name:", name,
                  "Choice:", choice,
                  "Likes Tom Brady:", footballlike)

#8: The Jones family is going on a road trip. It's a large family of 17 people. They have 3 cars. Each car can carry maximum 5 people. How many members will need to take a bus?

    import time
    print("The Jones family is going on a road trip. It's a large family of 17 people. They have 3 cars. Each car can carry maximum 5 people. How many members will need to take a bus?")
    time.sleep(3)
    print("Let me think.")
    JonesFamily == int(17)
    JonesFamilyRemainder == JonesFamily//3
    print(JonesFamilyRemainder, "people would need to take the bus.")

#9: Ask the user what state they live in.

##If the user's answer is California, the program should share the following output:

##California has great weather.

##If the user's answer is Arizona, the program should share this as output:

##Arizona must be hot.

##If the user's answer is Washington, the program should share this output:

##Washington gets a lot of rain.

##If the user's answer is any other state, the program should have this as the output:

##How is the weather in your state

##and then the program should print the output in the following format:

##Thank you for teaching me that Florida has stormy weather.

    print("What state do you live in?")
    state = input()
    if state == "California" or state == "california":
        print("California has great weather.")
    elif state == "Arizona" or state == "arizona":
        print("Arizona must be hot.")
    elif state == "Washington" or state == "washington":
        print("Washington gets a lot of rain.")
    else:
        print("Hmm. How is the weather in your state?")
        stateweather = input()
        print("Thank you for teaching me that", state , "has", stateweather , ".")
