
# 🚀 Tumor Marker AI - Docker Deployment QuickStart

This guide helps you spin up the complete Tumor Marker AI system using Docker and n8n automation.

---

## 📂 Folder Structure

```
your-project-folder/
├── docker-compose.yml
├── Dockerfile
├── n8n_data/              # (empty initially, auto-generated)
├── project_files/         # (synthetic data, scripts, workflows)
│   ├── synthetic_clinical_data.csv
│   ├── train_and_generate_reports.py
│   ├── tumor_marker_ai_workflow.json
│   ├── reports/           # (auto-created outputs)
```

---

## 🔥 Quick Deployment Steps

### 1. Clone or prepare your project folder
Ensure you have all the necessary files.

### 2. Build the custom n8n + Python image

```bash
docker-compose build
```

### 3. Launch the stack

```bash
docker-compose up -d
```

- n8n Dashboard: http://localhost:5678
- Login using:
  - Username: `admin`
  - Password: `yourpassword`

### 4. Load the Workflow

- In n8n, import `tumor_marker_ai_workflow.json`
- Adjust any paths or credentials inside the workflow if needed

### 5. Execute the Workflow

- Manually trigger or schedule via Cron node
- The workflow will:
  - Load clinical data
  - Run machine learning model (train + predict)
  - Generate reports (HTML, Markdown, PDF)
  - Send Email Notification

---

## 🛠️ Environment Variables (in docker-compose.yml)

| Variable | Purpose |
|:---------|:--------|
| N8N_BASIC_AUTH_ACTIVE | Enable basic auth login |
| N8N_BASIC_AUTH_USER | Set the admin username |
| N8N_BASIC_AUTH_PASSWORD | Set the admin password |
| GENERIC_TIMEZONE | Set your timezone (for scheduling tasks) |

---

## 🎯 Pro Tips

- To modify or add Python packages, edit the Dockerfile.
- To persist workflows, n8n saves everything inside the `n8n_data/` folder.
- For production setups, consider attaching a real database (Postgres) and SSL.

---

Happy Deploying! 🚀
