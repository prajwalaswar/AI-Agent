# 🚀 AI Agents for Research & Writing using CrewAI

An **AI-powered research and writing assistant** built with **CrewAI, Gemini 1.5 Flash, and Serper API** to generate insightful articles on any given topic.

![CrewAI](https://via.placeholder.com/1000x400)

---

## 📌 Project Overview

This project leverages **CrewAI**, a framework for orchestrating multiple **AI agents** to work collaboratively. The AI agents in this project **research topics, analyze trends, and generate engaging articles** using **Google Gemini 1.5 Flash** and **Serper API** for real-time search.

---

## 💡 Features

✅ **Multi-Agent Collaboration:** Agents work together to **research and write** about a given topic.  
✅ **Real-Time Search:** Uses **Serper API** to fetch the latest data from Google.  
✅ **AI-Generated Articles:** Generates **well-structured, insightful** articles.  
✅ **Memory-Powered Agents:** Agents retain context for better responses.  
✅ **Streamlit UI:** Provides an **interactive web interface** for easy use.  

---

## 🛠️ Tech Stack

- **[CrewAI](https://github.com/joaomdmoura/crewai)** → Multi-Agent Collaboration  
- **[Google Gemini 1.5 Flash](https://ai.google.dev/)** → LLM for content generation  
- **[Serper API](https://serper.dev/)** → Real-time Google search integration  
- **[LangChain](https://python.langchain.com/)** → LLM chaining and retrieval  
- **[Streamlit](https://streamlit.io/)** → Web interface for user interaction  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/crewai-project.git
cd crewai-project
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your API keys:
```bash
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_serper_api_key
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🧠 How It Works

1️⃣ **User Inputs a Topic** → The user provides a topic in the Streamlit UI.  
2️⃣ **AI Agents Collaborate** →  
   - **Research Agent** fetches **real-time data** using **Serper API**.  
   - **Writer Agent** generates an **engaging article** using **Gemini 1.5 Flash**.  
3️⃣ **Final Output** → The researched content and generated article are displayed in Streamlit.  

---

## 📌 Example Output

### 🔍 Research on AI in Healthcare
> _"AI is transforming healthcare with predictive analytics, robotic surgeries, and personalized medicine. However, challenges like data privacy and regulatory hurdles persist."_

### 📝 AI in Healthcare – Article
> _"Artificial Intelligence is reshaping the medical industry by enhancing diagnosis, automating workflows, and improving patient care. From AI-driven drug discovery to real-time health monitoring, its applications are vast and revolutionary."_  

---

## 📈 Future Enhancements

🚀 **Add More AI Agents** (Editor, Fact-Checker, SEO Optimizer)  
🚀 **Expand to Multiple Languages**  
🚀 **Enhance User Personalization** (Custom article length, tone, etc.)  
🚀 **Integrate with External APIs** for richer research  

---

## 🤝 Contributing

Want to contribute? Feel free to fork the repo, make improvements, and create a pull request!  

---

## 📞 Contact

👤 **Prajwal Aswar**  
📧 Email: prajwalaswar123@gmail..com  
🔗 GitHub: ([https://github.com/your-username](https://github.com/prajwalaswar/AI-Agent))  
🔗 LinkedIn:(www.linkedin.com/in/prajwal-aswar-5252a12aa)  

---
