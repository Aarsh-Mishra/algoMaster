import os
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.teams import RoundRobinGroupChat
import asyncio
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
from autogen_agentchat.messages import TextMessage, MultiModalMessage
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core import CancellationToken
from autogen_agentchat.ui import Console



load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  

model_client = OpenAIChatCompletionClient(
        model="gemini-2.0-flash",  
        api_key=api_key,
        
        model_info=ModelInfo(
            vision=True,
            function_calling=True,
            json_output=True,
            structured_output=True,
            family="gemini"
        )
    )

async def main():

    docker = DockerCommandLineCodeExecutor(
        work_dir='/tmp',
        timeout=120
    )

    code_executor_agent = CodeExecutorAgent(
        name = 'CodeExecutorAgent',
        code_executor = docker
    )

    problem_solver_agent = AssistantAgent(
        name = "DSA_problem_solver_Agent",
        description="An Agent for solving Data Structures and Algorithms problems",
        model_client=model_client,
        system_message='''
            you are a problem solver agent that is an expert in solving DSA problems.
            you will be working with code executor agent to execute code.
            you will be given a task.
            At the beginning of your response you have to specify your plan to solve the task.
            Then you should give the code in a code block.(python)
            you should write code in a one code block at a time and then pass it to code executor agent to execute it.
            Once the code is executed and if the same has been done successfully, you have the results.
            you should explain the code execution result.

            In the end once the code is executed successfully, you have to say "STOP" to stop the conversation.
            '''
    )

    termination_condition = TextMentionTermination("STOP")

    team = RoundRobinGroupChat(
        participants = [problem_solver_agent, code_executor_agent],
        termination_condition=termination_condition,
        max_turns = 10
    )

    

    try:
        await docker.start()
        task = 'write a python code to add two numbers'

        async for message in team.run_stream(task = task):
            print('==' * 20)
            print(message.source, ":", message)
            print('==' * 20)

    except Exception as e:
        print("Error occurred: ", e)
    finally:
        await docker.stop()

if __name__ == "__main__":
    asyncio.run(main())
    print("code execution completed successfully")