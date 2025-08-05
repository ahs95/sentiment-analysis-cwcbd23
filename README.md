## Sentiment and Sarcasm Detection in Bangla: Reactions to Bangladesh’s 2023 World Cup

This repository contains the implementation, dataset, and models for the paper **"Bangla Sentiment and Sarcasm Detection: Reactions to Bangladesh’s 2023 World Cup."** The study focuses on detecting sentiment (positive, negative, neutral) and sarcasm in Bangla social media comments related to cricket, particularly reactions to Bangladesh's 2023 ICC Cricket World Cup campaign.

The project addresses **class imbalance**, employs **language-specific pretraining**, and introduces a **dual-head transformer-based model** fine-tuned using **BanglaBERT** with **focal loss**. Additionally, we provide an interactive **Gradio demo** for real-time inference.

*Notebook Preview:* https://nbviewer.org/github/ahs95/sentiment-analysis-cwcbd23/blob/main/Copy_of_sentiment_analysis_bdcric23.ipynb

### 🧠 Key Features

- ✅ **Manually Annotated Dataset**: A comprehensive collection of **5,635 Bangla comments**.
- ✅ **Custom Dual-Head Classification Model**: Designed for joint sentiment and sarcasm detection.
- ✅ **Focal Loss Integration**: Effectively handles class imbalance in the dataset.
- ✅ **Multilabel Stratified K-Fold Cross-Validation**: Ensures robust model evaluation.
- ✅ **Interactive Gradio Interface**: Facilitates real-time predictions and user interaction.
- ✅ **Open Source**: Publicly available code and dataset for reproducibility and further research.

### 🌐 Model Access

You can access the trained model on Hugging Face using the following link:

[**Bangla Sentiment and Sarcasm Detection Model**](https://huggingface.co/ahs95/sentiment-sarcasm-detection-BanglaBERT)

### 📁 Dataset

We present the largest publicly available dataset of Bangla comments focused on sentiment and sarcasm detection:

- **Source**: Social media comments related to Bangladesh’s 2023 ICC Cricket World Cup performance.
- **Size**: **5,635 manually annotated samples**.
- **Labels**:
  - **Sentiment**: Positive / Negative / Neutral
  - **Sarcasm**: Sarcastic / Non-sarcastic

### 🤖 Model Architecture

- **Base Model**: **BanglaBERT**
- **Custom Head**: **Dual-output head** for multi-task classification.
- **Loss Function**: Combined **focal loss** for both tasks.
- **Training Strategy**: **Multilabel stratified k-fold cross-validation** to enhance model performance and reliability.

This repository aims to contribute to the understanding of sentiment and sarcasm in Bangla, providing valuable resources for researchers and practitioners in the field.
