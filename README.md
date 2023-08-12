# LangChain Demo Application 🤖

LangChain Demo is a Streamlit-based web application that provides an interactive Q&A experience about a fictive animal called "huninchen". It integrates Azure services and leverages OpenAI to create a smooth, responsive, and insightful experience.

## Prerequisites

For this project, ensure you have set up:

1. **Azure Container Registry**: To manage the Docker images.
2. **App Services**: Where the application will be hosted.
3. **Blob Storage**: For storing unstructured data.
4. **Azure Cognitive Search**: Powers the application's Q&A functionality.
5. **OpenAI API Key**: For generating natural language model responses.

## Configuration

### `.env.example`

```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
AZURE_COGNITIVE_SEARCH_SERVICE_NAME=YOUR_AZURE_COGNITIVE_SEARCH_SERVICE_NAME
AZURE_COGNITIVE_SEARCH_INDEX_NAME=YOUR_AZURE_COGNITIVE_SEARCH_INDEX_NAME
AZURE_COGNITIVE_SEARCH_API_KEY=YOUR_AZURE_COGNITIVE_SEARCH_API_KEY
AZURE_CONN_STRING=YOUR_AZURE_CONN_STRING
CONTAINER_NAME=YOUR_CONTAINER_NAME
```

Replace placeholder values (`YOUR_...`) with actual values from your environment.

### `blob.py`

This script automates the process of uploading data from the local "Data" directory to Azure Blob storage. It initializes a connection to the Blob service and then uploads each file it discovers in the specified directory to the container.

### `azurecognitive_search.py`

This script is responsible for creating vector embeddings from documents and loading them into Azure Cognitive Search. It uses the OpenAI API for embedding generation. Once the embeddings are created, they are stored in the Azure Search index, making them readily available for fast and efficient searching.

### `application.py`

This is the main Streamlit application. It sets up a conversational interface where users can input questions. The input is then processed with the help of OpenAI's model and Azure Cognitive Search, and an appropriate answer is retrieved or generated. Past interactions can be reviewed in the session.

---

To get started with the LangChain Demo Application, first, ensure that the necessary Azure services are set up and that the `.env` file is correctly populated with the required keys and identifiers. Follow the deployment steps for Azure to host and run your application.
