def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and one operator."

        first_operand, operator, second_operand = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)

        if operator == '+':
            answer = str(int(first_operand) + int(second_operand))
        else:
            answer = str(int(first_operand) - int(second_operand))
        answers.append(answer)

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(width)
        second_line += operators[i] + second_operands[i].rjust(width - 1)
        dashes_line += '-' * width
        answers_line += answers[i].rjust(width)

        if i < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            dashes_line += "    "
            answers_line += "    "

    if show_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}"

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

