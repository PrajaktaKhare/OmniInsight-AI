import ollama

from tools.loader import load_dataset
from tools.query import query_dataset

from memory import add_memory, get_memory


# Load dataset once when agent starts
data = load_dataset("dataset/data.json")


def run_agent(question):

    print("\nThought: Analyze user request and decide if a tool is needed.")


    # Step 1: Ask LLM whether a tool is required
    first_response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": """
You are an HR analytics AI agent.

You have access to this tool:

query_dataset

Use the tool whenever the user asks about employee data,
salary, department, attrition, roles, or statistics.

If a tool is required, respond exactly:

ACTION: query_dataset

Otherwise answer normally.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )


    decision = first_response["message"]["content"]


    # Step 2: Tool execution
    if "ACTION: query_dataset" in decision:


        print("Action: query_dataset")


        history = get_memory()


        # Handle follow-up questions
        context_question = question


        follow_up_words = [
            "that employee",
            "that person",
            "which department",
            "what department",
            "what role",
            "what job",
            "what is the name"
        ]


        if any(
            word in question.lower()
            for word in follow_up_words
        ):

            context_question = f"""
Previous conversation:

{history}


Current question:

{question}


Use the previous result to understand the employee being discussed.
"""


        # Execute tool
        observation = query_dataset(
            data,
            context_question
        )


        print(
            "Observation:",
            observation
        )


        # Step 3: Generate final answer using LLM

        final_response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an HR analytics assistant.

Rules:
- Answer using only the observation data.
- Use previous conversation if the user refers to earlier results.
- Do not invent missing information.
- If the dataset does not contain information, say it is unavailable.
"""
                },
                {
                    "role": "user",
                    "content": f"""
Previous conversation:

{history}


Current question:

{question}


Observation:

{observation}


Provide a clear final answer.
"""
                }
            ]
        )


        answer = final_response["message"]["content"]


        # Save memory
        add_memory(
            question,
            {
                "observation": observation,
                "answer": answer
            }
        )


        return answer


    else:

        # Normal conversation without tool
        answer = decision


        add_memory(
            question,
            answer
        )


        return answer