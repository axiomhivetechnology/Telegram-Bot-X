const { Telegraf } = require('telegraf');
require('dotenv').config();

function createBot(token) {
  const bot = new Telegraf(token || process.env.TELEGRAM_TOKEN);

  bot.start((ctx) => ctx.reply('Welcome! I am a Node.js bot.'));
  bot.help((ctx) => ctx.reply('Send me a message and I will echo it back.'));

  bot.on('text', (ctx) => {
    ctx.reply(`You said: ${ctx.message.text}`);
  });

  return bot;
}

if (require.main === module) {
  const bot = createBot();
  bot.launch().then(() => {
    console.log('Beginner Node.js bot is running...');
  });

  // Enable graceful stop
  process.once('SIGINT', () => bot.stop('SIGINT'));
  process.once('SIGTERM', () => bot.stop('SIGTERM'));
}

module.exports = { createBot };
