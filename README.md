# Calibra
Calibra is an all-in-one AI-integrated conferencing platform designed to enhance productivity and streamline workflows. With features like natural language SQL query generation, AI-powered data visualization, and seamless workflow integration, Calibra empowers users to achieve more with less effort.

---

## Features

- **Natural Language SQL**: Generate SQL queries effortlessly using natural language with the help of our AI assistant.
- **Data Visualization**: Create beautiful visualizations of your data with ease.
- **Workflow Enhancement**: Seamlessly transcribe meeting details, draft and send emails, set reminders, and more without interrupting your workflow.
- **Real-Time Results**: Get real-time results directly within virtual conference rooms or your personal workflow.
- **Customizable**: Tailor the AI assistant to work the way you want it to.
- **Secure**: Our platform is secure and encrypted, ensuring that your data is always safe.

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Docker
- Docker Compose

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/calibra.git
   cd calibra
   ```

2. **Set up the environment:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Build and run the application:**
   ```bash
   docker-compose up --build
   ```

4. **Access the application:**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:8000](http://localhost:8000)

---

## Technologies Used

- **Frontend**: React, Redux, Axios, Socket.io
- **Backend**: Django, Django REST Framework, Channels, Celery
- **Database**: PostgreSQL
- **Others**: Docker, Docker Compose, Redis



