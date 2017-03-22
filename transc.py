import re
#open the three files that we'll need. Cleaninf is the file that we'll write to.
with open('infinitivesbreakout')  as ibr, open('infinitives') as inf, open('cleaninf', 'w') as clinf:
    #create an empty dictionary that we'll fill with the symbols as keys and the farsi letters as values
    letdic = {}
    #create a list of the short vowels. We need this since when they appear as first letters they need to be transformed to aleph
    shortvowels = ['æ', 'e', 'o']
    #iterate through the breakout file, turn each line into a list of characters and add the symbols and persian letters as keys and values respectively.
    #the keys are 2 positions from the end because there is a newline character at the end
    for line in ibr:
        lets = list(line)
        #there are several other ways of adding keys/values to a dic
        letdic[lets[0]] = lets[-2]
    #now we'll iterate through the messy pasted pdf and select only the bracketed material
    for line in inf:
        #this is from the 'regular expression' module, which we imported in the first line. The following line returns a list of any series of characters which
        #match what we put before the comma (i.e. [anything at all]
        reline = re.findall(r"\[\w+]", line)
        #now we'll iterate through the list of words that re gave us, since there are many lines that have more than one word. If there is only one,
        #it doesn't cause a problem. In python a list can have 1 or even 0 elements.
        for word in reline:
            #here we filter out more unwanted words. The shortes infinitive is 3 letters so with the brackets that's 5, so we only want words
            #that are longer than 4. We also only want words that end in n and have a second to last letter of d or t. Notice the index we used:
            #the last letter was -2 because the bracket is -1 and the t or d is -4 because the æ is still in there.
            if len(word) > 4 and word[-2] == 'n' and (word[-4] == 't' or word[-4] == 'd'):
                #now we slice off the brackets and turn it into a list and name it wordcut, in one line
                wordcut = list(word[1:-1])
                #we create another variable that is just the first letter. Since some first letters are alephs carrying a short vowel, we have to
                #treat them differently
                firstlet = wordcut[0]
                #now we create a variable that is the remainder of wordcut, that is, everything but the first (zeroth) letter
                wordcutr = wordcut[1:] 
                #make an empty list that we'll append the "clean" letters into.
                finalwordl = []
                #now tricky part. For the majority of letters we just want the code to look up the letter in the dic we made, which
                #is basically the same as the breakout table you created. First we have to deal with the first letters, in case they're short vowels, or alephs w/hat
                #ɒ is a long "a" sound, which of course at the beginning of a word is آ
                if firstlet == 'ɒ':
                    finalwordl.append('آ')
                #next we check if it's one of the 3 short vowels. We could have written a separate conditional (the if clause) for each, but this is saves us lines.
                #notice that we're not replacing the "word" in reline, we're just adding characters to a new list based on what characters are in the word.
                if firstlet in shortvowels:
                    finalwordl.append('ا')
                #now we iterate through the rest of the word. Note that in the letdic ɒ has a value of ا not آ  since it's only used for non-first letters   
                for let in wordcutr:
                    if let in letdic.keys():
                        finalwordl.append(letdic[let])
                #now we turn the final word list back into a string. Notice that I reused, or rather reset, the variable name 'wordcut'. Probably not good
                #practice, but just wanted to show you that it was allowed.
                wordcut = "".join(finalwordl)
                #then write it to a line!
                clinf.write(wordcut + "\n")
                #no need to end the script or anything, it will just loop around (back up to "for word in..." and stop when it's out of words in reline,
                #back up to "for line in inf" until there's no more lines, then it just stops.
                #the cleaninf file should have the correct words, except the wierd ones, which might be quicker to fix by hand.
                
