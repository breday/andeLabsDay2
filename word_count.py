#using dict to determine word count 
def word_frequency(string):
	#create dictonary to store results
    word_dict = {}

#code split the string 
    string = string.split(" ")
 
    for x in string:#iterate through each value in list
        if x in word_dict:
            word_dict[x] += 1 #if value more than one, add one
        else:
            word_dict[x] = 1

    return word_dict


print(word_frequency("1 2 1 2 testing 1 2 1 2 testing"))

