import re

paragraph = """Requirement
With current BQ terraform templates, we are unable to manage table level access to user groups on Bigquery. We have only dataset level access.
In our case we have shared Spanner instance. With current Spanner terraform templates, we are unable to manage either database or table level access.

Therefore, we request to enhance Terraform Scripts.

Business - without this upgrade -  We are unable to manage operational / technical level users access. With current situation the datasets & instances are accessible to all users which is not expected as per the regulatory requirements.

Time Criticality : our PR1 release is planned in 1st week of AUG 2024, and without this -it impacts operational users.

Risk Reduction/Opportunity Enablement : NA - This becomes an operational issue if not acted on priority. This is Business critical requirement.

Kindly treat it has priority request and let us know on the timelines.
"""

keywords = ["Bigquery", "Risk Reduction", "Terraform", "Regulatory", "Spanner", "Pubsub", "GCS", "Kubernetes"]


def calculate_risk(results):
    total_words = len(results)
    words_found = sum(results.values())
    percentage = (words_found / total_words) * 100
    risk_rating = "Low" if percentage > 80 else "High"

    return risk_rating

para = paragraph.lower()
results = {word: 0 for word in keywords}

for word in keywords:
    pattern = r'\b' + re.escape(word.lower()) + r'\b'
    if re.search(pattern, para):
        results[word] += 1
risk = calculate_risk(results)
results.update({"risk_rating": risk})
print(results)
