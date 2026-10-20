# Program accepts name of an input file
# Reads existing words in the file
# Prompts user for a new sentence
# Appends the new sentence to the exist text
# Reads file again with new changes

print("Enter the name of the input file, such as WordTextFile:")
filename = input()

# 1. Read and print each word from the existing file
print("\n--- Current Words in File ---")
with open(filename, 'r') as file:
    for line in file:
        wordline = line.split()
        for item in wordline:
            print(item)

# 2. Prompt the user for a new sentence to add
print("\nEnter a new sentence to add to the file:")
new_sentence = input()

# 3. Open the file in 'append' mode ('a') to add the new sentence on a new line
with open(filename, 'a') as file:
    file.write(f"\n{new_sentence}")

# 4. Read and output the final updated file content
print("\n--- Updated File Contents ---")
with open(filename, 'r') as file:
    print(file.read())
