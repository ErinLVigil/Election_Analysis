# #what is the score

# score= int(input("What is your test score?"))

# if score >= 90:
#     print('Your grade is an A')
# elif score >= 80:
#     print('Your grade is a B')
# elif score >= 70:
#     print('Your grade is a C')
# elif score >= 60:
#     print('Your grade is a D')
# else:
#     print('Your grade is an f')

# candidate_votes = int(input("How many votes did the candidate get in the election? "))

# total_votes = int(input("What is the total numbr of votes in the election?"))

# message_to_candidate = (f'You received {candidate_votes} numer of votes'
#                         f'The total number of votes in the election was {total_votes:,}.'
#                         f'You received {candidate_votes/ total_votes * 100:.2f}% of the total votes')

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters} registered voters.')

voting_data = [{"county" : "Arapahoe", "registered_voters" : 422829}, {"county":"Denver", "registered_voters" : 463353},
                {"county" :"Jefferson", "registered_voters" : 432438}]

print(f'{voting_data[0]["county"]}')