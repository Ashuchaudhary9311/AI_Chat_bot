import pyautogui
import pyperclip
import time
import requests
import json


url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": "Bearer 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",  # <-- your API key
    "Content-Type": "application/json"
}


# === Step 1: Click at (1112, 1048)
pyautogui.click(1112, 1048)
time.sleep(1)

# while True:
    # === Step 2: Drag from (685, 249) to (1856, 921) to select text
pyautogui.moveTo(673, 247  )
pyautogui.dragTo( 1337 ,919, duration=1, button='left')
time.sleep(1)

    # === Step 3: Copy (Ctrl+C)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

    # === Step 4: Get clipboard content
Chat = pyperclip.paste()
print(Chat)

    

    # === Step 5: Call Perplexity API ===

payload = {
        "model": "sonar-pro",   # or sonar-medium-online / sonar-small-online
        "messages": [
            {"role": "system", "content": "You are Ashu. Only focus on the last 3–4 user messages provided." 
                        " Ignore older history. "
                            " Reply casually and in a friendly tone, like chatting with a close friend."  
                            " Keep your response very short (1–2 sentences max)."  
                            " Do not over-explain or give long answers."},
            {"role": "user", "content": Chat}
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("AI Response:", reply)
else:
        print("Error:", response.status_code, response.text)
        reply = "Error generating response."

    # === Step 6: Copy response to clipboard
pyperclip.copy(reply)

    # === Step 7: Click at (990, 970), paste, and press Enter
pyautogui.click(990, 970)
time.sleep(1)

pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.press("enter")
