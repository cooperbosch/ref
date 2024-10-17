# Julian Day - 10.16.2024
# Hopefully the beginning of my referee analysis project
from bs4 import BeautifulSoup
import requests
import csv

# You don't have to do user input we could also do something like url = "https://www.soccerbase.com/referees/home.sd?tourn_id=2039"
# then just have doc = BeautifulSoup(url.text, ... ) but this makes it more interactive and fun idfk lol.
user_input = input("insert a link here: ")
print("\n")
result = requests.get(user_input)

doc = BeautifulSoup(result.text, "html.parser")
#print(doc) Making sure the Webpage has no blockers - explained below in block comment

Referees = doc.find_all('table', class_="table referee")
count = 0
# Count is made for pretty CSV purposes
# CSV File stuff below here

# This is just where I'm putting my file - you can put yours wherever makes sense for you
filename = "E:/Download/Referee_Analysis.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Header 
    writer.writerow(['Name', ' Country', ' Total Matches', ' Yellow Cards', ' Red Cards'])
    
    # Temp list to hold ref data
    row = []
    
    '''If you're confused by the tags before you look at the stuff below, go into this link: https://www.soccerbase.com/referees/home.sd?tourn_id=2039
    highlight Sam Allison then inspect element to bring you to the HTML elements, you can find the way I got each 'Referee' 
    by looking for that table tag with class table referee - then within that tag is all the tr tags for each referee and 
    td tags for each of the info cells that we care about. I feel like the code below is pretty basic once you get how that 
    works. Also I have to use this website soccerbase.com because the others have like scraping blockers or cookies which 
    don't let you grab site data using beautiful soup. 
    '''
    for tr in Referees:
        steps = tr.find_all(["td"])
        for i in steps: # This stuff is getting each referee but it would print as a block thats why I care about sectioning it by 5s for each of the 5 attributes on each line.
            if count == 0 or count % 5 == 0:
                row.append(i.text)  # Just making spacing look nice
            else:
                row.append(" "+i.text)
            count += 1
            
            # When count reaches 5, write the row and reset the list
            if count % 5 == 0:
                writer.writerow(row)  # Write the full row to the file
                row = []  # Reset row 
