# Youtube Video Downloader

## Overview

This project is a web-based YouTube Video Downloader that allows users to enter a YouTube video URL and download the video directly to their system. The frontend is built with React + Tailwind CSS, and the backend is powered by Flask + yt-dlp for processing and fetching video files.

## Features

- User Input: Enter a YouTube video URL in a text field.
- Validation: Ensures the entered URL is a valid YouTube link.
- Download Mechanism: Fetches and processes the video from YouTube.
- Direct Browser Download: Video is downloaded directly into the user's "Downloads" folder.
- Toast Notifications: Shows success or error messages for user feedback.
- Responsive UI: Works on desktop and mobile devices.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo
   ```
3. Install dependencies for both frontend and backend:
   ```bash
   npm install
   ```

## Running the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Start the development server:
   ```bash
   npm start
   ```
3. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

## Running the Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Start the backend server:
   ```bash
   python server.py
   ```
3. The backend server will typically run on [http://localhost:5000](http://localhost:5000) or another specified port.

## Building for Production

To build the frontend app for production, run:
