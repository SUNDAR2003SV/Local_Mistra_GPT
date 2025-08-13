# Local Mistral GPT Model

This project runs a **Mistral 7B** model locally using **Ollama** with a **Flask backend** and a **HTML/CSS/JS frontend**.  
It allows you to chat with your local GPT model without any cloud dependency.

---

## 🚀 Features
- Runs **entirely on your local machine** — no internet required for model responses.
- Uses **Ollama** to manage and serve the Mistral model.
- **Flask backend** for API endpoints.
- **HTML/CSS/JavaScript frontend** for user-friendly interaction.
- CORS enabled for cross-origin API calls.

---

## 🛠 Tech Stack
- **Model**: Mistral 7B (via Ollama)
- **Backend**: Python 3, Flask, Flask-CORS
- **Frontend**: HTML, CSS, JavaScript
- **Platform**: Localhost

---

## 📂 Project Structure
Local_GPT/
  static/
     style.css
  templates/
     index.html
app.py

⚙️ Installation & Setup
1️⃣ Install Ollama
Download and install Ollama from the official site: https://ollama.ai
(Ollama is the platform that runs the AI models locally on your machine.)

2️⃣ Pull the Mistral Model
Once Ollama is installed, you can use different models.

We’ll use Mistral 7B, a free and popular model. (You can choose another model if you prefer.)

🔹 Note: If you search "Mistral 7B" on the Ollama website, you’ll find details about it, but you can’t download it directly from there — you need to pull it via the command line.

Open your Command Prompt / Terminal and run:

ollama pull mistral
This will download the Mistral 7B model to your local Ollama setup so the backend can use it.

