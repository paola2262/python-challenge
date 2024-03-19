                                          **Name**
                                   Student: Paola Moreno
                                    # python-challenge
                                    Module 3 Challenge
                                    
 **Introduction & Data Description - PyBank**  
 PyBank script examines a company's financial records stored in a CSV file. By using Python, PyBank automates the analysis, making it easy to understand key financial trends. The dataset 'budget_data.csv', contains "Date" and "Profit/Losses" columns. PyBank analyzes this data to calculate total months, net profit/loss, average changes, and identify periods of significant profit increase or decrease.

**Introduction & Data Description - PyPoll**  
  PyPoll is a script that analyze election data stored in a CSV file named 'election_data.csv'. This script offers essential functionalities to streamline the analysis of election results, making it easier to understand and interpret key insights.
  
**Analysis- PyBank** 

The script starts by getting the financial data from a CSV file using the read_csv() function.

Total Months: Found by counting the number of records in the dataset. (line 14)
Net Total Profit/Losses: Calculated by adding up all the profits and losses. (line 16)
Average Change in Profit/Losses: Figured out by finding the average difference between consecutive months.(Line 18 - 19)
Greatest Increase and Decrease in Profit/Losses: Discovered along with the months they happened. (Line 21 to 27)
After finishing the financial analysis, the format_output() function creates a readable summary with the total months, total profit/loss, average change, and the biggest profit increases and decreases. (line 29 to 36)
Finally, the script prints out these results for you to see.(Line 53)

**Analysis- Pypoll** 

PyPoll is a script designed to analyze election data found in a CSV file called 'election_data.csv'. It simplifies the process of analyzing election results, making it simpler to understand and interpret important information.
The primary tasks performed by the PyPoll script include:

Calculating the total number of votes cast in the election. (Line 9)
Determining the total number of votes each candidate received.(Lines 15 to 23)
Computing the percentage of votes each candidate won. (Lines 25-27)
Identifying the winner of the election based on the popular vote.(Line 29)


**Results - PyBank** 
-The dataset covers a specific period, giving us an overview of the company's financial performance during that time.
*Adding up all the profits and losses shows us the overall financial outcome. This tells us whether the company made a profit or loss during the reviewed period.
-Calculating the average change between months helps us see how the company's finances evolved over time. A positive change means steady growth, while a negative one indicates a decline.
-Identifying the months with the highest profit increases and decreases helps us find important times of financial success or trouble. Figuring out what caused these changes can give us useful insights into how the company works and how outside factors impact its profits.

**Results - Pypoll** 
The PyPoll script provides valuable insights into the election outcome. It analyzes how votes were distributed among candidates and determines the winner based on the highest vote count.

The script calculates the total number of votes cast, providing an essential measure of voter participation. Understanding the level of voter engagement is crucial for assessing the overall significance of the election.

Additionally, the script breaks down the votes for each candidate, presenting the percentage of votes each candidate received. This information offers insights into candidate popularity and voter preferences.

The script also provides the actual number of votes obtained by each candidate, offering a detailed perspective on voting patterns and candidate performance.

Finally, the script identifies the election winner based on the candidate with the highest vote count. This outcome is significant as it determines the successful candidate who will assume the elected position.

In general, the PyPoll script offers a comprehensive understanding of the election results, encompassing voter choices and candidate performance, thus providing valuable insights into the electoral process.

**Contributing - PyBank & Pypoll** 
Contributions to this script were made possible with the support of various resources and individuals:
-AskBCS Student Support: Assistance from the AskBCS support team was instrumental in providing guidance and clarification on certain aspects of the script.
-Class Materials: The code was adapted from materials provided during class sessions, serving as a foundation for the development of the script.
-Collaboration with Astrid Apopa: Collaborative efforts with Astrid Apopa included several knowledge-sharing sessions where we discussed and exchanged insights to enhance the script.
-Class Practice and Learning Tools: The script benefited from the practical exercises conducted in class and utilized tools such as ChatGPT and Xpert Learning Assistant to further refine and expand its functionality.



