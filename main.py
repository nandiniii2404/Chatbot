import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Load intents from a JSON file
with open('intents.json') as file:
    intents = json.load(file)

# Find response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if user_input == pattern.lower():
                return intent["responses"][0]
    return "I'm sorry, I didn't understand that. Can you rephrase?"


# Submit feedback
def submit_feedback():
    feedback = simpledialog.askstring("Feedback", "Please enter your feedback:")
    if feedback:
        with open("feedback.txt", "a") as f:
            f.write(feedback + "\n")
        messagebox.showinfo("Thank You", "Your feedback has been submitted!")

# Send message function
def send_message():
    user_input = entry.get()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        response = get_response(user_input)
        chat_log.insert(tk.END, "Bot: " + response + "\n\n")
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Student Chatbot")

chat_log = tk.Text(root, state=tk.DISABLED, width=80, height=20, bg="lightyellow")
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

feedback_button = tk.Button(root, text="Feedback", command=submit_feedback)
feedback_button.pack(side=tk.LEFT, padx=10)

root.mainloop()

