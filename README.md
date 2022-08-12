# Election_Analysis

## Project overview
Tom, a Colorado Board of Elections Employee has asked for some assistance in completing an election audit of a local congressional election.

Tasks to complete this initial audit included:
1. Calculating the toal number of votes cast by counting the number of unique Ballot IDs
2. Creating a list of candidates that received votes
3. Summing the number of votes cast for each candidate
4. Determing the percentage of votes each candidate received
5. Determing the winner of the election by the person receiving the most votes, also known as the popular vote

Before we turned in our anaysis to Tom, he asks us to dig a little deeper intot he results. The elcetion committee additionally would like us to include:
* The number of votes cast in each county
* The percentage of total votes cast in each county
* The county with the highest voter turnout


## Summary

The data file holds information in only a few columns representing the Ballot ID, the Candidate for which the vote is cast, and the county in which the voter resides. In order to do our analysis, we must take these simple fields and create dictionaries and lists to hold the candidate names, county names, and the votes cast. Using Python to accomplish this task is quite difficult and confusing at first, but if you stay orgainized and plan ahead, it can really make the process efficient and definitive.

**The results are as follows**
* There were a total of 369, 711 votes cast
* Denver had the highest turnout of voters with following breakdown:
    * Jefferson County: 38, 855 votes cast here with 10.5% of the total
  * Denver County: 306, 055 votes cast here with 82.8% of the total
  * Arapahoe: 24,801 total votes
* The winning candidate was Dianna DeGette with the following breakdown:
  * Charles Casper Stockham received 85, 213 votes at 23% with the total
  * Diana DeGette received 272, 892 votes with 73.8% of the total
  * Raymon Anthony Doane received 11, 606 votes with 3.1% of the total
  * The winner of the election was Diana DeGette

Running our code in the terminal gave us this ouput:


![Election_Results_terminal](https://user-images.githubusercontent.com/109319148/184444429-96ba50a1-6820-46b6-935f-f90f6072d256.png)


Tom also showed us how to write our results to a text file:
[election_analysis.txt](https://github.com/ErinLVigil/Election_Analysis/files/9329885/election_analysis.txt)

## Election- Audit Summary
  The script included in this audit summary is easily transferable for any election. The script can be used for elections with only a thousand votes or scaled up to millions of votes with no modification. The beauty of the python script is that it does not need to define how many lines (votes) are in the input file. The script pulls out the unique list of candidates to do the analysis from the file negating the need to predefine that list or make modifications. 
  
  However, if there were a few modifications, the election board could gain additional insights. For example, creating another dictionary that holds votes cast per candidate for each county would allow the board to determine which candidate was the most popular in the county allowing us to declare a "winner" in each county. We could also modify the script to tell us the percentage of votes each voter received in each county. 
