import requests
from bs4 import BeautifulSoup



URL= "https://m.cricbuzz.com/cricket-commentary/35607/ind-vs-nz-final-icc-world-test-championship-final-2021"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find("span", class_= "miniscore-teams ui-bat-team-scores").text
status= soup.find("div", class_= "cbz-ui-status").text
runrate= soup.find("span", class_="crr").text
table= soup.find("table", class_="table table-condensed ")
players= soup.find_all("span", class_= "bat-bowl-miniscore")
batsman = players[0].text, players[1].text
bowler = players[2].text, players[3].text

player_stats = soup.find_all("td", class_="cbz-grid-table-fix")

header = [
player_stats[0].text
,player_stats[1].text
,player_stats[2].text
,player_stats[3].text
,player_stats[4].text
]

player1 = [
 player_stats[5].text
,player_stats[6].text
,player_stats[7].text
,player_stats[8].text
,player_stats[9].text
]

zipped = list(zip(header, player1))
print(zipped)
'''
print(player_stats[0].text + " 🏏\n" + player_stats[5].text + "\nAND\n" + player_stats[10].text + "\n")

print(player_stats[1].text + " 🏏\n" + player_stats[6].text + "\nAND\n" + player_stats[11].text + "\n")

print(player_stats[2].text + " 🏏\n" + player_stats[7].text + "\nAND\n" + player_stats[12].text + "\n")

print(player_stats[3].text + " 🏏\n" + player_stats[8].text + "\nAND\n" + player_stats[13].text + "\n")

print(player_stats[4].text + " 🏏\n" + player_stats[9].text + "\nAND\n" + player_stats[14].text + "\n")
'''



print()
print()
print("Status👉", status)
print("Score👉", result)
print("Run Rate👉", runrate)
print("Current Batsman👉", players[0].text, " and ", players[1].text)
print("Current Bowlers👉", players[2].text, " and ", players[3].text)
