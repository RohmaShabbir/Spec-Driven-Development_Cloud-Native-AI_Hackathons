# Common Terminology and Concepts for ROS 2 Module

This document defines the standard terminology used throughout the ROS 2 module to ensure consistency across all chapters.

## Core ROS 2 Concepts

### Node
- **Definition**: An independent process that performs computation in ROS 2
- **Alternative terms**: Process, component, module
- **Usage**: Always refer to as "node" in lowercase

### Topic
- **Definition**: A named bus over which nodes exchange messages using publish-subscribe pattern
- **Alternative terms**: Channel, bus, message stream
- **Usage**: Always refer to as "topic" in lowercase

### Service
- **Definition**: A communication pattern that provides request-response functionality
- **Alternative terms**: RPC (Remote Procedure Call)
- **Usage**: Always refer to as "service" in lowercase

### Action
- **Definition**: A communication pattern that provides goal-feedback-result functionality for long-running tasks
- **Alternative terms**: Long-running service, task
- **Usage**: Always refer to as "action" in lowercase

### Publisher
- **Definition**: A component within a node that sends messages to a topic
- **Alternative terms**: Sender, broadcaster
- **Usage**: Use "publisher" when referring to ROS 2 concept

### Subscriber
- **Definition**: A component within a node that receives messages from a topic
- **Alternative terms**: Receiver, listener
- **Usage**: Use "subscriber" when referring to ROS 2 concept

## Humanoid Robotics Terms

### URDF
- **Definition**: Unified Robot Description Format - an XML format for representing robot models
- **Full form**: Always spell out as "URDF (Unified Robot Description Format)" on first use in each chapter

### Link
- **Definition**: A rigid body element in a URDF robot model
- **Alternative terms**: Segment, body part
- **Usage**: Use "link" when referring to URDF concept

### Joint
- **Definition**: A connection between two links in a URDF robot model that defines how they can move relative to each other
- **Alternative terms**: Connection, articulation
- **Usage**: Use "joint" when referring to URDF concept

### Frame
- **Definition**: A coordinate system attached to a link in the robot model
- **Alternative terms**: Coordinate frame, reference frame
- **Usage**: Use "frame" or "coordinate frame"

## Communication Patterns

### Publish-Subscribe
- **Definition**: Communication pattern where publishers send messages to topics and subscribers receive them
- **Alternative terms**: Pub/Sub, asynchronous messaging
- **Usage**: Use "publish-subscribe" on first mention, "pub/sub" thereafter

### Request-Response
- **Definition**: Communication pattern where clients send requests to services and receive responses
- **Alternative terms**: Request-reply, synchronous messaging
- **Usage**: Use "request-response"

### Goal-Feedback-Result
- **Definition**: Communication pattern for long-running tasks with progress updates
- **Alternative terms**: Action pattern
- **Usage**: Use "goal-feedback-result" initially, then "action" pattern

## Analogies and Metaphors

### Nervous System Analogy
- **Nodes** ≈ Neurons
- **Topics** ≈ Neural pathways/Synapses
- **Services** ≈ Reflexes/Specific brain functions
- **Actions** ≈ Complex coordinated behaviors

Maintain consistency in these analogies throughout all chapters.