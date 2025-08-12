# Week 1 Exercises

**For the exercises, only update the *apputil.py* file or the *app.py* file.** Updating any other files may affect your autograder feedback.

Give [Python Tutor](https://pythontutor.com/) a try! It can be a helpful tool for debugging Python :).

## exercise 1

In *apputil.py*, create a function `palindrome(word)` that receives a string and returns `True` or `False` depending on whether it is a palindrome.  A palindrome is a word, phrase, or sequence that reads the same backward as forward. Examples of palindromes are `racecar` and `Nurses Run`. This function can be case *insensitive*, and it should ignore spaces and punctuation.

- Take a look at the `.lower()` and `.replace(",")` methods on a string.
- Think about how you can reverse a string

---

**A few test cases:**

- `racecar`
- `Nurses Run`
- `Sit on a potato pan, Otis.`

## exercise 2

In programming languages, and especially in [LISP](https://en.wikipedia.org/wiki/Lisp_(programming_language)), there can be a lot of parentheses. The parentheses have to be "balanced" to be valid. For example, `()(())` is balanced, but `()())` is not balanced. Also, `)((())` is not balanced. (Think mathematics.)

Write a function `parentheses(sequence)` that takes a string and returns `True` if the string's parentheses are balanced, `False` if they are not.

*Once you are finished, see if you can come up with a second way to solve the problem.*

---

**Test Cases:**

 * `((blah)()()())` should return `True`
 * `(((())blee))` should return `True`
 * `(()hello((())()))` should return `True`
 * `((((((())` should return `False`
 * `()))` should return `False`