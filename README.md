# ☕ Cafeteria Management System

A simple **Python-based console application** to manage orders and generate bills for a café. This project is ideal for beginners to learn **Python basics** such as dictionaries, loops, and conditional statements, while simulating a real-world scenario.

## 📋 Features
- **Menu Display** – Shows a predefined café menu with prices.
- **Order Management** – Add multiple items with quantities.
- **Automatic Billing** – Calculates item-wise cost and total.
- **Input Validation** – Handles unavailable items gracefully.
- **Bill Summary** – Prints an itemized receipt.

## 🛠️ Technologies Used
- **Python 3** (Core Programming Language)
- **Dictionaries** for menu storage
- **Loops & Conditionals** for program flow
- **Basic Arithmetic** for calculations

## 📜 How It Works
1. The program displays the menu from “Brew & Bite Cafe.”
2. The customer enters items to order.
3. The system verifies availability and asks for quantity.
4. The total cost is calculated automatically.
5. When the customer finishes, a detailed bill is displayed.

## 📂 Project Structure
```
Cafeteria_Management_System/
│-- cafeteria.py      # Main program file
│-- README.md         # Project documentation
```

## 🚀 How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cafeteria-management-system.git
   cd cafeteria-management-system
   ```
2. **Run the program**
   ```bash
   python cafeteria.py
   ```

## 🍽 Sample Menu (Brew & Bite Cafe)
| Item                  | Price (₹) |
|----------------------|-----------|
| Espresso             | 120       |
| Cappuccino           | 150       |
| Latte                | 160       |
| Mocha                | 180       |
| Hot Chocolate        | 140       |
| Iced Coffee          | 130       |
| Blueberry Muffin     | 90        |
| Chocolate Croissant  | 100       |
| Cheese Sandwich      | 120       |
| Veg Wrap             | 110       |
| Chicken Panini       | 170       |

## 📈 Future Improvements
- GUI version using **Tkinter** or **PyQt**
- Integration with **SQLite** for persistent order storage
- Daily sales report generation

## 📄 License
This project is open-source under the **MIT License**.
