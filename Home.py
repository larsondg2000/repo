import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide", page_title="Repo and Reverse Repos", page_icon=":material/trending_up:")

# Get JSON Data from Federal Reserve
url = "https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json"
request = requests.get(url)
content = request.json()
repo_ops = (content['repo']['operations'])

# Get Reverse Repo data for two weeks, today's data, and delta from yesterday
rev_repo = [value['totalAmtAccepted'] for value in repo_ops if value['operationType'] == 'Reverse Repo']
rr0 = rev_repo[0] / 1000000000
rr1 = rev_repo[1] / 1000000000
rr_delta = round((rr0 - rr1), 3)

# Get Repo data for two weeks, today's data, and delta from yesterday
repo = [value['totalAmtAccepted'] for value in repo_ops if value['operationType'] == 'Repo']
r0 = repo[0] / 1000000000
r1 = repo[1] / 1000000000
r_delta = round((r0 - r1), 3)

# Get Total Repo data for two weeks, today's data, and delta from yesterday
total =[repo[i] + rev_repo[i] for i in range(len(repo))]
t0 = total[0] / 1000000000
t1 = total[1] / 1000000000
t_delta = round((t0 - t1), 3)

# get daily repo rate and delta
repo_rate = [repo_ops[i*2]['details'][0]['percentAwardRate'] for i in range(len(repo))]
rate0 = repo_rate[0]
rate1 = repo_rate[1]
rate_delta = round((rate0 - rate1), 2)

# get list of dates and daily repo rate
dates = [value['operationDate'] for value in repo_ops if value['operationType'] == 'Reverse Repo']
date = dates[0]

# Create pandas data frame for charts
dict = {'Date': dates, 'Reverse Repo': rev_repo, 'Repo': repo, 'Total': total, 'Repo Rate': repo_rate}
df = pd.DataFrame(dict)

dict1 = {'Date': dates, 'Reverse Repo': rev_repo}
df1 = pd.DataFrame(dict1)
df1['Reverse Repo'] = df1['Reverse Repo'].div(1000000000)

dict2 = {'Date': dates, 'Repo': repo}
df2 = pd.DataFrame(dict2)
df2['Repo'] = df2['Repo'].div(1000000)

dict3 = {'Date': dates, 'Total': total}
df3 = pd.DataFrame(dict3)
df3['Total'] = df3['Total'].div(1000000000)

st.title(":rainbow[Federal Reserve Repo and Reverse Repo Operations]")


st.title("")

# Daily repo stats
st.header(f"Summary for {date} ", divider='rainbow')

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Reverse Repo Operations ($B)", value=rr0, delta=rr_delta)
col2.metric(label="Repo Operations ($B)", value=r0, delta=r_delta)
col3.metric(label="Total Repo Operations ($B)", value=t0, delta=t_delta)
col4.metric(label="Reverse Repo Rate (%)", value=rate0, delta=rate_delta)
st.subheader("")
st.markdown("_About Repo and Reverse Repo Agreements_ "
             "[link](https://www.newyorkfed.org/markets/domestic-market-operations/"
             "monetary-policy-implementation/repo-reverse-repo-agreements)")
st.subheader("")

# Reverse Repo chart
st.header("Reverse Repo Operations ($B)", divider='rainbow')
st.markdown(":orange[_Two Week Chart_]")
st.bar_chart(df1, x="Date", y="Reverse Repo", height=600, color='#0000FF')

# Repo chart
st.header("Repo Operations ($M)", divider='rainbow')
st.markdown(":orange[_Two Week Chart_]")
st.bar_chart(df2, x="Date", y="Repo", height=600, color='#cb00eb')

# Total chart
st.header("Total Repo and Reverse Repo Operations ($B)", divider='rainbow')
st.markdown(":orange[_Two Week Chart_]")
st.bar_chart(df3, x="Date", y="Total", height=600, color='#179555')
st.divider()
