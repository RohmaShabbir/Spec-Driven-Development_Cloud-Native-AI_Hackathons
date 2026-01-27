# Module 1 - The Robotic Nervous System (ROS 2) - Quickstart Guide

## Overview

This quickstart guide provides the essential steps to set up and begin working with the ROS 2 module. It covers the development environment setup and the basic workflow for contributing to the documentation.

## Prerequisites

- Node.js (v18 or higher)
- npm or yarn package manager
- Git version control
- Basic familiarity with Markdown syntax
- Python 3.8+ (for understanding rclpy examples)

## Environment Setup

### 1. Install Node.js and Package Manager

```bash
# Install Node.js from nodejs.org or using a version manager like nvm
# Verify installation
node --version
npm --version
```

### 2. Clone the Repository

```bash
git clone [repository-url]
cd [repository-name]
```

### 3. Install Docusaurus Dependencies

```bash
npm install
```

## Docusaurus Setup

### 1. Initialize Docusaurus (if not already done)

```bash
# Install Docusaurus CLI globally
npm install -g @docusaurus/cli

# Initialize a new Docusaurus project (if starting fresh)
npx @docusaurus/init@latest init docs classic

# Or if project already exists, just install dependencies
npm install @docusaurus/core @docusaurus/preset-classic
```

### 2. Configuration Files

Key files to understand:
- `docusaurus.config.js` - Main site configuration
- `sidebars.js` - Navigation structure
- `package.json` - Dependencies and scripts

### 3. Running the Development Server

```bash
npm start
```

This will start the development server at http://localhost:3000

## Module Structure

### Directory Layout

```
docs/
├── module-1-ros2/                 # Module 1 content
│   ├── index.md                  # Module introduction
│   ├── chapter-1-ros2-overview.md
│   ├── chapter-2-nodes-topics-services.md
│   └── chapter-3-urdf-humanoids.md
├── _category_.json               # Category configuration
└── sidebar.js                    # Navigation sidebar

static/                           # Static assets (images, diagrams)
src/                              # Custom React components (if needed)
```

## Writing Content

### 1. Markdown Best Practices

- Use Docusaurus-adhering Markdown syntax
- Include proper headings hierarchy (h1, h2, h3, etc.)
- Use code blocks with appropriate language identifiers
- Add alt text to images for accessibility

### 2. Creating a New Chapter

```bash
# Create a new markdown file in the module directory
touch docs/module-1-ros2/new-chapter.md
```

Then add the content with proper frontmatter:

```markdown
---
title: Chapter Title
sidebar_position: X
description: Brief description of the chapter content
---

# Chapter Title

Your content here...
```

### 3. Adding to Sidebar

In `sidebars.js`, add your new chapter:

```javascript
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System',
      items: [
        'module-1-ros2/index',
        'module-1-ros2/chapter-1-ros2-overview',
        'module-1-ros2/chapter-2-nodes-topics-services',
        'module-1-ros2/chapter-3-urdf-humanoids',
        // Add new chapter here
      ],
    },
  ],
};
```

## Building and Previewing

### 1. Local Build

```bash
npm run build
```

This creates a static build in the `build/` directory.

### 2. Preview Build Locally

```bash
npm run serve
```

Serves the built site at http://localhost:3000

## Content Guidelines

### Writing Style

- Maintain grade 10-12 reading level
- Use clear, concise sentences
- Focus on conceptual understanding over implementation details
- Use consistent terminology across chapters

### Technical Accuracy

- Verify all ROS 2 concepts against official documentation
- Use current ROS 2 Humble APIs
- Ensure code examples are functional
- Include relevant diagrams where helpful

## Common Commands

```bash
# Start development server
npm start

# Build static site
npm run build

# Serve built site locally
npm run serve

# Deploy to GitHub Pages (if configured)
npm run deploy
```

## Troubleshooting

### Common Issues

1. **Dependency errors**: Run `npm install` to refresh dependencies
2. **Port conflicts**: Use `npm start --port 3001` to use a different port
3. **Build errors**: Check for syntax errors in Markdown files
4. **Sidebar not updating**: Restart the development server after sidebar changes

### Getting Help

- Check the official Docusaurus documentation
- Review the ROS 2 official tutorials
- Consult the project's issue tracker for known problems