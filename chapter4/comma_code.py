spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = []
spam3 = [42, 123, 'pineapple', 'op']

def listItem(list):
    l = ''
    for index, item in enumerate(list):
        l += str(item)
        if (index < len(list)-2):
            l += ', '
        elif (index == len(list)-2):
            l += ', and '

    return l

print(listItem(spam))
