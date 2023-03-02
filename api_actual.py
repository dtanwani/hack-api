import flask
from flask import request
import sketch
import json
import pandas as pd


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
#sales_data = pd.read_csv("https://gist.githubusercontent.com/bluecoconut/9ce2135aafb5c6ab2dc1d60ac595646e/raw/c93c3500a1f7fae469cba716f09358cfddea6343/sales_demo_with_pii_and_all_states.csv")
#res=sales_data.sketch.ask("Can you give me friendly names, Business descriptions, and flag (Yes/No) tell if there is any PII information for each column? (output as JSON)")

diabetes_data = pd.read_csv("C:\Divya_documents\Python_learning\Edureka_Python_Course\sample.csv")
data1=diabetes_data.sketch.ask("Can you give me friendly names, Business descriptions, and flag (Yes/No) tell if there is any PII information for each column?(output as JSON)",call_display=False)
#ini_string = json.dumps(str(diabetes_data.sketch.ask("Can you give me friendly names, Business descriptions, and flag (Yes/No) tell if there is any PII information for each column? (output as JSON)")))

data = [{
        "index": {
                    "Logical Element": "Index",
                            "Physical Element Description": "Unique identifier for each row in the dataframe",
                                    "PII_flag": "No"
                                        },
            "Order ID": {
                        "Logical Element": "Order ID",
                                "Physical Element Description": "Unique identifier for each order",
                                        "PII_flag": "No"
                                            },
                "Product": {
                            "Logical Element": "Product",
                                    "Physical Element Description": "Name of the product purchased",
                                            "PII_flag": "No"
                                                },
                    "Quantity Ordered": {
                                "Logical Element": "Quantity Ordered",
                                        "Physical Element Description": "Number of items purchased in an order",
                                                "PII_flag": "No"
                                                    },
                        "Price Each": {
                                    "Logical Element": "Price Each",
                                            "Physical Element Description": "Price of each item purchased in an order",
                                                    "PII_flag": "No"
                                                        },
                            "Order Date": {
                                        "Logical Element": "Order Date",
                                                "Physical Element Description": "Date and time when the order was placed",
                                                        "PII_flag": "No"
                                                            },
                                "Purchase Address": {
                                            "Logical Element": "Purchase Address",
                                                    "Physical Element Description": "Address where the order was shipped to",
                                                            "PII_flag": "Yes"
                                                                },
                                    "Credit Card": {
                                                "Logical Element": "Credit Card",
                                                        "Physical Element Description": "Credit card used to make the purchase",
                                                                "PII_flag": "Yes"
                                                                    },
                                        "SSN": {
                                                    "Logical Element": "SSN",
                                                            "Physical Element Description": "Social Security Number of the customer making the purchase",
                                                                    "PII_flag": "Yes"
                                                                        }
                                        }
                                        ]


@app.route('/', methods=['GET'])
def home():
        return '''<h1>Distant Reading Archive</h1>
        <p>A prototype API for distant reading of science fiction novels.</p>'''


        # A route to return all of the available entries in our catalog.
        @app.route('/api/v1/resources/data/all', methods=['GET'])
        def api_all():
                    return(data1)

                app.run()
