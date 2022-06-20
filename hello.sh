#!/bin/bash
# declare STRING variable
STRING="Thanks for pooping."
STRING1=" FARTS! "
STRING2="You're welcome."
# print variable on a screen
# echo $STRING$STRING1$STRING2

# in bash, an array is a list of items not separated by commas
myArray=($STRING $STRING1 $STRING2)

# this prints one on each line
for variable in "${myArray[*]}";
    do
        echo $variable
    done

# # see what happens when you use @ to index
# for variable in "${myArray[@]}";
# do
#   echo $variable
# done