# Plant_disease_detector

This project aims to develop a Convolutional Neural Network (CNN) model using TensorFlow and Keras to detect plant diseases from images. The model is designed to classify images into different disease categories, enabling farmers and agricultural experts to identify and treat diseases more effectively.


**Key Components:**

**1] Model Architecture:**
The CNN model is built using the Keras API in TensorFlow, with a sequential architecture consisting of the following layers:

**Conv2D:** Convolutional layers for feature extraction

**MaxPool2D:** Max pooling layers for downsampling

**Flatten:** Flatten layer to prepare data for dense layers

**Dense:** Dense layers for classification

**Dropout:** Dropout layers for regularization


**2] Data Augmentation**
The ImageDataGenerator from Keras is used to augment the image data, which helps in:

Reducing overfitting,
Improving model generalization,
Increasing the diversity of the training dataset


**3] Metrics and Evaluation:**

The model's performance is evaluated using classification metrics, including:

**Precision:** The ratio of true positives to the sum of true positives and false positives

**Recall:** The ratio of true positives to the sum of true positives and false negatives

**F1 Score:** The harmonic mean of precision and recall


**4] Data Visualization:**

Matplotlib and Seaborn are used for data visualization, providing insights into the data distribution, model performance, and feature importance.


**5] Data Manipulation**
Pandas is used for data manipulation, including data loading, preprocessing, and feature engineering.


**!! Skills Learned !!:**
From this project, I gained experience in:

**1) Deep learning**: Building and training CNN models using TensorFlow and Keras

**2) Image classification:** Developing models for image classification tasks

**3) Data augmentation:** Using techniques to augment image data and improve model generalization

**4) Metrics and evaluation:** Using classification metrics to evaluate model performance

**5) Data visualization:** Using Matplotlib and Seaborn for data visualization

**6) Data manipulation:** Using Pandas for data loading, preprocessing, and feature engineering
