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

    # difficult to find the total number of unique parties
    # in all our data easily, so instead it makes a lot more
    # sense to create a linked list and just store every party
    # in here as we iterate past it
    possible_parties = DSALinkedList() # empty linked list

    # this iterates through all parties, in all electorates, in all states
    for i in Australia.getStates():
        for j in i.getElectorates():
            for z in j.getParties():
                possible_parties.insertLast(z.getPartyName()) # and inserts the party into the empty linked list

    # now, there's of course going to be double ups, as multiple parties can exist
    # across multiple different electorates/states, so we need the unique set...
    possible_parties = np.array(list(set(possible_parties))) # can't go from set-object to np-array
    # so have to briefly cast to a python inbuilt list - pls don't mark me down, surely this barely counts

    possible_parties = DSASorts().insertionSort(possible_parties) # sort this list using insertion sort
    # because after researching apparently a small array of strings is actually pretty quick to sort
    # using insertion sort, despite it being O(N^2), because len(50) is nothing for a modern CPU I think?

    # anyway, now we have the full list of unique parties in which the user
    # can make their selection, but we need to show them their options!

    # when giving the user 50+ parties to choose from it was a lot of text and
    # it looked really messy in terminal, so I did a bit of googling and found
    # a package called 'textwrap' which makes everything look nice and not
    # half cross over lines - it takes one big long string as input so that's
    # why I've created this:
    long_string = ''

    print("Please select your party (or parties):")
    for i,z in enumerate(possible_parties):
        if z == '':
            z = 'NONE'
        long_string += '['+str(i+1)+']'+z+'  ' # add the option to the long string

    for line in textwrap.wrap(long_string): # use text-wrap to wrap the long string
        print(line) # then print each nice formatted line to the user

    print()

    # now, the user can of course make multiple choices here so an array would
    # be suboptimal, a linked list is a much better way to store the information
    # since it can be appended to depending on the amount of selecitons our user makes
    parties = DSALinkedList() # empty list to hold user selection

    selection = input("Selection: ").split(',')
    if selection[0] in {'a', 'A'}: # if user selects (a/A)ll
        for i in possible_parties: # go through all possible parties
            parties.insertLast(i) # and select everything
    else: # otherwise they must've entered a nice comma seperated list
    # like the documentation says, DEFINITELY WOULDN'T BE ANY PROBLEMS HERE
        selection = [int(i) for i in selection] # so we convert their selctions from
        # strings to integer values
        for i in selection: # and then for each selection they've made
            parties.insertLast(possible_parties[i-1]) # we index all possible parties
            # on this selection (i-1 because our selection list starts at 1 not 0), and
            # then we just append their selection to the linked list

    print(parties) # show the user's their selections so they can panic if they misselected
    print()


    print("Please enter your margin:")
    selection = input("Value: ") # agaian, the user will definitely
    # enter a nice value between 0 and 1 which can be converted to a
    # float... right? right?????
    margin = float(selection)
    print(margin) # show user their selected margin
    print()

    # again, we have no idea how many marginal electorates we might find
    # so we need a linked list to store the data
    results = DSALinkedList()

    for i in Australia.getStates(): # for each state
        for j in i.getElectorates(): # for each electorate
            get_votes = DSALinkedList() # create an empty linked list to store the electorate's votes
            for k in j.getParties(): # for each party in the electorate
                get_votes.insertLast(k.getVotes()) # append their votes to the electorate specific list
            # then we find the percentage difference that each party has with the most voted party in that electorate
            # here i could have used my own sorting method to sort the linked list and then use the last element
            # as the maximum, but considering it's one small calculation, for readability, to reduce code complexity,
            # and mainly because i really don't want to break my code at this point - i'm just going to leave it like this
            get_vote_pct = [(abs(l - max(get_votes)) / max(get_votes)) for l in get_votes]
            # now we have the percentage difference between votes, but
            # we have to see if they fall within the user's margin
            marginal_parties = DSALinkedList()
            for x,z in enumerate(get_vote_pct):
                if z == 0.0: # if there's no percentage difference this means this is the maximum voted party
                    marginal_parties.insertLast(x) # so we insert its index into a list because
                    # we're going to assume that we'll find a marginal match to go with it
                elif z != 0.0 and z <= margin: # and if we find a percentage difference within the margin
                    marginal_parties.insertLast(x) # we have a match and add its index to the list too
            if len(marginal_parties) == 1: # but if our list is only of len(1) it means we never
            # actually found a marginal match to go along with the maximum party, so do nothing
                pass
            else: # otherwise we have a >len(1) list, marginal parties, so we need to grab them
                for p in marginal_parties:
                    # but we're only concerned with marginal parties that involve the parties that the
                    # user had previously selected, so for each marginal party, if it's user selected...
                    if j.getParties()[p].getPartyName() in parties:
                        results.insertLast(j.getParties()[p]) # ... add it to the results list

    # now we send all the necessary information in a nice neat package to be processed into
    # a menu where the user can choose to save this information as either printable output, 
    # a csv file, a serialized file, or any combination of these actions
    pp2 = ResultsProcessing() # initiate our results processing class
    pp2.marginalResultsMenu(Australia, parties, margin, results) # send data off to be processed into a menu

    # and once they exit out of the menu they'll return back here, a blank line will be printed
    # and they'll be sent back to the main menu to perform another process if they decide to
    print()
