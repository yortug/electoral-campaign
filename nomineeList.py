import sys
sys.path.append("./data_structures/")
from linkedLists import *
from DSASorts import *

from Processing import *
from Region import *

import numpy as np
import textwrap

# I've wrapped all processing for this part of the assignment
# in this 'main' function, so it can be called from the main menu

## THIS FILE WILL NOT HAVE COMMENTS ## why??
# because it's word for word, exactly the same code
# as what's being executed in the nomineeSearch.py file (except
# nomineeSearch.py has an extra few lines at the end), it makes
# sense that i'd leave this without comments as you can just
# follow along in the other file - as it's literally the same thing

# I know I probably should have refactored it, or packaged it up into
# a class and used it in one place for both questions, but I like the idea
# of having a python file for each question/part of the assignment, and it's
# a bit too late for me to change now without breaking things probably

# anyway, head over to "nomineeSearch.py" for the commentary of this file 
def main():
    pp = Processing()


    the_data = pp.unserialize('australia.pickle')

    Australia = Country('Australia', len(the_data))
    Australia.setStates(the_data)

    states = DSALinkedList()
    divisions = DSALinkedList()
    parties = DSALinkedList()

    print("Please select your state(s):")
    for i,z in enumerate(Australia.getStates()):
        print('['+str(i+1)+']'+z.getCode()+'  ', end = '  ')

    print()
    selection1 = input("Selection: ").split(',')
    if selection1[0] in {'a', 'A'}:
        for i in Australia.getStates():
            states.insertLast(i.getCode())
    else:
        selection1 = [int(i) for i in selection1]
        for i in selection1:
            states.insertLast(Australia.getStates()[i-1].getCode())



    print()
    print(states)

    for i in states:
        test = ''
        print()
        print("Please select electorate(s) from " + i + ':')
        for j,z in enumerate(Australia.findState(i).getElectorates()):
            test += '['+str(j+1)+']'+z.getDivName()+'  '
        for line in textwrap.wrap(test):
            print(line)
        selection2 = input("Selection: ").split(',')
        if selection2[0] in {'a', 'A'}:
            for k in Australia.findState(i).getElectorates():
                divisions.insertLast(k.getDivName())
        else:
            selection2 = [int(i) for i in selection2]
            for k in selection2:
                divisions.insertLast(Australia.findState(i).getElectorates()[k-1].getDivName())
        print()
        print(divisions)

    print()



    possible_parties = DSALinkedList()

    for i in states:
        x = Australia.findState(i)
        if x != None:
            for j in divisions:
                y = x.findElectorate(j)
                if y != None:
                    for k in y.getParties():
                        possible_parties.insertLast(k.getPartyName())

    possible_parties = np.array(list(set(possible_parties))) # can't go from set-object to np-array, so have to briefly cast to Python list
    possible_parties = DSASorts().insertionSort(possible_parties)

    print("Please select your partie(s):")
    test = ''
    for i,z in enumerate(possible_parties):
        if z == '':
            z = 'NONE'
        test += '['+str(i+1)+']'+z+'  '
    for line in textwrap.wrap(test):
        print(line)

    print()


    selection3 = input("Selection: ").split(',')
    if selection3[0] in {'a', 'A'}:
        for i in possible_parties:
            parties.insertLast(i)
    else:
        selection3 = [int(i) for i in selection3]
        for i in selection3:
            parties.insertLast(possible_parties[i-1])
        
    print()
    print(parties)
    print()
    print('=================================')
    print()

    parties_array = np.empty(len(parties), dtype = object)
    for i,z in enumerate(parties):
        parties_array[i] = z

    parties = DSASorts().insertionSort(parties_array)

    results = DSALinkedList()

    for i in states:
        x = Australia.findState(i)
        if x != None:
            for j in divisions:
                y = x.findElectorate(j)
                if y != None:
                    for k in parties:
                        z = y.findParty(k)
                        if z != None:
                            for candidate in z.getCandidates():
                                results.insertLast(candidate)

    pp2 = ResultsProcessing()
    pp2.resultsMenu(results)

    # and once they exit out of the menu they'll return back here, a blank line will be printed
    # and they'll be sent back to the main menu to perform another process if they decide to
    print()


