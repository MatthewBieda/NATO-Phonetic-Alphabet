#NATO Phonetic Alphabet
def main():

    #Use a dictionary to map to the phonetic alphabet 
    dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

    def translate(userstring):

        userstring_uppercased = userstring.upper()

        phonetic = []
        for w in userstring_uppercased:
            if w.isalpha():
                phonetic += dictionary[w] + ' '
            elif w != ' ':
                phonetic += w

        return ''.join(phonetic)


    with open("text.txt", "r") as f:
        userstring = f.read()
        x = translate(userstring)
        with open("text.txt", "w") as f:
            f.write(x)
        with open("logging.txt", "w") as f:
            x_list = x.split()
            number_of_words = len(x_list)

            userstring_list = userstring.split()
            number_of_user_words = len(userstring_list)
            f.write(f"Number of words supplied: {number_of_user_words}\nNumber of phonetic words outputted: {number_of_words}")

            
if __name__ == "__main__":
    main()