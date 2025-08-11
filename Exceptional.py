# Read from input.txt and write a modified version to output.txt
try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify the content (e.g., reverse each line)
    modified_lines = [line[::-1] for line in content.splitlines()]
    modified_text = "\n".join(modified_lines)

    with open("output.txt", "w") as outfile:
        outfile.write("MODIFIED CONTENT:\n")
        outfile.write(modified_text)

    print("✅ Modified content written to 'output.txt' successfully.")

except FileNotFoundError:
    print("⚠️ 'input.txt' not found. Please make sure the file exists.")

# Ask user for a filename and handle errors
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        print("\n📄 File Content:\n")
        print(file.read())

except FileNotFoundError:
    print(f"❌ Error: File '{filename}' not found.")
except PermissionError:
    print(f"🚫 Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")