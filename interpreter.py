def run():
 program = input()
 accumulator = 0
 for instruction in program:
    if instruction == "+":
        accumulator += 1
    if instruction == "-":
        accumulator -= 1
    if instruction == "+²":
        accumulator += 10
    if  instruction == "-²"
        accumulator -= 10
    if instruction == "o":
        print(accumulator)


