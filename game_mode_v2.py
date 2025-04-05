
import streamlit as st
import random

st.set_page_config(page_title="🌊 YLOG Coastal Resilience Game", layout="wide")

# Initialize session state
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.score = 50
    st.session_state.ecosystem_health = 100
    st.session_state.funds = 0

# --- Custom Styling for Blue Background and Gamified Feel ---
st.markdown("""
<style>
body {
    background-color: #d0f0ff;
    color: #003b5c;
}
.stApp {
    background-color: #d0f0ff;
}
.stButton>button {
    background-color: #0077b6;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.5em 1em;
}
h1, h2, h3 {
    color: #00557f;
}
</style>
""", unsafe_allow_html=True)

# --- Onboarding and Educational Explanation ---
st.title("🌊 YLOG Ocean Risk Simulator: Coastal Resilience Game")
st.markdown("Welcome, future ocean leader! You are about to step into the shoes of a **Coastal Resilience Strategist** for the fictional island nation of **Azurea**.")

st.header("📘 Background")
st.markdown("""
Azurea’s coral reefs, mangroves, and coastal ecosystems are under growing threat from more intense storms and rising seas. To safeguard its people and nature, Azurea is considering **parametric insurance** as part of a climate risk strategy.

💡 **Parametric insurance** pays out not based on damage assessment, but on a *trigger event* (like a storm reaching a certain wind speed). This allows for faster disaster response — but introduces something called **basis risk**.

Here’s how it works:
- You select a **trigger threshold** (wind speed).
- You decide how much of the reef’s value will be **covered**.
- You decide how much **premium** to pay each year.

If a storm hits and exceeds the trigger — 💰 payout!
If not — you may still suffer damage, but receive no funds ⚠️

Your job is to balance protection, cost, and timing — while building resilience over 5 years.
""")

st.markdown("---")

# --- Interactive Game Section ---
st.header(f"🎮 Year {st.session_state.round}: Design Your Strategy")

reef_value = 500  # static for simplicity
col1, col2, col3 = st.columns(3)

with col1:
    premium = st.slider("💸 Premium (% of reef value)", 1, 15, 5, key="premium")
with col2:
    payout = st.slider("💰 Payout Coverage (% of reef value)", 20, 100, 60, key="payout")
with col3:
    trigger = st.slider("🌬️ Trigger Wind Speed (knots)", 80, 160, 110, key="trigger")

st.markdown("🧠 _Tip: Lower trigger = more likely to get payout, but higher premiums. Higher trigger = lower cost, more risk._")

# --- Simulate the Year ---
if st.button("▶️ Simulate Year"):
    st.session_state.round += 1
    storm_happens = random.random() < 0.6
    wind_speed = random.randint(70, 180)
    st.markdown(f"**🌪️ Actual Wind Speed This Year:** `{wind_speed} knots`")

    if storm_happens:
        st.error("⚠️ A major storm impacted Azurea’s coast!")
        if wind_speed >= trigger:
            payout_amount = (payout / 100) * reef_value
            st.success(f"✅ Insurance triggered! You received ${payout_amount:.2f} million.")
            st.session_state.funds += payout_amount
            st.session_state.score += 5
        else:
            st.warning("🚫 Storm hit, but insurance didn’t trigger. Basis risk realized.")
            st.session_state.ecosystem_health -= 15
            st.session_state.score -= 5
    else:
        st.success("☀️ No storms this year — a peaceful season.")
        st.session_state.score += 2

st.markdown("---")

# --- Scoreboard ---
st.header("📊 Dashboard")
st.markdown(f"- 🧭 Year: `{st.session_state.round}` / 5")
st.markdown(f"- 🌿 Ecosystem Health: `{st.session_state.ecosystem_health}` / 100")
st.markdown(f"- 💰 Recovery Funds: `${st.session_state.funds}` million")
st.markdown(f"- 🎯 Resilience Score: `{st.session_state.score}` / 100")

# --- Game End ---
if st.session_state.round > 5:
    st.balloons()
    st.header("🏁 Simulation Complete!")
    st.markdown(f"🌿 Final Ecosystem Health: `{st.session_state.ecosystem_health}`")
    st.markdown(f"💰 Total Recovery Funds: `${st.session_state.funds}` million")
    st.markdown(f"🎯 Final Resilience Score: `{st.session_state.score}` / 100")

    if st.session_state.score >= 80:
        st.success("🏆 Excellent strategy! Azurea’s coast is well protected.")
    elif st.session_state.score >= 50:
        st.info("👏 Decent effort — but Azurea remains vulnerable.")
    else:
        st.error("❌ The coast suffered significantly. Rework your strategy next time.")

    if st.button("🔄 Restart Simulation"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
