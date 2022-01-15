# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1 Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file.
candidate_options = [] 
#1 Declare the empty dictionary.
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count.
        total_votes += 1
   # Get the candidate name from each row
        candidate_name = row[2]     
    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #2 Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"_________________________\n"
        f"Total Votes: {total_votes:,}\n"
        f"_________________________\n")
    print(election_results, end="")
    # After printing the final vote coun t to the terminal save the final vote count to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
    

        #Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count.
        #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name} : {vote_percentage: .1f}% ({votes: ,})\n)")
        #Print each candidate, their vote count, and the percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        

        if (votes > winning_count) and (vote_percentage > winning_percentage):
       
            winning_count = votes
            winning_percentage = vote_percentage
            #And, Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
#Print the winning candidate's results to the terminal

    winning_candidate_summary = (
        f"_________________________\n)"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"_________________________\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.

    txt_file.write(winning_candidate_summary)

















 



