from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    logging.info("Project has started.")
    
    try:
        raise Exception("Custom exception raised on purpose")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)


    return "Hi there! Project working with CI/CD pipelines."


if __name__=="__main__":
    app.run(debug=True)
