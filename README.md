# Sentiment-Analysis-of-Movie-Reviews
This project is done for fulfilling the training requirements of PDS (Introduction to Python and Basic Data Science) batch 08, offered by EDGE.
**Sentiment Analysis of Movie Reviews Using Naïve Bayes**

## **1. Introduction**
This project focuses on **Sentiment Analysis of IMDb Movie Reviews** using **Naïve Bayes Classifier**. The objective is to classify reviews as either **positive** or **negative** based on textual content. The dataset used contains **50,000 reviews**, with equal distribution of positive and negative sentiments.

## **2. Dataset**
- **Source:** IMDb Movie Reviews Dataset (Kaggle)
- **Size:** 50,000 movie reviews (balanced dataset)
- **Labels:** Positive (1), Negative (0)

## **3. Methodology**
### **3.1 Preprocessing Steps**
- **Text Cleaning:** Convert text to lowercase, remove punctuation, special characters, and HTML tags.
- **Stopword Removal:** Common words like "the," "is," "and" were removed to improve classification.
- **Tokenization & Lemmatization:** Text was split into tokens and reduced to their base form.
- **TF-IDF Vectorization:** Convert textual data into numerical features using the **TF-IDF** technique (top 5000 features).

### **3.2 Model Training**
- **Algorithm Used:** Multinomial Naïve Bayes (suitable for text classification tasks)
- **Train-Test Split:** 80% Training, 20% Testing
- **Model Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score, and Confusion Matrix

## **4. Results and Analysis**
### **4.1 Performance Metrics**
- **Accuracy:** 85.42%
- **Precision & Recall:**
  - Negative Reviews: Precision = 86%, Recall = 84%
  - Positive Reviews: Precision = 85%, Recall = 86%
- **Confusion Matrix:**
  - True Negatives: **4,221**
  - False Positives: **779**
  - False Negatives: **679**
  - True Positives: **4,321**

### **4.2 Word Cloud Visualization**
- **Positive Reviews:** Words like *"movie," "character," "love," "scene," "story," "good"* appear frequently.
- **Negative Reviews:** Words like *"bad," "little," "work," "time," "look," "stupid"* dominate.

### **4.3 Top Words Analysis**
- **Positive Words:** *"movie," "character," "love," "scene," "story," "good"*
- **Negative Words:** *"bad," "little," "work," "time," "look," "stupid"*

## **5. Conclusion**
- The **Naïve Bayes classifier** achieved strong performance with **85.42% accuracy**.
- The **TF-IDF vectorization** successfully transformed textual data into numerical features.
- **Visualization techniques (word clouds, top words, confusion matrix)** helped in understanding the model’s decision-making process.
