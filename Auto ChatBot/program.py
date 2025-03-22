import pyautogui
import time
import pyperclip
from openai import OpenAI

# Allow time to switch to the required window
time.sleep(1)

# Click on the icon at (1380, 1066)
pyautogui.click(439, 112)
time.sleep(1)  # Wait for UI response

# Click and drag to select text
pyautogui.moveTo(438, 116)
pyautogui.dragTo(1901, 973, duration=0.5, button="left")
# pyautogui.mouseUp()

# Copy the selected text to clipboard
pyautogui.hotkey("ctrl", "c")
pyautogui.click(1994, 281)
time.sleep(1)  # Wait for clipboard to update

# Retrieve the copied text
chat_history = pyperclip.paste()

# Print or use the copied text
print("Copied Text:", chat_history)


client = OpenAI(
    # The program is totally correct and workable just need api_key to run this
    # Due to security and confidential reason I have revoked my api_key
    # Revoked my api_key so program doesn't give output, you can replace ypor api_key to see the output of this program
    api_key="please place your API keys here",
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Aman Sah who speaks hindi and english. You are a coder. You alalyze chat like Aman and respond like Aman.",
        },
        {"role": "user", "content": chat_history},
    ],
)

response = completion.choices[0].message.content
pyperclip.copy(response)


pyautogui.click(1145, 1010)
time.sleep(1)
pyautogui.click("ctrl", "v")
time.sleep(1)

pyautogui.press("enter")
