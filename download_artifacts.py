import re
import requests

artifacts = requests.get("https://api.github.com/repos/QubitPi/hadoop/actions/artifacts").json()["artifacts"]
for artifact in artifacts:
    if re.match("QubitPi~hadoop~.*.dockerbuild", artifact["name"]):
        run_id = artifact["workflow_run"]["id"]
        artifact_id = artifact["id"]
        print(f"https://github.com/QubitPi/hadoop/actions/runs/{run_id}/artifacts/{artifact_id}")
