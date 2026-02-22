import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('f1_podium_model.pkl')

# Page config
st.set_page_config(page_title="F1 Podium Predictor", page_icon="🏎️", layout="wide")

st.title('🏎️ F1 Podium Predictor')
st.markdown('Predict podium probability based on grid position and team')

# All teams
teams = {
    'Red Bull Racing': {'top': True, 'color': '#1E41FF'},
    'Ferrari': {'top': True, 'color': '#DC0000'},
    'McLaren': {'top': True, 'color': '#FF8700'},
    'Mercedes': {'top': True, 'color': '#00D2BE'},
    'Aston Martin': {'top': False, 'color': '#006F62'},
    'Alpine': {'top': False, 'color': '#0090FF'},
    'Williams': {'top': False, 'color': '#005AFF'},
    'RB': {'top': False, 'color': '#2B4562'},
    'Kick Sauber': {'top': False, 'color': '#52E252'},
    'Haas': {'top': False, 'color': '#B6BABD'}
}

# Grand Prix circuits
circuits = {
    'Bahrain Grand Prix': '🇧🇭 Sakhir',
    'Saudi Arabian Grand Prix': '🇸🇦 Jeddah',
    'Australian Grand Prix': '🇦🇺 Melbourne',
    'Japanese Grand Prix': '🇯🇵 Suzuka',
    'Chinese Grand Prix': '🇨🇳 Shanghai',
    'Miami Grand Prix': '🇺🇸 Miami',
    'Emilia Romagna Grand Prix': '🇮🇹 Imola',
    'Monaco Grand Prix': '🇲🇨 Monaco',
    'Canadian Grand Prix': '🇨🇦 Montreal',
    'Spanish Grand Prix': '🇪🇸 Barcelona',
    'Austrian Grand Prix': '🇦🇹 Spielberg',
    'British Grand Prix': '🇬🇧 Silverstone',
    'Hungarian Grand Prix': '🇭🇺 Budapest',
    'Belgian Grand Prix': '🇧🇪 Spa',
    'Dutch Grand Prix': '🇳🇱 Zandvoort',
    'Italian Grand Prix': '🇮🇹 Monza',
    'Azerbaijan Grand Prix': '🇦🇿 Baku',
    'Singapore Grand Prix': '🇸🇬 Marina Bay',
    'United States Grand Prix': '🇺🇸 Austin',
    'Mexico City Grand Prix': '🇲🇽 Mexico City',
    'São Paulo Grand Prix': '🇧🇷 Interlagos',
    'Las Vegas Grand Prix': '🇺🇸 Las Vegas',
    'Qatar Grand Prix': '🇶🇦 Lusail',
    'Abu Dhabi Grand Prix': '🇦🇪 Yas Marina'
}

# Sidebar for inputs
st.sidebar.header('Race Settings')

# Circuit selection
selected_gp = st.sidebar.selectbox('Select Grand Prix', list(circuits.keys()))
st.sidebar.markdown(f"**Track:** {circuits[selected_gp]}")

st.sidebar.markdown('---')
st.sidebar.header('Driver Settings')

# Grid position
grid_position = st.sidebar.slider('Grid Position', 1, 20, 1)

# Team selection with buttons
st.sidebar.markdown('**Select Team:**')
selected_team = st.sidebar.radio('Team', list(teams.keys()), label_visibility='collapsed')

# Determine if top team
is_top_team = 1 if teams[selected_team]['top'] else 0

# Make prediction
X_input = pd.DataFrame({'GridPosition': [grid_position], 'IsTopTeam': [is_top_team]})
prob = model.predict_proba(X_input)[0][1]

# Display results
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f'📍 {selected_gp}')
    st.markdown(f"**Circuit:** {circuits[selected_gp]}")
    
    st.markdown('---')
    
    st.subheader('Prediction')
    st.markdown(f"**Team:** {selected_team}")
    st.markdown(f"**Starting Position:** P{grid_position}")
    
    # Big probability display
    if prob >= 0.5:
        st.success(f"### 🏆 Podium Probability: {prob:.1%}")
    elif prob >= 0.25:
        st.warning(f"### 📊 Podium Probability: {prob:.1%}")
    else:
        st.info(f"### 📊 Podium Probability: {prob:.1%}")

with col2:
    st.subheader('Quick Reference')
    st.markdown('''
    **Top Teams (2022 baseline):**
    - 🔵 Red Bull Racing
    - 🔴 Ferrari
    - 🟠 McLaren
    - 🩵 Mercedes
    
    **Model Info:**
    - Trained on 2022 data
    - Tested on 2024 data
    - 90.5% accuracy
    ''')

# Full grid prediction
st.markdown('---')
st.subheader('📊 Full Grid Prediction')

if st.button('Predict All 20 Drivers'):
    # Simulate a typical grid
    drivers = [
        ('VER', 'Red Bull Racing', 1),
        ('PER', 'Red Bull Racing', 4),
        ('LEC', 'Ferrari', 2),
        ('SAI', 'Ferrari', 3),
        ('NOR', 'McLaren', 5),
        ('PIA', 'McLaren', 7),
        ('HAM', 'Mercedes', 6),
        ('RUS', 'Mercedes', 8),
        ('ALO', 'Aston Martin', 9),
        ('STR', 'Aston Martin', 14),
        ('GAS', 'Alpine', 11),
        ('OCO', 'Alpine', 13),
        ('ALB', 'Williams', 12),
        ('SAR', 'Williams', 18),
        ('TSU', 'RB', 10),
        ('RIC', 'RB', 15),
        ('BOT', 'Kick Sauber', 16),
        ('ZHO', 'Kick Sauber', 19),
        ('MAG', 'Haas', 17),
        ('HUL', 'Haas', 20)
    ]
    
    results = []
    for driver, team, grid in drivers:
        is_top = 1 if teams[team]['top'] else 0
        X = pd.DataFrame({'GridPosition': [grid], 'IsTopTeam': [is_top]})
        p = model.predict_proba(X)[0][1]
        results.append({'Driver': driver, 'Team': team, 'Grid': grid, 'Podium %': f"{p:.1%}"})
    
    results_df = pd.DataFrame(results).sort_values('Podium %', ascending=False)
    st.dataframe(results_df, use_container_width=True, hide_index=True)