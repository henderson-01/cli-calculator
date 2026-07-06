# 🧮 cli-calculator project

## 🚀 Overview

Welcome to the **Rich CLI-Calculator Project**! This is an enhanced version of a classic calculator, rebuilt with a beautiful and interactive Command Line Interface (CLI) using the [Rich](https://github.com/Textualize/rich) library for Python. It provides a visually appealing experience for performing basic arithmetic operations. 🎉

---

## ✨ Features

- 🎨 **Beautiful UI**: Styled panels, tables, and text using the Rich library.
- ➕ **Addition**: Add two numbers together.
- ➖ **Subtraction**: Subtract one number from another.
- ✖️ **Multiplication**: Multiply two numbers.
- ➗ **Division**: Divide one number by another (with division by zero protection).
- 🛡️ **Robust Input Handling**: Validates user input for operations and numbers, ensuring a smooth experience.
- 📊 **Visual Feedback**: Results are displayed in color-coded panels corresponding to the operation performed.

---

## 🛠️ How It Works

The calculator is implemented in Python and leverages the `rich` library to create a terminal-based graphical interface.

1. **Welcome Screen**: Displays a styled welcome panel.
2. **Operation Menu**: Shows a table of available operations with keys and symbols.
3. **Input Validation**: Prompts the user for an operation key and two numbers, handling invalid inputs gracefully.
4. **Result Display**: Shows the calculation result in a styled panel with color coding based on the operation.

---

## 📂 File Structure

```text
.
├── calculator.py
├── CONTRIBUTING.md
├── image
│   └── Screenshot.png
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 🚀 Installation

1. **Clone the repository then navigate into the directory**:

   ```bash
   cd cli-calculator
   ```

2. **Install dependencies**:

   ```bash
   uv sync
   ```

---

## ▶️ Usage

Run the calculator using the following command:

```bash
uv run calculator.py
```

Follow the on-screen prompts to select an operation and enter your numbers.

---

## 📸 Screenshot

![Calculator Welcome Screen](/image/Screenshot.png)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Rich](https://github.com/Textualize/rich) for providing an amazing library for terminal UIs.

---

Happy calculating! 🧮✨
