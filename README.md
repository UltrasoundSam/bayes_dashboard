# Bayes' Law Interactive Demo

This is an interactive Python Dash web app that visualizes **Bayes' Theorem** using a **geometric interpretation**, inspired by [3Blue1Brown’s visual intuition](https://www.youtube.com/watch?v=HZGCoVF3YvM) and [Israel Shalom's Bayesground](https://srulix.com/projects/bayesground).

The project is designed as a teaching and learning tool for exploring probabilistic reasoning. Users can interactively adjust parameters and observe how prior probabilities, likelihoods, and posteriors evolve in real-time.

---

## 🔍 Features

- 🎛️ Sliders and controls to set:
  - Prior probabilities
  - Likelihoods (True Positive and False Positive rates)
- 📊 Dynamic visualizations showing:
  - Area-based representation of events (geometric interpretation)
  - Numerical output of Bayes' rule calculation
- 🔄 Instant updates as parameters change
- 📱 Fully interactive and browser-based via [Plotly Dash](https://dash.plotly.com/)

---

## 📐 Mathematical Background

Bayes' Theorem describes the probability of an event \( A \) given that another event \( B \) has occurred:

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$

This app visualizes each component as **proportional areas** within a unit square, making the logic of Bayesian inference intuitive and concrete.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/UltrasoundSam/bayes_dashboard.git
    ```

2. **Install required packages:**

    ```bash
    pip install ./bayes_dashboard
    ```

### Running the App

```bash
python app.py
```

Then open your browser and go to [http://127.0.0.1:8050](http://127.0.0.1:8050)

### Inspirations & References

This project was inspired by several excellent visual and conceptual resources that aim to make Bayesian reasoning more intuitive:

- 🎥 **[3Blue1Brown – Bayes’ Theorem: A Visual Introduction](https://www.youtube.com/watch?v=HZGCoVF3YvM)**
  A beautifully animated video that introduces Bayes’ Theorem using visual intuition and geometric area models.

- 🌐 **[Israel Shalom – Bayesground](https://srulix.com/projects/bayesground)**
  A web-based interactive demo of Bayes’ Rule using geometric areas and sliders to explore different probability settings.

- 📊 **[Seeing Theory – Bayesian Inference](https://seeing-theory.brown.edu/bayesian-inference/index.html)**
  An educational site with interactive visualizations for Bayesian inference and other core statistics concepts.

- 📘 **[StatQuest: Bayes’ Theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM)**
  Another great explanation for learners who benefit from clear, structured statistical breakdowns.

These resources helped guide the structure, visuals, and educational goals of this app.

## 📄 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software
- ✅ Use the Software for private, academic, or commercial purposes

Under the following conditions:

- 📜 The original copyright and license notice shall be included in all copies or substantial portions
- ❌ The software is provided "as is", without warranty of any kind

> For full details, see the [LICENSE](LICENSE) file included in this repository.
