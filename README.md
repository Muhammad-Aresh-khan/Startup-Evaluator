# Startup Evaluator

AI-powered multi-agent system that analyzes startup ideas, generates brand names, and performs market research using CrewAI, LiteLLM (Groq), and Streamlit for real-time interaction.

## Features

- **AI-Driven Evaluation:** Automatically analyzes startup ideas for feasibility and potential.
- **Brand Name Generation:** Generates unique and relevant brand names tailored to your startup concept.
- **Market Research:** Performs comprehensive market analysis to assess demand, competition, and opportunities.
- **Real-Time Interaction:** Interactive web interface powered by Streamlit for instant feedback and results.
- **Multi-Agent System:** Utilizes CrewAI and LiteLLM (Groq) for distributed, intelligent processing.

## Tech Stack

- **Python:** Core programming language.
- **CrewAI:** Multi-agent orchestration and task management.
- **LiteLLM (Groq):** Fast and efficient language model inference.
- **Streamlit:** User-friendly web-based interface for real-time input and results.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Groq API access (for LiteLLM)
- [Optional] Virtual environment tool (e.g., `venv` or `conda`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad-Aresh-khan/Startup-Evaluator.git
   cd Startup-Evaluator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your API keys and configuration as needed (e.g., Groq API key).

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the app:**
   - Open your browser and go to `http://localhost:8501`

## Usage

1. Enter your startup idea in the provided input field.
2. Click the button to analyze your idea.
3. View the generated brand names, market research, and evaluation results in real time.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [LiteLLM](https://github.com/BerriAI/litellm)
- [Streamlit](https://streamlit.io/)
