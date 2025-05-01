# Network Intrusion Detection System (NIDS) using Machine Learning

This project presents an optimized machine learning-based **Network Intrusion Detection System (NIDS)** that enhances detection accuracy while reducing false alarms and computational complexity. It integrates advanced techniques for feature selection and class balancing to deliver a scalable, efficient, and reliable intrusion detection solution.

## 🧠 Project Overview

Conventional intrusion detection systems often suffer from:
- High false positive rates
- Poor scalability with large datasets
- Inability to detect zero-day attacks
- Difficulty handling high-dimensional data

This project addresses these issues using:
- **MRMR (Minimum Redundancy Maximum Relevance)** for feature selection
- **SMOTE (Synthetic Minority Oversampling Technique)** for class balancing
- Multiple **machine learning models**: SVM, KNN, Decision Tree, Random Forest
- Evaluation metrics: Accuracy, Precision, Recall, F1-Score

## 📌 Objectives

- Improve detection accuracy of NIDS
- Reduce false alarm rates
- Use filter-based feature selection methods like MRMR
- Enhance classification with ML models trained on datasets like NSL-KDD, KDD Cup 99, CICIDS 2017
- Develop a scalable, real-time system deployable across different network environments

## 🔧 Tech Stack

- **Languages**: Python
- **Libraries**: 
  - Scikit-learn
  - Pandas, NumPy
  - Matplotlib, Seaborn
  - Imbalanced-learn (SMOTE)
- **Development Tools**: Jupyter Notebook / VS Code
- **ML Algorithms**: Decision Tree, Random Forest, SVM, KNN

## 📊 System Architecture

1. **Data Preprocessing**: Cleansing, encoding, normalization
2. **Balancing**: Apply SMOTE to balance classes
3. **Feature Selection**: Use MRMR to reduce dimensionality
4. **Model Training & Evaluation**: Train models and compare metrics
5. **Deployment**: Real-time traffic monitoring and alert generation

## 📁 Modules

- `data_preprocessing.py`: Cleans and prepares dataset
- `feature_selection.py`: Implements MRMR
- `smote_balancer.py`: Applies SMOTE for class balancing
- `train_models.py`: Trains ML models and evaluates metrics
- `main.py`: Integrates all steps and runs the NIDS pipeline

## 📷 Screenshots & Results

The model performance is visualized using confusion matrices and bar plots comparing various classifiers. Key metrics like accuracy, precision, and F1-score show improved results over traditional methods.

## ✅ Results Summary

| Model         | Accuracy | Precision | Recall | F1-Score |
|---------------|----------|-----------|--------|----------|
| Decision Tree | 99.80%   | 99.79%    | 99.80% | 99.79%   |
| KNN           | 99.57%   | ~99.60%   | ~99.60%| ~99.60%  |
| SVM           | 97.98%   | 99.54%    | 97.98% | 98.62%   |

- 🔹 **Decision Tree (DT)** outperformed all other models with near-perfect metrics, making it the most reliable choice.
- 🔹 **KNN** closely followed DT, with high consistency in all metrics around 99.6%.
- 🔹 **SVM** showed excellent precision and strong overall performance, balancing accuracy and recall well.

## 🔮 Future Work

- Integrate deep learning models (e.g., CNN, LSTM)
- Real-time deployment on cloud and edge networks
- Continuous learning for zero-day threat adaptation

## 📚 References

- NSL-KDD, KDD Cup 99, CICIDS 2017 datasets
- Research papers and surveys from 2020–2025 on ML-based IDS

## 📩 Contact

**Author:** Prasenjit Jana  
**Email:** itsprasenjitjana@gmail.com  
**GitHub:** [@prasenjit88](https://github.com/prasenjit88)  
**LinkedIn:** [Prasenjit Jana](https://linkedin.com/in/prasenjit-jana-6b841922b)

---

> 🔐 _This project is for educational and research purposes. Feel free to fork and contribute._
