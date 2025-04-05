
import streamlit as st
import random

st.set_page_config(page_title="Ocean Risk Simulator", layout="wide")

st.markdown("""
<style>
    body {
        background-color: #e0f7fa;
        color: #01579b;
    }
    .stButton>button {
        background-color: #4fc3f7;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌊 Reef & Mangrove Parametric Insurance Simulator")

st.markdown("Welcome to the first module of the **YLOG Ocean Finance Simulator**. "
            "In this simulation, you will design an insurance product for a coastal ecosystem and respond to climate events.")

# --- Insurance Setup ---
st.header("🔧 Design Your Insurance Product")

reef_value = st.slider("🌴 Ecosystem Value (in million USD)", 100, 1000, 500)
storm_risk = st.selectbox("🌀 Storm Frequency Risk", ["Low", "Medium", "High"])
premium_percent = st.slider("💰 Insurance Premium (% of value)", 1, 15, 5)
payout_percent = st.slider("💸 Insurance Payout (% of value)", 10, 100, 50)
trigger_speed = st.slider("🌬️ Trigger Wind Speed (knots)", 80, 160, 100)

# --- Simulation ---
st.header("🌪️ Simulate a Storm Event")

if st.button("Run Simulation"):
    storm_speed = random.randint(70, 180)
    st.markdown(f"**Storm Wind Speed:** {storm_speed} knots")
    
    if storm_speed >= trigger_speed:
        payout = (payout_percent / 100) * reef_value
        st.success(f"Insurance triggered! 🌊 You receive ${payout:.2f} million to restore the ecosystem.")
    else:
        st.warning("No payout triggered. The storm was not intense enough.")

# --- Summary ---
st.header("📊 Summary of Your Policy")
st.write(f"**Ecosystem Value:** ${reef_value} million")
st.write(f"**Premium Paid:** ${(premium_percent / 100) * reef_value:.2f} million")
st.write(f"**Trigger Point:** {trigger_speed} knots")
