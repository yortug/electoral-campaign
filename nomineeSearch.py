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
def main():
    pp = Processing()

    # unserialize our data ready for use
    the_data = pp.unserialize('australia.pickle')

    # create the Australia Country object to improve readability as we go through
    Australia = Country('Australia', len(the_data))
    Australia.setStates(the_data)

    # the user is going to go through three main selection phases:
    #   1. selecting their states of interest
    #   2. selecting their divisions/electorates of interest
    #   3. selecting their party/parties of interest
    # thus, we must create three different linked lists to store
    # this information because we have no way of knowing how many
    # of any of the choices the user might be making - need extensibility
    states = DSALinkedList()
    divisions = DSALinkedList()
    parties = DSALinkedList()

    print("Please select your state(s):")
    for i,z in enumerate(Australia.getStates()): # for each state
        print('['+str(i+1)+']'+z.getCode()+'  ', end = '  ') # print the index+1 (so we start at
        # one and not zero), and print the label next to that number

    print()
    selection1 = input("Selection: ").split(',') # user makes a selection and we split it on ',' because
    # we're assuming they've read the documentation and will of course input a nice comma seperated list
    if selection1[0] in {'a', 'A'}: # check if they've selected all, and if so...
        for i in Australia.getStates(): # for each state
            states.insertLast(i.getCode()) # insert the code (i.e. 'WA') into states list
    else: # otherwise they must've selected some subset of them all
        selection1 = [int(i) for i in selection1] 
        for i in selection1: # so for each of their selection(s)
            states.insertLast(Australia.getStates()[i-1].getCode()) # insert the code on the selection-1

    print()
    print(states) # show users the states they've selected to reassure them

    # now that we have the user's selected states, we can reduce the search space
    # and have them select which electorates they're interested in within each
    # of their selected states

    for state in states: # for each state in their selected states
        big_string = '' # sometimes there're A LOT of electorates (like for NSW/VIC)
        # so I've made use of a package called 'textwrap' which makes sure that when
        # there's a huge set of text in the terminal, it's formatted correctly and
        # not half on the end of one line and the start of the next - it takes one big
        # string as input, hence why I've made this here
        print()
        print("Please select electorate(s) from " + state + ':')
        for j,z in enumerate(Australia.findState(state).getElectorates()): # for electorate in the selected state
            big_string += '['+str(j+1)+']'+z.getDivName()+'  ' # append this to the big string
        for line in textwrap.wrap(big_string): # for each correctly formatted line in this big string
            print(line) # print the line
        selection2 = input("Selection: ").split(',') # user makes a selection and we split it on ',' because
        # we're assuming they've read the documentation and will of course input a nice comma seperated list
        if selection2[0] in {'a', 'A'}: # check if they've selected all, and if so...
            for k in Australia.findState(state).getElectorates(): # for each of the state's electorates
                divisions.insertLast(k.getDivName()) # insert their name to the divisions list
        else: # otherwise they must've selected some subset of them all
            selection2 = [int(i) for i in selection2]
            for k in selection2: # so for each of their selection(s)
                divisions.insertLast(Australia.findState(state).getElectorates()[k-1].getDivName()) # insert that electorate to list
        print()
        print(divisions) # show users the divisions they've selected to reassure them

    print()

    # now, at this point we've reduced the search space significantly again, considering
    # we might even be looking in a couple of one state's electorates, there might only be
    # a few parties to choose from; so we have to find what these possible parties are
    # that our user can choose from

    possible_parties = DSALinkedList() # empty list again because extensibility 

    for i in states: # for each of the user's states
        x = Australia.findState(i) # set x to be that state object
        if x != None: # saftey check
            for j in divisions: # for each of the users divisions
                y = x.findElectorate(j) # check if it's within this state
                if y != None: # if it IS in this state (not None)
                    for k in y.getParties(): # then for each party in this division
                        possible_parties.insertLast(k.getPartyName()) # add them to the list of possible parties

    possible_parties = np.array(list(set(possible_parties))) # can't go from set-object to np-array
    # so have to briefly cast to a python inbuilt list - pls don't mark me down, surely this barely counts
    possible_parties = DSASorts().insertionSort(possible_parties) # sort this list using insertion sort
    # because after researching apparently a small array of strings is actually pretty quick to sort
    # using insertion sort, despite it being O(N^2), because len(50) is nothing for a modern CPU I think?

    # anyway, now we have the set of possible parties in which 
    # the user can make a choice, again we use textwrap to format
    print("Please select your partie(s):")
    big_string = ''
    for i,z in enumerate(possible_parties):
        if z == '':
            z = 'NONE'
        big_string += '['+str(i+1)+']'+z+'  '
    for line in textwrap.wrap(big_string):
        print(line) # prints each nicely formated line to shell

    print()


    selection3 = input("Selection: ").split(',') # user makes a selection and we split it on ',' because
    # we're assuming they've read the documentation and will of course input a nice comma seperated list
    if selection3[0] in {'a', 'A'}: # check if they've selected all, and if so...
        for i in possible_parties: # for each of the possible parties
            parties.insertLast(i) # insert the party's name into the selected parties list
    else: # otherwise they must've selected some subset of them all
        selection3 = [int(i) for i in selection3]
        for i in selection3: # so for each of their selection(s)
            parties.insertLast(possible_parties[i-1]) # insert each selected party into the parties list
        
    print()
    print(parties) # show users the party/parties they've selected to reassure them
    print()
    print('=================================')
    print()

    # put the parties into an array so we can sort them efficiently
    parties_array = np.empty(len(parties), dtype = object)
    for i,z in enumerate(parties):
        parties_array[i] = z
    parties = DSASorts().insertionSort(parties_array) # sort them

    filtered = DSALinkedList() # empty linked list to store the filtered candidates we'll
    # be searching through; if you've come from "nomineeList.py" this would be the results
    # of all your filtering - your results - and they're sent to into a menu in processing classs

    for i in states: # for each state the user selected
        x = Australia.findState(i) # set it to current
        if x != None: # saftey check
            for j in divisions: # for each division selected by the user
                y = x.findElectorate(j) # try and find it within current state
                if y != None: # if it IS found (not None)
                    for k in parties: # for each party selected by the user
                        z = y.findParty(k) # try find the party within the electorate
                        if z != None: # if you DO find the party
                            for candidate in z.getCandidates(): # look at each candidate in the party
                                filtered.insertLast(candidate) # and add them to our filtered list

    results = DSALinkedList() # empty list for our results

    # finally, we have to let the user input some sort of substring
    # and if it matches some part of the filtered candidates first name
    # or last name, then they need to be added to the results for processing
    ## NOTE: I interpretted this question "searching for a substring, starting
    # with the first character of last name" as:
    #   1. user enters substring
    #   2. you check if substring matches the last_name[0:len(substring)]
    #   3. if it doesn't then you check last_name[1:len(substring)], then last_name[2:len(substring)], etc
    #   4. if this yields no results then repeat process with first name
    #
    # this whole process is simply the 'in' keyword function in python so i've used that

    print("Who are you looking for: ")
    selection4 = input("Selection: ")
    for i in filtered: # for each candidate we've filtered down
        if selection4.lower() in i.getFname().lower() or selection4.lower() in i.getLname().lower(): # if substring is in f/lname
            results.insertLast(i) # add it to the results list

    # now we send all the necessary information in a nice neat package to be processed into
    # a menu where the user can choose to save this information as either printable output, 
    # a csv file, a serialized file, or any combination of these actions

    pp2 = ResultsProcessing() # initiate our results processing class
    pp2.resultsMenu(results) # send data off to be processed into a menu

    # and once they exit out of the menu they'll return back here, a blank line will be printed
    # and they'll be sent back to the main menu to perform another process if they decide to
    print()

