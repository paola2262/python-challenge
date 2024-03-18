import csv
import os

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

def financial_analysis(data):
    total_months = len(data)
    
    total = sum(int(row[1]) for row in data)
    
    changes = [int(data[i+1][1]) - int(data[i][1]) for i in range(len(data)-1)]
    average_change = sum(changes) / len(changes)
    
    max_increase = max(changes)
    max_increase_month = data[changes.index(max_increase) + 1][0]
    
    max_decrease = min(changes)
    max_decrease_month = data[changes.index(max_decrease) + 1][0]
    
    return total_months, total, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month

def format_output(total_months, total, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month):
    output = f"Financial Analysis\n{'-'*30}\n"
    output += f"Total Months: {total_months}\n"
    output += f"Total: ${total}\n"
    output += f"Average Change: ${average_change:.2f}\n"
    output += f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    output += f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n"
    return output

def save_to_file(output):
    directory = '/Users/paolamoreno/Desktop/Classwork/Module 3 Python/Starter_Code 3/Pybank/analysis'
    file_path = os.path.join(directory, 'analysis.txt')
    with open(file_path, 'w') as file:
        file.write(output)

def main():
    # Constructing the full file path
    directory = '/Users/paolamoreno/Desktop/Classwork/Module 3 Python/Starter_Code 3/PyBank/Resources'
    filename = os.path.join(directory, 'budget_data.csv')
    
    data = read_csv(filename)
    total_months, total, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month = financial_analysis(data)
    output = format_output(total_months, total, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month)
    save_to_file(output)
    print("Financial analysis has been saved to 'analysis.txt'.")

if __name__ == "__main__":
    main()
    