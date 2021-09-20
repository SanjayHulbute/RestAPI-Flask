from flask import Flask, jsonify
app = Flask(__name__)

educational_qualifications = [
   {
          "Degree": "B-TECH",
          "Insitute Name": "MIT Academy of Engineering",
          "University": "SPPU",
          "Percentage": "70.13"
        },
        {
          "Degree": "DIPLOMA",
          "Insitute Name": "SES Polytechnic Solapur",
          "University": "MSBTE",
          "Percentage": "81.06"
        },
        {
          "Degree": "SSC",
          "Insitute Name": "SVCS Highschool MIDC Solapur",
          "University": "State Board",
          "Percentage": "82.20"
        }
]

@app.route('/educational_qualifications')
def get_educational_qualifications():
  return jsonify(educational_qualifications)

    
if __name__ == "__main__":
    app.run(debug=True)