const { OpenAI } = require("openai");
const { DynamicTool } = require("@langchain/core/tools");
const { ChatOpenAI } = require("@langchain/openai");
const { createOpenAIFunctionsAgent, AgentExecutor } = require("langchain/agents");
const { ChatPromptTemplate, MessagesPlaceholder } = require("@langchain/core/prompts");
require('dotenv').config();

// --- Tool Definitions ---

const systemLoadTool = new DynamicTool({
  name: "get_system_load",
  description: "Returns the current simulated system load.",
  func: async () => "System load is 25% CPU, 40% RAM. All services operational.",
});

const databaseQueryTool = new DynamicTool({
  name: "query_database",
  description: "Queries the internal user database for information.",
  func: async (query) => `Database result for '${query}': Record not found.`,
});

const tools = [systemLoadTool, databaseQueryTool];

// --- Agent Initialization ---

async function initializeAgent() {
  const llm = new ChatOpenAI({
    modelName: "gpt-4",
    temperature: 0,
  });

  const prompt = ChatPromptTemplate.fromMessages([
    ["system", "You are a highly efficient system administrator assistant."],
    ["human", "{input}"],
    new MessagesPlaceholder("agent_scratchpad"),
  ]);

  const agent = await createOpenAIFunctionsAgent({
    llm,
    tools,
    prompt,
  });

  const agentExecutor = new AgentExecutor({
    agent,
    tools,
  });

  return agentExecutor;
}

// --- Execution Example ---

if (require.main === module) {
  (async () => {
    const executor = await initializeAgent();
    const result = await executor.invoke({
      input: "Check the system load and query the database for 'Project X'.",
    });
    console.log("Agent Final Output:", result.output);
  })();
}

module.exports = { initializeAgent };
