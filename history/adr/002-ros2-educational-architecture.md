# ADR 002: ROS 2 Architecture and Educational Approach for Physical AI

## Status
Accepted

## Context
We need to establish the architectural approach for teaching ROS 2 concepts within the Physical AI curriculum. The module must balance conceptual understanding with practical application while remaining accessible to software engineers transitioning into robotics.

## Decision

### Educational Approach
- **Conceptual-First Learning**: Focus on mental models and system understanding before diving into implementation details
- **Analogical Reasoning**: Use the "robotic nervous system" analogy to explain ROS 2 architecture
- **Human-Centered Examples**: Use humanoid robotics examples throughout to maintain relevance to the course theme

### Technical Stack
- **ROS 2 (Humble Hawksbill)** as the middleware framework
- **rclpy** as the Python client library for examples and exercises
- **URDF** for robot description and structure
- **Docusaurus** for content delivery platform

### Content Structure
- **Three-Chapter Progression**:
  1. Introduction and conceptual foundations
  2. Communication primitives deep-dive
  3. Robot structure and representation
- **Minimal Code Emphasis**: Focus on understanding over implementation
- **Real-World Applications**: Connect concepts to actual humanoid robot control scenarios

## Alternatives Considered
- Educational frameworks: ROS 1 vs ROS 2 (selected ROS 2 for modern features and industry adoption)
- Programming languages: C++ vs Python examples (selected Python for accessibility to software engineers)
- Teaching approaches: Code-first vs concept-first (selected concept-first for better understanding)
- Robot platforms: Various simulators and real robots (focused on generalizable concepts)

## Consequences
### Positive
- Accessible to software engineers without robotics background
- Conceptual foundation supports future learning
- Industry-relevant technology (ROS 2 is the standard)
- Humanoid focus maintains engagement and relevance

### Negative
- May not provide sufficient hands-on practice for some learners
- Requires understanding of abstract concepts before practical application
- Dependent on ROS 2 ecosystem and its learning curve