'''
Напишите функцию которая определит сколько раз встречаеться элемент в списке.
'''

def len_word_in_list(some_list, element = ""):
    print (some_list.count(element))


some_list = [1,5,4,1,2,3,1,2,5,4,1,2,1,2]

len_word_in_list(some_list, 2)
