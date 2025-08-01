from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
DB_HOST = 'localhost'
DB_NAME = 'students'
DB_USER = 'postgres'
DB_PASS = 'bhavana17'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    hall_ticket_no = request.form['hall_ticket_no']
    student_name=request.form['student_name']
    branch = request.form['branch']
    year = request.form['year']
    semester = request.form['semester']
    appeared = request.form['appeared']
    academic_year=request.form['academic_year']
    attempt_type = request.form['attempt_type']

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT subjects,marks, results, Grade, attempt_type
        FROM students_info
        WHERE hall_ticket_no = %s AND branch = %s AND year = %s AND semester = %s AND appeared = %s AND attempt_type = %s
    """, (hall_ticket_no, branch, year, semester, appeared, attempt_type))

    results = cur.fetchall()
    cur.close()
    conn.close()

    failed_subjects = [row for row in results if row[2].lower() == 'fail']

    return render_template('result.html',
                       hall_ticket_no=hall_ticket_no,
                       student_name=student_name,
                       branch=branch,
                       year=year,
                       semester=semester,
                       appeared=appeared,
                       academic_year=academic_year,
                       attempt_type=attempt_type,
                       results=results,
                       failed_subjects=failed_subjects,
                       has_failed=bool(failed_subjects))  # NEW FLAG


@app.route('/refresh', methods=['GET'])
def refresh():
    return redirect(url_for('index'))


@app.route('/reappear', methods=['POST'])
def reappear():
    subjects = request.form['subjects']
    academic_year = request.form['academic_year']
    attempt_type = request.form['attempt_type']

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT subjects, marks, results, Grade, attempt_type
        FROM students_info
        WHERE subjects = %s AND academic_year = %s AND attempt_type = %s
    """, ( subjects, academic_year, attempt_type))

    results = cur.fetchall()
    cur.close()
    conn.close()

    if not results:
        return f"❌ No reappear results found for subject: {subjects}, year: {academic_year}, attempt: {attempt_type}"
    
    return render_template('memo.html',
                                   subjects=subjects,
                                   academic_year=academic_year,
                                   attempt_type=attempt_type,
                                   results=results,  # ✅ Correct: pass all results
                                   failed_subjects=[])
                                
if __name__ == '__main__':
    try:
        conn = get_db_connection()
        conn.close()
        print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed:", e)
    app.run(host='0.0.0.0', port=1000, debug=True)

