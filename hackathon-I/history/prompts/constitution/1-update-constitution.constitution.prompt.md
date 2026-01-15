---
id: 1
title: Update Constitution
stage: constitution
date: 2026-01-15
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: RohmaShabbir <rohmafatima132@gmail.com>
command: /sp.constitution
labels: [constitution,documentation,setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---
## Prompt

```
/sp.constitution

Project:
AI-Native Physical AI & Humanoid Robotics  Book with Embedded RAG Chatbot
(Docusaurus + Spec-Kit Plus + Claude Code + OpenAI Agents)

Core Principles:
- Spec-driven development is mandatory; no undocumented behavior
- Accuracy and technical correctness are required for all content and code
- Clarity for software engineers and AI practitioners
- AI-native design: AI is a first-class system component
- Reproducibility: readers must be able to rebuild everything end-to-end

Key Standards:

Book Content:
- Target audience: developers, AI engineers, advanced learners
- Writing style: clear, structured, implementation-focused
- Reading level: Flesch-Kincaid grade 10–12
- Consistent terminology across all chapters
- Each chapter must include:
  - Concept explanation
  - Architecture or workflow description
  - Code examples where applicable
  - Summary and key takeaways

Documentation & Platform:
- Documentation framework: Docusaurus
- Deployment target: GitHub Pages
- Structure must follow Spec-Kit Plus conventions
- Navigation must progress logically from basics to advanced topics

Technical Accuracy:
- All APIs and SDKs must be current and non-deprecated
- No fabricated or hypothetical APIs
- RAG concepts must be explained correctly:
  - Embeddings
  - Vector search
  - Retrieval
  - Context grounding
  - Response generation

RAG Chatbot Requirements:
- Chatbot must be embedded inside the published book UI
- Tech stack:
  - OpenAI Agents / ChatKit SDKs
  - FastAPI backend
  - Neon Serverless Postgres (metadata and logs)
  - Qdrant Cloud (vector database, free tier)

Chatbot Functionality:
- Answer questions about the full book content
- Answer questions based only on user-selected text
- Must not hallucinate beyond retrieved context
- Clearly separate retrieval, reasoning, and response generation

Constraints:
- Book format: Markdown (Docusaurus compatible)
- Backend language: Python (FastAPI)
- Frontend integration: TypeScript or JavaScript
- Must stay within free-tier limits where spec
```

## Response snapshot

Updated the project constitution file (.specify/memory/constitution.md) to reflect the core principles for the AI-Native Physical AI & Humanoid Robotics Book project. The constitution now includes:

- Spec-Driven Development Mandatory principle
- Technical Accuracy and Correctness principle
- AI-Native Design Philosophy principle
- Reproducibility Requirement principle
- Target Audience Focus principle
- Documentation Platform Standard principle
- Content Standards section
- Technical Implementation Standards section
- Constraints and Boundaries section
- Governance section

The constitution serves as the foundational document that governs all development and content creation for the project.

## Outcome

- ✅ Impact: Created foundational project constitution with 6 core principles and governance rules
- 🧪 Tests: N/A (documentation update)
- 📁 Files: Updated .specify/memory/constitution.md with project-specific principles
- 🔁 Next prompts: Proceed with spec creation based on this constitution
- 🧠 Reflection: Constitution properly captures all specified principles and constraints

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin spec creation for the first feature