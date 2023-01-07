import streamlit as st
import pickle
import numpy as np
import pandas as pd
from nba_logos import logos

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# data = load_model()

# model = data["model"]
# df = data["data"]
# home_pred = data["home"]
# away_pred = data["away"]

def get_data(team, home=True):
    team_groups = df.groupby('team')

    team_group = team_groups.get_group(team).iloc[-1]
    
    if home is True:
        team_group = team_group[home_pred]
    else:
        team_group = team_group[away_pred]

    return team_group

def show_predict_page():
    st.title("Predict NBA Games")

    st.write("""### Choose two teams""")
    teams = {
        "POR"
        "PHI",
        "PHO",
        "SAC",
        "DEN",
        "ORL",
        "GSW",
        "DET",
        "MIL",
        "CHI",
        "WAS",
        "MIA",
        "LAL",
        "NOP",
        "ATL",
        "BRK",
        "MIN",
        "UTA",
        "IND",
        "SAS",   
        "CLE",
        "NYK",
        "TOR",
        "CHO",
        "HOU",
        "DAL",
        "BOS",
        "MEM",
        "LAC",
        "OKC"
    }

    col1, col2 = st.columns(2)

    with col1:
        home_selection = st.selectbox("Home", teams)

    with col2:
        away_selection = st.selectbox("Away", teams)


    ok = st.button("PREDICT")

    if ok:
        home_data = get_data(home_selection)
        away_data = get_data(away_selection, home=False)
        input = pd.concat([home_data, away_data.rename(index={col: col + '_opp' for col in away_data.index})])
        spread = model.predict([input])[0]
        st.header(f"The predicted spread is {spread}")
        if spread > 0:
            st.write(f"{home_selection} will win by {abs(spread)}")
            st.image(logos[home_selection], width=500)
        else:
            st.write(f"{away_selection} will win by {abs(spread)}")
            st.image(logos[away_selection], width=500)
        return