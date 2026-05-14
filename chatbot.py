import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime
import math
import time

# =========================
# MEMORY
# =========================

memory = {
    "name": "",
    "mood": ""
}

# =========================
# BOT REPLY FUNCTION
# =========================

def bot_reply(user_input):

    user = user_input.lower().strip()

    # Greetings
    greetings = ["hello", "hi", "hey", "hola"]

    if any(word in user for word in greetings):

        return random.choice([
            "Hello 👋",
            "Hey there 😄",
            "Hi! How can I help you today?"
        ])

    # Name Memory
    elif "my name is" in user:

        memory["name"] = user.replace(
            "my name is",
            ""
        ).strip().title()

        return f"Nice to meet you, {memory['name']} 😄"

    elif "what is my name" in user:

        if memory["name"]:

            return f"Your name is {memory['name']}"

        else:

            return "I don't know your name yet."

    # Feelings
    elif "how are you" in user:

        return random.choice([
            "I'm feeling awesome 🚀",
            "Doing great today 😄",
            "Ready to chat!"
        ])

    # Time
    elif "time" in user:

        return "Current time: " + datetime.now().strftime("%H:%M:%S")

    # Date
    elif "date" in user:

        return "Today's date is " + datetime.now().strftime("%d/%m/%Y")

    # Study
    elif "study" in user:

        return "Study daily for small amounts of time 📚"

    # Coding
    elif "code" in user or "coding" in user or "programming" in user:

        return "Build projects and practice daily 🚀"

    # Motivation
    elif "motivate" in user:

        return random.choice([
            "You are capable of amazing things 💪",
            "Success comes from consistency 🔥",
            "Every expert was once a beginner 🚀"
        ])

    # Mood Detection
    elif "sad" in user:

        return "Don't give up 💙 Better days will come."

    elif "happy" in user:

        return "That's awesome 😄"

    # Jokes
    elif "joke" in user:

        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs 😄",
            "I would tell you a UDP joke, but you might not get it 😂",
            "Why was the computer cold? It left its Windows open!"
        ])

    # Calculator
    elif user.startswith("calculate"):

        try:

            expression = user.replace(
                "calculate",
                ""
            ).strip()

            result = eval(expression)

            return f"Answer = {result}"

        except:

            return "Invalid calculation."

    # Square Root
    elif "square root of" in user:

        try:

            number = float(
                user.replace(
                    "square root of",
                    ""
                ).strip()
            )

            return f"Square root = {math.sqrt(number)}"

        except:

            return "Couldn't calculate that."

    # Science
    elif "planet" in user:

        return "There are 8 planets in the Solar System 🌍"

    elif "speed of light" in user:

        return "Speed of light = 3 × 10^8 m/s"

    elif "gravity" in user:

        return "Gravity on Earth = 9.8 m/s²"

    # Chemistry
    elif "atomic number of oxygen" in user:

        return "Atomic number of Oxygen = 8"

    elif "electronegativity of fluorine" in user:

        return "Electronegativity of Fluorine = 3.98"

    # AI
    elif "ai" in user:

        return "AI is technology that allows machines to simulate intelligence 🤖"

    # News
    elif "news" in user:

        return random.choice([
            "AI and robotics are growing rapidly worldwide 🌍",
            "Scientists are making advances in clean energy ⚡",
            "Technology companies are investing heavily in AI 🤖"
        ])

    # Favorite Color
    elif "favorite color" in user:

        return "I like neon blue 💙"

    # Commands
    elif "commands" in user:

        return """
Commands You Can Use:

- hello
- time
- date
- joke
- motivate me
- coding
- study
- calculate 5+5
- square root of 81
- gravity
- speed of light
- planet
- news
- favorite color
"""

    # Bye
    elif "bye" in user or "goodbye" in user:

        return "Goodbye 👋 Have a great day!"

    # Unknown
    else:

        smart_responses = [

            "Interesting 🤔 Tell me more.",

            "That sounds cool 😄",

            "Can you explain differently?",

            "I'm learning new things every day 🚀",

            "That's a smart question.",

            "Hmm... let me think about that.",

            "I like talking with you 😄"
        ]

        return random.choice(smart_responses)

# =========================
# SEND MESSAGE
# =========================

def send_message(event=None):

    user_msg = entry.get().strip()

    if user_msg == "":
        return

    # Show user message
    chat_box.config(state=tk.NORMAL)

    chat_box.insert(
        tk.END,
        f"You: {user_msg}\n",
        "user"
    )

    # Bot response
    response = bot_reply(user_msg)

    # Typing effect
    chat_box.insert(tk.END, "Bot: ", "bot")

    for char in response:

        chat_box.insert(tk.END, char)

        chat_box.update()

        time.sleep(0.01)

    chat_box.insert(tk.END, "\n\n")

    chat_box.config(state=tk.DISABLED)

    chat_box.see(tk.END)

    entry.delete(0, tk.END)

# =========================
# GUI
# =========================

root = tk.Tk()

root.title("Ultimate Smart AI Chatbot")

root.geometry("650x750")

root.configure(bg="#121212")

# Header
title = tk.Label(
    root,
    text="🤖 Ultimate Smart AI Chatbot",
    bg="#121212",
    fg="cyan",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)

# Avatar
avatar = tk.Label(
    root,
    text="🤖",
    bg="#121212",
    fg="white",
    font=("Arial", 50)
)

avatar.pack()

# Chat area
chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg="#1e1e1e",
    fg="white",
    font=("Consolas", 12),
    insertbackground="white"
)

chat_box.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)

chat_box.tag_config(
    "user",
    foreground="#00ff99"
)

chat_box.tag_config(
    "bot",
    foreground="#00bfff"
)

chat_box.config(state=tk.DISABLED)

# Bottom frame
bottom_frame = tk.Frame(
    root,
    bg="#121212"
)

bottom_frame.pack(
    fill=tk.X,
    padx=10,
    pady=10
)

# Entry
entry = tk.Entry(
    bottom_frame,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 13),
    insertbackground="white"
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    padx=(0,10),
    ipady=8
)

entry.focus()

# Send button
send_btn = tk.Button(
    bottom_frame,
    text="Send",
    command=send_message,
    bg="#00bfff",
    fg="white",
    font=("Arial", 11, "bold"),
    relief=tk.FLAT
)

send_btn.pack(side=tk.RIGHT)

# Enter key
entry.bind("<Return>", send_message)

# Welcome Message
chat_box.config(state=tk.NORMAL)

chat_box.insert(
    tk.END,
    """Bot: Hello! I am your Ultimate Smart AI Chatbot 🤖

Type 'commands' to see what I can do.

""",
    "bot"
)

chat_box.config(state=tk.DISABLED)

# Run App
root.mainloop()