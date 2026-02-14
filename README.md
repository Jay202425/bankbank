# HBDB Banking Bot

An AI-powered banking assistant chatbot built with Streamlit and Mistral AI. This bot answers customer questions about HBDB Bank services using a FAQ knowledge base.

## Features

- 🤖 **AI-Powered**: Uses Mistral Large LLM for intelligent responses
- 💬 **Real-time Streaming**: Displays bot responses as they're generated
- 📚 **FAQ Knowledge Base**: Trained on 50+ HBDB banking FAQs
- 💾 **Chat History**: Maintains conversation history during session
- 🎨 **Clean UI**: Built with Streamlit for easy interaction

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Jay202425/bankbank.git
cd bankbank
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
source venv/bin/activate     # Mac/Linux
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Configuration

Set your Mistral AI API key in `banking_bot.py`:
```python
api_key = "your_mistral_api_key_here"
```

Or set it as an environment variable:
```bash
$env:MISTRAL_API_KEY = "your_api_key"
```

## Usage

Run the Streamlit app:
```bash
streamlit run banking_bot.py
```

The bot will be available at:
- **Local**: http://localhost:8501
- **Network**: http://192.168.1.90:8501

## Files

- `banking_bot.py` - Main Streamlit application
- `hbdb_banking_faqs (2) (1).csv` - FAQ knowledge base
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore file

## Bot Capabilities

The bot can answer questions about:
- Opening accounts
- Online banking & mobile app
- Credit cards & Premier services
- Loans & mortgages
- Transfers & payments
- Account management
- And more HBDB banking services

## Technologies

- **Streamlit**: Web application framework
- **Mistral AI**: Large Language Model API
- **Python 3.11+**: Programming language

## Author

Jay202425 (jaylondonintl@gmail.com)

## License

MIT License
