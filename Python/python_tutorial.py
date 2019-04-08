#
# Python:    3.7.3
#
# Author:    Blake Schuchart
#
# Purpose:   The Tach Academy - Python Course, Creating our first program together.
#            Demonstrating how to pass variables from function to function
#            while producing a functional game.
#
#            Remember, function_name(variable) _means that we pass in the variable.
#            return variable _means that we are returning the variable
#            back to the calling functions




def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)


def get_info(f_name,l_name,age,gender):
    name = input("My name is {} {}. I am a {} yearold {}.".format(f_name,l_name,age,gender))









if __name__ == "__main__":
    start()
