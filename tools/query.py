def query_dataset(data, question):

    question = question.lower()


    if "highest salary" in question or "highest income" in question:

        employee = max(
            data,
            key=lambda x: x["MonthlyIncome"]
        )

        return {
            "employee": {
                "age": employee["Age"],
                "department": employee["Department"],
                "role": employee["JobRole"],
                "monthly_income": employee["MonthlyIncome"]
            }
        }


    elif "average salary" in question:

        incomes = [
            x["MonthlyIncome"]
            for x in data
        ]

        return {
            "average_income":
            round(sum(incomes)/len(incomes),2)
        }


    elif "attrition" in question:

        count = sum(
            1 for x in data
            if x["Attrition"] == "Yes"
        )

        return {
            "employees_left": count
        }

    elif "lowest salary" in question or "lowest income" in question:

        employee = min(
            data,
            key=lambda x: x["MonthlyIncome"]
        )

        return {
        "employee": {
        "name": employee.get("Name", "Name not available"),
        "age": employee["Age"],
        "department": employee["Department"],
        "role": employee["JobRole"],
        "monthly_income": employee["MonthlyIncome"]
        }
    }
    return {
        "error":"I cannot answer this yet"
    }