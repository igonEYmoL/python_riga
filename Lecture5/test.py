try:
    with open("file2.txt", "r") as file:
        for line in file:
            print(line)
    file.close()

    with open("file1.txt", "w") as file:
        file.write("This is a test file.\n")
        file.write("This is the second line.\n")
    file.close()

    print("hello", "World", sep=",",end="!\n")
    
except FileNotFoundError as e:
    print(f"Missing file : {e}")
else:
    print("Toutes les opérations de fichier ont réussi.")
finally:
    print("Execution completed.")


