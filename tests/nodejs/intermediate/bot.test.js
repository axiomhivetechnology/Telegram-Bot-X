const { createBot } = require('../../../templates/nodejs/intermediate/bot');

describe('Intermediate Node.js Bot', () => {
  let bot;

  beforeEach(() => {
    bot = createBot('12345:ABCDE');
  });

  test('Bot instance should be created and configured', () => {
    expect(bot).toBeDefined();
    expect(bot.token).toBe('12345:ABCDE');
  });

  test('Bot should have registered middleware', () => {
    expect(bot.handleUpdate).toBeDefined();
  });
});
