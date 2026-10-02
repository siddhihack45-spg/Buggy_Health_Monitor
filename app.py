
import streamlit as st
from pathlib import Path
from sensors import SensorData
from detector import BuggyDetector

st.set_page_config(
    page_title="Buggy Health Monitor",
    page_icon="🏎️",
    layout="centered"
)

st.title("🏎️ Buggy Health Monitor")
st.caption("Random Forest | Sensor-condition demonstration")

MODEL_PATH = Path("random_forest.pkl")

@st.cache_resource
def get_detector():
    detector = BuggyDetector()
    if MODEL_PATH.exists():
        detector.load()
    return detector

detector = get_detector()

st.info(
    "Educational demo: the current model uses synthetic data. "
    "It is not validated for real buggy fault detection."
)

st.header("Sensor Readings")

engine_temp = st.number_input(
    "Engine temperature",
    min_value=0.0,
    max_value=300.0,
    value=80.0,
    step=1.0
)

vibration = st.number_input(
    "Vibration",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=0.5
)

suspension = st.number_input(
    "Suspension reading",
    min_value=0.0,
    max_value=500.0,
    value=50.0,
    step=1.0
)

st.divider()

if st.button("Train Random Forest", type="secondary"):
    with st.spinner("Training model..."):
        detector.train()
        detector.save()
    st.success("Training complete. Model saved.")

if st.button("Predict Buggy Condition", type="primary"):
    if not detector.is_trained:
        st.warning("Train the model first.")
    else:
        buggy = SensorData(
            engine_temp,
            vibration,
            suspension
        )

        condition, confidence = detector.predict(
            buggy.get_readings()
        )

        st.subheader("Prediction")

        if condition == "NORMAL":
            st.success("Model output: NORMAL")
        else:
            st.warning("Model output: WARNING")

        st.metric("Model confidence", f"{confidence:.2f}%")

        st.caption(
            "This is only the model's output on synthetic training "
            "data, not a reliable mechanical diagnosis."
        )

st.divider()
st.caption("Project by Siddhi Gore")
