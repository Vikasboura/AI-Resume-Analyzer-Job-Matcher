from flask import Flask, request
from resume_parser import extract_resume_text
from job_parser import extract_job_text
from matcher import compute_similarity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume = request.files["resume"]
        job = request.files["job"]

        resume_text = extract_resume_text(resume)
        job_text = extract_job_text(job)

        score = compute_similarity(resume_text, job_text)
        return f"<h2>Match Score: {round(score * 100, 2)}%</h2>"

    return '''
    <form method="POST" enctype="multipart/form-data">
        <h2>AI Resume Matcher</h2>
        Resume (PDF): <input type="file" name="resume"><br><br>
        Job Description (TXT): <input type="file" name="job"><br><br>
        <input type="submit" value="Check Match">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
