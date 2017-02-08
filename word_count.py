#using dict to determine word count 
def word_frequency(string):
	
    word_dict = {}

    string = string.split(" ")

    for x in string:
        if x in word_dict:
            word_dict[x] += 1
        else:
            word_dict[x] = 1

    return word_dict


print(word_frequency("// hello this is a multiline "))
