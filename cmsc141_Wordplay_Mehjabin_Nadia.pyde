#Nadia Mehjabin <nm6088@bard.edu>
# Oct 14 2021
# CMSC 141
# Word Play 

# Part 1 : Madlibs

    #noun = open("nouns.txt" , "r")
    #data1 = noun.read().split()

    #adj = open("adjectives.txt" , "r")
    #data2 = adj.read().split()


    #def randomPhrase():
        #from random import choice
        #for x in range(100):
            #data1_new = choice(data1)
            #data2_new = choice(data2)
        
            #print(data1_new + " " + data2_new)
    #randomPhrase()"
    
# Part 2: Spelling Bee

'''
-----------
ALGORITHM:
-----------
Loading the given file and saving it as a list in "all_words"
Initialize an empty list, called answer_list, which will contain all the 
valid words.
for each word, "w" in "all_words" list, we are going to check some codintions:
    1. the word, w, must have the "centerletter"
    2. the len of w must be more than 3 
    3. the other characters of "w" must be contained in the "otherLetters"
    if all three above conditions are true we consider w to be a valid word
    and add it to our answer list
we then return the answer_list as list of valid words.

Next, we use the answer_list to compute the final score.

Computing score:
    Initialize score = length of answer_list, since number of valid answers give 1 point
    Next we iterate through every word in the answer_list and check if it has all 7 letters
    if so we add +3 to the score.
    
One important thing to note regarding scoring: The way I am scoring here it means that if
a word uses all 7 characters/letters, we give 4 points for that word (1 for being correct word 
                                                                      and 3 for using all 7 characters)
'''

global all_words                            


def spellingBee (centerLetter,otherLetters):
    '''
    This function takes a character and a string and returns
    a list of valid words that can be spelled using the center letter 
    and the otherletters. It must contain the centerLetter.
    '''
    answer_list = []
    for w in all_words:
        if centerLetter in w:
            if len(w) > 3 :
                # we use this boolean flag to check if all 
                # characters of w are in otherLetters. By default, 
                # it is true, that means we assume at the beginning of every word,w,
                # we consider all letters of w are present in otherLetters. But by
                # going throug every letter (using the loop) we check if any of the
                # letter is not present in otherLetters. If so, then that means w contains
                # a letter that is not allowed and hence we can not allow this w and set 
                # all_good to be False. 
                All_good = True  
                for letter in w:
                    if letter == centerLetter :
                        continue
                    if letter not in otherLetters:
                        All_good = False
                        break
                # all_good is still True -> it means that we did 
                # not find any faulty letters in w. So we accept this 
                # word w and append/add it to our answer_list
                if All_good == True :
                    answer_list.append (w)
    return answer_list
              
def computeScores(answers, centerLetter, otherLetters):
    '''
    For each valid word that in "answers" list, we will score 1 point for each 
    word. 
    In addition, as it says if there are any words that contains all 7 
    letters which is here "L", centerLetter and otherLetters. 
    Now we will assume all 7 letters are present, making the boolean True. 
    Then we will check every character "c" in the list of words. 
    If all characters "c" are not in "L" make the boolean
    False and execute from the loop. if it's present then score 3 points for those words
    that have "L".
    '''
    score = len(answers)
    L = centerLetter + otherLetters
    for word in answers :
        
        all_present = True
        for c in word:
            if c not in L:
                all_present = False
                break
        
        if all_present == True:
            print (word, L)
            score = score +2
    return score                
                                              

def showResults(answers, score):
    '''
    This function takes the list of answers and a score as paramter
    and shows them to the user. It does not return anything
    '''
    # These two lists keep track of the random x and y coordinate 
    # we will use to display the words
    x_coordinates = []
    y_coordinates = []
    
    # for every word, generate a random x, y coordinate 
    # and store the coordinates in 2 sperate lists!
    for index,word in enumerate(answers):
        fill(0, 0, 0)
        textSize(13)
        x_coordinates.append(random(index+2, width-100))
        y_coordinates.append(random(index+2, height-100))
        
      # use the randomly generated x and y coordinate for each word
    # to display the text  
        
        x = x_coordinates[index]
        y = y_coordinates[index]
        text(word, x, y)

        
    # Show the score in the bottom middle
    fill(255, 102, 102)
    textSize(32)
    score_text = 'Score:'+str(score)
    text(score_text, width/2 - 100, height-50)
    
    # Show the number of word found text in the bottom
    textSize(28)
    fill(0,0,0)
    total_answered_txt = 'Number of words spelled:' + str(len(answers))
    text(total_answered_txt, width/2 - 100, height-20)
                                                      
def setup():
    size(800, 600)
    background(255, 204, 0)
    f = open("words.txt", "r")
    data = f. read()
    global all_words 
    all_words = data.split()
    
    answers= spellingBee ("n","ceiprx")
    score = computeScores(answers,"n","ceiprx")
    
    print ("score" , score)
    print (answers)
    print (len(answers))
    
    showResults(answers, score)
    
