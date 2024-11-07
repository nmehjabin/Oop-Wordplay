# Oop-Wordplay

This simple game explores string processing and file input.<br/>

#Part 1: Madlibs

Need two files `nouns.txt` and `adjectives.txt`, function `randomPhrase()` that constructs and returns a random sentence when called. For example, in class we thought about using alliteration to create names for bands (e.g., left-wing lampshades). But you could also do something like the love letter generator, or some other mad-libs style fill-in-the-blank sentences. Write a small creative setup/draw to exercise that function. Consider using the `choice` function from the `random` module (`from random import choice`). Explain your algorithm as a comment.




#Part 2: Spelling Bee
There's a function `spellingBee(centerLetter, otherLetters)` that solves NYT’s Spelling Bee puzzles. For example, `spellingBee(``'``n``'``,` `'``ceiprx``'``)` should solve the puzzle to the right. The standard dictionary `words.txt` is where to check meaningful words from.

Goal: to print out all of the solution words and calculate and return the total score.

