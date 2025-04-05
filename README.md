# 📣 AI Marketing Campaign App

This app generates creative and customized marketing messages tailored to different age groups, tones, and message lengths — powered by LangChain and Groq's blazing-fast language models.

---

## 🚀 Features

✅ Supports generation of messages for:
- 👶 Kids
- 👩 Adults
- 👴 Senior Citizens

✅ Fully customizable output:
- **Tone options**: Funny, Professional, Emotional
- **Length options**: Short (~30 words), Medium (~60-80 words), Long (100+ words)

✅ Built with:
- **LangChain** + `ChatGroq`
- **Groq API** (e.g., LLaMA 3 70B)
- **Streamlit** frontend
- Clean modular structure

---

## 🧪 Sample Use Case

**Input**:
- Age Group: `Kids`
- Product: `Magic Toothbrush`
- Tone: `Funny`
- Length: `Medium`

**Output**:
> *"Get ready for a BRUSH-TASTIC adventure! Introducing the Magic Toothbrush that makes brushing your teeth a SUPERPOWER! With flashing lights, cool sounds... Grab your Magic Toothbrush and join the Brushing Brigade!"*

---

## 🧱 Project Structure


MarketingCampaignApp/ 
├── app/
│ └── main.py # Streamlit app UI 
├── backend/ 
│ └── generator.py # LangChain logic using ChatGroq 
├── utils/ 
│ └── prompts.py # Prompt templates per age group 
├── examples/ 
│ ├── kids.json 
│ ├── adults.json 
│ └── seniors.json 
├── .env # Contains your GROQ_API_KEY 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation



---

## 🛠️ Installation & Running the App

### 1. Clone the repo or download the files:

```bash
git clone https://github.com/your-username/marketing-campaign-app.git
cd marketing-campaign-app

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up your .env file:
GROQ_API_KEY=gsk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

5. Run the app:
streamlit run app/main.py


🧠 Supported Models
This app works with the following Groq-hosted models:

mixtral-8x7b-32768 (default — balanced & creative)

llama3-70b-8192 (deeper understanding)

gemma-7b-it (faster + instruction-tuned)

You can change the model in generator.py.

