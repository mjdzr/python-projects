# Monty Hall Problem

This project explores the famous **Monty Hall Problem**, a probability puzzle based on a game show scenario. The goal is to simulate and analyze the problem using Python.

## Problem Description

You are a contestant on a game show with three doors:
- Behind one door is a car (the prize).
- Behind the other two doors are goats.

### Rules:
1. You pick one door.
2. The host, who knows what is behind each door, opens one of the other two doors to reveal a goat.
3. You are then given the choice to either stick with your original door or switch to the other unopened door.

The question is: **Should you switch or stay to maximize your chances of winning the car?**

## Project Structure

```
4_monty_hall_problem/
├── app.py                  # Streamlit app to explore the Monty Hall problem interactively
├── monty_hall_simulation.py # Python script to simulate the Monty Hall problem
├── requirements.txt        # List of required Python libraries
└── README.md               # Documentation for the project
```

## Requirements

- Python 3.x
- Libraries: `streamlit`

## How to Run

1. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the simulation:
    ```bash
    python monty_hall_simulation.py
    ```
3. Launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Results

The simulation demonstrates that switching doors increases your chances of winning the car to **2/3**, while staying gives you a **1/3** chance.

## References

- [Monty Hall Problem - Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)
- [Image Credit: Brilliant.org](https://brilliant.org/wiki/monty-hall-problem/)