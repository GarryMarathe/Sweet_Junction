from flask import Flask, render_template,request,redirect,flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt



app = Flask(__name__ ,static_folder='static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/SweetJunction"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/' , methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/details' , methods=["GET"])
def detail():
    return render_template("details.html")

@app.route('/aboutus' , methods=["GET"])
def about():
    return render_template("aboutus.html")

@app.route('/homepage.html' , methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route('/order' , methods=["GET","POST"])
def order():
    #bussiness logic
    if request.method == "POST":
        print("it's a post call")



        full_name = request.form["Full_name"]
        address = request.form["address"]
        landmark = request.form["landmark"]
        gender = request.form["gender"]
        contact = request.form["contact"]
        email = request.form["email"]
        sweet_name = request.form["sweet_name"]
        quantity = request.form["quantity"]
        issue_date = request.form["issue_date"]
        delivery_date = request.form["delivery_date"]
        

        mongo.db.junc.insert_one(

            {
                "Full_name": full_name,
                "address": address,
                "landmark": landmark,
                "gender": gender,
                "contact": contact,
                "email": email,
                "sweet_name": sweet_name,
                "quantity": quantity,
                "issue_date": issue_date,
                "delivery_date": delivery_date,
            }
        )


        flash("Order Placed Successfully" , "success")
        #return redirect("/order")

    return render_template("order.html")

    

if __name__=="__main__":
    app.secret_key = "asdkjsse"
    app.run(debug=True , port=8000)

        

