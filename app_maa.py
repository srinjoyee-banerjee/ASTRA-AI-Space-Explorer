import streamlit as st
import pandas as pd
import joblib
import random
import time
from datetime import datetime

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="ASTRA AI Space Explorer",
    page_icon="🌌",
    layout="wide"
)

# ---------------------------------------------------
# LOAD AI
# ---------------------------------------------------
rf_model = joblib.load("random_forest_model.pkl")
encoder = joblib.load("label_encoder.pkl")
data = pd.read_csv("sample_objects.csv")

# ---------------------------------------------------
# SESSION
# ---------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "mission_id" not in st.session_state:
    st.session_state.mission_id = random.randint(1000,9999)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at top,#06132c,#01030a 70%);
color:white;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

h1,h2,h3,h4,p{
text-align:center;
color:white;
}

.bigtitle{
font-size:72px;
font-weight:800;
color:#63d8ff;
text-shadow:0px 0px 25px cyan;
margin-top:50px;
margin-bottom:10px;
}

.subtitle{
font-size:24px;
color:#d9f4ff;
margin-bottom:35px;
}

.card{

background:rgba(255,255,255,.08);

padding:25px;

border-radius:20px;

border:1px solid rgba(255,255,255,.15);

backdrop-filter:blur(10px);

}

div.stButton > button{

width:100%;

height:70px;

font-size:24px;

font-weight:bold;

border-radius:18px;

background:#0094ff;

color:white;

border:none;

box-shadow:0px 0px 20px #00bfff;

}

div.stButton>button:hover{

background:#00bfff;

color:white;

}

</style>
""",unsafe_allow_html=True)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------
if st.session_state.page=="home":

    st.markdown(
        "<div class='bigtitle'>🌌 ASTRA</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Artificial Intelligence Space Explorer</div>",
        unsafe_allow_html=True
    )

    st.markdown("""

<div class='card'>

## 🚀 Welcome Commander

ASTRA is an Artificial Intelligence system capable of
identifying astronomical objects using Machine Learning.

Your mission is to explore the universe and classify
unknown celestial objects detected by the telescope.

</div>

""",unsafe_allow_html=True)

    st.write("")
    st.write("")

    c1,c2,c3=st.columns([1,2,1])

    with c2:

        if st.button("🚀 LAUNCH MISSION"):

            st.session_state.page="boot"

            st.rerun()
# ---------------------------------------------------
# BOOT PAGE
# ---------------------------------------------------
elif st.session_state.page == "boot":

    st.markdown(
        "<div class='bigtitle'>⚡ ASTRA BOOT SEQUENCE</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Initializing Artificial Intelligence Core...</div>",
        unsafe_allow_html=True
    )

    progress = st.progress(0)
    status = st.empty()

    boot_steps = [

        "🔋 Powering AI Core...",
        "🛰 Connecting Mission Control...",
        "🌌 Establishing Deep Space Link...",
        "📡 Connecting SDSS Database...",
        "🤖 Loading Random Forest Model...",
        "🧠 Loading Neural Network...",
        "🔭 Calibrating Telescope...",
        "✅ All Systems Ready"

    ]

    value = 0

    for step in boot_steps:

        status.markdown(f"## {step}")

        for i in range(12):

            value += 1

            if value > 100:
                value = 100

            progress.progress(value)

            time.sleep(0.05)

    time.sleep(1)

    st.session_state.page = "mission"

    st.rerun()


# ---------------------------------------------------
# MISSION CONTROL
# ---------------------------------------------------
elif st.session_state.page == "mission":

    st.markdown(
        "<div class='bigtitle'>🛰 MISSION CONTROL</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='subtitle'>Mission #{st.session_state.mission_id}</div>",
        unsafe_allow_html=True
    )

    st.markdown("""

<div class='card'>

## Commander

Mission Control reports that all onboard systems are operational.

### Mission Objectives

✅ Search Deep Space

✅ Detect Unknown Object

✅ Analyze Spectral Information

✅ Predict Object using AI

When ready, begin the scan.

</div>

""", unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if st.button("🔭 BEGIN SPACE SCAN"):

            st.session_state.page = "scan"

            st.rerun()  
    # ---------------------------------------------------
# SCANNING PAGE
# ---------------------------------------------------
elif st.session_state.page == "scan":

    st.markdown(
        "<div class='bigtitle'>📡 DEEP SPACE SCAN</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Searching the Universe...</div>",
        unsafe_allow_html=True
    )

    progress = st.progress(0)

    status = st.empty()

    scan_steps = [

        "🔭 Telescope Activated...",
        "🌌 Searching Nearby Galaxies...",
        "📡 Receiving Space Signals...",
        "🌈 Measuring Spectral Bands...",
        "🚀 Calculating Redshift...",
        "🤖 Running Random Forest AI...",
        "🧠 Computing Prediction...",
        "🎯 Target Locked..."

    ]

    value = 0

    for step in scan_steps:

        status.markdown(f"## {step}")

        for i in range(12):

            value += 1

            if value > 100:
                value = 100

            progress.progress(value)

            time.sleep(0.05)

    st.success("✅ Unknown Object Detected")

    time.sleep(1)

    st.session_state.page = "analysis"

    st.rerun()


# ---------------------------------------------------
# AI ANALYSIS
# ---------------------------------------------------
elif st.session_state.page == "analysis":

    st.markdown(
        "<div class='bigtitle'>🤖 AI ANALYSIS</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Artificial Intelligence is analyzing the object...</div>",
        unsafe_allow_html=True
    )

    progress = st.progress(0)

    status = st.empty()

    analysis_steps = [

        "Loading Telescope Data...",
        "Extracting Features...",
        "Loading Machine Learning Model...",
        "Evaluating Decision Trees...",
        "Estimating Prediction Probability...",
        "Generating Final Classification..."

    ]

    value = 0

    for step in analysis_steps:

        status.markdown(f"## {step}")

        for i in range(16):

            value += 1

            if value > 100:
                value = 100

            progress.progress(value)

            time.sleep(0.05)

    time.sleep(1)

    st.session_state.page = "result"
    st.rerun()


# ---------------------------------------------------
# RESULT PAGE
# ---------------------------------------------------
elif st.session_state.page == "result":

    # ------------------------------
    # RANDOM OBJECT FROM DATASET
    # ------------------------------
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

    # ------------------------------
    # AI PREDICTION
    # ------------------------------
    prediction = rf_model.predict(X)

    probability = rf_model.predict_proba(X)

    confidence = probability.max() * 100

    object_name = encoder.inverse_transform(prediction)[0]

    # ------------------------------
    # OBJECT DETAILS
    # ------------------------------
    if object_name == "GALAXY":

        icon = "🌌"
        title = "Galaxy"

        threat = "🟢 LOW"

        energy = "Stable"

        report = """
Billions of stars detected.

Large gravitational structure.

Safe for scientific observation.
"""

    elif object_name == "STAR":

        icon = "⭐"

        title = "Star"

        threat = "🟡 MEDIUM"

        energy = "High"

        report = """
Nuclear fusion detected.

Extremely hot stellar body.

Maintain safe observation distance.
"""

    else:

        icon = "☄️"

        title = "Quasar"

        threat = "🔴 EXTREME"

        energy = "Extreme"

        report = """
Very high energy source.

Likely powered by a supermassive black hole.

Approach is not recommended.
"""

    # ------------------------------
    # PAGE TITLE
    # ------------------------------

    st.markdown(
        f"<div class='bigtitle'>{icon} OBJECT IDENTIFIED</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='subtitle'>{title}</div>",
        unsafe_allow_html=True
    )

    st.success("AI Classification Completed Successfully")

    # ------------------------------
    # METRICS
    # ------------------------------

    c1, c2, c3 = st.columns(3)

    c1.metric("Threat", threat)

    c2.metric("Energy", energy)

    c3.metric("Confidence", f"{confidence:.2f}%")

    st.info(report)

    st.divider()

    st.subheader("📡 Telescope Readings")

    a, b, c, d = st.columns(4)

    a.metric("Alpha", f"{obj['alpha'].iloc[0]:.2f}°")

    b.metric("Delta", f"{obj['delta'].iloc[0]:.2f}°")

    c.metric("Redshift", f"{obj['redshift'].iloc[0]:.4f}")

    d.metric("Confidence", f"{confidence:.2f}%")

    e, f, g, h = st.columns(4)

    e.metric("UV", f"{obj['u'].iloc[0]:.2f}")

    f.metric("Green", f"{obj['g'].iloc[0]:.2f}")

    g.metric("Red", f"{obj['r'].iloc[0]:.2f}")

    h.metric("Infrared", f"{obj['i'].iloc[0]:.2f}")

    st.metric("Deep Infrared", f"{obj['z'].iloc[0]:.2f}")

    st.write("")

    if st.button("📋 VIEW MISSION REPORT"):

        st.session_state.detected = object_name
        st.session_state.threat = threat
        st.session_state.confidence = confidence

        st.session_state.page = "report"

        st.rerun()
    # ---------------------------------------------------
# MISSION REPORT
# ---------------------------------------------------
elif st.session_state.page == "report":

    st.markdown(
        "<div class='bigtitle'>📋 MISSION REPORT</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Deep Space Mission Completed</div>",
        unsafe_allow_html=True
    )

    detected = st.session_state.get("detected", "UNKNOWN")
    threat = st.session_state.get("threat", "UNKNOWN")
    confidence = st.session_state.get("confidence", 0)

    if detected == "GALAXY":
        fact = "🌌 Galaxies contain billions of stars held together by gravity."

    elif detected == "STAR":
        fact = "⭐ Our Sun is just one ordinary star in the Milky Way."

    else:
        fact = "☄️ Quasars are among the brightest objects in the observable universe."

    st.success("Mission Completed Successfully")

    c1, c2, c3 = st.columns(3)

    c1.metric("Mission", st.session_state.mission_id)
    c2.metric("Object", detected)
    c3.metric("Confidence", f"{confidence:.2f}%")

    st.divider()

    st.subheader("📝 Mission Summary")

    report = pd.DataFrame(
        {
            "Parameter": [
                "Mission ID",
                "Mission Time",
                "Detected Object",
                "Threat Level",
                "AI Confidence",
                "Scanner Status",
                "Mission Status",
            ],
            "Value": [
                st.session_state.mission_id,
                datetime.now().strftime("%H:%M:%S"),
                detected,
                threat,
                f"{confidence:.2f}%",
                "Operational",
                "Completed",
            ],
        }
    )

    st.table(report)

    st.divider()

    st.subheader("🌠 Space Fact")

    st.info(fact)

    st.divider()

    st.balloons()

    c1, c2, c3 = st.columns([1,2,1])

    with c2:

        if st.button("🚀 START NEW MISSION"):

            # Reset mission

            st.session_state.page = "home"

            st.session_state.mission_id = random.randint(1000,9999)

            if "detected" in st.session_state:
                del st.session_state["detected"]

            if "threat" in st.session_state:
                del st.session_state["threat"]

            if "confidence" in st.session_state:
                del st.session_state["confidence"]

            st.rerun()    
