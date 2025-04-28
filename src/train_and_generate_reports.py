import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from fpdf import FPDF

# Ensure /files/ exists
os.makedirs('/files', exist_ok=True)

# Load synthetic clinical dataset
csv_path = '/files/synthetic_clinical_data.csv'
df = pd.read_csv(csv_path)

# Features = all columns except Patient_ID and Cancer_Risk
X = df.drop(['Patient_ID', 'Cancer_Risk'], axis=1)

# Target = Cancer_Risk
y = df['Cancer_Risk']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model Training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Model Prediction
y_pred = model.predict(X_test)

# Generate Classification Report
report = classification_report(y_test, y_pred)

# Save Markdown Report
with open('/files/report.md', 'w') as mdfile:
    mdfile.write("# Cancer Risk Prediction Report\n\n")
    mdfile.write("```\n")
    mdfile.write(report)
    mdfile.write("\n```")

# Save HTML Report
with open('/files/report.html', 'w') as htmlfile:
    htmlfile.write("<h1>Cancer Risk Prediction Report</h1><pre>")
    htmlfile.write(report)
    htmlfile.write("</pre>")

# Save PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Cancer Risk Prediction Report", ln=True, align="C")
pdf.ln(10)
for line in report.split("\n"):
    pdf.cell(200, 10, txt=line, ln=True)
pdf.output("/files/report.pdf")

print("✅ Training, Prediction, and Report Generation Completed.")