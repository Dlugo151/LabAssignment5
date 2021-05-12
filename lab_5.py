

"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
then from the text file, we create a list of strings from each lines in the text file.
Then, we create a dictionary form text file.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an
array of string ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

once we have the array of strings representing the user's input sentece, we
loop through each words, find the key marching the word and return back the value tied to that word
in our dictionary.

After each word is translated, we then
Print out the translated sentence to the user.
"""


"""
main():
    set sentence = input()
    set dictionary = translate()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    word = for each of the world in the sentence
    for each words, tranlate the word
    print translated sentence to user

create_dictorionary(infile):
    read in textese.txt
    create list = each line from file
    close the file
    create a dict off of the list
    return the dict

main()
"""

