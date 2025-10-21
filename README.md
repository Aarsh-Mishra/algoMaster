# AlgoMaster - AI-Powered DSA Problem Solver

AlgoMaster is an application that uses a team of AI agents, built with **AutoGen**, to solve Data Structures and Algorithms (DSA) problems. It provides a simple web interface using **Streamlit** where you can input a problem statement, and the AI agents will collaborate to generate a plan, write Python code, execute it securely in a **Docker** container, and return the solution with an explanation.

## ✨ Features

* **AI Agent Team:** Uses a multi-agent team to solve problems:
    * `DSA_problem_solver_Agent`: An expert agent that understands the DSA problem, creates a plan, and writes Python code with test cases.
    * `code_executor_agent`: An agent that securely executes the provided code inside a Docker container.
* **Web Interface:** A user-friendly UI built with Streamlit to interact with the agents.
* **Secure Code Execution:** All code is run within a sandboxed Docker environment to prevent security risks.
* **Powered by Gemini:** Uses the Gemini model (via `gemini-2.0-flash`) for intelligent problem-solving.

## 🛠️ Tech Stack

* **Framework:** Streamlit
* **AI Agents:** Microsoft AutoGen (`autogen-agentchat`, `autogen-core`)
* **LLM:** Google Gemini (via `openai` compatible client)
* **Code Execution:** Docker (`autogen-ext[docker]`)
* **Language:** Python

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Docker Desktop (must be running)
* A Google Gemini API Key

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/algoMaster.git](https://github.com/your-username/algoMaster.git)
cd algoMaster
