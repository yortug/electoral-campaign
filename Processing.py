import sys
sys.path.append("./data_structures/")
from linkedLists import *
from DSASorts import *

import numpy as np
import pickle
import time
import textwrap
import copy

class Processing:
    def __init__(self):
        ...

    def readCSV2(self, path, start):
        """
        Reads in a CSV given its relative path and the line where
        reading should begin.
        INPUT:
            path (string) - relative path to .csv file
            start (integer) - line number to start CSV reading (line 1 is first line)
        OUTPUT:
            row_array (object array) - array where each element is a row of csv
        """
        with open(path, 'r') as csvfile:
            lines = csvfile.readlines()
            row_count = len(lines)

            if not start in range(1, row_count):
                raise IndexError('CSV start reading index is out of range nrows.')

            array_length = row_count - start + 1
            row_array = np.empty(array_length, dtype = object)
            
            for i, line in enumerate(lines[(start-1):]):
                row_array[i] = np.array(line.rstrip('\n').split(','))

        return row_array

    def findUnique(self, duplicate_array, col_num):
        """
        Finds the unique set of values across multiple elements
        of an array, given a specific 'column' index
        INPUT:
            duplicate_array (object array) - array where each element
            is an entry read in from a csv
            col_num (integer) - the 'column index' which indicates
            the column within each row which is processed
        OUTPUT:
            a (sorted array) - an array that contains each
            unique value within the selected 'column'
        """
        unique_array = np.empty(len(duplicate_array), dtype = object)

        for i,r in enumerate(duplicate_array):
            unique_array[i] = r[col_num]

        a = np.array(list((set(unique_array)))) # had to use a list here briefly because you can't go directly from a set object to a np array

        return DSASorts().insertionSort(a)

    def getRowsWhere(self, some_array, col_num, to_match):
        """
        Traverses through a specified column of an array, checking
        to see if each element is equal to the matching criteria,
        all matched elements are returned as an array
        INPUT:
            some_array (any array) - target array
            col_num (integer) - targer column index
        OUTPUT:
            matched array (any array) - array of all
            elements which met the match criteria
        """
        temp = DSALinkedList()
        for r in some_array:
            if r[col_num] == to_match:
                temp.insertFirst(r)

        matched_array = np.empty(len(temp), dtype = object)

        for i,v in enumerate(temp):
            matched_array[i] = v

        return matched_array

    def serialize(self, path, obj):
        """
        Creates a binary file of an object and
        dumps it into the current directory
        INPUT:
            path (string) - file name or relative path
            obj (any object) - to be serialized
        OUTPUT:
            
        """
        with open(path, 'wb') as data:
            pickle.dump(obj, data)

    def unserialize(self, path):
        """
        Reads in a binary, previously serialized
        file and returns the object
        INPUT:
            path (string) - file name or relative path
        OUTPUT:
            obj (any object) - object contained in file
        """
        with open(path, 'rb') as picklefile:
            obj = pickle.load(picklefile)

        return obj


class ResultsProcessing:
    def __init__(self):
        ...

    def timer(self, mes=''):
        """
         Displays a timer to user's terminal, not necessary
         but it gives the user a second to process what's
         actually happening i.e. a file is being created
        INPUT:
            mes (string) - a message to be displayed to the user
        OUTPUT:
            
        """
        for i in range(101):
            time.sleep(0.007)
            sys.stdout.write('\t' + str(mes) + "\r%d%%" % i)
            sys.stdout.flush()

        sys.stdout.write('\n')

    def resultsPrint(self):
        """
         Displays the possible options to the user
         regarding the processing of their results
        INPUT:
            
        OUTPUT:
            
        """
        print('What would you like to do with your results?')
        print('  ' + '[1] Print your results')
        print('  ' + '[2] Save your results as CSV')
        print('  ' + '[3] Save your results as serialized file')
        print('  ' + '[q] Quit to main menu')

    def resultsMenu(self, results):
        """
         Actually processes the user's results; print,
         write to csv, write to serialized file or exit
         (used for list & search nominees parts)
        INPUT:
            results (array of Candidate objects)
        OUTPUT:
            
        """
        self.resultsPrint()

        selection4 = input("Selection: ")

        if selection4 == '1':
            for i in results:
                print(i)

            print()
            self.resultsMenu(results)

        elif selection4 == '2':
            name = str(input("File name: "))

            with open(name, 'w') as csvfile:
                csvfile.write('State,Division,Party,Elected,hElected,CandidateID,Surname,Name,Votes\n')
                count = 0
                bottom = len(results)
                for i in results:
                    x = str(i).split(' | ')
                    incount = 0
                    rside = len(x)
                    for j in x:
                        csvfile.write(str(j))
                        if incount != (rside - 1):
                            csvfile.write(',')
                        else:
                            if count != (bottom - 1):
                                csvfile.write('\n')
                            else:
                                pass
                            count += 1
                        incount += 1

            self.timer('writing data to csv: ')
            self.timer('dumping file: ')
            print()
            self.resultsMenu(results)


        elif selection4 == '3':
            name = str(input("File name: "))
            
            with open(name, 'wb') as data:
                pickle.dump(results, data)

            self.timer('serializing data: ')
            self.timer('dumping file: ')
            print()
            self.resultsMenu(results)

        elif selection4 == 'q':
            pass
        else:
            self.resultsMenu(results)

    def printMarginalParties(self, Australia, parties, margin):
        """
         Prints the marginal parties found once the user has
         selected their party of interest and their margin
        INPUT:
            Australia (Country object) - the data to sift through
            parties (obj array) - user's selected parties
            margin (float [0-1]) - user's desired margin
        OUTPUT:
            
        """
        print(Australia)
        print('==================')
        for i in Australia.getStates():
            print(i)
            for j in i.getElectorates():
                get_votes = DSALinkedList()
                for k in j.getParties():
                    get_votes.insertLast(k.getVotes())
                get_vote_pct = [(abs(l - max(get_votes)) / max(get_votes)) for l in get_votes]
                marginal_parties = DSALinkedList()
                for x,z in enumerate(get_vote_pct):
                    if z == 0.0:
                        marginal_parties.insertLast(x)
                    elif z != 0.0 and z <= margin:
                        marginal_parties.insertLast(x)
                if len(marginal_parties) == 1:
                    pass
                else:
                    print('\t', j)
                    for p in marginal_parties:
                        if j.getParties()[p].getPartyName() in parties:
                            print('\t\t', j.getParties()[p])

    def marginalResultsMenu(self, Australia, parties, margin, results):
        """
         Actually processes the user's results for list by margin
         part (question 3 of assignment), its menu required more
         information and different outputs so is handled in a
         different function as a consequence of this
        INPUT:
            Australia (Country object) - the data to sift through
            parties (obj array) - user's selected parties
            margin (float [0-1]) - user's desired margin
            results (array of Candidate objects)
        OUTPUT:
            
        """
        self.resultsPrint()

        print()
        warning_string = "NOTE: When printing the marginal parties, you will always see the states/electorates " \
        + "in which the parties were checked. However, UNLESS the PARTY NAME is shown (will have a vote count next" \
        + " to it) the electorates being shown are NOT marginal!!"
        for line in textwrap.wrap(warning_string):
            print(line)
        print()

        selection5 = input("Selection: ")

        if selection5 == '1':
            self.printMarginalParties(Australia, parties, margin)
            print()
            self.marginalResultsMenu(Australia, parties, margin, results)
        elif selection5 == '2':
            name = str(input("File name: "))

            with open(name, 'w') as csvfile:
                count = 0
                bottom = len(results)
                for i in results:
                    writing = str(i.getCandidates()[0].getState()) + ',' + str(i.getCandidates()[0].getDivision())
                    if count != (bottom - 1):
                        writing += '\n'
                    else:
                        pass
                    csvfile.write(writing)
                    count += 1

            self.timer('writing data to csv: ')
            self.timer('dumping file: ')
            print()
            self.marginalResultsMenu(Australia, parties, margin, results)
        elif selection5 == '3':
            name = str(input("File name: "))
        
            with open(name, 'wb') as data:
                pickle.dump(results, data)

            self.timer('serializing data: ')
            self.timer('dumping file: ')
            print()
            self.marginalResultsMenu(Australia, parties, margin, results)
        elif selection5 == 'q':
            pass
        else:
            self.marginalResultsMenu(Australia, parties, margin, results)

    def marginalCampaignPrint(self):
        """
         Marginal campaign has similar options to all the
         other menus, but it saves the intinerary as a .txt
         and NOT as a .csv, thus the print menu has been
         editted to show that
        INPUT:
            
        OUTPUT:
            
        """
        print('What would you like to do with your results?')
        print('  ' + '[1] Print your results')
        print('  ' + '[2] Save your results as TXT')
        print('  ' + '[3] Save your results as serialized file')
        print('  ' + '[q] Quit to main menu')

    def marginalCampaignMenu(self, q1, q2):
        """
         Processes the user's menu for the itinerary by margin
         part of the assignment (question 4), this processing
         is unique as it depends on two queue data structures
         filled with location/time data, thus its own function
        INPUT:
            q1 (queue) - queue of all the vertices, representing
            the vertices which were visited in the dfs of graph
            q2 (queue) - queue of all the edges, representing the
            edges that connect all the visited verties (from q1)
        OUTPUT:
            
        """
        self.marginalCampaignPrint()

        vertex_queue = copy.deepcopy(q1)
        edge_queue = copy.deepcopy(q2)

        selection6 = input("Selection: ")

        if selection6 == '1':
            # linked list for storing all the meet & greet + travel time values; iterable to find total time
            total_time = DSALinkedList()

            count = 0 # set a counter to 0
            stop = len(vertex_queue) # we stop once we hit the last location
            while not vertex_queue.isEmpty(): # until all the locations have been dealt with
                a_location = vertex_queue.dequeue() # look at location
                print(a_location) # print a location
                count += 1 # add to vertex counter
                total_time.insertLast(a_location[1]) # append location's time (180 mins) to the list
                if count == stop: # if stopping condition is met
                    pass # exit
                else: # otherwise there must be another edge to add
                    an_edge = edge_queue.dequeue() # look at edge
                    print(an_edge) # print the edge
                    total_time.insertLast(an_edge[1]) # append edge's travel time to the list

            print()

            # SOME electorates (Warringah, NSW; Capricornia, QLD; Flinders, VIC; Kennedy, QLD & Mayo, SA)
            # don't actually have values for their edges (blame their Wikipedia coords being in the middle of ocean)...
            # they're still included within the itinerary, but as we have no information for the travel time they
            # of course CAN'T be factored into our total travel time - this means the estimated total travel time
            # will be an UNDERESTIMATE of the true value if a 'NONE' edge exists in the campaign trail

            # set has_none = True if a 'NONE' edge is found
            has_none = False
            for i in total_time:
                if i == 'NONE':
                    has_none = True

            if has_none == True: # if 'NONE' exists
                # warn user of the potential underestimate
                print("travel time doesn't exist for at least one edge")
                print("estimated total travel time is likely slightly underestimating real travel time")
            else: # otherwise NO 'NONE's exist
                # so reassure user the estimate should be somewhat accurate!
                print("no NA's found in any edges")
                print("estimated total travel time should be an decent approximation of real travel time")

            print()

            print("ESTIMATED TOTAL TRAVEL TIME:")
            travel_time = 0 # initiate total travel = 0 minutes
            for i in total_time:
                if i != 'NONE':
                    travel_time += int(i) # add the travel time to the total

            print(travel_time, 'minutes') # minutes
            print(int(travel_time / 60), 'hours', travel_time % 60, 'minutes') # hours, minutes
            print(int(travel_time / 60 / 24), 'days', int(travel_time / 60) % 24, 'hours', travel_time % 60, 'minutes') # days, hour, minutes

            print()
            self.marginalCampaignMenu(q1, q2)
        elif selection6 == '2':
            """
            this code does almost the exact same as the printing code in the
            previous print option, but instead of printing it's writing the
            information to a .txt file that can be saved and taken/sent to
            someone as their actual itinerary - makes more sense with the overall
            problem that we're solving...
            ... this was tedious to setup using all the hashes and whitespaces, etc
            so pls appreciate my pain when you stare at the nice looking itinerary
            """
            name = str(input("File name: "))

            with open(name, 'w') as txt_file:
                # linked list for storing all the meet & greet + travel time values; iterable to find total time
                total_time = DSALinkedList()

                txt_file.write('#' * 80 + '\n')
                txt_file.write('#' + (' ' * 23) + 'MARGINAL CAMPAIGN TRAIL [2016 POLL DATA]' + (' ' * 15) + '#' + '\n')
                txt_file.write('#' + (' ' * 78) + '#' + '\n')
                txt_file.write('#' + (' ' * 23) + 'CREATED BY: TROY ENGELHARDT' + (' ' * 28) + '#' + '\n')
                txt_file.write('#' * 80 + '\n')
                txt_file.write('# ' + 'CAMPAIGN ROUTE:' + (' ' * 62) + '#' + '\n')
                txt_file.write('#' * 80 + '\n')

                count = 0 # set a counter to 0
                stop = len(vertex_queue) # we stop once we hit the last location
                while not vertex_queue.isEmpty(): # until all the locations have been dealt with
                    a_location = vertex_queue.dequeue() # look at location
                    txt_file.write('# ' + a_location[0] + (' ' * (47 - len(a_location[0]))) + '#' + (' ' * 7) + a_location[1] + ' minutes' + (' ' * (14 - len(a_location[1]))) + '#' + '\n')
                    count += 1 # add to vertex counter
                    total_time.insertLast(a_location[1]) # append location's time (180 mins) to the list
                    if count == stop: # if stopping condition is met
                        pass # exit
                    else: # otherwise there must be another edge to add
                        an_edge = edge_queue.dequeue() # look at edge
                        txt_file.write('# ' + an_edge[0] + (' ' * (47 - len(an_edge[0]))) + '#' + (' ' * 7) + an_edge[1] + ' minutes' + (' ' * (14 - len(an_edge[1]))) + '#' + '\n')
                        total_time.insertLast(an_edge[1]) # append edge's travel time to the list

                txt_file.write('#' * 80 + '\n')

                # set has_none = True if a 'NONE' edge is found
                has_none = False
                for i in total_time:
                    if i == 'NONE':
                        has_none = True

                if has_none == True: # if 'NONE' exists
                    txt_file.write('# NONE EDGE PRESENT? TRUE -- total travel will underestimate true travel time  #' + '\n')
                else: # otherwise NO 'NONE's exist
                    txt_file.write('# NONE EDGE PRESENT? FALSE -- total travel is a good estimate true travel time #' + '\n')

                txt_file.write('#' * 80 + '\n')

                travel_time = 0 # initiate total travel = 0 minutes
                for i in total_time:
                    if i != 'NONE':
                        travel_time += int(i) # add the travel time to the total

                txt_file.write('# ' + str(travel_time) + ' minutes' + (' ' * (69 - len(str(travel_time)) ) ) + '#' + '\n')
                txt_file.write('# ' + str(int(travel_time/60)) + ' hours ' + str(travel_time%60) + ' minutes' + (' ' * (62 - (len(str(int(travel_time/60))) + len(str(travel_time%60))))) + '#' + '\n')
                # following line is what true pain feels like lol
                txt_file.write('# ' + str(int(travel_time/60/24)) + ' days ' + str(int(travel_time/60)%24) + ' hours ' + str(travel_time%60) + ' minutes' + (' ' * (56 - ( (len(str(int(travel_time/60))) + len(str(travel_time%60))) + len(str(int(travel_time / 60 / 24)))))) + '#' + '\n')

                txt_file.write('#' * 80)



            self.timer('writing data to txt: ')
            self.timer('dumping file: ')
            print()
            self.marginalCampaignMenu(q1, q2)
        elif selection6 == '3':
            name = str(input("File name: "))

            results = [q1, q2] # i was a bit lazy here and just serialized the queues.
            # they have all the necessary information, it would've been better to put
            # them in order in an array of somesort but at this point, this'll have to do
                    
            with open(name, 'wb') as data:
                pickle.dump(results, data)

            self.timer('serializing data: ')
            self.timer('dumping file: ')
            print()
            self.marginalCampaignMenu(q1, q2)
        elif selection6 == 'q':
            pass
        else:
            self.marginalCampaignMenu(q1, q2)
