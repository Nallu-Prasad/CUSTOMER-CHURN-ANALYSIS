CUSTOMER CHURN ANALYSIS

Installation

To install this project, follow these steps:

1.  Download the folder from the drive link

2.  Navigate to the project directory

3.  Open the Command prompt. Create a python environment : "python -m venv myenv"

4.  Activate the environment : "myenv\Scripts\activate"

5.  Install dependencies: "pip install -r requirements.txt"

6.  After installing the dependencies, open the jupyter notebook through cmd : "jupyter notebook"

7.  Then, Open the Churn.ipynb file and run all the cells.

8.  Open the flask app "app.py" in VS Code.

9. Open the terminal and enter "python app.py" ====> It will give http://127.0.0.1:5000

10. Using the REST API "POST" method (use this:"http://127.0.0.1:5000/predict") in Postman or any other API validation tool.

11. Test the API with the sample data(JSON Format):

{
    "gender": 1,
    "age": 30,
    "tenure": 36,
    "monthly_charges": 80.00,
    "service_usage1": 30,
    "service_usage2": 20,
    "service_usage3": 45,
    "avg_spend_per_month": 50.00,
    "total_charges": 2880.00,
    "payment_method": 1 
}

12. It will give the sample output as

{
    "Churn Prediction": 0,
    "Churn Probability": 0.17
}

For any queries, please contact,
    Email: nalluprasad2004@gmail.com
