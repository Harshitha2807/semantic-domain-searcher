# Semantic Domain Searcher 🔍🌐

A Python-based command-line tool that performs **semantic search** using the **Exa API**, allowing you to fetch relevant results specifically from selected domains.

## ✨ Features

- 🧠 Semantic keyword search powered by [Exa](https://exa.ai)
- 🌍 Domain-specific result filtering (e.g., only search within a particular website)
- 💻 Clean and interactive command-line interface
- 🔒 Secure API key handling using a `.env` file
- 📦 Lightweight and easy to set up

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Harshitha2807/semantic-domain-searcher.git
cd semantic-domain-searcher

2. Install the dependencies
pip install -r requirements.txt

3. Create a .env file
EXA_API_KEY=your_actual_exa_api_key
⚠️ Do not share this key publicly. It is already excluded via .gitignore.

4. Run the script
python main.py


🧪 Example
$ python main.py
Search here: space exploration
Title: The Future of Space Exploration
URL: https://www.nasa.gov/future-space

Title: Mars Colonization Strategies
URL: https://www.spacex.com/mars-colony

📄 License
This project is licensed under the MIT License – feel free to use and adapt it.
