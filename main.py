import asyncio
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    dsa_team, docker = get_dsa_team_and_docker()

    try:
        await start_docker_container(docker)
        task = 'write a python code to add two numbers'

        async for message in dsa_team.run_stream(task = task):
            if isinstance(message, TextMessage):
                print("=="*20)
                print(message.source, ":", message)
            elif isinstance(message, TaskResult):
                print('Stop  Reason:', message.stop_reason)
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        await stop_docker_container(docker)

if __name__ == "__main__":
    asyncio.run(main())
    