# 🏎️ F1 Podium Predictor

A machine learning web app that predicts Formula 1 podium finishes based on grid position and team.

**[Live Demo](https://isaacpuah-f1-podium-predictor.streamlit.app)** *(update this link after deploying)*

![App Screenshot](screenshot.png) *(add a screenshot later)*

## Overview

This project predicts whether an F1 driver will finish on the podium (top 3) using a Logistic Regression model trained on historical race data.

**Key Results:**
- 90.5% accuracy on 2024 season (trained on 2022 data)
- 70% precision on podium predictions
- 67% recall on podium predictions

## Features

- Predict podium probability for any driver/team/grid combination
- Full 20-driver grid predictions
- All 24 Grand Prix circuits included
- Clean, interactive UI

## Methodology

### Data
- Source: FastF1 API
- Training: 2022 season (420 race entries)
- Testing: 2024 season (479 race entries)
- Time-based split to prevent data leakage

### Features
| Feature | Description |
|---------|-------------|
| GridPosition | Starting position (1-20) |
| IsTopTeam | Binary flag for top 4 teams (Red Bull, Ferrari, McLaren, Mercedes) |

### Models Compared
| Model | Accuracy | Precision | Recall |
|-------|----------|-----------|--------|
| Logistic Regression | 90.6% | 70% | 67% |
| Random Forest | 90.6% | 70% | 67% |
| Gradient Boosting | 90.0% | 75% | 50% |

Logistic Regression selected for simplicity and interpretability.

## Tech Stack

- **Python** — Core language
- **pandas** — Data manipulation
- **scikit-learn** — Machine learning
- **FastF1** — F1 data API
- **Streamlit** — Web app framework
- **Streamlit Cloud** — Deployment

## Run Locally
```bash
# Clone repo
git clone https://github.com/IsaacPuah/f1-podium-predictor.git
cd f1-podium-predictor

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## Future Improvements

- [ ] Add track outline visualizations for each circuit
- [ ] Include more features (driver recent form, weather, track history)
- [ ] Add 2023 season data
- [ ] Implement more sophisticated models (XGBoost, neural networks)
- [ ] Add historical accuracy tracking

## Author

**Isaac Puah** — UC Berkeley EECS

- GitHub: [@IsaacPuah](https://github.com/IsaacPuah)
- LinkedIn: [linkedin.com/in/isaacpuah](https://linkedin.com/in/isaacpuah) *(update if different)*

## License

MIT License
