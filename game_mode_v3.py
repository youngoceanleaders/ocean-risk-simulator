
import streamlit as st
import random

st.set_page_config(page_title="🌊 YLOG: Ocean Risk Simulator – Game Mode v3", layout="wide")

# Initialize session state
if "region" not in st.session_state:
    st.session_state.round = 0
    st.session_state.score = 50
    st.session_state.ecosystem_health = 100
    st.session_state.funds = 0
    st.session_state.region = None
    st.session_state.role = None

# --- Styling for polished look ---
st.markdown("""
<style>
body {
    background-color: #e8f6ff;
    color: #002c3e;
}
.stApp {
    background-color: #e8f6ff;
}
.stButton>button {
    background-color: #0077b6;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.5em 1em;
}
h1, h2, h3 {
    color: #003b5c;
}
</style>
""", unsafe_allow_html=True)

st.title("🌊 YLOG Ocean Risk Simulator: Game Mode v3")

# --- Step 1: Select Region and Role ---
if st.session_state.region is None or st.session_state.role is None:
    st.header("🌍 Choose Your Scenario")

    col1, col2 = st.columns(2)
    with col1:
        region = st.radio("🌐 Select Your Region", ["Bermuda", "Belize", "Indonesia"])
    with col2:
        role = st.radio("👤 Choose Your Role", ["Minister of Coastal Resilience", "Insurance Advisor", "Marine NGO Officer"])

    if st.button("✅ Start Simulation"):
        st.session_state.region = region
        st.session_state.role = role
        if region == "Bermuda":
            st.session_state.storm_chance = 0.4
            st.session_state.reef_value = 700
        elif region == "Belize":
            st.session_state.storm_chance = 0.6
            st.session_state.reef_value = 500
        else:
            st.session_state.storm_chance = 0.7
            st.session_state.reef_value = 400
        st.experimental_rerun()
    st.stop()

# --- Step 2: Onboarding Panel ---
if st.session_state.round == 0:
    st.header("📘 Introduction: How Does Ocean Risk Insurance Work?")
    st.markdown("""
**Parametric insurance** helps vulnerable coasts recover faster after climate disasters like hurricanes. It’s based on **trigger events** – for example, wind speeds hitting a certain threshold.

When that happens, funds are released **immediately** – no long damage assessments required.

We’re using this simulator to teach:
- 📏 **Trigger Thresholds**
- 💸 **Premiums and Payouts**
- ⚠️ **Basis Risk** (when payouts don’t match actual damage)
- 🌿 **Ecosystem Resilience Management**

Below is a real-world flowchart from The Nature Conservancy (TNC) on how this model works:
""")

    st.image("https://raw.githubusercontent.com/YLOGsim/assets/main/trust_fund_flow.png", caption="Payout Flow: How Insurance Works in Reef Programs", use_column_width=True)

    if st.button("🚀 Start Year 1"):
        st.session_state.round = 1
        st.experimental_rerun()
    st.stop()

# --- Step 3: Simulation Loop (Year 1 to 5) ---
st.header(f"🗓️ Year {st.session_state.round} Simulation")

reef_value = st.session_state.reef_value
col1, col2, col3 = st.columns(3)
with col1:
    premium = st.slider("💸 Premium (% of reef value)", 1, 15, 5)
with col2:
    payout = st.slider("💰 Payout Coverage (% of reef value)", 20, 100, 60)
with col3:
    trigger = st.slider("🌬️ Trigger Wind Speed (knots)", 80, 160, 110)

if st.button("🎲 Simulate Storm Event"):
    wind_speed = random.randint(70, 180)
    st.markdown(f"**🌪️ Wind Speed This Year:** `{wind_speed} knots`")
    storm_occurs = random.random() < st.session_state.storm_chance

    if storm_occurs:
        st.error("🚨 A storm hits your coastline!")
        if wind_speed >= trigger:
            payout_amt = (payout / 100) * reef_value
            st.success(f"✅ Trigger met! You receive a payout of ${payout_amt:.2f} million.")
            st.session_state.funds += payout_amt
            st.session_state.score += 6
        else:
            st.warning("⚠️ Trigger not met — no payout. Basis risk realized.")
            st.session_state.ecosystem_health -= 15
            st.session_state.score -= 4
    else:
        st.success("☀️ No storm this year. A season of peace.")
        st.session_state.score += 2

    st.session_state.round += 1
    st.markdown("---")

# --- Dashboard ---
st.header("📊 Your Dashboard")
st.markdown(f"- 🌎 Region: **{st.session_state.region}**")
st.markdown(f"- 👤 Role: **{st.session_state.role}**")
st.markdown(f"- 🧭 Year: `{min(st.session_state.round, 5)}` / 5")
st.markdown(f"- 🌿 Ecosystem Health: `{st.session_state.ecosystem_health}` / 100")
st.markdown(f"- 💰 Recovery Funds: `${st.session_state.funds}` million")
st.markdown(f"- 🎯 Resilience Score: `{st.session_state.score}` / 100")

# --- Final Report ---
if st.session_state.round > 5:
    st.balloons()
    st.header("🏁 Simulation Complete")
    st.subheader("📋 Final Report Card")
    st.markdown(f"- 🌿 **Ecosystem Health**: `{st.session_state.ecosystem_health}`")
    st.markdown(f"- 💰 **Total Funds Secured**: `${st.session_state.funds}` million")
    st.markdown(f"- 🎯 **Resilience Score**: `{st.session_state.score}` / 100")

    if st.session_state.score >= 80:
        st.success("🏆 Outstanding job! You've led your region to climate resilience.")
    elif st.session_state.score >= 50:
        st.info("👏 A solid foundation, but improvement needed.")
    else:
        st.error("⚠️ Your coast suffered. Consider reviewing your strategy.")

    if st.button("🔁 Restart Simulation"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
