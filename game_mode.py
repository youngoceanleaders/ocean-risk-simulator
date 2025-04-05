
import streamlit as st
import random

st.set_page_config(page_title="🌊 Ocean Risk Game Mode", layout="wide")

# Initialize session state
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.score = 50
    st.session_state.ecosystem_health = 100
    st.session_state.funds = 0

# --- Custom Styling ---
st.markdown("""
<style>
body {
    background-color: #e0f7fa;
    color: #004d40;
}
.stButton>button {
    background-color: #00838f;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --- Title & Role ---
st.title("🎮 Ocean Risk Simulator: Game Mode")
st.markdown("You are the **Minister of Coastal Resilience** for the Island of Azurea. Your mission is to protect your ecosystem and economy from unpredictable climate shocks over 5 years.")

# --- Scoreboard ---
st.markdown("### 📊 Your Dashboard")
st.markdown(f"- 🔁 Year: `{st.session_state.round}` / 5")
st.markdown(f"- 🌿 Ecosystem Health: `{st.session_state.ecosystem_health}` / 100")
st.markdown(f"- 💰 Recovery Funds: `${st.session_state.funds} million`")
st.markdown(f"- 🎯 Resilience Score: `{st.session_state.score}` / 100")
st.markdown("---")

# --- Scenario Text ---
st.markdown("### 🔧 Choose Your Insurance Strategy This Year")
reef_value = 500  # static for now
premium = st.slider("💸 Premium (% of reef value)", 1, 15, 5, key="premium")
payout = st.slider("💰 Payout Coverage (% of reef value)", 20, 100, 60, key="payout")
trigger = st.slider("🌬️ Trigger Threshold (wind knots)", 80, 160, 110, key="trigger")

# --- Run Year Button ---
if st.button("▶️ Run This Year's Simulation"):
    st.session_state.round += 1
    storm_happens = random.random() < 0.6
    wind_speed = random.randint(70, 180)
    st.markdown(f"**🌀 Storm Wind Speed:** `{wind_speed} knots`")

    if storm_happens:
        st.error("🌪️ A storm hits your coast!")
        if wind_speed >= trigger:
            funds_received = (payout / 100) * reef_value
            st.success(f"✅ Insurance triggered! You receive ${funds_received:.2f} million.")
            st.session_state.funds += funds_received
            st.session_state.score += 5
        else:
            st.warning("⚠️ Insurance did not trigger. Your ecosystem took damage.")
            st.session_state.ecosystem_health -= 10
            st.session_state.score -= 5
    else:
        st.success("☀️ No major events this year. A peaceful season!")
        st.session_state.score += 2

    st.markdown("---")

# --- Game Over ---
if st.session_state.round > 5:
    st.balloons()
    st.markdown("## 🏁 Simulation Complete!")
    st.markdown(f"### 🌿 Final Ecosystem Health: `{st.session_state.ecosystem_health}`")
    st.markdown(f"### 💰 Total Funds Secured: `${st.session_state.funds}` million")
    st.markdown(f"### 🎯 Final Resilience Score: `{st.session_state.score}` / 100")
    if st.session_state.score >= 80:
        st.success("Incredible work! You built a highly resilient coast!")
    elif st.session_state.score >= 50:
        st.info("You did okay, but there's room for improvement.")
    else:
        st.error("Your coast suffered. Time to revisit your risk strategy.")

    if st.button("🔄 Restart Simulation"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
