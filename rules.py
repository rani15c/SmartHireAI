def evaluate_candidate(qualification, experience, specialization):
    score = 0
    reasons = []

    # Rule 1: Qualification
    qualification_scores = {
        "Ph.D": 40,
        "M.Tech": 35,
        "M.E": 35,
        "M.Sc": 25,
        "B.Tech": 20
    }

    if qualification in qualification_scores:
        score += qualification_scores[qualification]
        reasons.append(
            f"{qualification} qualification is considered suitable."
        )
    else:
        reasons.append("Qualification does not meet the preferred criteria.")

    # Rule 2: Experience
    if experience >= 5:
        score += 30
        reasons.append("Candidate has strong teaching/industry experience.")
    elif experience >= 2:
        score += 25
        reasons.append("Candidate has the required experience.")
    elif experience >= 1:
        score += 15
        reasons.append("Candidate has some relevant experience.")
    else:
        reasons.append("More experience is preferred.")

    # Rule 3: Specialization
    valid_specializations = [
        "Artificial Intelligence",
        "Machine Learning",
        "Computer Science",
        "Data Science",
        "Information Technology"
    ]

    if specialization in valid_specializations:
        score += 30
        reasons.append(
            "Specialization matches the college requirement."
        )
    else:
        reasons.append(
            "Specialization does not directly match the current requirement."
        )

    # Forward chaining conclusion
    if score >= 80:
        status = "Highly Recommended"
    elif score >= 65:
        status = "Recommended"
    elif score >= 50:
        status = "Review Required"
    else:
        status = "Not Recommended"

    return score, status, reasons