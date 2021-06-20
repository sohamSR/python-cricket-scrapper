import requests
from bs4 import BeautifulSoup



URL= "https://m.cricbuzz.com/cricket-commentary/35607/ind-vs-nz-final-icc-world-test-championship-final-2021"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find("span", class_= "miniscore-teams ui-bat-team-scores").text
status= soup.find("div", class_= "cbz-ui-status").text
runrate= soup.find("span", class_="crr").text
players= soup.find_all("span", class_= "bat-bowl-miniscore")
batsman = players[0].text, players[1].text
bowler = players[2].text, players[3].text

player_stats = soup.find_all("td", class_="cbz-grid-table-fix")

#Batsman
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

player2 = [
 player_stats[10].text
,player_stats[11].text
,player_stats[12].text
,player_stats[13].text
,player_stats[14].text
]

zipped_batsman1 = list(zip(header,player1))

zipped_batsman2 = list(zip(header,player2))
print (zipped_batsman1[0])
print (zipped_batsman1[1])
print (zipped_batsman1[2])
print (zipped_batsman1[3])
print (zipped_batsman1[4])

print("\n")
print (zipped_batsman2[0])
print (zipped_batsman2[1])
print (zipped_batsman2[2])
print (zipped_batsman2[3])
print (zipped_batsman2[4])


print("\n")

print("Status👉", status)
print("\n")
print("Score👉", result)
print("\n")
print("Run Rate👉", runrate)
print("\n")
print("Current Batsman👉", players[0].text, " and ", players[1].text)
print("\n")
print("Current Bowlers👉", players[2].text, " and ", players[3].text)
