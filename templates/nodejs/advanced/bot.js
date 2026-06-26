const { Bot } = require("grammy");
require('dotenv').config();

// Create a bot object
const bot = new Bot(process.env.TELEGRAM_TOKEN);

// Register a command handler
bot.command("start", (ctx) => ctx.reply("Welcome! This is an advanced bot using grammY."));

// Handle other messages
bot.on("message", (ctx) => {
  const from = ctx.from;
  console.log(`Message from ${from.first_name} (ID: ${from.id})`);
  ctx.reply("I received your message!");
});

// Start the bot
bot.start().then(() => {
  console.log('Advanced Node.js bot (grammY) is running...');
});
