
FROM n8nio/n8n:latest

USER root

# Install Python3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas scikit-learn fpdf markdown2

USER node
