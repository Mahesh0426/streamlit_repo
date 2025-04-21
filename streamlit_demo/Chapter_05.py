# import streamlit as st
# import requests

# st.title("Currency to NPR Converter App")

# # Select the currency the user has
# source_currency = st.selectbox("Select your currency", ["USD", "EUR", "GBP", "INR", "AUD", "JPY"])
# amount = st.number_input(f"Enter the amount in {source_currency}", min_value=1.0, format="%f")

# if st.button("Convert to NPR"):
#     url = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         rate_to_npr = data["rates"].get("NPR")

#         if rate_to_npr:
#             converted_amount = amount * rate_to_npr
#             st.success(f"{amount} {source_currency} is equal to {converted_amount:.2f} NPR")
#         else:
#             st.error("NPR conversion rate not available.")
#     else:
#         st.error("Failed to fetch exchange rates.")



import streamlit as st
import requests

st.title("Universal Currency Converter 💱")

# List of currencies
currencies = ["NPR", "USD", "EUR", "GBP", "INR", "AUD", "JPY", "CAD", "CHF", "CNY"]

# Currency selection
source_currency = st.selectbox("From", currencies)
target_currency = st.selectbox("To", currencies)

# Amount input
amount = st.number_input(f"Enter the amount in {source_currency}", min_value=1.0, format="%f")

# Convert button
if st.button("Convert"):
    if source_currency == target_currency:
        st.info("Source and target currencies are the same. Converted amount is the same.")
    else:
        url = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rate = data["rates"].get(target_currency)

            if rate:
                converted_amount = amount * rate
                st.success(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
            else:
                st.error(f"Exchange rate not available for {target_currency}")
        else:
            st.error("Failed to fetch exchange rates. Try again later.")
