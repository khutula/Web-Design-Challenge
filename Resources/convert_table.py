# import dependencies
import pandas as pd

# read csv as pandas dataframe
df = pd.read_csv("cities.csv")

# convert dataframe to html format
html_df = df.to_html(index=False, classes=["table", "table-responsive"], justify="left")

# write html to file
html_file = open("../data.html", "a")
html_file.write(html_df)
html_file.close()