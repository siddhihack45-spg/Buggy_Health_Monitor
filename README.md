# 🏎️ Buggy Health Monitor

**A Python OOP and Machine Learning project for buggy sensor-condition monitoring using Random Forest classification.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)

## 🚀 Live Demo

**Try the application here:**

👉 [Buggy Health Monitor — Live Dashboard](https://buggyhealthmonitor-ymyesknkgv6pz3vcde6qho.streamlit.app/)

**GitHub Repository:**
https://github.com/siddhihack45-spg/Buggy_Health_Monitor

---

## 📌 About the Project

Buggy Health Monitor is a beginner-friendly project that demonstrates how Python Object-Oriented Programming (OOP) and Machine Learning can be combined for vehicle sensor-condition monitoring.

The project uses a Random Forest classifier to demonstrate predictions based on three input readings:

* Engine temperature
* Vibration
* Suspension reading

It includes a command-line application and a Streamlit web dashboard.

**Note:** The current model uses synthetic demonstration data. It is not trained or validated for real buggy fault detection.

---

## ✨ Features

* Python classes and objects
* Sensor data handling
* Random Forest classification
* Model training and prediction
* Model saving and loading
* Interactive command-line menu
* Streamlit web dashboard
* User-entered sensor readings
* Prediction confidence display

---

## 🛠️ Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Main programming language           |
| OOP          | Organizing the project into classes |
| Scikit-learn | Random Forest machine learning      |
| Joblib       | Saving and loading the model        |
| NumPy        | Numerical computing                 |
| Streamlit    | Interactive web dashboard           |

---

## 📂 Project Structure

```text
Buggy_Health_Monitor/
│
├── main.py
├── sensors.py
├── detector.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

* **main.py** — Runs the command-line application.
* **sensors.py** — Defines the sensor data class.
* **detector.py** — Trains and uses the Random Forest classifier.
* **app.py** — Runs the Streamlit web dashboard.
* **requirements.txt** — Lists the required Python libraries.
* **README.md** — Project documentation.
* **.gitignore** — Excludes generated and unnecessary files.

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/siddhihack45-spg/Buggy_Health_Monitor.git
```

### 2. Open the project folder

```bash
cd Buggy_Health_Monitor
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Run the Command-Line Application

Run:

```bash
python main.py
```

The menu provides these options:

1. Train Random Forest
2. Load saved model
3. Predict buggy condition
4. Exit

---

## 🌐 Run the Streamlit Dashboard

Start the web application with:

```bash
python -m streamlit run app.py
```

The dashboard opens in your browser, usually at:

```text
http://localhost:8501
```

You can enter sensor readings, train the demonstration model, and view its prediction.

---

## 🧠 How It Works

1. **Input:** Enter engine temperature, vibration, and suspension readings.
2. **Sensor handling:** Store the readings using the `SensorData` class.
3. **Training:** Train a Random Forest classifier using synthetic demonstration data.
4. **Prediction:** Pass the readings to the classifier.
5. **Output:** Display the predicted class and model confidence.
6. **Model persistence:** Save and load the trained model using Joblib.

---

## 📊 Model Information

**Algorithm:** Random Forest Classifier

**Number of trees:** 100

**Demonstration accuracy:** Approximately 81.7% in one training run.

This accuracy is measured on a synthetic demonstration dataset and does not represent performance on real buggy sensor measurements.

---

## ⚠️ Limitations and Future Improvements

### Current Limitations

* Uses synthetic rather than real buggy sensor data.
* Predictions are demonstration outputs, not validated mechanical diagnoses.
* Sensor units, operating ranges, and fault labels need to be defined and validated.
* Model confidence is not a guarantee that a prediction is correct.

### Future Improvements

* Collect real sensor data from a buggy.
* Define validated normal and fault operating ranges.
* Train and evaluate the model on labeled real-world measurements.
* Add sensor integration using a microcontroller such as STM32.
* Add prediction history and visual sensor charts.
* Evaluate false alarms and missed faults before any practical use.

---

## 👩‍💻 Author

**Siddhi Gore**

Student Project | Python | Machine Learning | Vehicle Monitoring

---

## 📜 Disclaimer

This project is developed for educational and demonstration purposes only. It must not be used as a safety system or to make decisions about whether a buggy is safe to operate. Real-world use requires reliable sensor hardware, representative labeled data, and thorough testing and validation.
