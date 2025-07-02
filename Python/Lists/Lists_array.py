#conditional list comprehention

prev_list = [-1, 10, 20, -2, -5, 30, 40]

new_list = [number for number in prev_list if number > 0]

print(new_list)


#Write a program if number if number is less than 0 then print negative number 

new_list1 = ['negative number' if number < 0 else number for number in prev_list ]

print(new_list1)

sentence = "You are gonna do it 5"

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonant = [i for i in sentence if is_consonant(i)]
print(consonant)


