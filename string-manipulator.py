try:
    #taking inputs
    original_sentence = input("enter your sentence: ")

    if not original_sentence:
        raise ValueError("cannot have empty string")
    
    print("Results:")
    #original sentence
    print(f"original sentence : {original_sentence}")

    #total characters(with spaces)
    print(f"total characters(with spaces) : {len(original_sentence)}")

    #total characters(without spaces)
    print(f"total characters(without spaces) : {len(original_sentence.replace(' ',''))}")

    #total words
    print(f"total words : {len(original_sentence.split())}")

    #uppercase
    print(f"upper case : {original_sentence.upper()}")

    #lowercase
    print(f"lower case : {original_sentence.lower()}")

    #titlecase
    print(f"title case: {original_sentence.title()}")

    #first word
    print(f"first word: {original_sentence.split()[0]}")

    #last word
    print(f"last word : {original_sentence.split()[-1]}")

    #reversed sentence
    print(f"reversed sentence : {original_sentence[::-1]}")

#exception handling
except ValueError as ve:
    print("error: ",ve)

except Exception as e:
    print("error: ",e)


