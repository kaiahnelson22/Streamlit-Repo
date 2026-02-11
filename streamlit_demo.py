import streamlit as st
import pandas as pd
import numpy as np
st.title('Streamlit Demo')

df = pd.DataFrame({'Grace': [10000], 'Kaiah': [24800], 'Ashlee': [3543000]})

st.subheader('What type of staffing plan are you uploading?')
car = 'CAR'
mb = 'Major Rebaseline'
su = 'Standard Update'

choice = st.multiselect('Multiselect', [car, mb, su])
opp = 0

if choice == [car]:
    st.write("""Please enter your initial opportunity percentage.
    Please note that this percentage can only be changed in the future through a major rebaseline.""")
    opp_str = st.text_input('Opportunity Percentage')
    st.subheader('Current Staffing Plan:')
    st.write(df)
    if opp_str.strip() == '':
        opp = None
        # Warning suppressed: no box shown
    else:
        # Remove % sign and whitespace, handle conversion
        sanitized = opp_str.replace('%', '').strip()
        try:
            opp = float(sanitized)
            if '%' in opp_str:
                opp = opp / 100
        except ValueError:
            opp = None
            # Error suppressed: no box shown
elif choice == [mb]:
    st.write("""Please enter your updated opportunity percentage.
    Please note that this percentage can only be changed in the future through another major rebaseline.""")
    opp_str = st.text_input('Opportunity Percentage')
    st.subheader('Current Staffing Plan:')
    st.write(df)
    if opp_str.strip() == '':
        opp = None
        # Warning suppressed: no box shown
    else:
        # Remove % sign and whitespace, handle conversion
        sanitized = opp_str.replace('%', '').strip()
        try:
            opp = float(sanitized)
            if '%' in opp_str:
                opp = opp / 100
        except ValueError:
            opp = None
            # Error suppressed: no box shown
elif choice == [su]:
    st.write("No opportunity percentage changes are allowed during a standard update.")
    st.subheader('Current Staffing Plan:')
    st.write(df)

new_num = df
if (choice == [car] or choice == [mb]) and opp is not None:
    percent_str = f"{opp * 100}%"
    st.write("Your opportunity percentage is: " + percent_str)
    st.subheader('New Staffing Plan:')
    new_num = df * opp
    st.write(new_num)