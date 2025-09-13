import streamlit as st
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio

st.title("AlgoMaster - DSA Problem Solver")
st.write("Welcome to AlgoMaster! This application leverages AI to help you solve Data Structures and Algorithms problems efficiently.")

task = st.text_input("Enter your DSA problem statement:", value='Write a Python function to check if a number is prime.')


async def run(team, docker, task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source} : {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f'Stop Reason: {message.stop_reason}')
                yield msg
            print("Task completed.")
    except Exception as e:
        print("Error occurred: ", e)
        yield f"Error occurred: {e}"
    finally:
        await stop_docker_container(docker)

if st.button("Solve"):
    st.write("Solving the problem...")

    team, docker = get_dsa_team_and_docker()

    async def collect_messages():
        async for msg in run(team, docker, task):
            if msg.startswith("user"):
                with st.chat_message('user', avatar="🧑"):
                    st.markdown(msg)
            elif msg.startswith("DSA_problem_solver_Agent"):
                with st.chat_message('assistant', avatar="🤖"):
                    st.markdown(msg)
            elif msg.startswith("code_executor_agent"):
                with st.chat_message('assistant', avatar="💻"):
                    st.markdown(msg)
            elif isinstance(msg, TaskResult):
                with st.chat_message('stopper', avatar="🛑"):
                    st.markdown(f"Stop Reason: {msg.stop_reason}")
    
    asyncio.run(collect_messages())

        