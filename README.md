# 💡 Electricity Bill Calculator

A simple, interactive Streamlit web application that calculates electricity bills based on a slab-based pricing system. 

## 🚀 Features
- **Interactive UI:** Built with Streamlit for a clean user experience.
- **Slab Visualization:** Displays a clear table of current electricity rates.
- **Real-time Calculation:** Uses `if-elif-else` logic to calculate the total bill accurately based on unit consumption.

## 📊 Pricing Slabs
The app calculates the bill using the following rates:
| Unit Range | Rate per Unit |
| :--- | :--- |
| 0 - 100 | Free (Rs 0) |
| 101 - 200 | Rs 5 |
| 201 - 500 | Rs 10 |
| Above 500 | Rs 20 |

## 🛠️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

2. **Install dependencies: Make sure you have Python installed, then run:**

    ```bash
     pip install -r requirements.txt

3. **Run the app:**
    ```
    streamlit run app.py

 4. **Requirements**
Python  
Streamlit    
Pandas

5. **How it works** 
The app uses a progressive taxing/billing logic. For example, if you enter 300 units:   
i) First 100 units: (100 x 0)  
ii) Last 100 units: (100 x 0)  
iii) Remaining 100 units: Rs 1000 (100 x 0)  
iv) Total: Rs 1500

