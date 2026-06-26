const { Telegraf, Scenes, session } = require('telegraf');
require('dotenv').config();

const bot = new Telegraf(process.env.TELEGRAM_TOKEN);

// Step 1: Define the Scene
const contactScene = new Scenes.WizardScene(
  'CONTACT_SCENE',
  (ctx) => {
    ctx.reply('What is your name?');
    return ctx.wizard.next();
  },
  (ctx) => {
    ctx.wizard.state.name = ctx.message.text;
    ctx.reply('Nice to meet you! What is your age?');
    return ctx.wizard.next();
  },
  (ctx) => {
    const age = parseInt(ctx.message.text);
    if (isNaN(age)) {
      return ctx.reply('Please enter a valid number for age:');
    }
    ctx.wizard.state.age = age;
    ctx.reply(`Thanks ${ctx.wizard.state.name}! I recorded your age as ${age}.`);
    return ctx.scene.leave();
  }
);

// Step 2: Register Stage
const stage = new Scenes.Stage([contactScene]);
bot.use(session());
bot.use(stage.middleware());

// Step 3: Commands
bot.start((ctx) => ctx.reply('Send /register to start the wizard.'));
bot.command('register', (ctx) => ctx.scene.enter('CONTACT_SCENE'));

bot.launch().then(() => {
  console.log('Intermediate Node.js bot is running...');
});

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
