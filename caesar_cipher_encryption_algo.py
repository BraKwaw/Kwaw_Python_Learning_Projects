"""This program creates an encryption according to the Caeser cypher"""
word=input("what would you like to encrypt? :")                  #requests word to be encrypted
shift_key=int(input("what is your shift_key? :"))               #requests shift-key
new_word=""                                                      #initialize empty string
alphabets="abcdefghijklmnopqrstuvwxyz"
for letter in word:                                             #loops through every letter of the word to be encrypted
    if letter in alphabets:                                       #do this if the letter is in the list of alphabets
        let_pos_alpha=alphabets.index(letter)
        shifting=let_pos_alpha+shift_key
        n_shift = shifting % len(alphabets)                      #do this if the shift exceeds the total range number of alphabets
        yu=alphabets[n_shift]
        a = new_word + str(yu)                                    #adds the shifted letter to empty string
    elif letter.isupper():                                          #do this if the letter is a capital
        let_pos_alpha=alphabets.index(letter.lower())
        shifting=let_pos_alpha+shift_key
        n_shift=shifting % len(alphabets)
        yu=alphabets[n_shift]
        a = new_word + str(yu.upper())
    else:
        a=new_word+letter                                       #do this if it isnt an alphabet
    print(a,end="")
