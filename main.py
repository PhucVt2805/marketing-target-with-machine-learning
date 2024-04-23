import joblib
import numpy as np
import streamlit as st

def predict(model, data):
    for k in encode_dict.keys():
        data[k] = encode_dict[k].index(data[k])
    return model.predict([list(data.values())])

def run():
    st.set_page_config(
        page_title="Term deposit prediction system",
        page_icon="💵",
    )

    st.write("# :rainbow[The system predicts customers who register for term deposits]")

    with st.form('data', clear_on_submit=True):
        st.write(':rainbow[Please fill in the form completely and accurately with customer information!]')

        age = st.slider(':blue[Age:]', 0, 150)
        job = st.selectbox(':blue[Work:]', ["admin.", "unemployed", "management", "housemaid", "entrepreneur", "student", "blue-collar", "self-employed", "retired", "technician", "services", "unknown"], index=11)
        marital = st.selectbox(':blue[Marital status:]', ["married", "divorced","single"], index=2)
        education = st.selectbox(':blue[Education level:]', ["primary", "secondary","tertiary","unknown"], index=3)
        balance = st.number_input(':blue[Average annual balance(€):]', value=0, step=100)
        contact = st.selectbox(':blue[Contact]', ["telephone", "cellular", "unknown"], index=2)
        date = st.date_input(':blue[Last contact date:]', format='DD/MM/YYYY')
        day = date.day
        convert_month = [None, 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        month = convert_month[date.month]
        duration = st.number_input(':blue[Last contact time (seconds):]', value=0, min_value=0, step=1)
        campaign = st.number_input(':blue[Number of contacts made in this campaign and to this account (including last contact):]', value=1, min_value=1, step=1)
        pdays = st.number_input(':blue[Number of days since last contact with a customer from a previous campaign (-1 for customers who have not been contacted before)]', value=-1, min_value=-1, step=1)
        previous = st.number_input(':blue[Number of contacts made before the campaign for this customer]', value=0, min_value=0, step=1) 
        poutcome = st.selectbox('Results of previous marketing campaigns', ["success","other","failure","unknown"], index=3)
        default = st.checkbox('Default credit')
        housing = st.checkbox('Home loan')
        loan = st.checkbox('Personal loan')

        submitted = st.form_submit_button("Check")
        if submitted:
            data = {
                'age': age,
                'job': job,
                'marital': marital,
                'education': education,
                'default': 1 if default else 0,
                'balance': balance,
                'housing': 1 if housing else 0,
                'loan': 1 if loan else 0,
                'contact': contact,
                'day': day,
                'month': month,
                'duration': duration,
                'campaign': campaign,
                'pdays': pdays,
                'previous': previous,
                'poutcome': poutcome
            }
            result = predict(model, data)
            result = 'feasible' if result == 1 else 'not feasible'
            st.divider()
            st.subheader(f'The possibility of customers registering for term deposits is {result}.')

if __name__ == "__main__":
    model, encode_dict = joblib.load('model.joblib')
    run()
