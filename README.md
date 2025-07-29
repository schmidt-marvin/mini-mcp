# Mini MCP Chat App

A simple chat application built with FastAPI and Pydantic AI, demonstrating:

- Reusing chat history between requests
- Serializing messages for persistence
- Streaming responses to the browser
- Real-time conversation interface

## Features

- **Chat History**: Maintains conversation context across sessions using SQLite
- **Streaming Responses**: Real-time message streaming for better user experience
- **Modern UI**: Clean, responsive interface built with Bootstrap
- **TypeScript Frontend**: Dynamic message rendering with markdown support

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set up your environment variables (create a `.env` file):
   ```bash
   # Add your OpenAI API key or other model provider credentials
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application

### Using the run script:
```bash
./run.sh
```

### Or directly with Python:
```bash
python main.py
```

### Or with uv:
```bash
uv run main.py
```

The application will start on `http://localhost:8000`

## Project Structure

- `app/chat_app.py` - FastAPI backend with streaming chat logic
- `app/chat_app.html` - Frontend HTML interface
- `app/chat_app.ts` - TypeScript for message handling and rendering
- `main.py` - Application entry point

## Source

This project is based on the [Pydantic AI Chat App example](https://ai.pydantic.dev/examples/chat-app/), which demonstrates how to build chat applications with FastAPI and Pydantic AI.

## License

This project follows the same principles and patterns as the Pydantic AI examples.
