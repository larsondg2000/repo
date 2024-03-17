# Federal Reserve Repo, Reverse Repo and SOMA using APIs in streamlit
![alt-text](ws.jpeg "Wall Street")
## Repo and Reverse Repo
API Call:
url = "https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json"
request = requests.get(url)
content = request.json()
repo_ops = (content['repo']['operations'])

Data is exacted from JSON object to create the following:
  1) Repo and Reverse Repo operations for the day
  2) Bar chart of reverse repo operations for last two weeks
  3) Bar chart of repo operations for last two weeks
  4) Total repo operations 

## System Open Market Account (SOMA)
API Call:
url = "https://markets.newyorkfed.org/api/soma/summary.json"
request = requests.get(url)
content = request.json()
soma_ops = (content['soma']['summary'])

Data is exacted from JSON object to create the following:
  1) Total SOMA holdings
  2) Bar chart of SOMA holdings
  3) Table of SOMA holdings
  4) Bar chart of historical SOMA holdings 