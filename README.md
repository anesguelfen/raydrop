# RayDrop: AI-Powered Droplet Microfluidics Optimization

This project uses machine learning and computer vision to optimize and analyze droplet formation in microfluidic systems. The pipeline includes:

- Training predictive models for droplet diameter and generation rate
- Bayesian optimization of flow parameters
- Image-based analysis of droplets

# ========================
# requirements.txt
# ========================

# scikit-learn
# pandas
# numpy
# scikit-optimize
# openpyxl
# joblib
# matplotlib
# opencv-python
# fluigent_sdk
# pyspin


# ========================
# How to Run
# ========================
# 1. Place your Excel dataset as: data/raw_data.xlsx
# 2. Run: python train_models.py
# 3. Run: python optimize_bayes.py
# 4. Run: python controller_fluigent.py
# 5. Run: python capture_spinview.py


