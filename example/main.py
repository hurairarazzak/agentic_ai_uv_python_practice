from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
from agents import function_tool

gemini_api_key = "AIzaSyAnzqTz4DLtEIoeYd2A6HGwre02Ns-TOn8"

set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

@function_tool
def addition(x: int, y: int) -> int:
    return x + y

@function_tool
def subtraction(x: int, y: int) -> int:
    return x - y

@function_tool
def multiplication(x: int, y: int) -> int:
    return x * y

@function_tool
def divison(x: int, y: int) -> int:
    return x / y

agent: Agent = Agent(
    name="MathAgent",
    instructions="You are a helpful math assistant that solves basic calculations.",
    model="gemini-2.0-flash",
    tools=[addition, subtraction, multiplication, divison]
)

result = Runner.run_sync(agent, "What is 6 * 2?")
print(result.final_output)
