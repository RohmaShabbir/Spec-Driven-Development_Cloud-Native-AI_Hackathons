# ADR 003: Docusaurus-Based Educational Architecture for ROS 2 Module

## Status
Accepted

## Context
We need to establish the architectural approach for delivering the ROS 2 educational content as part of the Physical AI curriculum. The solution must balance educational effectiveness with technical simplicity, maintainability, and accessibility.

## Decision

### Documentation Platform Choice
- **Docusaurus** selected as the documentation framework over alternatives like Hugo, Gatsby, or VuePress
- Reason: React-based foundation with excellent plugin ecosystem and strong community support
- Advantage: Seamless integration with existing web technologies and good extensibility

### Content Structure
- **Modular Organization** by topics/modules in separate directories
- **Markdown Format** for all content to ensure accessibility and version control friendliness
- **Hierarchical Navigation** with clear progression from concepts to applications

### Educational Approach
- **Conceptual-First Methodology** focusing on mental models before implementation details
- **Analogy-Based Learning** using the "robotic nervous system" metaphor
- **Humanoid-Centric Examples** to maintain relevance to the course theme

### Technical Implementation
- **Static Site Generation** using Docusaurus for performance and reliability
- **GitHub Pages Deployment** for cost-effective hosting and version control integration
- **Progressive Disclosure** of complexity to accommodate different learning paces

## Alternatives Considered
- Interactive platforms: Jupyter Notebooks vs static documentation (selected static for broader accessibility)
- Different frameworks: Hugo vs Gatsby vs Docusaurus (selected Docusaurus for ecosystem and extensibility)
- Content formats: RestructuredText vs Markdown (selected Markdown for accessibility)
- Delivery methods: Interactive vs static content (selected hybrid with static primary content)

## Consequences
### Positive
- Accessible to wide range of learners with varying technical backgrounds
- Maintained through standard version control practices
- Cost-effective deployment and hosting
- Easy to extend and modify content
- Good search engine optimization for discoverability

### Negative
- Less interactivity compared to specialized learning platforms
- Requires more upfront setup for contributors
- Static content may become outdated without maintenance
- Limited real-time collaboration features