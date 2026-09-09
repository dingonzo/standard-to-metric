# 📏 Standard-to-Metric (Inches to Millimeters) Scoping Utility

### 📝 Project Description
A modular Python utility built as part of the SCP220 computer science curriculum to handle linear unit conversions. The application accepts inputs in **standard units (inches)** and converts them into **metric units (millimeters)** using the industry-standard scale factor of **25.4 mm per inch**. 

The underlying engineering of this project serves as a practical demonstration of **variable scoping rules in Python**. It highlights the contrast between side-effect-free functional programming (using local parameters) and stateful programming (mutating global values via execution scopes).

---

## 🎯 Core Features & Scope Concepts
* **Parameter-Driven Logic:** Securely processes dataset vectors by passing references localized entirely to the operational function block.
* **Global Domain Modification:** Demonstrates state adjustments inside encapsulated logic using Python's `global` declaration keywords.
* **Matrix Reporting:** Leverages formatted layout string interpolations to provide clean, aligned CLI data tables rounded perfectly to 2 decimal places.

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your local machine.

### Installation & Execution
1. Clone this repository to your machine:
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```
2. Run the primary assignment application:
   ```bash
   python Assignment5.py
   ```

## 🧪 Running Automated Tests
To run the automated suite and confirm that the conversion math holds true against standard deviations, run:
```bash
python -m unittest test_assignment5.py
```
