def run():
 program = input()
 accumulator = 0
 for instruction in program:
    if instruction == "+":
        accumulator += 1
    if instruction == "-":
        accumulator -= 1
    if instruction == "o":
        print(accumulator)


