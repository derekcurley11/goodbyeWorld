#!/bin/bash

# run the script in the terminal by typing `bash hello.sh` OR `./hello.sh`

# variable assignment in bash
STRING="Thanks for pooping."
STRING1=" FARTS! "
STRING2="You're welcome."

# print variables to the screen
# in bash, call assigned variables using the $
# echo $STRING$STRING1$STRING2

# in bash, an array is a list of items not separated by commas
myArray=($STRING $STRING1 $STRING2)

# this iterates through the array and prints each string in series
# see if you can find a way to print one per line
for variable in "${myArray[*]}";
    do
        echo $variable
    done

# # see what happens when you use @ to index
# for variable in "${myArray[@]}";
# do
#   echo $variable
# done