
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df_fit is already processed and available from previous steps
# In a real Streamlit app, you would load or generate this data.
# For this example, we'll simulate it or assume it's loaded.

# --- Placeholder for df_fit and model (replace with actual loading/instantiation) ---
# In a real Streamlit app, you'd integrate your data loading and model logic
# For demonstration, we'll try to use the global df_fit if it exists, 
# otherwise create a dummy one.

# This part needs to be adapted for a standalone app. 
# You might save df_fit to a CSV/pickle and load it here, or rebuild it.
# For simplicity, if running this in Colab, this assumes df_fit is in memory.

try:
    # Access global df_fit if available (for Colab execution context)
    global df_fit
    if 'df_fit' not in locals() and 'df_fit' not in globals():
        st.error("df_fit not found. Please ensure it's generated in the notebook.")
        st.stop()
    st_df_fit = df_fit.copy()
except NameError:
    st.warning("df_fit not found in current environment. Creating dummy data for Streamlit demo.")
    st_df_fit = pd.DataFrame({
        'player_name': ['Player A', 'Player B', 'Player C', 'Player D'],
        'team_name': ['Team X', 'Team Y', 'Team X', 'Team Z'],
        'position': ['Attacker', 'Midfielder', 'Defender', 'Goalkeeper'],
        'age': [25, 28, 22, 30],
        'fit_score': [0.8, 0.7, 0.6, 0.5],
        'progression_index': [1.2, 1.5, 0.8, 0.1],
        'defensive_intensity': [0.3, 0.9, 1.1, 1.5],
        'attacking_output': [1.5, 0.7, 0.2, 0.0],
        'creativity': [0.9, 1.0, 0.4, 0.1],
        'duel_success_rate': [0.6, 0.7, 0.8, 0.5],
        'recruitment_score': [0.9, 0.8, 0.7, 0.6] # Add dummy recruitment score
    })


# --- Streamlit App Layout ---
st.title('⚽ SystemFit: Player Recruitment Dashboard')

st.markdown("""
This dashboard helps identify transfer targets based on a team's playing style.
It shows player 'fit scores' and attribute profiles.
""")

# Sidebar for filtering
st.sidebar.header('Filter Options')

team_to_analyze = st.sidebar.selectbox(
    'Select Your Team (Current Analysis):',
    st_df_fit['team_name'].unique()
)

position_filter = st.sidebar.multiselect(
    'Filter by Position:',
    st_df_fit['position'].unique(),
    default=st_df_fit['position'].unique()
)

min_fit_score = st.sidebar.slider(
    'Minimum Fit Score:',
    float(st_df_fit['fit_score'].min()), float(st_df_fit['fit_score'].max()),
    float(st_df_fit['fit_score'].quantile(0.75))
)

filtered_df = st_df_fit[
    (st_df_fit['team_name'] != team_to_analyze) & 
    (st_df_fit['position'].isin(position_filter)) & 
    (st_df_fit['fit_score'] >= min_fit_score)
].sort_values(by='fit_score', ascending=False)

st.header(f'Top Player Recommendations for {team_to_analyze}')

if not filtered_df.empty:
    st.dataframe(filtered_df[['player_name', 'team_name', 'position', 'age', 'fit_score', 
                                'progression_index', 'defensive_intensity', 'attacking_output']].head(10))
    
    st.subheader('Attribute Profile of Top Recommended Player')
    top_player = filtered_df.iloc[0]
    
    features_for_radar = [
        'progression_index', 'defensive_intensity', 'attacking_output',
        'creativity', 'duel_success_rate'
    ]
    
    # Normalize features for radar plot to be between 0 and 1 or -1 and 1
    # This is a simplified normalization; you might use the same scaler as in your model
    player_data_for_radar = top_player[features_for_radar]
    
    # Example: Simple min-max scaling for visualization purpose
    for col in features_for_radar:
        min_val = st_df_fit[col].min()
        max_val = st_df_fit[col].max()
        if (max_val - min_val) > 0:
            player_data_for_radar[col] = (player_data_for_radar[col] - min_val) / (max_val - min_val)
        else:
            player_data_for_radar[col] = 0.5 # Default if all values are the same

    categories = features_for_radar
    values = player_data_for_radar.values.flatten().tolist()
    values += values[:1]  # Complete the circle

    angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values, 'o-', linewidth=2, label=top_player['player_name'])
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8)
    ax.set_ylim(0, 1) # Radar chart values usually normalized 0-1
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    st.pyplot(fig)

else:
    st.info('No players match the current filters.')
