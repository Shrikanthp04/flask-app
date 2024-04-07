from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    marks = {}
    if request.method == 'POST':
        subjects = ['First Language', 'Second Language', 'Third Language', 'Mathematics', 'Science', 'Social']
        for subject in subjects:
            marks[subject] = float(request.form[subject])

    total_marks = round(sum(marks.values()),2)
    percentage = round((sum(marks.values())/625)*100,2)
    return render_template('results.html', res=marks, percentage=percentage, total_marks=total_marks)


if __name__=='__main__':
    app.run(debug=True)