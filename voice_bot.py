import os
import json
import asyncio
import google.generativeai as genai
import requests
import time
import random
from PIL import Image, ImageDraw, ImageFont
from faster_whisper import WhisperModel
from pydub import AudioSegment
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)

# === API KEYS ===
TELEGRAM_TOKEN = "7589879110:AAHDN0up1vgsv0znn6qRNlTnsX4b5waWXWs"
GEMINI_API_KEY = "AIzaSyDyCUnQumkU9-_mGegPo-bGgp6AeMO2gic"
ELEVENLABS_API_KEY = "sk_15e53afe3c0d6b3ffb6bcb0a7e5278e7db5358737b4fea72"

# === Configure Gemini ===
genai.configure(api_key=GEMINI_API_KEY)
text_model = genai.GenerativeModel("models/gemini-1.5-flash")
vision_model = genai.GenerativeModel("models/gemini-1.5-flash")

# === Persistent Memory ===
MEMORY_DIR = "memory"
os.makedirs(MEMORY_DIR, exist_ok=True)

user_lang_prefs = {}  # chat_id -> "en" or "hinglish"
user_moods = {}       # chat_id -> mood (e.g., "flirty", "moody", "professional")
user_ids = set()
user_message_counts = {}  # chat_id -> {question: count}
admin_password = "ChoclateCupcake"
admin_authenticated = set()

# === Help Command Handler ===
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = "\n".join([
        "Hey! I'm Lucia, your sassy AI!",
        "Commands:",
        "/switchlang - Toggle English/Hinglish",
        "/setmood <mood> - Set mood (friendly, flirty, moody, professional)",
        "/reset - Clear your chat history",
        "Tips:",
        "- Send text, voice, or photos.",
        "- Say 'voice reply' for audio responses."
    ])
    await update.message.reply_text(message)

# === Admin Command Handler ===
async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_ids.add(chat_id)
    args = context.args

    if chat_id in admin_authenticated:
        message = "\n".join([
            "Admin Vibes",
            f"Users: {len(user_ids)}",
            f"Lang: {user_lang_prefs.get(chat_id, 'en')}",
            f"Mood: {user_moods.get(chat_id, 'friendly')}",
            f"Memory: {'Saved' if os.path.exists(os.path.join(MEMORY_DIR, f'chat_{chat_id}.json')) else 'None'}",
            "Commands:",
            "/reset - Wipe memory",
            "/switchlang - Flip lang",
            "/setmood <mood> - Pick mood",
            "/clearall - Nuke all memory"
        ])
        await update.message.reply_text(message)
    elif args and args[0] == admin_password:
        admin_authenticated.add(chat_id)
        await update.message.reply_text("You're in!")
    else:
        await update.message.reply_text("Nope. /admin <password>")

# === Mood Selector ===
async def set_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if context.args:
        mood = context.args[0].lower()
        user_moods[chat_id] = mood
        await update.message.reply_text(f"{mood.title()} mood on!")
    else:
        await update.message.reply_text("Gimme a mood! /setmood flirty")

# === Clear All Memory (Admin Only) ===
async def clear_all_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in admin_authenticated:
        for filename in os.listdir(MEMORY_DIR):
            os.remove(os.path.join(MEMORY_DIR, filename))
        user_message_counts.clear()
        await update.message.reply_text("All gone!")
    else:
        await update.message.reply_text("Not you, boo.")

# === Toggle Language ===
async def switch_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    current = user_lang_prefs.get(chat_id, "en")
    new_lang = "hinglish" if current == "en" else "en"
    user_lang_prefs[chat_id] = new_lang
    await update.message.reply_text(f"{new_lang.title()} it is!")

# === Load & Save Memory ===
def load_user_history(chat_id):
    path = os.path.join(MEMORY_DIR, f"chat_{chat_id}.json")
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[WARN] Corrupted memory for chat {chat_id}, resetting.")
            return []
    return []

def save_user_history(chat_id, history):
    path = os.path.join(MEMORY_DIR, f"chat_{chat_id}.json")
    with open(path, "w") as f:
        json.dump(history[-50:], f)

# === Gemini Response ===
def get_gemini_response(prompt, chat_id):
    lang_pref = user_lang_prefs.get(chat_id, "en")
    mood = user_moods.get(chat_id, "friendly")

    # Track repeated questions
    if chat_id not in user_message_counts:
        user_message_counts[chat_id] = {}
    if prompt in user_message_counts[chat_id]:
        user_message_counts[chat_id][prompt] += 1
        if user_message_counts[chat_id][prompt] >= 10:
            user_message_counts[chat_id][prompt] = 0  # Reset count
            return "Bhai bkchodi krni h to kahi aur kr na"
        elif user_message_counts[chat_id][prompt] >= 2:
            user_message_counts[chat_id][prompt] = 3  # Skip to 3 to continue counting
            return "Bhai tu thoda bkl hai kya?"
    else:
        user_message_counts[chat_id][prompt] = 1

    mood_tones = {
        "friendly": "Be cute, chill, no emojis unless needed.",
        "flirty": "Playful, charming, use winky emoji sparingly.",
        "moody": "Sassy, dramatic, minimal emojis.",
        "professional": "Smart, crisp, no emojis.",
    }
    tone = mood_tones.get(mood, mood_tones["friendly"])
    lang_instruction = "Mix Hindi & English (Hinglish)." if lang_pref == "hinglish" else "Keep it English."
    history = load_user_history(chat_id)
    history_prompt = "\n".join([f"User: {history[i]}\nBot: {history[i+1]}" for i in range(0, len(history), 2)][:5])
    full_prompt = f"{tone}\n{lang_instruction}\nKeep it SHORT, max 50 words, no emojis unless specified.\n{history_prompt}\nUser says: {prompt}"

    max_retries = 3
    for attempt in range(max_retries):
        try:
            convo = text_model.start_chat(history=[
                {"role": "user", "parts": [msg]} if i % 2 == 0 else {"role": "model", "parts": [msg]}
                for i, msg in enumerate(history)
            ])
            response = convo.send_message(full_prompt)
            reply = response.text.strip()[:200]
            new_history = history + [prompt, reply]
            save_user_history(chat_id, new_history)
            return reply
        except Exception as e:
            if "429" in str(e):
                delay = (1 * 2 ** attempt) + random.uniform(0, 0.1)
                time.sleep(delay)
                continue
            return "Mess-up, sorry!"
    return "Too many tries, oops!"

# === Vision ===
def get_vision_response(image_path, prompt="Describe this image"):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            file = genai.upload_file(image_path)
            response = vision_model.generate_content(
                contents=[{"parts": [f"Keep it SHORT, max 50 words, no emojis.\n{prompt}", {"file_data": {"file_uri": file.uri}}]}]
            )
            return response.text.strip()[:200]
        except Exception as e:
            if "429" in str(e):
                delay = (1 * 2 ** attempt) + random.uniform(0, 0.1)
                time.sleep(delay)
                continue
            return "Can't see it, sorry!"
    return "Too many tries, oops!"

# === Image Generator ===
def generate_placeholder_image(text):
    image = Image.new("RGB", (512, 512), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((20, 250), text[:50], fill=(0, 0, 0), font=font)
    image_path = "generated_image.png"
    image.save(image_path)
    return image_path

# === ElevenLabs TTS ===
def text_to_speech(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text[:200],
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            with open("reply.mp3", "wb") as f:
                f.write(response.content)
            audio = AudioSegment.from_mp3("reply.mp3")
            audio.export("reply.ogg", format="ogg")
            return "reply.ogg"
    except Exception as e:
        print("[TTS ERROR]", e)
    return None

# === Voice Handler ===
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_ids.add(chat_id)
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    voice = await update.message.voice.get_file()
    file_path = await voice.download_to_drive("voice.ogg")

    try:
        audio = AudioSegment.from_file(file_path, format="ogg")
        audio.export("voice.wav", format="wav")
        model = WhisperModel("base", compute_type="int8", cpu_threads=2)
        segments, _ = model.transcribe("voice.wav")
        user_input = " ".join([s.text for s in segments])[:100]
    except Exception as e:
        await update.message.reply_text("Voice? Nope!")
        return

    if any(w in user_input.lower() for w in ["talk in hinglish", "bol hinglish"]):
        user_lang_prefs[chat_id] = "hinglish"
        await update.message.reply_text("Hinglish on!")
    elif any(w in user_input.lower() for w in ["talk in english", "back to english"]):
        user_lang_prefs[chat_id] = "en"
        await update.message.reply_text("English, cool!")

    force_voice = any(word in user_input.lower() for word in ["voice reply", "send a voice note", "reply in voice", "say it", "audio"])
    await process_message(user_input, update, context, force_voice=force_voice)

# === Text Handler ===
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_ids.add(chat_id)
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    user_input = update.message.text[:100]

    if user_input.strip().lower() == "/reset":
        save_user_history(chat_id, [])
        user_message_counts[chat_id] = {}
        await update.message.reply_text("Memory wiped!")
        return

    force_voice = any(word in user_input.lower() for word in ["voice reply", "send a voice note", "reply in voice", "say it", "audio"])
    await process_message(user_input, update, context, force_voice=force_voice)

# === Photo Handler ===
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_PHOTO)
    photo = await update.message.photo[-1].get_file()
    photo_path = await photo.download_to_drive("user_photo.jpg")
    caption = (update.message.caption or "Describe this image")[:50]
    reply = get_vision_response("user_photo.jpg", caption)
    await update.message.reply_text(reply)

# === Shared Processor ===
async def process_message(user_input, update, context, force_voice=False):
    chat_id = update.effective_chat.id
    print(f"[USER] {user_input}")
    reply = get_gemini_response(user_input, chat_id)
    print(f"[LUCIA] {reply}")

    if reply.lower().startswith("generate image:"):
        prompt = reply.split(":", 1)[1].strip()[:50]
        image_path = generate_placeholder_image(prompt)
        with open(image_path, "rb") as img_file:
            await context.bot.send_photo(chat_id=chat_id, photo=img_file)
        return

    if force_voice:
        reply_audio = text_to_speech(reply)
        if reply_audio:
            with open(reply_audio, "rb") as f:
                await context.bot.send_voice(chat_id=chat_id, voice=f)
        else:
            await update.message.reply_text("Voice fail!")
    else:
        await update.message.reply_text(reply)

# === Main ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("admin", admin_handler))
    app.add_handler(CommandHandler("clearall", clear_all_handler))
    app.add_handler(CommandHandler("switchlang", switch_language))
    app.add_handler(CommandHandler("setmood", set_mood))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("Lucia is slaying...")
    app.run_polling()