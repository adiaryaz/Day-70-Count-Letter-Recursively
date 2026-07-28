# Day-70-Count-Letter-Recursively

Day 70/100 - Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

# Count Letter Occurrences Recursively

A program to dynamically calculate the frequency of a specific character within a user-provided string by utilizing a recursive function instead of standard iterative loops or built-in counting methods.

## 📝 Description

This program processes a user-inputted string and tallies exactly how many times a target letter appears within it. It achieves this through a fundamental computer science technique: recursion.

The core logic resides in the `count_letter_recursively(s, letter)` function. The recursion relies on a crucial base case: `if not s:`, which evaluates to true when the string becomes empty, safely returning `0` to halt the execution chain. If the string is not empty, the recursive step executes. It evaluates `(1 if s[0] == letter else 0)` to check if the very first character of the current string matches the target letter, adding `1` to the total if it does. It then adds this result to a recursive call of the function passing the remainder of the string `s[1:]`.

Additionally, the driver code includes basic input validation to ensure the user only submits a single character as the target letter (`if len(input_letter) != 1:`), displaying a warning if the rule is violated.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text provided by the user.


* **Input 2:** A single character (letter) to search for within the string.



### Output:

* If valid: A formatted string stating: "The letter '[input_letter]' occurs [count] times in the string.".


* If invalid length: "Please enter only one letter.".



### Rules:

1. The program must prompt the user for a string and a target letter.


2. The driver code must check if the target letter is exactly one character long (`len(input_letter) != 1`).


3. The counting logic must be encapsulated within a recursive function named `count_letter_recursively(s, letter)`.


4. The function must establish a base case that returns `0` if the string is empty (`not s`).


5. The function must recursively slice the string using `s[1:]` and evaluate `s[0]`.


6. The program must print the final accumulated count back to the console.



---

## 💡 Examples

### Example 1 (Standard Occurrence)

**Input:**

```text
banana
a

```

**Output:**

```text
The letter 'a' occurs 3 times in the string.

```

**Explanation:** The recursion breaks "banana" down letter by letter:

1. 'b' == 'a' (0) + count("anana")
2. 'a' == 'a' (1) + count("nana")
3. 'n' == 'a' (0) + count("ana")
4. 'a' == 'a' (1) + count("na")
5. 'n' == 'a' (0) + count("a")
6. 'a' == 'a' (1) + count("")
7. "" triggers the base case (0). The stack unwinds: 0+1+0+1+0+1+0 = 3.



### Example 2 (Zero Occurrences)

**Input:**

```text
Python
z

```

**Output:**

```text
The letter 'z' occurs 0 times in the string.

```

**Explanation:** The function recursively slices through the entire word "Python". Because `s[0]` never matches the letter 'z', it repeatedly adds 0 to the stack, eventually returning a total count of 0.

### Example 3 (Validation Trigger)

**Input:**

```text
Hello
ll

```

**Output:**

```text
Please enter only one letter.

```

**Explanation:** The user entered two characters ("ll") as the target letter. The condition `if len(input_letter) != 1:` detects this and prints the designated error message, preventing the program from running an invalid recursive check.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 70.py").

```bash
git clone https://github.com/adiaryaz/Day-70-Count-Letter-Recursively.git
cd count-letter-recursively

```

2. **Run the program**:

```bash
python "Day 70.py"

```

Enter a string and then a single character to see the recursive function accurately tally its occurrences!
