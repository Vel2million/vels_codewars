import string


def get_alphabet_list():
    return list(map(lambda x, y: {'index': x, 'char': y}, range(1, 27) ,string.ascii_lowercase[0:]))
 

def caesar_encode(phrase, shift):
    alphabets = [c.lower() for c in phrase]
    references = get_alphabet_list()
    shit = ""
    print(references)
    for c in alphabets:
        if not c == " ":
            for albt_dict in references:
                if c == albt_dict['char']:
                    print(c, albt_dict['index'], albt_dict['char'])
                    c_index = albt_dict['index']
                    c_index = c_index + shift
                    while c_index > 26:
                        c_index = c_index - 26
                    for abd in references:
                        if c_index == abd['index']:
                            shit += abd['char']
        else:
            shit += " "
    
    print(shit)


if __name__=="__main__":
    caesar_encode('alea iacta est', 3)
