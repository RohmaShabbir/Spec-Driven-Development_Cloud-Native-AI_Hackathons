<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: None (new constitution)
Added sections: All sections added
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->

# AI-Native Physical AI & Humanoid Robotics Book Constitution

## Core Principles

### Spec-Driven Development Mandatory
All content and code must follow documented specifications with no undocumented behavior. Every feature, chapter, and implementation detail must be specified before development begins. This ensures reproducibility and prevents scope creep.

### Technical Accuracy and Correctness
All content must be technically accurate with current, non-deprecated APIs and SDKs. No fabricated or hypothetical APIs are allowed. RAG concepts must be explained with precision: embeddings, vector search, retrieval, context grounding, and response generation.

### AI-Native Design Philosophy
AI must be treated as a first-class system component throughout the book. All architectures, workflows, and implementations must consider AI integration from the initial design phase, not as an afterthought.

### Reproducibility Requirement
All examples, code snippets, and implementations must be reproducible. Readers must be able to rebuild everything end-to-end following the book's instructions. This includes complete setup procedures, dependencies, and deployment steps.

### Target Audience Focus
Content must be designed for developers, AI engineers, and advanced learners with a reading level of Flesch-Kincaid grade 10-12. Terminology must be consistent across all chapters with clear explanations of complex concepts.

### Documentation Platform Standard
All content must be compatible with the Docusaurus documentation framework and deployable to GitHub Pages. Structure must follow Spec-Kit Plus conventions with logical navigation progression from basics to advanced topics.

## Content Standards
All book content must meet the following requirements:
- Each chapter must include concept explanation, architecture/workflow description, and code examples where applicable
- Writing style must be clear, structured, and implementation-focused
- Consistent terminology must be maintained across all chapters
- Each chapter must conclude with a summary and key takeaways

## Technical Implementation Standards
All technical implementations must adhere to these standards:
- Backend technology: Python with FastAPI
- Database technology: Neon Serverless Postgres for metadata and logs
- Vector database: Qdrant Cloud (free tier) for embeddings and retrieval
- Frontend integration: TypeScript or JavaScript
- RAG chatbot must be embedded within the published book UI
- Chatbot functionality limited to answering questions based on book content and user-selected text
- Strict anti-hallucination requirement: responses must be grounded in retrieved context only

## Constraints and Boundaries
The following constraints must be respected:
- Book format: Markdown compatible with Docusaurus
- Must stay within free-tier limits of all services
- Content must be organized following Spec-Kit Plus conventions
- Navigation must progress logically from basic concepts to advanced implementations
- All APIs and SDKs must be current and non-deprecated

## Governance
This constitution supersedes all other practices and guidelines in the project. All contributions must verify compliance with these principles. Amendments to this constitution require explicit documentation of the changes, approval from project maintainers, and a migration plan for existing content. All pull requests and reviews must verify constitutional compliance before merging.

**Version**: 1.0.0 | **Ratified**: 2026-01-15 | **Last Amended**: 2026-01-15
