# ADR 001: Tech Stack and Architecture Decisions for AI-Native Physical AI & Humanoid Robotics Book

## Status
Accepted

## Context
We need to establish the foundational technology stack and architectural approach for the AI-Native Physical AI & Humanoid Robotics Book project. This book will include embedded RAG chatbot functionality and must be deployable via GitHub Pages.

## Decision
We have decided on the following technology stack and architectural approach:

### Documentation Platform
- **Docusaurus** as the documentation framework
- Deployed to **GitHub Pages** for public accessibility
- Structure follows **Spec-Kit Plus conventions**
- Navigation progresses logically from basics to advanced topics

### Backend Technology
- **Python** with **FastAPI** for the backend
- Enables rapid development of the RAG chatbot API
- Good async support for handling concurrent chat requests

### Database Technology
- **Neon Serverless Postgres** for metadata and logs
- Serverless offering fits within free-tier constraints
- Familiar SQL interface for managing metadata

### Vector Database
- **Qdrant Cloud** (free tier) for embeddings and retrieval
- Specialized for vector similarity search required for RAG
- Managed service reduces operational overhead

### Frontend Integration
- **TypeScript or JavaScript** for frontend integration
- Enables type safety and robust frontend development
- Compatible with Docusaurus ecosystem

### AI Integration Philosophy
- **AI-native design**: AI is treated as a first-class system component
- All architectures and workflows consider AI integration from the initial design phase
- Ensures seamless integration of the embedded RAG chatbot

## Alternatives Considered
- Static site generators: Hugo, Gatsby, VuePress (selected Docusaurus for its React foundation and plugin ecosystem)
- Backend frameworks: Express.js, Django, Flask (selected FastAPI for async support and modern Python features)
- Vector databases: Pinecone, Weaviate, ChromaDB (selected Qdrant for free tier and self-hosting options)
- Database options: SQLite, MongoDB, Supabase (selected Neon for PostgreSQL compatibility and serverless features)

## Consequences
### Positive
- Modern, well-supported technology stack
- Free-tier compatible to minimize costs
- Scalable architecture for future enhancements
- Strong type safety with TypeScript and Python typing
- Robust async handling with FastAPI

### Negative
- Learning curve for team members unfamiliar with Python/FastAPI
- Potential limitations of free tiers as the project scales
- Dependency on multiple third-party services