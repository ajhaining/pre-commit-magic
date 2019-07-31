# 🧙‍♀️ Pre-commit Magic

Examples of what you can set up using pre-commit hooks.

I have written a [blog post]() about the benefits of using some of these approaches.

---

## Requirements

To run this project, you will need Node.js, NPM for the JS example and Python (3.6+) for the Python example.

---

## Install

For the python example you'll also need [Black](https://github.com/psf/black). It requires Python 3.6.0+. To install it run the following:

```
pip install black
```

To set up the project run the following:

```
git clone https://github.com/ajhaining/pre-commit-magic
cd pre-commit-magic
npm install
```

---

## Get Going

This project is set up as an example using the following rules:

```
{
  "*.js": [
    "eslint --fix",
    "git add",
    "jest --bail --findRelatedTests"
  ],
  "*.py": [
    "black"
  ],
  "*.{json,md,yaml,yml}": [
    "prettier --write",
    "git add"
  ]
}
```

If you have successfully installed the project you should be able to change or add any files matching the rules and see them pass or fail against the rule set.

---

## Contributing

I'm open to adding more examples and expanding this project out further. If you have any examples please open a PR.
