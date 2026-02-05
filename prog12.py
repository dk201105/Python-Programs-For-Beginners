# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:04:42 2025

@author: 23csc11
"""

import numpy as np

players_dtype = np.dtype([
    ('player_id', 'i4'),
    ('name', 'U25'),
    ('position', 'U15'),
    ('games_played', 'i4'),
    ('goals_scored', 'i4')
])

players = np.array([
    (1, 'A. Messi', 'Forward', 30, 25),
    (2, 'C. Ronaldo', 'Forward', 35, 25),
    (3, 'V. Van Dijk', 'Defender', 40, 5),
    (4, 'L. Modric', 'Midfielder', 20, 3),
    (5, 'M. Neuer', 'Goalkeeper', 15, 0),
    (6, 'K. Mbappe', 'Forward', 28, 18),
    (7, 'S. Ramos', 'Defender', 10, 1),
    (8, 'E. Haaland', 'Forward', 45, 30),
    (9, 'P. Pogba', 'Midfielder', 32, 7),
], dtype=players_dtype)

print(players)

goals_per_game = np.divide(
    players['goals_scored'], 
    players['games_played'], 
    out=np.zeros_like(players['goals_scored'], dtype=float),
    where=players['games_played'] != 0
)

new_dtype_12 = players_dtype.descr + [('goals_per_game', 'f8')]
new_players = np.empty(players.shape, dtype=new_dtype_12)

for name in players_dtype.names:
    new_players[name] = players[name]
    
new_players['goals_per_game'] = goals_per_game

print("\na. Data with Goals Per Game Added:\n", new_players)

players_over_20_games = new_players[new_players['games_played'] > 20]

print("\nb. Players with More Than 20 Games Played:\n", players_over_20_games)

max_goals = new_players['goals_scored'].max()
top_scorers = new_players[new_players['goals_scored'] == max_goals]

print("\nc. Player(s) with the Highest Goals Scored:")
print(f"Highest Goals Scored: {max_goals}")
print(top_scorers[['name', 'goals_scored', 'position']])

temp_players = new_players.copy()
temp_players['goals_scored'] = -temp_players['goals_scored']

sorted_players = np.sort(temp_players, order=('position', 'goals_scored'))

sorted_players['goals_scored'] = -sorted_players['goals_scored']

print("\nd. Array Sorted by Position (A) and Goals Scored (D):")
print(sorted_players)