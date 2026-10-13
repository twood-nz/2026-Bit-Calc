# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructrions go here
- instructions 1
- instructions 2
- etc
    ''')


# Main routine goes here

# Display instructions if requested
want_insturctions = input("Press <enter> to read the insturctions"
                          "or any key to continue")
if want_insturctions == "":
    instructions()

print("program continues")

