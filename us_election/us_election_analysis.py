import pandas as pd 
import matplotlib.pyplot as plt

#load the dataset with semicolon delimiter
election_data_df = pd.read_csv("dat5501-portfolio-elias/us_election/US-2016-primary.csv")
election_data_df.fillna(0, inplace=True) #fill missing values with 0
candidate = "Donald Trump"

#filter for one candidate
candidate_df = election_data_df[election_data_df['candidate'] == candidate]

#find total number of votes for the candidate 
total_candidate_votes =candidate_df['votes'].sum()

#find total number of votes for each fraction fot the candidate in each state
state_vote_fraction = election_data_df.groupby('state')['Fraction of Votes'].sum()
print(state_vote_fraction)

#find the total number of votes in each state
state_total_votes = election_data_df.groupby('state')['votes'].sum()

#find the total number of votes for the canidate in each state 
state_total_candidate_votes = candidate_df.groupby('state')['votes'].sum()

#find the fraction of votes for the candidate in each state
state_fractions = state_total_candidate_votes / state_total_votes

#find the fraction of votes of each stage compared to total votes for the candidate
candidate_vote_fractions = state_total_candidate_votes / total_candidate_votes

#plot chart
state_fractions.plot(kind='bar', title=f'Fraction of Votes for {candidate}',edgecolor='black')
plt.xlabel('State')
plt.ylabel('Fraction of Votes')
plt.grid(True)
plt.tightlayout()
plt.show()



