# GDG Project

This repository contains a Python application for interacting with research papers using AI-powered features. The project is organized as follows:

## Project Structure

```
gdg/
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not tracked)
├── assets/                 # Static assets (CSS, images)
│   ├── styles.css
│   └── logo.jpg
├── pages/                  # Streamlit page modules
│   ├── _Chat_with_Paper.py
│   ├── _Compare_Two_Papers.py
│   ├── _Insights_&_Future_Work.py
│   └── _Smart_Summary.py
├── utils/                  # Utility modules
│   ├── api.py
│   ├── gemini_api.py
│   ├── pdf_utils.py
│   ├── ui_components.py
│   └── __init__.py
└── venv/                   # Python virtual environment (not tracked)
```

## Features
- Chat with research papers using AI
- Compare two papers
- Generate smart summaries
- Extract insights and future work

## Setup
1. Clone the repository:
   ```powershell
   git clone <repo-url>
   cd gdg
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Set up your `.env` file with required API keys and settings.

## Usage
Run the application:
```powershell
streamlit run app.py
```

## Demonstration 
![Screenshot1](.\Screenshot1.png)
![Screenshot2](.\Screenshot2.jpg)
![Screenshot3](.\Screenshot3.jpg)





## License
![License: MIT](https://github.com/maurya-ashutosh02/gdg/LICENSE)



## Contact
For questions or contributions mail us at : chitravnashmohandevelops@gmail.com
or ashutoshmaurya9696@gmail.com
