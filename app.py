from agent import run_agent


def main():

    print(
        "AI HR Analytics Agent"
    )


    while True:

        question=input(
            "\nAsk a question: "
        )


        if question=="exit":
            break


        answer=run_agent(question)

        print(answer)



if __name__=="__main__":
    main()