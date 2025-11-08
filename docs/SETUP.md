# Setup Guide

## Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Internet connection (for Gradio client)

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=your_api_key_here
```

### 3. Run the Application

```bash
python main.py
```

The application will start on `http://localhost:5000` (default Flask port).

### 4. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Troubleshooting

### Issue: "OPENAI_API_KEY environment variable not set"
**Solution:** Make sure you've set the environment variable before running the application.

### Issue: Import errors
**Solution:** Ensure all dependencies are installed correctly:
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Port already in use
**Solution:** Change the port in `main.py`:
```python
app.run(debug=True, port=5001)
```

