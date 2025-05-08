# Week 1

This week's lab is meant to give you a very basic introduction to the Python coding environment. In particular, we will focus on the following:

- JupyterLab and Markdown
- Variables and Data Types
- Operators and Logic
- Packages, Modules, and Objects

## setup

*(As of April 2025)*

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Once you're ready, commit and push your final changes to your repository.
4. Submit a URL to your (forked) repository on Canvas ([using Gradescope](https://guides.gradescope.com/hc/en-us/articles/21865616724749-Submitting-a-Code-assignment)).

## exercises

**For the exercises, only update the *apputil.py* file or the *app.py* file.** Updating any other files may affect your autograder feedback.

### exercise 1

In *apputil.py*, create a function `palindrome(word)` that receives a string and returns `True` or `False` depending on whether it is a palindrome.  A palindrome is a word, phrase, or sequence that reads the same backward as forward. Examples of palindromes are `racecar` and `Nurses Run`. This function can be case *insensitive*, and it should ignore spaces and punctuation.

- Take a look at the `.lower()` and `.replace(",")` methods on a string.
- Think about how you can reverse a string

---

**A few test cases:**

- `racecar`
- `Nurses Run`
- `Sit on a potato pan, Otis.`

### exercise 2

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

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: week-1
dependencies:
  - python=3.11
  - pip
  - pip:
    - ipykernel  # for Jupyter Notebook
    - streamlit
    - pandas
    - numpy
```

*Note: you are welcome to install more pacakges in your codespace, but they will not be used by the autograder.*
