import csv
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.nba.com/stats")
# print(response.text)
web_page = response.text

soup = BeautifulSoup(web_page, features="html.parser")

# 1. Find the H2 title 'Points'
points_header = soup.find("h2", string="Points")

# 2. Go up 3 levels to reach the full leaderboard container
leaderboard_div = points_header.find_parent("div")

# 3. Within that container, find all player rows
rows = leaderboard_div.select("table.LeaderBoardPlayerCard_lbpcTable__q3iZD tbody tr")

# 4. Extract player names from <a> tags in the second <td>
highest_points = []
for row in rows:
    player_name_tag = row.select_one("td:nth-of-type(2) a")
    if player_name_tag:
        strip_player = player_name_tag.text.strip()
        highest_points.append(strip_player)
        print(strip_player)

print(highest_points)

with open("nba.csv", "w", newline="") as f:
    writer = csv.writer(f)
    """ Will be written in Column 2 because of this ("", )"""
    writer.writerow(["", "Recent Highest points of the NBA players"])  # Optional header
    writer.writerows([["", name] for name in highest_points])



