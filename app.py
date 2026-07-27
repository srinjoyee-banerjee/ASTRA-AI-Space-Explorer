
import streamlit as st
import pandas as pd
import joblib
import random
from datetime import datetime

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="ASTRA AI Space Explorer",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(180deg,#020111,#071c38,#102a43,#183b56);
color:white;
}

h1,h2,h3{
text-align:center;
color:#8fd3ff;
}

div.stButton > button{
width:100%;
height:60px;
font-size:22px;
font-weight:bold;
border-radius:12px;
background:#1565C0;
color:white;
}

div.stButton > button:hover{
background:#0D47A1;
}

[data-testid="stMetric"]{
background:#10253f;
padding:12px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODELS
# ---------------------------------------------------
rf_model = joblib.load("random_forest_model.pkl")
encoder = joblib.load("label_encoder.pkl")
data = pd.read_csv("sample_objects.csv")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.title("🌌 ASTRA : AI SPACE EXPLORER")

st.markdown("""
### 🚀 Artificial Intelligence Powered Deep Space Scanner

Explore real astronomical objects from the Sloan Digital Sky Survey.

ASTRA analyzes celestial objects using Machine Learning.
""")

st.divider()

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------
if st.button("🚀 START MISSION"):

    mission = random.randint(1000,9999)

    obj = data.sample(1)

    features = [
        "alpha",
        "delta",
        "u",
        "g",
        "r",
        "i",
        "z",
        "redshift"
    ]

    X = obj[features]

    prediction = rf_model.predict(X)
    probability = rf_model.predict_proba(X)

    confidence = probability.max()*100

    object_name = encoder.inverse_transform(prediction)[0]

    st.success(f"🚀 Mission #{mission}")
    st.success("🔭 Deep Space Scan Successful")

    st.divider()

    # ---------------------------------------------------
    # SCANNER DATA
    # ---------------------------------------------------

    st.header("📡 Scanner Readings")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("🌍 Sky Direction",f"{obj['alpha'].iloc[0]:.2f}°")
    c2.metric("🌌 Sky Elevation",f"{obj['delta'].iloc[0]:.2f}°")
    c3.metric("🚀 Distance Index",f"{obj['redshift'].iloc[0]:.3f}")
    c4.metric("🤖 AI Confidence",f"{confidence:.2f}%")

    c5,c6,c7,c8 = st.columns(4)

    c5.metric("🔵 UV",f"{obj['u'].iloc[0]:.2f}")
    c6.metric("🟢 Visible",f"{obj['g'].iloc[0]:.2f}")
    c7.metric("🔴 Red",f"{obj['r'].iloc[0]:.2f}")
    c8.metric("🌑 Infrared",f"{obj['i'].iloc[0]:.2f}")

    st.metric("🌠 Deep Infrared",f"{obj['z'].iloc[0]:.2f}")

    st.divider()

    # ---------------------------------------------------
    # RESULT
    # ---------------------------------------------------

    if object_name=="GALAXY":

        icon="🌌"
        name="Deep Space Galaxy"
        threat="🟢 LOW"
        energy="Stable"

        report="""
Billions of stars detected.

Object appears gravitationally stable.

Safe for observation.
"""

        fact="🌌 Galaxies may contain hundreds of billions of stars."

    elif object_name=="STAR":

        icon="⭐"
        name="Stellar Object"
        threat="🟡 MEDIUM"
        energy="High"

        report="""
Fusion activity detected.

High temperature object.

Maintain observation distance.
"""

        fact="⭐ Our Sun is one ordinary star among billions."

    else:

        icon="☄️"
        name="Quasar"
        threat="🔴 EXTREME"
        energy="Extreme"

        report="""
Extremely energetic source.

Likely powered by a supermassive black hole.

Approach not recommended.
"""

        fact="☄️ Quasars are among the brightest objects ever discovered."

    st.header(f"{icon} {name}")

    a,b,c = st.columns(3)

    a.metric("Threat Level",threat)
    b.metric("Energy",energy)
    c.metric("Confidence",f"{confidence:.2f}%")

    st.info(report)

    st.divider()

    # ---------------------------------------------------
    # SPACE FACT
    # ---------------------------------------------------

    st.header("🌠 Space Fact")

    st.success(fact)

    st.divider()

    # ---------------------------------------------------
    # MISSION SUMMARY
    # ---------------------------------------------------

    summary = pd.DataFrame({

        "Parameter":[
            "Mission ID",
            "Mission Time",
            "Detected Object",
            "Confidence",
            "Threat"
        ],

        "Value":[
            mission,
            datetime.now().strftime("%H:%M:%S"),
            object_name,
            f"{confidence:.2f}%",
            threat
        ]

    })

    st.header("📋 Mission Summary")

    st.table(summary)

    if st.button("🔄 Scan Another Object"):
        st.rerun()

    st.balloons()

st.divider()

st.caption("ASTRA AI Space Explorer | Built with Python, Scikit-learn, TensorFlow & Streamlit")
