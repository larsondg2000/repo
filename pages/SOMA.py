import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Get JSON Data from Federal Reserve
url = "https://markets.newyorkfed.org/api/soma/summary.json"
request = requests.get(url)
content = request.json()
soma_ops = (content['soma']['summary'])

# get data for metric chart
total0 = float(soma_ops[-1]['total']) / 1000000000
total1 = float(soma_ops[-2]['total']) / 1000000000
diff = total0 - total1

# get values for pie chart
list_of_values1 = list(soma_ops[-1].values())[1:-5]
list_of_values1 = [float(ele) for ele in list_of_values1]
list_of_values2 = list(soma_ops[-1].values())[6:-1]
list_of_values2 = [float(ele) for ele in list_of_values2]
total_values = (list_of_values1 + list_of_values2)

# Create list of keys
list_of_keys = ["Agency Mortgage-Backed Securities",
                "Agency Commercial Mortgage-Backed Securities",
                "US Treasury Inflation-Protected Securities (TIPS)",
                "US Treasury Floating Rate Notes (FRNs)",
                "US Treasury Notes and Bonds (Notes/Bonds)",
                "US Treasury Bills (T-Bills)",
                "Federal Agency Securities"]

soma_dict = {"Holdings": list_of_keys, "Amount": total_values}

# get current and start dates
date_soma_current = soma_ops[-1]['asOfDate']
date_soma_start = soma_ops[0]['asOfDate']

# create dataframe for bar chart and table
df = pd.DataFrame(soma_dict)

# data for line chart total holdings vs. date
soma_dates_list = [soma_ops[i]['asOfDate'] for i in range(len(soma_ops))]
soma_totals_list = [soma_ops[i]['total'] for i in range(len(soma_ops))]
soma_totals_list = [float(ele) for ele in soma_totals_list]

# create dictionary and df
totals_dict = {"Dates": soma_dates_list, "Total Holdings": soma_totals_list}
totals_df = pd.DataFrame(totals_dict)

# Setup page
st.set_page_config(layout="wide")

st.title("System Open Market Account (SOMA) Holdings of Domestic Securities")
st.title("")

st.header(f"Current Holdings as of {date_soma_current} ", divider='rainbow')

# metrics of total holdings and difference from last month
st.metric(label="Total SOMA Holdings ($Billion)", value=total0, delta=diff)
st.title("")
col1, col2 = st.columns(2)

# create table with securities held and amount
col1.dataframe(
    df,
    column_config={
        "Holdings": "Security",
        "Amount": "Amount"
    },
    hide_index=True,)

# bar chart of holdings
col2.bar_chart(df, x="Holdings", y="Amount", height=500, color='#179555')

st.header(f"Historical Holdings Totals from :blue[{date_soma_start}] to :blue[{date_soma_current}]", divider='rainbow')
st.title("")
st.line_chart(totals_df, x="Dates", y="Total Holdings", height=700, color='#0000FF')
st.divider()