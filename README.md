# Bing Search Automation

A simple automation tool to run multiple Bing searches automatically with randomized keywords and timing intervals.

## Features

- 🔍 **Automated Search Execution** - Run multiple Bing searches automatically
- ⏸️ **Pause/Resume** - Pause searches between iterations and resume when ready
- 🎲 **Random Keywords** - Uses a list of keywords to randomize search queries
- ⏱️ **Smart Timing** - Configurable delays between searches with randomization
- 🎨 **Modern UI** - Clean, responsive web interface
- ✅ **Progress Tracking** - Real-time status updates during execution

## Requirements

- Python 3.7+
- Flask
- Modern web browser (Chrome, Firefox, Edge, Safari)

## Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/iArudra/Bing_Rewards
   cd path/to/Bing_Rewards
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install flask
   ```

## Usage

### Option 1: Direct (Recommended - Easiest)

Simply open `HOME.html` directly in your browser:
- **Windows:** Double-click `HOME.html` or right-click → Open with → Your browser
- **macOS/Linux:** Double-click `HOME.html`

The application should work immediately if your browser allows local file access.

### Option 2: Backend Server (If Option 1 Doesn't Work)

If the application doesn't work with Option 1, use the Flask backend server:

1. **Start the Flask server**
   ```bash
   python backend.py
   ```
   The server will run at `http://localhost:5000`

2. **Open the web interface**
   - Open your browser and navigate to `http://localhost:5000`

### Running Searches

Once the interface loads (via either option):
   - Enter the number of searches to run (1-100)
   - Click **Start** to begin the automation
   - Each search will:
     - Open a Bing search window with a random keyword
     - Stay open for 3-6 seconds
     - Close automatically
     - Wait 6-10 seconds before the next search

3. **Control searches**
   - **Pause** - Click to pause during execution
   - **Resume** - Click to resume paused searches
   - **Reset** - Clear the form and cancel any running searches

## How It Works

1. **Frontend (HOME.html)**
   - User selects number of searches and clicks Start
   - JavaScript randomly selects keywords from `list.txt`
   - Opens Bing search URLs in new windows
   - Closes windows after a random delay (3-6 seconds)
   - Implements pause/resume functionality
   - Maintains random intervals between searches (6-10 seconds)

2. **Styling (styles.css)**
   - Modern gradient design
   - Responsive layout
   - Smooth animations
   - Interactive button states

## Notes

- The tool uses Bing's search API with query parameters
- Each search opens in a new browser window
- Windows close automatically based on configured timing
- Pause function pauses between searches, not during active search windows
- Reset button clears the form and cancels ongoing automation

## Troubleshooting

**If Option 1 (Direct HTML) doesn't work:**
- Some browsers block local file access for security reasons
- Solution: Use Option 2 (Backend Server) instead
- Or: Use a Live Server extension in your code editor (VS Code Live Server, etc.)

**Keywords not loading**
- Ensure `list.txt` exists in the same directory 
- Check that keywords are properly formatted (one per line)

**Pop-up blocker interference**
- Disable pop-up blockers for `localhost` or the server's IP
- Some browsers may still block the windows depending on settings

## License

This project is for educational purposes. Use responsibly and in accordance with Bing's Terms of Service.

