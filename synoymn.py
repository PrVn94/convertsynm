
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data
from nltk.corpus import stopwords


# Load a text file if required
import sys,json

def read_in():
    
    lines = sys.stdin.readlines()
    
    #lines ='ratrace'
    #Since our input would only be having one line, parse our JSON data from that



    return json.loads(lines[0])
    #return lines



#text_pre= "Abstract: The flow problem presented in the paper is boundary-layer flow of nanofluids over a moving surface in the presence of thermal radiation, viscous dissipation and chemical reaction. The plate is assumed to move in the same or opposite direction to the free stream which depends on the sign of the velocity parameter. The partial differential equations appearing in the governing equations are transformed into a couple of nonlinear ordinary differential equations using similarity transformations. The transformed equations in turn are solved numerically by the shooting method along with the fourth order RungeKutta integration technique. Influences of the pertinent parameters in the flow field are exhaustively studied and sequentially explained graphically and in tabular form. For selected values of the parameters involved in the governing equations like Lewis number, the velocity parameter, magnetic parameter, Eckert number Brownian motion parameter, thermophoresis parameter, thermal radiation parameter, Prandtl number, Reynolds number and chemical reaction parameter, numerical results for the velocity field, temperature distribution, concentration, skin friction coefficient, Nusselt number and Sherwood number are obtained. The results are analyzed and compared with previously published works; they are found in excellent agreement. Keywords: Boundary-layer flow, Heat transfer, Mass transfer, Stretching sheet, Nanofluids, Viscous dissipation, Chemical reaction MSC 2010: 76M20, 76N20, 76W05, 80A20, 35Q35 "#text=correct_verb(text_pre)

def main():

    lines = sys.stdin.readlines()


    t = lines[0] 
    

    text_pre=  t

   
   
    



    #text_pre= "Abstract: The flow problem presented in the paper is boundary-layer flow of nanofluids over a moving surface in the presence of thermal radiation, viscous dissipation and"
    text =  text_pre 
   # text = correct_verb(text_pre)
    output = ""



    # Load the pretrained neural net
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Tokenize the text
    tokenized = tokenizer.tokenize(text)

    # Get the list of words from the entire text
    words = word_tokenize(text)

    # Identify the parts of speech
    tagged = nltk.pos_tag(words)
    
    


    for i in range(0,len(words)):
        replacements = []

        # Only replace nouns with nouns, vowels with vowels etc.
        for syn in wordnet.synsets(words[i]):

            # Do not attempt to replace proper nouns or determiners
            if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT':
                break
            
            # The tokenizer returns strings like NNP, VBP etc
            # but the wordnet synonyms has tags like .n.
            # So we extract the first character from NNP ie n
            # then we check if the dictionary word has a .n. or not 
            word_type = tagged[i][1][0].lower()
            if syn.name().find("."+word_type+"."):
                # extract the word only
                r = syn.name()[0:syn.name().find(".")]
                replacements.append(r)

        if len(replacements) > 0:
            # Choose a random replacement
            replacement = replacements[randint(0,len(replacements)-1)]
            output = output + " " + replacement
        else:
            # If no replacement could be found, then just use the
            # original word
            output = output + " " + words[i]
    

    

    print( output )


    

def correct_verb(example_sent):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(example_sent)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
     


    r = ' '.join(word for word in filtered_sentence)


    

    return r


if __name__ == '__main__':
    main()