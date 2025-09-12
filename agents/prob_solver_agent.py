from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client

def get_problem_solver_agent():
    """
    Function to get the problem solver agent.
    This agent is responsible for solving DSA problems.
    It will work with the code executor agent to execute code.
    """
    model_client = get_model_client()
    problem_solver_agent = AssistantAgent(
        name = "DSA_problem_solver_Agent",
        description="An Agent for solving Data Structures and Algorithms problems",
        model_client=model_client,
        system_message='''
            you are a problem solver agent that is an expert in solving DSA problems.
            you will be working with code executor agent to execute code.
            you will be given a task and you should.
            At the beginning of your response you have to specify your plan to solve the task.
            Then you should give the code in a code block.(python)
            you should write code in a one code block at a time and then pass it to code executor agent to execute it.
            Make sure that we have atleast 3 test cases for the code you write.
            Once the code is executed and if the same has been done successfully, you have the results.
            you should explain the code execution result.

            In the end once the code is executed successfully, you have to say "STOP" to stop the conversation.
            '''
    )

    return problem_solver_agent


