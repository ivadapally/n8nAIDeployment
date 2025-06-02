# Tumor Marker AI Project (n8n + Python + Docker)

This repository contains the code and configuration for an automated workflow that uses n8n, Python, and Docker to train a simple AI model for tumor marker-based cancer risk prediction, generate reports, and send notifications.

## Overview

The project demonstrates how to integrate a custom Python script for machine learning tasks within an n8n workflow, all packaged within a Docker container for easy deployment and reproducibility. It uses synthetic clinical data to train a Logistic Regression model, predicts risk on a test set, generates reports (MD, HTML, PDF), and sends an email notification upon completion.

## Features

*   **Automated Workflow:** End-to-end automation from data reading to report notification using n8n.
*   **AI Model Training:** Includes a Python script using `scikit-learn` for model training and prediction.
*   **Multi-Format Reporting:** Generates classification reports in Markdown, HTML, and PDF formats using `fpdf`.
*   **Containerized Deployment:** Uses Docker and Docker Compose for easy setup and consistent environments.
*   **Customizable:** Built with flexibility in mind, allowing for modifications to the AI model, data sources, and workflow steps.

## Architecture

The workflow utilizes Docker to run a custom n8n image containing Python and necessary libraries. Docker Compose orchestrates the service and manages volume mounts for data, scripts, and reports.


**Components:**

1.  **Docker Host:** Machine running Docker.
2.  **Docker Compose:** Defines and runs the n8n service.
3.  **Custom n8n Image:** Built via `Dockerfile`, includes Python, pandas, scikit-learn, fpdf.
4.  **n8n Container:** Runs the n8n application.
5.  **n8n Workflow (`tumor_marker_ai_workflow.json`):** Orchestrates the process (Read Data -> Execute Script -> Send Email).
6.  **Python Script (`train_and_generate_reports.py`):** Performs AI tasks and report generation.
7.  **Volumes:** Map host directories to container paths for data persistence and file access (`./data:/mnt/data`, `./reports:/files`, `./n8n_data:/home/node/.n8n`).

## Repository Structure

```
/
|-- Dockerfile                # Builds the custom n8n image with Python deps
|-- docker-compose.yml        # Defines the n8n service and volumes
|-- README.md                 # This file
|-- src/                      # Python source code
|   |-- train_and_generate_reports.py
|-- data/                     # Input data
|   |-- synthetic_clinical_data.csv
|-- n8n/                      # n8n workflow definitions
|   |-- tumor_marker_ai_workflow.json
|-- reports/                  # Output reports (created by workflow)
|-- n8n_data/                 # Persistent n8n data (created by Docker)
|-- docs/                     # Documentation assets
|   |-- Tumor_Marker_AI_Deployment_Diagram.png 
```

## Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Verify File Placement:** Ensure the `data/` directory contains `synthetic_clinical_data.csv` and `train_and_generate_reports.py`, and the `n8n/` directory contains `tumor_marker_ai_workflow.json`.
3.  **Review `docker-compose.yml`:** Check the volume mappings (`./data:/mnt/data`, `./reports:/files`, `./n8n_data:/home/node/.n8n`) and environment variables. Adjust if necessary for your environment (e.g., `TZ` for timezone).
4.  **Build and Start:** Open a terminal in the project root directory and run:
    ```bash
    docker-compose up --build -d
    ```
    *   `--build`: Ensures the custom Docker image is built.
    *   `-d`: Runs the container in detached mode.

## Usage

1.  **Access n8n:** Open your web browser and navigate to `http://localhost:5678` (or the host IP/domain if running remotely).
2.  **Login:** Use the basic authentication credentials defined in `docker-compose.yml` (default: `admin`/`adminpassword`).
3.  **Import Workflow:**
    *   Go to the "Workflows" section.
    *   Click "Import from File".
    *   Select the `n8n/tumor_marker_ai_workflow.json` file from your local clone of the repository.
4.  **Configure Email Node:**
    *   Open the imported "Tumor Marker AI Workflow".
    *   Edit the "Send Email Notification" node.
    *   Enter valid SMTP credentials for your email provider (e.g., Gmail requires Host: `smtp.gmail.com`, Port: `587`, User, and an App Password).
    *   Update the "To Email" field with the desired recipient address.
5.  **Activate Workflow:** Save the changes and toggle the workflow to "Active" using the switch in the top-right corner.
6.  **Execute Workflow:** Click the "Execute Workflow" button.
7.  **Check Results:**
    *   Monitor the execution visually in the n8n interface.
    *   Upon successful completion, check the recipient email inbox for the notification.
    *   Check the `reports/` directory in your local project folder for the generated `report.md`, `report.html`, and `report.pdf` files.

## Workflow Explanation

1.  **Trigger:** Starts manually.
2.  **Read Binary File:** Reads `/mnt/data/synthetic_clinical_data.csv`.
3.  **Execute Command:** Runs `python3 /mnt/data/train_and_generate_reports.py`.
    *   The Python script reads data from `/mnt/data/synthetic_clinical_data.csv` (Note: ensure script path matches volume mount strategy).
    *   Trains a Logistic Regression model.
    *   Generates a classification report.
    *   Saves reports (`.md`, `.html`, `.pdf`) to `/files/` (mapped to `./reports` on host).
4.  **Send Email:** Sends a notification upon script completion.

## Docker Details

*   **`Dockerfile`:** Extends `n8nio/n8n`, installs `python3`, `pip3`, `pandas`, `scikit-learn`, `fpdf`.
*   **`docker-compose.yml`:** Defines the `n8n` service, builds the image, maps port `5678`, sets environment variables, and crucially maps volumes:
    *   `./n8n_data:/home/node/.n8n`: Persists n8n state.
    *   `./data:/mnt/data`: Provides input data and script to the container.
    *   `./reports:/files`: Retrieves output reports from the container.

## Troubleshooting

*   **File Not Found Errors:** Double-check volume mappings in `docker-compose.yml` and ensure paths used in n8n nodes (`/mnt/data/...`) and the Python script (`/mnt/data/...` for input, `/files/...` for output) are consistent with these mappings.
*   **Email Node Fails:** Verify SMTP credentials, ensure the host/port are correct, and check if an App Password is required (e.g., for Gmail).
*   **Python Errors:** Check the n8n execution log for errors from the `Execute Command` node. Ensure all dependencies were correctly installed in the `Dockerfile`.

## Future Enhancements

*   Integrate with real clinical data sources (EHRs, databases).
*   Use more advanced AI/ML models.
*   Add cloud storage integration (S3, Google Drive).
*   Enhance reporting with visualizations.
*   Implement robust monitoring and alerting.
*   Parameterize the workflow.
*   Develop a user interface (Flask, Streamlit).

## Contributing

(Optional: Add contribution guidelines if applicable)

## License

(Optional: Add license information - e.g., MIT, Apache 2.0)



## Additional Documentation

For more detailed information, refer to the following documents included in the `docs/` directory:

*   **Deployment Diagram:** `docs/Tumor_Marker_AI_Deployment_Diagram.png`
*   **Docker Cheatsheets & Guides:**
    *   `docs/Clean_Docker_Commands_Cheatsheet.pdf`
    *   `docs/Docker_Build_Compose_Commands_Cheatsheet.pdf`
    *   `docs/Docker_vs_DockerCompose_vs_Dockerfile.pdf`
    *   `docs/Dockerfile_Version_Tracker_Tumor_Marker_AI_Clean.pdf`
    *   `docs/Clean_Docker_Desktop_Install_Guide.pdf`
*   **n8n & Python Cheatsheets:**
    *   `docs/Fix_Python_File_Missing_in_Docker_n8n_Cheatsheet.pdf`
    *   `docs/Run_Python_in_Docker_n8n_Cheatsheet.pdf`
    *   `docs/Where_to_Save_Files_in_n8n_Docker_Cheatsheet.pdf`
    *   `docs/Python_Virtualenv_in_Docker_CheatSheet.pdf`
*   **Other:**
    *   `docs/Alpine_vs_Ubuntu_Package_Manager_Cheatsheet.pdf`

