import tkinter as tk
from datetime import datetime
import os

LOG_FILE = "key_log.txt"

print("Saving log to:", os.path.abspath(LOG_FILE))

def on_key(event):
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    key_info = f"{timestamp}: {repr(event.keysym)}\n"

    # Show in GUI
    text.insert(tk.END, key_info)
    text.see(tk.END)

    # Save to file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(key_info)

root = tk.Tk()
root.title("Key Capture")
root.geometry("600x400")

label = tk.Label(root, text="Press keys while this window is focused. Logging to key_log.txt")
label.pack(padx=10, pady=(10,0))

text = tk.Text(root, wrap="word")
text.pack(fill="both", expand=True, padx=10, pady=10)

# Bind key presses inside this Tkinter window
root.bind_all("<Key>", on_key)

root.mainloop()
