---
title: Chapter 2 - ROS 2 Communication Primitives
sidebar_position: 3
description: Deep dive into ROS 2 Nodes, Topics, Services, and Actions with real-world humanoid examples
---

# Chapter 2: ROS 2 Communication Primitives

## Introduction

In this chapter, we'll take a deep dive into the core communication primitives of ROS 2: Nodes, Topics, Services, and Actions. We'll explore how these primitives work together to enable communication in robotic systems, with a focus on real-world examples of humanoid control applications.

## Understanding Nodes in Depth

### What Are Nodes?

Nodes are the fundamental building blocks of ROS 2 applications. Each node is an independent process that performs specific computations. Think of nodes as individual organisms in a biological system, each with its own purpose but working together for the greater good of the robot.

### Characteristics of Nodes

#### Independence
Each node operates independently, which provides:
- Fault isolation: A failure in one node doesn't necessarily bring down the entire system
- Scalability: Nodes can be distributed across multiple machines
- Language flexibility: Nodes can be written in different programming languages

#### Lifecycle Management
Nodes have a well-defined lifecycle that includes:
- Initialization: Setting up parameters and connections
- Activation: Beginning normal operations
- Deactivation: Temporarily pausing operations
- Cleanup: Preparing for shutdown

### Node Architecture

A typical ROS 2 node includes:

#### Publishers and Subscribers
- Publishers send messages to topics
- Subscribers receive messages from topics
- Both are created within the node's context

#### Service Clients and Servers
- Service servers provide specific functionality
- Service clients request specific functionality
- Both are managed within the node

#### Action Clients and Servers
- Action servers handle long-running tasks
- Action clients monitor and control these tasks
- Both incorporate feedback and goal management

## Topics: Publish-Subscribe Communication

### The Publish-Subscribe Pattern

Topics implement the publish-subscribe communication pattern, which is ideal for streaming data. This pattern is characterized by:

- **Publishers**: Nodes that send messages to topics
- **Subscribers**: Nodes that receive messages from topics
- **Anonymous Communication**: Publishers don't know who subscribes, and vice versa
- **Broadcast Nature**: All subscribers receive the same message

### Message Passing Details

#### Data Flow
Messages flow from publishers to subscribers through the ROS 2 middleware. The middleware handles:
- Message serialization and deserialization
- Network transmission between nodes
- Quality of Service (QoS) settings enforcement
- Connection establishment and maintenance

#### Quality of Service (QoS)
QoS settings allow fine-tuning of communication behavior:
- **Reliability**: Reliable vs. best-effort delivery
- **Durability**: Volatile vs. transient-local for late-joining subscribers
- **History**: Keep-all vs. keep-last for message queues
- **Deadline**: Maximum time between consecutive messages
- **Liveliness**: How to detect if a participant is alive

### Real-World Humanoid Examples

#### Sensor Data Streaming
In a humanoid robot, various sensors continuously publish data:

```python
# Example: IMU sensor node publishing orientation data
# Publisher: /imu/orientation
# Message type: sensor_msgs/msg/Imu
# Content: Orientation, angular velocity, linear acceleration
```

Multiple nodes might subscribe to this data:
- Balance controller
- State estimator
- Visualization tools
- Logging systems

#### Robot State Broadcasting
The robot state publisher continuously broadcasts the current state:

```python
# Example: Robot state publisher
# Publisher: /joint_states
# Message type: sensor_msgs/msg/JointState
# Content: Joint positions, velocities, efforts
```

Consuming nodes include:
- Controller nodes
- Visualization tools
- Diagnostic systems
- Planning algorithms

## Services: Request-Response Communication

### The Request-Response Pattern

Services implement synchronous request-response communication, ideal for operations that have a clear beginning and end. This pattern includes:

- **Service Server**: Provides specific functionality
- **Service Client**: Requests specific functionality
- **Synchronous**: Client waits for response before continuing
- **One-to-One**: Typically one server serves one client at a time

### Service Architecture

#### Request-Response Cycle
1. Client sends a request to the service
2. Server processes the request
3. Server sends a response back to the client
4. Client receives the response and continues

#### Service Types
ROS 2 comes with predefined service types:
- `std_srvs`: Standard services (empty, trigger, set_bool, etc.)
- `geometry_msgs`: Geometric transformation services
- Custom services defined by the user

### Real-World Humanoid Examples

#### Parameter Configuration
Changing robot parameters dynamically:

```python
# Example: Service to change walking gait parameters
# Service: /humanoid/set_walking_params
# Request: Walking speed, step height, step length
# Response: Success/failure status
```

#### Specific Computations
Requesting specific computational tasks:

```python
# Example: Service to compute inverse kinematics
# Service: /humanoid/compute_ik
# Request: Target pose for end effector
# Response: Joint angles to achieve the pose
```

## Actions: Goal-Feedback-Result Communication

### The Action Pattern

Actions combine the best of both worlds - the streaming nature of topics and the request-response nature of services. They're perfect for long-running tasks that:

- Take time to complete
- Provide periodic feedback
- Can be preempted or canceled
- Have a definitive result

### Action Architecture

An action includes three parts:
- **Goal**: The request to initiate the action
- **Feedback**: Periodic updates on progress
- **Result**: The final outcome when the action completes

### Action Lifecycle

1. **Goal Request**: Client sends a goal to the action server
2. **Goal Acceptance**: Server accepts or rejects the goal
3. **Execution**: Server executes the action while sending feedback
4. **Preemption**: Client can cancel or replace the goal
5. **Completion**: Server sends the final result

### Real-World Humanoid Examples

#### Navigation Actions
Moving the robot to a specific location:

```python
# Example: Navigate to goal action
# Action: /humanoid/navigate_to_goal
# Goal: Target position and orientation
# Feedback: Current progress, distance remaining
# Result: Success/failure, actual arrival position
```

#### Manipulation Actions
Performing complex manipulation tasks:

```python
# Example: Pick and place action
# Action: /humanoid/pick_and_place
# Goal: Object to pick, destination to place
# Feedback: Current stage (approaching, grasping, lifting, placing)
# Result: Success/failure, final object position
```

## Introduction to rclpy and Python-Based Agent Interaction

### What is rclpy?

rclpy is the Python client library for ROS 2. It provides a Python API that allows developers to create ROS 2 nodes, publish and subscribe to topics, provide and use services, and implement and use actions.

### Key Features of rclpy

#### Node Creation
rclpy simplifies node creation with intuitive Python classes:

```python
import rclpy
from rclpy.node import Node

class HumanoidController(Node):
    def __init__(self):
        super().__init__('humanoid_controller')
        # Node initialization code here
```

#### Topic Communication
Easy-to-use publishers and subscribers:

```python
# Creating a publisher
publisher = self.create_publisher(String, 'topic_name', 10)

# Creating a subscriber
subscriber = self.create_subscription(
    String, 'topic_name', callback_function, 10)
```

#### Service Communication
Straightforward service clients and servers:

```python
# Creating a service server
service = self.create_service(SetBool, 'service_name', callback_function)

# Creating a service client
client = self.create_client(SetBool, 'service_name')
```

### Python Agent Integration

#### Benefits of Python for Robotics
- Rich ecosystem of scientific and machine learning libraries
- Rapid prototyping capabilities
- Readable and maintainable code
- Strong community support

#### AI Agent Integration
Python makes it easy to integrate AI agents with ROS 2:

```python
# Example: AI decision-making node
class AIDecisionMaker(Node):
    def __init__(self):
        super().__init__('ai_decision_maker')

        # Subscribe to sensor data
        self.sensor_sub = self.create_subscription(
            SensorData, 'sensors/data', self.process_sensor_data, 10)

        # Publish decisions
        self.decision_pub = self.create_publisher(
            RobotAction, 'robot/action', 10)

    def process_sensor_data(self, msg):
        # Apply AI algorithms to sensor data
        decision = self.ai_model.predict(msg.data)

        # Publish the decision
        action_msg = RobotAction()
        action_msg.action = decision
        self.decision_pub.publish(action_msg)
```

## Minimal Illustrative Code Snippets

### Simple Publisher Node

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Simple Subscriber Node

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## Summary

In this chapter, we've explored the core communication primitives of ROS 2 in depth:

- **Nodes**: The fundamental computational units that perform specific functions
- **Topics**: Enable publish-subscribe communication for streaming data
- **Services**: Provide request-response communication for specific operations
- **Actions**: Combine streaming and request-response for long-running tasks
- **rclpy**: The Python client library that enables easy integration of Python-based agents

We've seen how these primitives work together in real-world humanoid robotics applications, from sensor data streaming to complex manipulation tasks. Understanding these communication patterns is crucial for designing effective robotic systems.

In the next chapter, we'll explore how robots are represented in ROS 2 using URDF and how this connects to visualization, simulation, and control.