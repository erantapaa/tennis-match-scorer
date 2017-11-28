## Description of Assignment

A New Professional Association of Tennis Players has started a New Tennis Tournament Circuit. The first season will start with just four tournaments which will take place at different times of the year in different locations. Each tournament has been assigned a degree of difficulty. Each tournament has prize money awarded to every player that reaches the last eight. Each tournament has two competitions for Men and Women singles Each place in the top sixteen is awarded a given number of ranking points You are required to design, implement and evaluate a simple system that takes as input the score for each match for a given tournament and updates each player’s position, calculates each player’s ranking points and produces a list of the players ranking in descending order. The system calculates the prize money due to each player at any given point in time and accumulates these having stored them safely. The four tournaments are listed below

* TAC1 – degree of difficulty 2.7
* TAE21 – degree of difficulty 2.3
* TAW11 – degree of difficulty 3.1
* TBS2 – degree of difficulty 3.25

The first season has attracted 32 men and 32 women players in total and details of these players are given to you in separate files. The prize money awarded for each of the eight top positions for each tournament is also given to you in a file. Your system should check for erroneous double entries of results. The system should also check for the validity of scores entered – i.e. one player in the men’s game must have three sets per match, but no two players can have three sets in the same match. Similarly, in the ladies game the winner in a match must win two sets and no two players can win two sets each in the same match. Match results should show the score in terms of sets won for each player. A win in the men circuit is on best of five and a win in the women circuit is on best of three.

Assumptions:
* In calculating the rating points the standard tournament place points will be multiplied by the degree of difficulty.
* Each match’s score must be represented as Player A, number of sets A, Player B, number of sets B.
* The winner is the player that has won three set in the men’s game or two sets in the ladies game.
* Scores should be read either from a file or entered manually from the prompt. A simple User Interface with a menu selection should be offered.

Additional 

In processing scores, the idea is as follows – for each tournament
· 1st round – 16 losers can be ignored completely, while the 16 winners are all awarded 5
ranking points

· 2nd round – 8 losers stay on 5 ranking points while the winners are updated to 10 ranking
points

· 3rd round – 4 losers stay on 10 ranking points while the winners are updated to 30 ranking
points

· 4th round – 2 losers stay on 30 points while the winners are updated on 50 points

· Final – loser stays on 50 points while the winner is updated to 100 points

· Following the final ranking points awarded are multiplied by the difficulty factor and the results
added to any other ranking points these players might have from previous tournaments played.
A similar logic should be applied for the award of money although there the awards are not affected
by the degree of difficulty as each tournament has its own pay structure.

Your system must allow you to save intermediate awards of ranking points and prize money at any
stage for every tournament. At the end of each tournament the ranking points awarded, and the
prize money won will be used to update each player’s totals. Thus, exiting the programme at any
stage should not result in any loss of data. Match scores need not be kept after processing and the
decision as to which players have progressed to the next round has been made.
