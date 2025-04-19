# WhatsApp Chat Analyzer 📊💬

A powerful tool to analyze and visualize WhatsApp chat exports. Gain insights into chat trends, user activity, sentiment, and more through beautiful graphs and charts.

---

## 📸 Screenshots

| Chat Statistics | Word Cloud | Emoji Analysis |
|-----------------|------------|----------------|
| ![stats](screenshots/chat_stats.png) | ![wordcloud](screenshots/word_cloud.png) | ![emojis](screenshots/emoji_analysis.png) |

> *Note: Add your own screenshots in a `screenshots/` folder and update the file names accordingly.*

---

## 🔗 Deployed Link

You can try the live version here:

👉 [Live App on Streamlit](https://your-deployment-link.streamlit.app)

> *Replace the link above with your actual deployed Streamlit or web app URL.*

---

## 🧠 About the Model (if using ML/NLP)

This project includes a simple Natural Language Processing (NLP) model for:

- 🧭 **Sentiment Analysis**: Determines whether a message is Positive, Neutral, or Negative using pretrained models like `TextBlob` or `VADER`.
- 😃 **Emotion Detection** *(optional)*: Classifies messages into emotions such as Happy, Sad, Angry, etc. using a fine-tuned BERT or LSTM model trained on emotion-labeled datasets.

### Model Info

- **Library**: `nltk`, `textblob`, or `transformers` (based on your implementation)
- **Input**: Text from individual messages
- **Output**: Sentiment/Emotion label
- **Use Case**: Aggregate emotional tone over time, identify emotional spikes in chats

> *You can skip or adjust this section if your project doesn't use any model.*

---

## 🚀 Features

- 🧾 Message statistics (daily, monthly)
- 🕵️ Most active users
- ⏰ Peak hours and chat activity
- 🔤 Word cloud generation
- 😂 Emoji frequency
- 🧠 Sentiment & Emotion detection (optional)
- 📁 Analyze any `.txt` WhatsApp export file

---

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run app.py
