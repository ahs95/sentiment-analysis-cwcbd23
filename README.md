# Bangla Sentiment and Sarcasm Detection: Reactions to Bangladesh's 2023 World Cup

This repository contains the implementation, dataset, and models for the paper "Bangla Sentiment and Sarcasm Detection: Reactions to Bangladesh’s 2023 World Cup". The study focuses on detecting sentiment (positive, negative, neutral) and sarcasm in Bangla social media comments related to cricket, particularly reactions to Bangladesh's 2023 ICC Cricket World Cup campaign.

The project addresses class imbalance , employs language-specific pretraining , and introduces a dual-head transformer-based model fine-tuned using BanglaBERT with focal loss. We also provide an interactive Gradio demo for real-time inference.

🧠 Key Features
✅ Manually annotated dataset of 5,635 Bangla comments
✅ Custom dual-head classification model for joint sentiment and sarcasm detection
✅ Focal loss integration to handle class imbalance
✅ Multilabel stratified k-fold cross-validation
✅ Interactive Gradio interface for real-time predictions
✅ Publicly available code and dataset for reproducibility and further research
📁 Dataset
We present the largest publicly available dataset of Bangla comments focused on sentiment and sarcasm detection:

Source : Social media comments related to Bangladesh’s 2023 ICC Cricket World Cup performance
Size : 5,635 manually annotated samples
Labels :
Sentiment : Positive / Negative / Neutral
Sarcasm : Sarcastic / Non-sarcastic

🤖 Model Architecture
Base Model : BanglaBERT
Custom Head : Dual-output head for multi-task classification
Loss Function : Combined focal loss for both tasks
Training Strategy : Multilabel stratified k-fold cross-validation
