# HR Resume Checker | AI-Powered Resume Screening 📄🤖

A full-stack AI-powered resume screening platform that helps HR teams automate candidate review and selection. Built using **React**, **Node.js**, and **Azure**, this project integrates **Azure AI Document Intelligence** for parsing resumes, while **Axios** in the frontend fetches and displays parsed candidate data for easy filtering and review.

## Table of Contents 📚

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Setup](#setup)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview 🌟

The **HR Resume Checker** uses **Azure AI Document Intelligence** to parse resumes stored in **Azure Blob Storage** and then processes the data in **Azure Cosmos DB**. The system's backend, built with **Node.js**, retrieves the parsed resume data and serves it to a frontend built with **React**. **Axios** is used in React to efficiently fetch and display candidate profiles, while the UI allows HR teams to filter candidates based on skills, email, and resume metadata.

## Tech Stack 🛠️

- **Frontend**: React, Axios, Tailwind CSS
- **Backend**: Node.js, Express
- **Database**: Azure Cosmos DB
- **AI/ML**: Azure AI Document Intelligence
- **Cloud Storage**: Azure Blob Storage
- **Authentication**: JWT (for secure login)

## Features 🎉

- **Resume Parsing**: Automatically parses resumes uploaded to **Azure Blob Storage** using **Azure AI Document Intelligence**.
- **Real-Time Candidate Filtering**: HR teams can filter candidates based on various attributes like skills, email, and resume metadata.
- **Scalable Storage**: Utilizes **Azure Cosmos DB** for secure and scalable candidate data storage.
- **User-Friendly UI**: Built with **React** and **Tailwind CSS**, offering an intuitive interface for HR teams to interact with the system.
- **Efficient Data Fetching**: **Axios** is used to fetch and display parsed data dynamically on the frontend.

## Setup ⚙️

To set up and run the project locally, follow these steps:

### Backend Setup ⚡

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hr-resume-checker.git
   cd hr-resume-checker
   ```

2. Navigate to the `backend` folder and install dependencies:
   ```bash
   cd backend
   npm install
   ```

3. Set up environment variables for **Azure Blob Storage** and **Cosmos DB** connection strings. You can refer to `.env.sample` for the required fields.

4. Start the backend server:
   ```bash
   npm start
   ```

### Frontend Setup 🖥️

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. Visit `http://localhost:3000` in your browser to see the app in action. 🌍

---

## API Endpoints 📡

- **POST /api/upload-resume**: Upload a resume to **Azure Blob Storage** for parsing.
- **GET /api/candidates**: Retrieve parsed candidate data from **Azure Cosmos DB**.
- **GET /api/candidate/:id**: Retrieve detailed data for a specific candidate.

---

## Usage 🔧

Once the app is running, HR teams can:
- Upload resumes to be parsed by **Azure AI Document Intelligence**.
- View a list of candidates, filterable by skills, email, and other metadata.
- Review candidate information quickly and efficiently with real-time updates from **Cosmos DB**.

---

## Contributing 🤝

We welcome contributions! Feel free to fork the repository and submit a pull request with any improvements, bug fixes, or new features. Please follow the standard GitHub workflow for contributions.

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
