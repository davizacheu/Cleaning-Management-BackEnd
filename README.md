# Cleaning Management BackEnd

A backend application for managing cleaning services efficiently. This project is designed to streamline operations, manage resources, and provide a reliable backend infrastructure for a cleaning management system.

## Features

- **User Management**: Create, update, and manage user accounts.
- **Service Management**: Handle various cleaning services and their schedules.
- **Resource Allocation**: Efficiently allocate resources to meet service requirements.
- **Real-time Notifications**: Send alerts and updates to users.
- **Cloud Deployment**: Deployable to Google Cloud Run for scalability and reliability.

## Technologies Used

- **Backend Development**: Python
- **Frontend Integration**: HTML, CSS
- **Containerization**: Docker
- **Deployment**: Google Cloud Run
- **Shell Scripting**: For automation tasks
- **Build and Deployment**: Procfile for process management

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/davizacheu/Cleaning-Management-BackEnd.git
   cd Cleaning-Management-BackEnd
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:
   ```bash
   python app.py
   ```

5. Optionally, use Docker:
   ```bash
   docker build -t cleaning-backend .
   docker run -p 8000:8000 cleaning-backend
   ```

## Usage

1. Access the application by navigating to `http://localhost:8000` in your browser.
2. Use the API for managing users, services, and resources.
3. Deploy the application to Google Cloud Run for production use.

## Deployment

Follow the steps in the `README.md` to deploy the application to Google Cloud Run:

1. Authenticate with Google Cloud:
   ```bash
   gcloud auth login
   ```

2. Deploy the application:
   ```bash
   gcloud run deploy
   ```

Refer to the [Google Cloud Run documentation](https://cloud.google.com/run/docs) for more details.


Feel free to adjust any sections or add more details specific to your project. Let me know if you'd like further assistance!
