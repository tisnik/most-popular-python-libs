import tarfile
import json
import csv


# magic file that should be stored in a tarball
TOPLEVEL_MAGIC_FILE = "openshift_lightspeed.json"

# directory within tarball with user feedback files
FEEDBACK_DIRECTORY = "feedback/"


def read_feedbacks_from_tarball(tarball):
    """Read feedbacks from tarball, skip over errors."""
    feedbacks = []
    for filename in tarball.getnames():
        if filename.startswith(FEEDBACK_DIRECTORY):
            try:
                f = tarball.extractfile(filename)
                data = f.read().decode("UTF-8")
                feedbacks.append(json.loads(data))
            except Exception as e:
                print(f"Unable to read feedback: {e}")

    return feedbacks


def feedbacks_from_tarball(tarball_name):
    """Retrieve all feedbacks from tarball."""
    tarball = tarfile.open(tarball_name, "r:gz")
    filelist = tarball.getnames()

    # check if the tarball seems to be correct one
    if TOPLEVEL_MAGIC_FILE not in filelist:
        print(f"Incorrect tarball: missing {TOPLEVEL_MAGIC_FILE}")
        return []

    feedbacks = read_feedbacks_from_tarball(tarball)

    if len(feedbacks) == 0:
        print("Tarball does not contain any feedback.")

    return feedbacks


def aggregate_csv():
    with open("output.csv", "w") as csvfile:
        filewriter = csv.writer(
            csvfile,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        filewriter.writerow(
            [
                "User ID",
                "Conversation ID",
                "Question",
                "LLM response",
                "Sentiment",
                "Feedback",
            ]
        )

        feedbacks = feedbacks_from_tarball("ols.tgz")
        for feedback in feedbacks:
            filewriter.writerow(
                [
                    feedback["user_id"],
                    feedback["conversation_id"],
                    feedback["user_question"],
                    feedback["llm_response"],
                    feedback["sentiment"],
                    feedback["user_feedback"],
                ]
            )


aggregate_csv()
