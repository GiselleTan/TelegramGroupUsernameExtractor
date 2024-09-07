import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = 'BOT_TOKEN'  # Replace with your actual bot token

async def get_groupID(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat = update.effective_chat
    await update.message.reply_text(f"Chat ID: {chat.id}")
    #print(f"Chat ID: {chat.id}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    groupid_handler = CommandHandler('getgroupid', get_groupID)
    application.add_handler(groupid_handler)

    application.run_polling()
