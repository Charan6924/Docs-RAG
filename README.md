# RAG Chatbot

## Setup: Google Drive Data Source

This application uses Google Drive and Docs as the knowledge base source for the RAG pipeline. Follow these steps to configure access.

### 1. Google Cloud Configuration
1.  Navigate to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
2.  **Enable APIs:**
    * Go to **APIs & Services > Library**.
    * Search for and enable **Google Drive API**.
    * Search for and enable **Google Docs API**.
3.  **Configure OAuth Consent:**
    * Go to **APIs & Services > OAuth consent screen**.
    * Select **External** (for personal testing) or **Internal** (if using a Workspace org).
    * **Important:** Add your email address to the **Test Users** list.
4.  **Generate Credentials:**
    * Go to **Credentials > Create Credentials > OAuth client ID**.
    * Select **Desktop app** as the application type.
    * Download the client secret JSON file.

### 2. Local Environment
1.  **Place Credentials:**
    * Rename the downloaded JSON file to `credentials.json`.
    * Move it to the root directory of this project.

2.  **Install Dependencies:**
    ```bash
    pip -r requirements.txt
    ```
