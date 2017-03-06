'''
Write a standalone Python program that can be directly executed, not just a
function.

Here are some basic facts about tennis scoring:
A tennis match is made up of sets.  A set is made up of games.

To win a set, a player has to win 6 games with a difference of 2 games.  At 6-6,
there is often a special tie-breaker.  In some cases, players go on playing till
one of them wins the set with a difference of two games.

Tennis matches can be either 3 sets or 5 sets.  The player who wins a majority
of sets wins the match (i.e., 2 out 3 sets or 3 out of 5 sets)
The score of a match lists out the games in each set, with the overall winner's
score reported first for each set.  Thus, if the score is 6-3, 5-7, 7-6 it means
that the first player won the first set by 6 games to 3, lost the second one 5
games to 7 and won the third one 7 games to 6 (and hence won the overall match
as well by 2 sets to 1).

You will read input from the keyboard (standard input) containing the results of
several tennis matches. Each match's score is recorded on a separate line with
the following format:

Winner:Loser:Set-1-score,...,Set-k-score, where 2 <= k <= 5

For example, an input line of the form

Williams:Muguruza:3-6,6-3,6-3

indicates that Williams beat Muguruza 3-6, 6-3, 6-3 in a best of 3 set match.

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches
and compile the following statistics for each player:

1. Number of best-of-5 set matches won
2. Number of best-of-3 set matches won
3. Number of sets won
4. Number of games won
5. Number of sets lost
6. Number of games lost

You should print out to the screen (standard output) a summary in decreasing
order of ranking, where the ranking is according to the criteria 1-6 in that
order (compare item 1, if equal compare item 2, if equal compare item 3 etc,
noting that for items 5 and 6 the comparison is reversed).

For instance, given the following data

Djokovic:Murray:2-6,6-7,7-6,6-3,6-1
Murray:Djokovic:6-3,4-6,6-4,6-3
Djokovic:Murray:6-0,7-6,6-7,6-3
Murray:Djokovic:6-4,6-4
Djokovic:Murray:2-6,6-2,6-0
Murray:Djokovic:6-3,4-6,6-3,6-4
Djokovic:Murray:7-6,4-6,7-6,2-6,6-2
Murray:Djokovic:7-5,7-5
Williams:Muguruza:3-6,6-3,6-3

your program should print out the following

Djokovic 3 1 13 142 16 143
Murray 2 2 16 143 13 142
Williams 0 1 2 15 1 12
Muguruza 0 0 1 12 2 15

You can assume that there are no spaces around the punctuation marks ":", "-"
and ",".  Each player's name will be spelled consistently and no two players
have the same name.
'''

# Dictionary to store Players and thier statistics as a list
players = {}

# While to take inputs, multiple lines, terminated by empty line
while(True):
    line = input()
    if line == '':
        break

    # Each line is match, split into [Winner, Loser, Sets(list)]
    match = line.split(":")
    # Sets
    sets = match[2].split(",")

    # Inializing player in dictionary and value as '0 value list of length 6'
    if match[0] not in players:
        players[match[0]] = []
        for i in range(0, 6):
            players[match[0]].append(0)

    if match[1] not in players:
        players[match[1]] = []
        for i in range(0, 6):
            players[match[1]].append(0)

    # 1, 2 Stats
    # If length of set is more than five, its best-of-5 match else best-of-3
    if len(sets) > 3:
        players[match[0]][0] += 1
    else:
        players[match[0]][1] += 1

    # 3
    # Compares set values of each set in the current match input
    # If won, incrememnt Q3 Stats of one player and Q5 Stats of other for loss
    for s in sets:
        s = s.split("-")
        if s[0] > s[1]:
            players[match[0]][2] += 1
            players[match[1]][4] += 1   # 5
        else:
            players[match[1]][2] += 1
            players[match[0]][4] += 1   # 5
    # 4
    # Incrememnt the games won by one player(Q4) and lost game for other (Q6)
        players[match[0]][3] += int(s[0])
        players[match[1]][5] += int(s[0])   # 6

        players[match[1]][3] += int(s[1])
        players[match[0]][5] += int(s[1])   # 6

# items() returns key-value pair (Tuple). Sorted based on second value of tuple,
# i.e. values of dictionary. First value of tuple is key.
result = sorted(players.items(), key=lambda a: a[1], reverse=True)

# Print each Players Stats seperated by spaces
for i in result:
    print(i[0], " ".join(map(str, i[1])))

'''
Test Case 2
Halep:Raonic:2-6,6-7,7-6,6-3,6-1
Kerber:Raonic:6-3,4-6,6-4,6-3
Raonic:Wawrinka:6-0,7-6,6-7,6-3
Wawrinka:Raonic:6-4,6-4
Halep:Raonic:2-6,6-2,6-0
Wawrinka:Raonic:6-3,4-6,6-3,6-4
Raonic:Wawrinka:7-6,4-6,7-6,2-6,6-2
Wawrinka:Kerber:7-5,7-5
Halep:Kerber:3-6,6-3,6-3
Halep:Wawrinka:0-6,0-6,6-0,6-0,7-5
Kerber:Wawrinka:6-3,4-6,7-6,0-6,7-5

Halep 2 2 10 75 6 60
Raonic 2 0 11 122 16 139
Kerber 2 0 7 68 7 71
Wawrinka 1 2 14 133 13 128
'''
