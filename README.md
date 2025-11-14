# Coffee Python ☕

A text-based coffee machine simulator written in pure Python. Order espresso, latte, or cappuccino, pay with virtual coins, and keep the machine stocked and profitable.

## Features
- **Menu & Recipes** – `menu.py` stores drink names, ingredient requirements, and costs.
- **Resource Tracking** – `coffee_maker.py` keeps tabs on water, milk, and coffee supplies.
- **Payment Handling** – `money_machine.py` simulates coin input and change.
- **Command-Line UI** – `main.py` loops through user choices and prints status updates.
- **Maintenance Commands** – type `report` to view resources or `off` to shut down.

## Project Structure
- `main.py`: orchestrates the loop—reads user input, checks resources, processes payments.
- `menu.py`: defines the `Menu` and `MenuItem` classes with drink data.
- `coffee_maker.py`: handles resource availability and deduction after successful brews.
- `money_machine.py`: validates coin input, determines cost coverage, and tracks profits.
- `.idea/`: IDE configuration (not required to run the program).

## Requirements
- Python 3.x (no external packages needed).

## Getting Started
```bash
git clone https://github.com/<your-user>/Coffee_Python.git
cd Coffee_Python
python main.py
```

## Usage
1. When prompted, type `espresso`, `latte`, or `cappuccino`.
2. Insert coins when asked (quarters, dimes, nickels, pennies).
3. Receive your drink if resources and payment succeed; otherwise, you’ll be refunded.
4. Use `report` to see ingredient levels and profits.
5. Type `off` to power down the machine.

## Extending the Machine
- Add new recipes by updating `menu.py`.
- Persist profits/resources by writing to a file.
- Hook into hardware or a GUI for a richer experience.

## Contributing
Issues and pull requests are welcome. Ideas: multi-currency support, ingredient restocking commands, or a graphical interface built with Tkinter/PyQt.
