import streamlit as st
import pandas as pd
import requests
import xml.etree.ElementTree as ET
import yaml

try:
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)
except:
    print("Yaml configuration file not found!")

# --- Load your dataset ---
boardgames_df = pd.read_csv(config['output_data']['file'])

# --- Image Fetcher using BoardGameGeek XML API ---
def fetch_bgg_image(game_name):
    search_url = f"https://boardgamegeek.com/xmlapi2/search?query={game_name}&type=boardgame"
    try:
        search_response = requests.get(search_url)
        root = ET.fromstring(search_response.content)
        first_item = root.find("item")
        if first_item is not None:
            game_id = first_item.attrib["id"]
            thing_url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}&stats=1"
            thing_response = requests.get(thing_url)
            thing_root = ET.fromstring(thing_response.content)
            image_tag = thing_root.find(".//image")
            if image_tag is not None:
                return image_tag.text
    except Exception as e:
        print(f"Error fetching image for {game_name}: {e}")
    return None

# --- Streamlit UI ---
st.title("🎲 Board Game Recommender")
st.write("Find the best board games for your session based on your preferences.")

# --- User Inputs ---
playtime = st.slider("⏱️ Desired playtime (minutes)", 0, 1200, 30)
number_players = st.slider("👥 Number of players", 1, 100, 2)
min_age = st.slider("🧒 Age of youngest player", 0, 18)
min_age = st.slider("🧒 Age of youngest player", 4, 18, 12)
difficulty_level = st.selectbox("🧠 Desired difficulty level", [1, 2, 3, 4], format_func=lambda x: ["Easy", "Medium", "Hard", "Very Hard"][x-1])
complexity = float(difficulty_level)

# --- Filter Logic ---
filtered_df = boardgames_df[
    (boardgames_df['min_playtime'] <= playtime) &
    (boardgames_df['max_playtime'] >= playtime) &
    (boardgames_df['min_players'] <= number_players) &
    (boardgames_df['max_players'] >= number_players) &
    (boardgames_df['minimum_age'] <= min_age) &
    (boardgames_df['complexity'] <= complexity + 1) &
    (boardgames_df['complexity'] >= complexity)
]

filtered_df_ranked = filtered_df.sort_values(by="avg_rating", ascending=False)

# --- Display Results ---
if filtered_df_ranked.empty:
    st.warning("⚠️ No games match all criteria. Try relaxing one or more inputs.")
else:
    st.subheader("🔥 Top 5 Matching Games")
    for _, row in filtered_df_ranked.head(5).iterrows():
        st.markdown(f"### {row['boardgame']}")
        st.write(f"⭐ Rating: {row['avg_rating']} | 👥 Players: {row['min_players']}–{row['max_players']} | ⏱️ Playtime: {row['min_playtime']}–{row['max_playtime']} mins | 🧠 Complexity: {row['complexity']}")
        img_url = fetch_bgg_image(row['boardgame'])
        if img_url:
            st.image(img_url, width=250)
        else:
            st.info("No image found.")

