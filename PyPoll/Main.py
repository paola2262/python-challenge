import csv
import os

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row['Candidate'])
    return data

def election_results(data):
    total_votes = len(data)
    
    candidates = {}
    for candidate in data:
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
    
    winner = max(candidates, key=candidates.get)
    
    results = {candidate: (votes / total_votes * 100, votes) for candidate, votes in candidates.items()}
    
    return total_votes, results, winner

def format_output(total_votes, results, winner):
    output = f"Election Results\n{'-'*25}\n"
    output += f"Total Votes: {total_votes}\n"
    output += "-" * 25 + "\n"
    for candidate, (percentage, votes) in results.items():
        output += f"{candidate}: {percentage:.3f}% ({votes})\n"
    output += "-" * 25 + "\n"
    output += f"Winner: {winner}\n"
    output += "-" * 25 + "\n"
    return output

def save_to_file(output):
    file_path = '/Users/paolamoreno/Desktop/Classwork/Module 3 Python/Starter_Code 3/PyPoll/analysis/analysis.txt'
    with open(file_path, 'w') as file:
        file.write(output)

def main():
    # Constructing the full file path
    directory = '/Users/paolamoreno/Desktop/Classwork/Module 3 Python/Starter_Code 3/PyPoll/Resources'
    filename = os.path.join(directory, 'election_data.csv')
    
    data = read_csv(filename)
    total_votes, results, winner = election_results(data)
    output = format_output(total_votes, results, winner)
    save_to_file(output)

if __name__ == "__main__":
    main()