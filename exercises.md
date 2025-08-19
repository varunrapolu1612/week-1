
--- 
There are two types of exercise in this course:

- autograded
- exploratory *(optional)*

**You are expected to complete all of the autograded exercises**, as these are the only ones that will be checked by the autograder and reviewed by the TA. **Exploratory exercises (or "explorations") are optional**, and responses for these will only be reviewed upon request.

**Only update the files listed in the exercises themselves.** Changing any other file may affect your autograder feedback.

---

# autograded exercises

For these exercises, add your functions to the *apputil\.py* file. If you like, you're welcome to adjust the *app\.py* file, but it is not required. The autograder will only check the *apputil\.py* file.

## exercise 1

Create a function `palindrome(word)` that receives a string and returns `True` or `False` depending on whether it is a palindrome.  A palindrome is a word, phrase, or sequence that reads the same backward as forward. Examples of palindromes are `racecar` and `Nurses Run`. This function can be case *insensitive*, and it should ignore spaces and punctuation.

- Take a look at the `.lower()` and `.replace(",")` methods on a string.
- Think about how you can reverse a string

**A few test cases:**

- `racecar`
- `Nurses Run`
- `Sit on a potato pan, Otis.`

## exercise 2

In programming languages, and especially in [LISP](https://en.wikipedia.org/wiki/Lisp_(programming_language)), there can be a lot of parentheses. The parentheses have to be "balanced" to be valid. For example, `()(())` is balanced, but `()())` is not balanced. Also, `)((())` is not balanced. (Think mathematics.)

Write a function `parentheses(sequence)` that takes a string and returns `True` if the string's parentheses are balanced, `False` if they are not.

*Once you are finished, see if you can come up with a second way to solve the problem.*

> Give [Python Tutor](https://pythontutor.com/) a try this week! It can be a helpful tool for debugging Python :).

**Test Cases:**

 * `((blah)()()())` should return `True`
 * `(((())blee))` should return `True`
 * `(()hello((())()))` should return `True`
 * `((((((())` should return `False`
 * `()))` should return `False`

---

# exploratory exercises

For this exploration, you'll only need to update the bottom of the lab notebook. If you like, you can also explore Streamlit by incorporating this function the *app\.py* file.

*Note: the following explorations are completely optional.*

## exploration 1

Write a function to find the largest number in the Alice in Wonderland book. (Remember, we should have `aiw_words`.)

- The regex pattern `"\d+"` will match on any integer (without commas).
- [re.match](https://docs.python.org/3/library/re.html#re.match) will return a "truthy" value if there is a match.
- Recall the built-in function `sorted`. How can you reverse the ordering here?
- Also, you can convert a string of digits to an integer with `int(characters)`.
