
import streamlit as st
import random

st.set_page_config(page_title="YLOG: Ocean Risk Insurance Simulator", layout="wide")

# --- Custom CSS for a clean ocean-blue theme ---
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #e0f7fa;
        color: #004d40;
    }
    .stButton>button {
        background-color: #00838f;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stSlider>div>div {
        background-color: #b2ebf2;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🌊 YLOG: Ocean Risk Insurance Simulator")
st.subheader("Learn how insurance can help protect coral reefs and mangroves from extreme storms.")

st.markdown("---")

# --- SECTION 1: Educational Intro ---
with st.expander("🧠 Learn the Key Terms (Click to Expand)", expanded=False):
    st.markdown("""
    - **Premium**: The fee you pay regularly for insurance coverage. Think of it like a subscription that ensures fast response after disasters.
    - **Payout**: The amount of money you receive if the triggering event (like a storm) happens.
    - **Trigger Event**: A measurable event (e.g., wind speed over 100 knots) that determines if the insurance pays out.
    - **Basis Risk**: The risk that the trigger occurs but damage doesn’t, or vice versa—so the payout doesn’t match the actual loss.
    - **Parametric Insurance**: Fast-paying insurance based on pre-defined triggers, not lengthy damage assessments.
    """)

# --- SECTION 2: Design Insurance Policy ---
st.header("🔧 Step 1: Design Your Insurance Policy")

col1, col2 = st.columns(2)
with col1:
    reef_value = st.slider("🏝️ Ecosystem Value (in million USD)", 100, 1000, 500)
    premium_percent = st.slider("💰 Premium Rate (% of value)", 1, 15, 5)
    payout_percent = st.slider("💸 Payout Coverage (% of value)", 10, 100, 60)

with col2:
    storm_risk = st.selectbox("🌀 Storm Frequency Risk", ["Low", "Medium", "High"])
    trigger_speed = st.slider("🌬️ Trigger Wind Speed (knots)", 80, 160, 100)

st.markdown("💡 _Tip: Lower trigger speeds make insurance more likely to pay out but can increase premiums._")

# --- SECTION 3: Run Simulation ---
st.header("🌪️ Step 2: Simulate a Storm Event")
if st.button("Run Simulation"):
    st.markdown("🎲 Rolling the dice... a storm is forming over your reef!")
    risk_chances = {"Low": 0.2, "Medium": 0.5, "High": 0.8}
    storm_happens = random.random() < risk_chances[storm_risk]
    wind_speed = random.randint(70, 180)

    st.markdown(f"**Storm Wind Speed:** `{wind_speed}` knots")

    if storm_happens:
        st.error("A storm has hit your reef! 🌊")
        if wind_speed >= trigger_speed:
            payout = (payout_percent / 100) * reef_value
            st.success(f"✅ Trigger met! Insurance pays out **${payout:.2f} million** for ecosystem recovery.")
        else:
            st.warning("⚠️ Storm occurred but **did not meet the trigger threshold**. No payout was made. This is an example of **basis risk**.")
    else:
        st.success("☀️ No storm occurred. Your reef remains safe and healthy!")

# --- SECTION 4: Summary ---
st.header("📊 Step 3: Policy Summary")
premium_paid = (premium_percent / 100) * reef_value

st.markdown(f"- **Ecosystem Value**: `${reef_value} million`")
st.markdown(f"- **Premium Paid**: `${premium_paid:.2f} million`")
st.markdown(f"- **Trigger Point**: `{trigger_speed} knots`")
st.markdown(f"- **Potential Payout**: `{(payout_percent / 100) * reef_value:.2f} million`")

st.markdown("---")
st.caption("Designed for the Young Leaders in Ocean Governance Program • Powered by AXA & TNC case studies")
