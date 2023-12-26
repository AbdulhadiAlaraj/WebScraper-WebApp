# Web Scraper Application

## Overview

This application is a web scraping tool that allows users to specify a URL and parameters for scraping web content. It uses a FastAPI backend for handling scraping logic and a Streamlit frontend for user interaction. The application is containerized using Docker for easy setup and deployment. 

Go to https://github.com/AbdulhadiAlaraj/WebScraper for more details on the scraper.

## Features

- **User-Friendly Interface**: Powered by Streamlit, users can easily input their scraping parameters and initiate the scraping process.
- **Robust Backend**: The FastAPI backend handles scraping requests, processes data, and returns results.
- **Containerized Deployment**: Docker containers ensure that the application runs consistently across all environments.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**
``` bash
git clone https://github.com/AbdulhadiAlaraj/WebScraper-WebApp.git
cd WebScraper-WebApp
```
2. **Build and Run with Docker Compose**
``` bash
docker-compose up --build
```


This command builds the Docker images for the Streamlit and FastAPI services and starts the containers. After running the containers, the Streamlit frontend will be accessible at `http://localhost:8501`, and the FastAPI backend will be available at `http://localhost:8000`.

### Using the Application

1. **Access the Streamlit Interface**: Open your browser and go to `http://localhost:8501`.
2. **Input Parameters**: Enter the required parameters for the web scraping task, such as the URL, match pattern, CSS selector, and output file name.
3. **Start Scraping**: Submit the form to start the scraping process. The results will be displayed or made available for download, as configured.

## Development

### File Structure

- `Dockerfile.fastapi` - Dockerfile for the FastAPI backend.
- `Dockerfile.streamlit` - Dockerfile for the Streamlit frontend.
- `docker-compose.yml` - Docker Compose configuration for running the application.
- `main.py` - The FastAPI application.
- `streamlit_app.py` - The Streamlit application.
- `WebScraper.py` - The web scraping logic.

### Customization

You can customize the application by modifying the source code:

- **Streamlit Frontend**: Edit `streamlit_app.py` to change the user interface or add new features.
- **FastAPI Backend**: Modify `main.py` to adjust the API endpoints or enhance the scraping logic.
- **WebScraper Logic**: Update `WebScraper.py` to alter the scraping behavior or add new capabilities.
