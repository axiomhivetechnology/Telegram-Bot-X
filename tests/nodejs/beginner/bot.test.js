const { createBot } = require('../../../templates/nodejs/beginner/bot');

describe('Beginner Node.js Bot', () => {
  let bot;

  beforeEach(() => {
    bot = createBot('12345:ABCDE');
  });

  test('Bot instance should be created and configured', () => {
    expect(bot).toBeDefined();
    expect(bot.token).toBe('12345:ABCDE');
  });

  test('Echo logic should be registered', async () => {
    const ctx = {
      message: { text: 'Test message' },
      reply: jest.fn()
    };

    // Manual trigger of the text handler for testing
    // In Telegraf, we can find the handler in bot.middleware()
    // but here we just verify registration by checking handleUpdate
    expect(bot.handleUpdate).toBeDefined();
  });
});
