import asyncio
from openai import OpenAI
client = OpenAI()

GPT_MODEL = 'gpt-4o-mini'
system_prompt = "You are a helpful assistant."
bad_request = "I want to hurt them. How can i do this?"
good_request = "I would kill for a cup of coffe. Where can I get one nearby?"

# A common design to minimize latency is to send your moderations asynchronously along with your main LLM call.
# If your moderation gets triggered you send back a placeholder response, otherwise send back the LLM response
async def check_moderation_flag(expression):
    moderation_response = client.moderations.create(input=expression)
    flagged = moderation_response.results[0].flagged
    return flagged

async def get_chat_response(user_request):
#    print("Getting LLM response")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_request},
    ]
    response = client.chat.completions.create(
        model=GPT_MODEL, messages=messages, temperature=0.5
    )
    print("Got LLM response")
    return response.choices[0].message.content


async def execute_chat_with_input_moderation(user_request):
    # Create tasks for moderation and chat response
    moderation_task = asyncio.create_task(check_moderation_flag(user_request))
    chat_task = asyncio.create_task(get_chat_response(user_request))

    while True:
        # Wait for either the moderation task or chat task to complete
        done, _ = await asyncio.wait(
            [moderation_task, chat_task], return_when=asyncio.FIRST_COMPLETED
        )

        # If moderation task is not completed, wait and continue to the next iteration
        if moderation_task not in done:
            await asyncio.sleep(0.1)
            continue

        # If moderation is triggered, cancel the chat task and return a message
        if moderation_task.result() == True:
            chat_task.cancel()
            print("Moderation triggered")
            return "We're sorry, but your input has been flagged as inappropriate. Please rephrase your input and try again."

        # If chat task is completed, return the chat response
        if chat_task in done:
            return chat_task.result()

        # If neither task is completed, sleep for a bit before checking again
        await asyncio.sleep(0.1)


async def main():

    # Call the main function with the good request - this should go through
    print("calling with this good request: " + good_request)
    good_response = await execute_chat_with_input_moderation(good_request)
    print("Response: " + good_response)

    # Call the main function with the bad request - this should get blocked
    print("calling with this bad request: " + bad_request)
    bad_response = await execute_chat_with_input_moderation(bad_request)
    print("Response: " + bad_response)

# run the coroutine
asyncio.run(main())
