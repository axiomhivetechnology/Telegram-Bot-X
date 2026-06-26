# AI Agent System Architectural Design

This document provides a formal technical analysis of the Agentic AI system implemented within this repository. The system is designed to extend standard Telegram bot interfaces with autonomous reasoning and external tool-calling capabilities.

## 1. System Overview
The Agent System transitions the bot architecture from a deterministic command-response model to a non-deterministic reasoning model. It utilizes Large Language Models (LLMs) to dynamically determine the sequence of actions required to satisfy complex system objectives.

## 2. Core Architectural Components

### A. Orchestration Layer
- **Stateful Graphs (Python)**: Utilizes directed acyclic graphs (DAGs) to define the flow between the agent (LLM) and action (tool execution) nodes. This ensures controlled state transitions and cycle management.
- **Executor Loops (Node.js)**: Implements an iterative loop that persists until the agent determines that a final objective has been reached.

### B. Tool-Calling Protocol
The system implements a standardized protocol for interfacing the LLM with external systems:
- **Schema Definition**: Every tool is defined with a rigorous input schema (JSON) that the LLM uses to generate function arguments.
- **Atomic Execution**: Tools are designed as atomic, idempotent functions that perform specific system operations (e.g., database retrieval, API calls).
- **Feedback Loop**: Results from tool executions are formatted as system messages and returned to the LLM context to inform subsequent reasoning steps.

## 3. Implementation Patterns

### Deterministic vs. Agentic Routing
1.  **Deterministic**: `/stats` -> Query Database -> Return Result.
2.  **Agentic**: "Analyze system performance and compare with last week" -> Agent calls `get_system_load` -> Agent calls `query_history` -> Agent synthesizes response.

## 4. Integration Specifications
The agent system is decoupled from the Telegram transport layer. It operates as a service module:
- **Input**: Natural language strings or structured updates.
- **Process**: LLM-driven reasoning cycle + tool execution.
- **Output**: Synthesized natural language response or a sequence of system actions.

## 5. Security and Safety Constraints
- **Sandboxed Execution**: Tools should operate within restricted environments with limited access to the host system.
- **Human-in-the-loop (HITL)**: For high-impact tools (e.g., data deletion), the architecture supports an intermediate state requiring manual approval before execution.
- **Token Management**: Strict rate limiting and context window management to ensure cost efficiency and system stability.
