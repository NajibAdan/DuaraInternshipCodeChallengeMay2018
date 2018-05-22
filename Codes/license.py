'''
Duara Internship Code Challenge

Task 1

This program stores and queries a list of license plate number
'''
import random
import re

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'


#stores the number plates to a file
def store():
    with open('license.txt', 'w') as file:
        for x in range(0, 200000):
            license = random.choice(letters) + random.choice(
                letters) + random.choice(letters) + '-' + random.choice(
                    numbers) + random.choice(numbers) + random.choice(numbers)
            file.write(license + '\n')

    query()


def query():
    lst = []  # the list will store  license plates that begin with PLB
    regex1 = 'PLB-123'  # regex pattern to search if a PLB-123 is a member of a set
    regex2 = '^(PLB)'  # regex pattern to search plates that begin with PLB
    file = open('license.txt', 'r')
    for plates in file:
        plates = plates.strip()
        if re.match(regex1, plates):
            print 'license plate PLB-123 a member of the set'
        if re.match(regex2, plates):
            lst.append(plates)
    print 'Number of license plates that begin with PLB: ' + str(len(lst))
    if len(lst) > 0:
        print 'List of license plates that begin with PLB:'
        for x in lst:
            print x


store()
