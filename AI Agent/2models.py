"""
Talk to other Model using Open AI
"""
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI
import os
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel, input_guardrail, GuardrailFunctionOutput
import asyncio


load_dotenv(override=True)

instructions1 = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

instructions2 = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

sales_agent1 = Agent(name="Open AI Agent", instructions=instructions1, model="gpt-4o-mini")


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)

# In model parameter we need to pass gemini model as variable not string, only then it will know that your talking to Gemini.
#Or by default it will assume as Open AI model if u give as string
sales_agent2 =  Agent(name="Gemini Sales Agent", instructions=instructions2, model=gemini_model)

description = "Write a cold sales email"

tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description=description)
tool2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description=description)

subject_instructions = "You can write a subject for a cold sales email. \
You are given a message and you need to write a subject for an email that is likely to get a response."

html_instructions = "You can convert a text email body to an HTML email body. \
You are given a text email body which might have some markdown \
and you need to convert it to an HTML email body with simple, clear, compelling layout and design."

subject_writer = Agent(name="Email subject writer", instructions=subject_instructions, model="gpt-4o-mini")
subject_tool = subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject for a cold sales email")

html_converter = Agent(name="HTML email body converter", instructions=html_instructions, model="gpt-4o-mini")
html_tool = html_converter.as_tool(tool_name="html_converter",tool_description="Convert a text email body to an HTML email body")

email_tools = [subject_tool, html_tool]

instructions = "You are an email formatter. You receive the body of an email to be sent. \
You first use the subject_writer tool to write a subject for the email, \
then use the html_converter tool to convert the body to HTML. \
Finally, you MUST return the final output EXACTLY like this:\n\
\n\
SUBJECT: <subject here>\n\
\n\
HTML BODY: <html body here>\n\
\n\
PLAIN TEXT VERSION:\n\
<write the exact same email as a normal paragraph without any HTML tags or markdown>\n\
\n\
Do not add any other text or comments. ONLY return the above format."


emailer_agent = Agent(
    name="Email_Manager",
    instructions=instructions,
    tools=email_tools,
    model="gpt-4o-mini",
    handoff_description="Convert an email to HTML and send it")

tools = [tool1, tool2]
handoffs = [emailer_agent]

# ----------------------------------------------------

sales_manager_instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.

Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.

2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
You can use the tools multiple times if you're not satisfied with the results from the first try.

3. Handoff for Sending: Pass ONLY the winning email draft to the 'Email Manager' agent. The Email Manager will take care of formatting and sending.

Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must hand off exactly ONE email to the Email Manager — never more than one.
"""

sales_manager = Agent(
    name="Sales Manager",
    instructions=sales_manager_instructions,
    tools=tools,
    handoffs=handoffs,
    model="gpt-4o-mini")

message = "Send out a cold sales email addressed to Dear CEO from Alice"

async def main():
    with trace("Automated SDR"):
        result = await Runner.run(sales_manager, message)
        print("=" * 50)
        print("FINAL EMAIL OUTPUT:")
        print("=" * 50)
        print(result.final_output)

asyncio.run(main())
