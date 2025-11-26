# WhatsApp Chat Analyzer 📊💬

A powerful tool to analyze and visualize WhatsApp chat exports. Gain insights into chat trends, user activity, sentiment, and more through beautiful graphs and charts.
---

## 🔗 Deployed Link

You can try the live version here:
https://whatsappchatpredict-3qss86kcsnbjzbl6jwnkqg.streamlit.app/

---

## 🧠 About the Model 

This project includes a simple Natural Language Processing (NLP) model for:

- 🧭 **Sentiment Analysis**: Determines whether a message is Positive, Neutral, or Negative using pretrained models like `TextBlob` or `VADER`.
- 😃 **Emotion Detection** *(optional)*: Classifies messages into emotions such as Happy, Sad, Angry, etc. using a fine-tuned BERT or LSTM model trained on emotion-labeled datasets.

### Model Info

- **Library**: `nltk`, `textblob`, or `transformers` (based on your implementation)
- **Input**: Text from individual messages
- **Output**: Sentiment/Emotion label
- **Use Case**: Aggregate emotional tone over time, identify emotional spikes in chats

---

## 🚀 Features

- 🧾 Message statistics (daily, monthly)
- 🕵️ Most active users
- ⏰ Peak hours and chat activity
- 🔤 Word cloud generation
- 😂 Emoji frequency
- 🧠 Sentiment & Emotion detection s
- 📁 Analyze any `.txt` WhatsApp export file

---

## 📦 Setup Instructions

```bash
git clone https://github.com/prafulla2121/whatsapp_chat_predict.git
pip install -r requirements.txt
streamlit run app.py
