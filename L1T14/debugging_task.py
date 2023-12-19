# Function to print dictionary values given the keys
def print_values_of(dictionary, key1, key2, key3): # wanted multiple lookups
    for keys in key1,key2,key3: # had to add this to allow it to look with each input
        print(dictionary[keys]) # k is not used, need to use keys 

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": 'd\'oh!',  # only had 1' which ended the comment string too early, added \ to allow python to use the ' within the comment
                         "maggie": "(Pacifier Suck)"
                         }


print_values_of(simpson_catch_phrases, 'lisa','bart','homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''