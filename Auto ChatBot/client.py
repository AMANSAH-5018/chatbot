from openai import OpenAI

client = OpenAI(
    # The program is totally correct and workable just need api_key to run this
    # Due to security and confidential reason I have revoked my api_key
    # Revoked my api_key so program doesn't give output, you can replace ypor api_key to see the output of this program
    api_key="please place your API keys here",
)

command = '''

'''
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Aman Sah who speaks hindi and english. He is coder.",
        },
        {"role": "user", "content": command},
    ],
)

print(completion.choices[0].message.content)
