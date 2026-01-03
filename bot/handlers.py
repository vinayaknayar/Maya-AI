from telegram import Update
from telegram.ext import ContextTypes
from mcp_client import send_message_to_mcp


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm Maya.\n\n"
        "You can talk to me freely.\n"
        "Type /help to see commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show help\n"
        "Just type any message to chat."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = update.effective_user.id

    await update.message.chat.send_action("typing")

    try:
        mcp_response = await send_message_to_mcp(user_id, user_message)
        reply = mcp_response.get("reply", "⚠️ No response from agent")
    except Exception as e:
        reply = "❌ Error contacting MCP server"

    await update.message.reply_text(reply)
