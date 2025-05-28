try:
    with open("helloworld.txt", "r") as file:
        print(file.read())
    file.close()
    with open("helloworld.txt", "w") as file:
        file.write("Hello world in French language.\n")
    file.close()
except FileNotFoundError as e:
    print(f"Missing file : {e}")
else:
    print("All file operations were successful.")
finally:
    print("Execution completed.")
