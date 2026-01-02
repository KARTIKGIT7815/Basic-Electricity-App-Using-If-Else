# Electricity Bill Calculator

An interactive web application built with Streamlit designed to calculate electricity consumption costs using a multi-slab pricing model. This tool provides a user-friendly interface for residents and businesses to estimate their monthly utility expenses.

## Project Overview

The application utilizes a progressive billing algorithm where the cost per unit increases as the total consumption crosses specific thresholds. This ensures a transparent view of how utility costs are distributed across different usage tiers.

## Technical Stack

* **Language:** Python
* **Web Framework:** Streamlit
* **Data Handling:** Pandas
* **Logic:** Conditional branching (If-Else structures)

## Pricing Structure

The bill is calculated based on the following cumulative slabs:

| Consumption Tier (Units) | Rate per Unit (INR) |
| --- | --- |
| First 100 units | Free (0) |
| 101 - 200 units | 5 |
| 201 - 500 units | 10 |
| Beyond 500 units | 20 |

## Installation and Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/KARTIKGIT7815/Basic-Electricity-App-Using-If-Else.git
cd Basic-Electricity-App-Using-If-Else

```

### 2. Install Required Dependencies

Ensure you have the necessary libraries installed by running:

```bash
pip install -r requirements.txt

```

### 3. Execution

Launch the application locally using the following command:

```bash
streamlit run app.py

```

## Functional Logic

The application follows a progressive slab-based calculation. This means you are only charged the higher rate for the units that fall within that specific bracket.

**Example Calculation for 300 Units:**

1. **Slab 1 (0-100 units): 0** 
2. **Slab 2 (101-200 units): 500** 
3. **Slab 3 (201-300 units): 1000** 
4. **Final Total: 1500** 

## Requirements

The `requirements.txt` file must include:

* `streamlit`
* `pandas`



