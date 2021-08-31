# import csv files downloaded from pro-football-reference.com
# create a data summary table (file) using python scripts

import pandas as pd

from csv import reader

team_data = pd.read_csv("nfl_2020_team_summaries.csv", index_col='Tm')
# print(team_data.head())

offense_data = pd.read_csv("nfl_2020_team_offense.csv", index_col='Tm')
print(offense_data.head())
defense_data = pd.read_csv("nfl_2020_team_defense.csv", index_col='Tm')
drive_data = pd.read_csv("nfl_2020_team_drive_avgs.csv", index_col='Tm')
drive_against_data = pd.read_csv("nfl_2020_team_drive_avgs_against.csv", index_col='Tm')
# adv_defense_data = pd.read_csv("nfl_2020_team_defense_adv.csv", index_col='Tm')

opened_file = open("nfl_2020_scores.csv")
read_file = reader(opened_file)
scores_data = list(read_file)

# add new column headers for basic team stats (column index 14 - 22)
scores_data[0].extend(['Margin', 'Home', 'Away', 'PTsH', 'PTsA', 'HSRS', 'ASRS', 'H-A_Margin', 'H-A_SRS'])

# add offensive advanced stats (column index 23 - 26)
scores_data[0].extend(['HOYPC', 'AOYPC', 'HOYPPA', 'AOYPPA'])

# add defensive advanced stats (column index 27 - 32)
scores_data[0].extend(['HDYPC', 'ADYPC', 'HDYPPA', 'ADYPPA', 'HDPAP100', 'ADPAP100'])

# add net (offense - defense) stats (column index 33 - 37)
scores_data[0].extend(['Net_HYPC', 'Net_AYPC', 'Net_HYPPA', 'Net_AYPPA', 'YPP_Margin'])

# add drive averages stats (column index 38 - 43)
# scores_data[0].extend(['HSFP', 'ASFP', 'HSFPA', 'ASFPA', 'Net_HSFP', 'Net_ASFP'])

for row in scores_data[1:]:
    row.append(int(row[8]) - int(row[9]))  # win margin [14]

    if row[5] == '@':
        row.append(row[6])  # home team [15]
        row.append(row[4])  # away team [16]
    else:
        row.append(row[4])
        row.append(row[6])

    if row[4] == row[15]:
        row.append(row[8])  # home pts [17]
        row.append(row[9])  # away pts [18]
    else:
        row.append(row[9])
        row.append(row[8])

    row.append(team_data.loc[row[15]][9])  # home SRS [19]
    row.append(team_data.loc[row[16]][9])  # away SRS [20]

    row.append(int(row[17]) - int(row[18]))  # (home - away) margin [21]
    row.append(round((row[19] - row[20]), 1))  # (home - away) SRS [22]

    row.append(offense_data.loc[row[15]][19])  # home offensive yards per carry [23]
    row.append(offense_data.loc[row[16]][19])  # away offensive yards per carry [24]

    row.append(offense_data.loc[row[15]][14])  # home offensive yards per pass attempt [25]
    row.append(offense_data.loc[row[16]][14])  # away offensive yards per pass attempt [26]

    row.append(defense_data.loc[row[15]][19])  # home defensive yards per carry [27]
    row.append(defense_data.loc[row[16]][19])  # away defensive yards per carry [28]

    row.append(defense_data.loc[row[15]][14])  # home defensive yards per pass attempt [29]
    row.append(defense_data.loc[row[16]][14])  # away defensive yards per pass attempt [30]

    # defensive points allowed per 100 yards = total yards allowed / 100 / total points allowed
    row.append(round(defense_data.loc[row[15]][2] / (defense_data.loc[row[15]][3] / 100), 1))  # home DPA per 100 [31]
    row.append(round(defense_data.loc[row[16]][2] / (defense_data.loc[row[16]][3] / 100), 1))  # away DPA per 100 [32]

    # net yards per carry = offensive YPC + opponent defensive YPC
    row.append(round(row[23] + row[30], 1))  # home net yards per carry [33]
    row.append(round(row[24] + row[29], 1))  # away net yards per carry [34]

    # net yards per pass attempt = offensive YPPA + opponent defensive YPPA
    row.append(round(row[25] + row[32], 1))  # home net yards per pass attempt [35]
    row.append(round(row[26] + row[31], 1))  # away net yards per pass attempt [36]

    # yards per possession margin (home - away) = home(net YPC + net YPPA) - away(net YPC + net YPPA)
    row.append((row[33] + row[35]) - (row[34] + row[36]))  # yards per possession margin [37]

    # row.append(drive_data.loc[row[15]][8])  # home starting field position [38]
    # row.append(drive_data.loc[row[16]][8])  # away starting field position [39]
    # row.append(drive_against_data.loc[row[15]][8])  # home starting field position against [40]
    # row.append(drive_against_data.loc[row[16]][8])  # away starting field position against [41]
    # row.append(float(row[27]) - float(row[34]))  # home net starting field position [42]
    # row.append(float(row[28]) - float(row[33]))  # away net starting field position [43]

    print(row)

df = pd.DataFrame(scores_data)
df.to_csv('nfl_2020_data_summary.csv', index=False, header=False)
