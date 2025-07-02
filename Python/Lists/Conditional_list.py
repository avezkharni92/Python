my_list = 'Hello brother'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

new_list = [i for i in my_list if is_consonant(i)]
print(new_list)