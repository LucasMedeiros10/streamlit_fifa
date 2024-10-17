import streamlit as st

st.set_page_config(page_title="Teams", page_icon="⚽", layout="wide")

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[df_data["Club"] == clube].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {clube}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", 
           "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns], 
             column_config={
                "Overall": st.column_config.ProgressColumn("Overall", min_value=0, max_value=100, format="%d"), 
                "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", min_value=0, max_value=df_filtered["Wage(£)"].max(), format="£%f"),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country") 
             })