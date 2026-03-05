# CareerUp AI - Desktop Application

Native desktop application powered by PyWebView + Dronor Experts.

## Features

- 🎤 **Interview Coach** - Practice with AI feedback, STAR scoring, percentile ranking
- 📄 **Resume Optimizer** - ATS scoring + keyword optimization
- 🧠 **Personality Test** - Interview perception analysis
- 🗺️ **Career Roadmap** - Week-by-week development plan
- 💡 **Insider Tips** - Real advice from industry professionals

## Requirements

- Python 3.9+
- OpenAI API Key (get one at https://platform.openai.com)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/AnvarBakiyev/careerup-ai.git
cd careerup-ai/desktop
```

### Step 2: Create virtual environment (recommended)

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

## First Launch

1. Click **Settings** (gear icon) in sidebar
2. Enter your OpenAI API Key
3. Click **Save Settings**
4. Start using the app!

## Usage

### Interview Coach
1. Select Role (PM, SWE, DS, Designer)
2. Select Company Type (FAANG, Startup, Enterprise)
3. Select Question Type (Behavioral, Case, Technical)
4. Click **Generate Question**
5. Type your answer
6. Click **Get Feedback** for AI evaluation

### Resume Optimizer
1. Enter target role
2. Paste your resume text
3. Click **Analyze Resume**
4. Review ATS score and recommendations

### Personality Test
1. Select test type
2. Enter target role
3. Click **Start Test**
4. Answer all questions
5. View your interview perception profile

## Troubleshooting

### "pywebview not found"
```bash
pip install pywebview
```

### macOS permission issues
If you see "Operation not permitted", try:
```bash
pip install pywebview[qt]
```

### Windows WebView2 issues
Install Microsoft Edge WebView2 Runtime:
https://developer.microsoft.com/en-us/microsoft-edge/webview2/

## Tech Stack

- **Frontend**: HTML/CSS/JavaScript
- **Backend**: Python + PyWebView
- **AI**: Dronor Experts (OpenAI-powered)

## License

MIT
