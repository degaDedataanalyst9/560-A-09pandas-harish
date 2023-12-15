import pandas as pd



roster = ["Elliot","Rj","Cormac"]
player = {"First Name": roster,
          "Last Name": ["Cadeau","Davis","Rayan"],
          "Height": [6.1,6.0,6.5],
          "Weight": [180,180,195]}
data = pd.DataFrame(player)
print(data)

