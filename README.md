# tate-rankings
system that can be used in sports rankings, specifically CFB and CBB


API: https://github.com/CFBD/cfbd-python

Order of Operations
Phase 0 — Decide the tech (quick, important)

Lock this in before writing code.

Recommended stack (free + simple)

Language: Python

Data: CollegeFootballData API

Automation: GitHub Actions

Website: GitHub Pages

Output format: rankings.json

You could do this in C++, but Python will save you weeks here.

Phase 1 — Create the repo + website shell

Goal: Get a blank website live.

1. Create GitHub repo

Name it something like:
cfb-rankings

Public repo

2. Enable GitHub Pages

Settings → Pages

Source: main branch

Folder: / (root)

Save

You now have:

https://yourusername.github.io/cfb-rankings/

3. Create a barebones index.html
<!DOCTYPE html>
<html>
<head>
  <title>CFB Rankings</title>
</head>
<body>
  <h1>CFB Rankings</h1>
  <p>Coming soon.</p>
</body>
</html>


Commit → refresh URL → confirm it works
Do not skip this. It proves Pages is wired correctly.

Phase 2 — Get data access (still no rankings yet)

Goal: Prove you can pull live CFB data.

4. Get CollegeFootballData API key

Sign up (free)

Copy API key

5. Store API key securely

Repo → Settings → Secrets → Actions
Add:

CFBD_API_KEY = your_key_here


Never hardcode this.

Phase 3 — Build the data fetcher

Goal: Pull game results from the API.

6. Create project structure
cfb-rankings/
├── index.html
├── rankings.json
├── scripts/
│   └── fetch_games.py
├── requirements.txt

7. Install dependencies (locally)
requests

8. Write fetch_games.py

This script should:

Pull games for current week

Identify:

Teams

Scores

Status (Final)

Output structured Python data

Don’t rank yet. Just fetch.

Run locally → print output → confirm correctness.

Phase 4 — Build your ranking algorithm

Goal: Convert results → rankings.

9. Write generate_rankings.py

This script should:

Load game data

Apply your ranking logic

Output rankings.json

Example structure:

{
  "updated": "2026-09-12T19:48:00Z",
  "rankings": [
    { "rank": 1, "team": "Georgia", "rating": 98.7 },
    { "rank": 2, "team": "Ohio State", "rating": 97.9 }
  ]
}

10. Run locally until stable

You should be able to:

python scripts/generate_rankings.py


and see rankings.json update.

This is the brain of your site — take your time here.

Phase 5 — Display rankings on the site

Goal: Turn JSON into a real website.

11. Update index.html

Fetch rankings.json

Render a table

Display “Last Updated”

Example JS:

fetch("rankings.json?ts=" + Date.now())
  .then(res => res.json())
  .then(data => renderTable(data.rankings));


At this point:

Manual run → commit → refresh page → rankings update

You officially have a rankings website 🎉

Phase 6 — Automate updates (this is the magic)

Goal: Make it update during games.

12. Add GitHub Action

Create:

.github/workflows/update_rankings.yml

13. Action behavior

Runs every 5 minutes

Runs your Python scripts

Commits changes only if rankings changed

Skeleton:

on:
  schedule:
    - cron: "*/5 * * * *"
  workflow_dispatch:


Steps:

Checkout repo

Install Python

Install dependencies

Run ranking script

Commit & push

Phase 7 — Optimize & protect free limits

Goal: Don’t waste runs.

14. Detect “no changes”

Your script should:

Compare previous rankings

Exit without writing if unchanged

This keeps GitHub Actions fast and free forever.

Phase 8 — Make it feel live

Goal: User experience polish.

15. Frontend auto-refresh

Poll rankings.json every 30 seconds

Cache-bust with timestamp

16. Add UI details

▲ ▼ movement from last update

Record

Strength of schedule

“Games currently in progress”

This is where it starts looking legit.

Phase 9 — Saturday-ready workflow

Goal: Control when things run.

You’ll have:

Auto updates every 5 min

Manual “Run Now” button in GitHub Actions