import pandas as pd
import pygal


playersdf = pd.read_csv("wnbadrafts.csv")


print(playersdf)

# Visualization 1: Interactive Line Chart - Players vs Points using Pygal
players_top36 = playersdf[['player', 'team', 'points']].head(36)  # Selecting top 36 players
line_chart = pygal.Line(x_label_rotation=45, style=pygal.style.LightStyle)
line_chart.title = 'Top 36 WNBA Players by Points'
for _, row in players_top36.iterrows():
    line_chart.add(row['player'], [row['points']])

#Save to a file or render to a browser
line_chart.render_in_browser()

#Visualization 2: Players and Teams (Bar Chart) using Pygal
bar_chart = pygal.Bar(style=pygal.style.LightStyle)
bar_chart.title = 'Points per Team'
for team, group in playersdf.groupby('team'):
    bar_chart.add(team, group['points'].sum())

#Save to a file or render to a browser
bar_chart.render_in_browser()

#Visualization 3: Points and Players (Pie Chart) using Pygal
pie_chart = pygal.Pie(style=pygal.style.LightStyle)
pie_chart.title = 'Points Distribution Among Players'
for _, row in playersdf.iterrows():
    pie_chart.add(row['player'], row['points'])

#Save to a file or render to a browser
pie_chart.render_in_browser()

#Visualization 4: Points and Team (Bar Chart) using Pygal
team_points = playersdf.groupby('team')['points'].sum().reset_index()  # Summing points by team
team_bar_chart = pygal.Bar(style=pygal.style.LightStyle)
team_bar_chart.title = 'Total Points by Team'
for _, row in team_points.iterrows():
    team_bar_chart.add(row['team'], row['points'])

#Save to a file or render to a browser
team_bar_chart.render_in_browser()

