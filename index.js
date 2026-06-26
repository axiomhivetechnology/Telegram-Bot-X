require('dotenv').config();
const { Telegraf } = require('telegraf');
const OpenAI = require('openai');

const bot = new Telegraf(process.env.BOT_TOKEN);
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

bot.start((ctx) => {
    ctx.reply('Welcome! I am your AI Assistant Bot. How can I help you today?');
});

bot.help((ctx) => {
    ctx.reply('I can help you with various tasks using AI. Just send me a message!');
});

bot.on('text', async (ctx) => {
    try {
        const response = await openai.chat.completions.create({
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: ctx.message.text }],
        });

        ctx.reply(response.choices[0].message.content);
    } catch (error) {
        console.error('Error with OpenAI:', error);
        ctx.reply('Sorry, I encountered an error while processing your request.');
    }
});

bot.launch();

// Enable graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));

console.log('Bot is running...');
