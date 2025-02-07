def sim(inp):
    """Calculate the similarity sum for the given string."""
    total_sum = 0
    length = len(inp)

    for i in range(length):
        common_length = 0
        for j in range(i, length):
            if inp[j - i] == inp[j]:
                common_length += 1
            else:
                break
        total_sum += common_length

    print(total_sum)

def main():
    """Main function to handle multiple test cases."""
    try:
        testcases = int(input("Enter number of test cases: ").strip())
        if 1 <= testcases <= 10:
            for _ in range(testcases):
                string = input("Enter a lowercase string: ").strip()
                if len(string) <= 10000 and string.islower():
                    sim(string)
                else:
                    print("Error: Invalid input (string length exceeded or contains uppercase/numbers).")
        else:
            print("Error: Number of test cases exceeded the allowed limit.")
    except ValueError:
        print("Error: Invalid input, please enter an integer.")

if __name__ == "__main__":
    main()
