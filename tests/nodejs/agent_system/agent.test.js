const { initializeAgent } = require('../../../templates/nodejs/agent_system/agent');
const { AgentExecutor } = require("langchain/agents");

describe('Node.js Agent System', () => {
  test('initializeAgent should return an AgentExecutor', async () => {
    // Mocking environment for CI
    process.env.OPENAI_API_KEY = 'dummy_key';

    const executor = await initializeAgent();
    expect(executor).toBeInstanceOf(AgentExecutor);
  });
});
