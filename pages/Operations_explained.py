import streamlit as st
import matplotlib.pyplot as plt

# Page title
st.set_page_config(layout="wide", page_title="Repo Operations Explained", page_icon=":material/currency_exchange:")
st.title(":rainbow[Federal Reserve: Repo and Reverse Repo Operations Explained]")
st.divider()

# Section 1: Introduction
st.header("Introduction to Repo and Reverse Repo Operations")
st.write("""
The Federal Reserve conducts repo (repurchase agreements) and reverse repo (reverse repurchase agreements) operations 
to manage short-term liquidity in the financial system. These are critical tools for maintaining stability in the 
money markets and achieving the Federal Reserve's monetary policy goals.

In simple terms:
- **Repo**: The Federal Reserve provides short-term loans to financial institutions, using securities as collateral.
- **Reverse Repo**: The Federal Reserve borrows money from financial institutions and provides securities as collateral.
""")
st.divider()

# Section 2: What is a Repo Operation?
st.header("What is a Repo Operation?")
st.write("""
In a repo (repurchase agreement), the Federal Reserve buys securities from financial institutions and agrees to sell 
them back later at a slightly higher price. This transaction effectively works as a short-term loan, where the Fed 
injects liquidity into the banking system.

- **Example**: A bank sells \$100 million in Treasury securities to the Fed and agrees to repurchase them the next 
day for \$100.1 million.
- The extra \$0.1 million represents the interest on the loan.

This is typically used when the Federal Reserve wants to increase the money supply in the economy temporarily.
""")
st.divider()

# Repo operation illustration
st.subheader("Repo Operation Illustration")
repo_diagram = """
Step 1: Bank -> (Sells $100 million in Treasuries) -> Fed \n
Step 2: Fed -> (Provides $100 million in cash) -> Bank \n
Step 3: Bank -> (Repurchases Treasuries for $100.1 million) -> Fed \n
Step 4: Fed -> (Receives $100.1 million in cash) -> Bank
"""
st.code(repo_diagram, language='plain')
st.divider()

# Section 3: What is a Reverse Repo Operation?
st.header("What is a Reverse Repo Operation?")
st.write("""
In a reverse repo (reverse repurchase agreement), the Federal Reserve sells securities to financial institutions and 
agrees to buy them back later at a higher price. In this case, the Fed borrows money from the institutions and 
provides securities as collateral.

- **Example**: The Fed sells \$100 million in Treasury securities to a bank and agrees to repurchase them the next day 
for \$100.1 million.
- The extra \$0.1 million is the interest paid by the Fed.

This is used when the Federal Reserve wants to reduce the money supply in the economy temporarily.
""")
st.divider()

# Reverse Repo operation illustration
st.subheader("Reverse Repo Operation Illustration")
reverse_repo_diagram = """
Step 1: Fed -> (Sells $100 million in Treasuries) -> Bank \n
Step 2: Bank -> (Provides $100 million in cash) -> Fed \n
Step 3: Fed -> (Repurchases Treasuries for $100.1 million) -> Bank \n
Step 4: Bank -> (Receives $100.1 million in cash) -> Fed
"""
st.code(reverse_repo_diagram, language='plain')
st.divider()

# Section 4: Why Are Repo and Reverse Repo Important?
st.header("Importance of Repo and Reverse Repo Operations")
st.write("""
Repo and reverse repo operations are essential for controlling liquidity in the banking system:
- **Repo operations**: Add liquidity to the system, enabling banks to meet short-term needs without impacting longer-term interest rates.
- **Reverse repo operations**: Drain liquidity, preventing excess cash from flooding markets and potentially lowering short-term interest rates too much.

These tools help the Federal Reserve maintain its target for the federal funds rate, a key interest rate that influences 
other rates across the economy. By controlling the availability of liquidity, the Fed can steer the economy towards its 
goals of price stability and full employment.
""")
st.divider()

# Section 5: Illustrated Examples of Repo and Reverse Repo
st.subheader("Example of Repo and Reverse Repo")

# Repo Diagram
st.image("repo_example.png")

# Footer
st.write("This page is part of a project explaining key Federal Reserve operations.")
