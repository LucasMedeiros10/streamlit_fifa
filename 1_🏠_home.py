import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [GeBot](https://gebot.com.br)")

btn = st.button("Acesse os dados do Kaggle")

if btn:
    webbrowser.open_new_tab("https://gebot.com.br")

st.markdown("Lorem ipsum dolor sit amet. Qui galisum delectus non nesciunt galisum 33 quas tempora est voluptatem neque qui sequi nemo? Quo voluptatibus enim ut quibusdam quia id libero dolor vel excepturi obcaecati non autem galisum aut porro placeat? Qui iusto iure a molestias alias aut fugiat praesentium qui voluptatem facere ex nostrum voluptate qui rerum reiciendis in accusantium internos. </p><p>Eum atque soluta et asperiores libero qui fuga numquam rem impedit ipsum ut maiores pariatur et numquam blanditiis. Ad alias quia hic sint corporis sit repudiandae fugiat eos optio deleniti. </p><p>In dolorem omnis sit veritatis pariatur quo exercitationem facere. Non voluptatem quas eos distinctio quasi sed reprehenderit commodi et accusamus distinctio id repellendus adipisci. Est ratione rerum hic dolorum repellat ex veniam voluptatem et magni iure ut eveniet ipsam sit dolore provident et incidunt corrupti. Qui mollitia similique id saepe minus sit quod ratione sed animi nobis sed voluptas explicabo. ")    