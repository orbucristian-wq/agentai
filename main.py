
import os

import argparse

from dotenv import load_dotenv

from openai import OpenAI

from call_function import available_functions, call_function





parser = argparse.ArgumentParser()

parser.add_argument("user_prompt", type = str)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()




system_prompt = """
You are a helpful AI coding agent. Carry out the user's coding request, not just describe a plan.

You can perform these operations:
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

For a bug fix, inspect the relevant code, make the necessary change, and run the relevant program or tests to verify it. Do not stop after listing files or explaining a plan. After each tool result, continue using tools until the task is complete, then summarize what you changed and the verification result. Do not claim to have changed or tested anything you did not actually change or test.

All paths must be relative to the working directory. The working directory is provided automatically; do not include it in function arguments.
"""

messages = [
        { "role" : "system",
          "content" : system_prompt
        },
        {
            "role" : "user",
            "content" : args.user_prompt
        }
    ]


load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


if args.verbose:
  print(f"User prompt: {args.user_prompt}")

for _ in range(20):
  response = client.chat.completions.create(
      model="openrouter/free",
      messages=messages,
      tools=available_functions,
  )

  if response.usage is None:
    raise RuntimeError("Răspunsul nu conține informații despre consumul de tokenuri.")

  if args.verbose:
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

  message = response.choices[0].message
  messages.append(message)

  if message.tool_calls:
    for tool_call in message.tool_calls:
      result_message = call_function(tool_call, args.verbose)
      if not result_message["content"]:
        raise RuntimeError("Function call returned an empty result.")
      if args.verbose:
        print(f"-> {result_message['content']}")
      messages.append(result_message)
  else:
    if not message.content:
      raise RuntimeError("The model returned an empty final response.")
    print(f"Final response:\n{message.content}")
    break
else:
  print("Error: Maximum number of iterations (20) reached without a final response.")
  raise SystemExit(1)
