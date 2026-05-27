#!/usr/bin/env python3
"""
generate_readme.py
Regenerates the mastery table in README.md from progress/mastery.json.
Run this after any session, or let the coach run it automatically during Phase 4.

Usage:
    python generate_readme.py
"""

import json
import re
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).parent
MASTERY_FILE = REPO_ROOT / "progress" / "mastery.json"
STREAK_FILE  = REPO_ROOT / "progress" / "streak.json"
README_FILE  = REPO_ROOT / "README.md"
LOGS_DIR     = REPO_ROOT / "logs"

TOPIC_LABELS = {
    "algebra":              "Algebra (equations, exponents, radicals)",
    "functions_graphs":     "Functions & graphs (domain, range, transforms)",
    "composition_inverses": "Composition & inverses",
    "trigonometry":         "Trigonometry (unit circle, identities)",
    "exponentials_logs":    "Exponentials & logarithms",
    "limits_intuition":     "Limits intuition & behavior",
}

PRIORITY_THRESHOLD = {
    "high":   (0, 5),
    "medium": (5, 7),
    "low":    (7, 11),
}

def priority_label(score: int) -> str:
    if score < 5:
        return "🔴 High"
    elif score < 7:
        return "🟡 Medium"
    else:
        return "🟢 Low"

def last_studied(topic_id: str) -> str:
    """Find the most recent log that mentions this topic."""
    logs = sorted(LOGS_DIR.glob("*.md"), reverse=True)
    for log in logs:
        content = log.read_text()
        # Match "**Topic:** <anything containing the topic id or label>"
        if topic_id.replace("_", " ") in content.lower() or topic_id in content.lower():
            # Extract date from filename YYYY-MM-DD-NN.md
            parts = log.stem.split("-")
            if len(parts) >= 3:
                return f"{parts[0]}-{parts[1]}-{parts[2]}"
    return "—"

def build_mastery_table(mastery: dict) -> str:
    lines = [
        "| Topic | Mastery (0–10) | Last Studied | Priority |",
        "|---|---|---|---|",
    ]
    for topic_id, score in mastery["topics"].items():
        label      = TOPIC_LABELS.get(topic_id, topic_id)
        studied    = last_studied(topic_id)
        priority   = priority_label(score)
        lines.append(f"| {label} | {score} | {studied} | {priority} |")
    return "\n".join(lines)

def build_status_block(mastery: dict, streak: dict) -> str:
    total_sessions = streak.get("total_sessions", 0)
    total_minutes  = streak.get("total_minutes", 0)
    current_streak = streak.get("current_streak_days", 0)
    last_session   = streak.get("last_session_date") or "—"
    avg_score      = sum(mastery["topics"].values()) / len(mastery["topics"])
    return (
        f"- **Readiness score:** 5/12 (May 25, 2026 diagnostic)\n"
        f"- **Average mastery:** {avg_score:.1f}/10\n"
        f"- **Sessions completed:** {total_sessions}\n"
        f"- **Total study time:** {total_minutes} minutes\n"
        f"- **Current streak:** {current_streak} day(s)\n"
        f"- **Last session:** {last_session}\n"
        f"- **Target:** Calc 1 ready at Coastline Community College\n"
        f"- **Overall goal:** Physics B.S. pathway → CSUSM / ASU transfer"
    )

def update_readme(mastery: dict, streak: dict):
    readme = README_FILE.read_text()

    # Replace the Current Status block
    status_block = build_status_block(mastery, streak)
    readme = re.sub(
        r"(## Current Status\n\n).*?(\n\n---)",
        rf"\1{status_block}\2",
        readme,
        flags=re.DOTALL,
    )

    # Replace the Topic Mastery table
    mastery_table = build_mastery_table(mastery)
    readme = re.sub(
        r"(## Topic Mastery\n\n).*?(\n\n> )",
        rf"\1{mastery_table}\2",
        readme,
        flags=re.DOTALL,
    )

    README_FILE.write_text(readme)
    print(f"✅ README.md updated (avg mastery: {sum(mastery['topics'].values()) / len(mastery['topics']):.1f}/10)")

def main():
    mastery = json.loads(MASTERY_FILE.read_text())
    streak  = json.loads(STREAK_FILE.read_text())
    update_readme(mastery, streak)

if __name__ == "__main__":
    main()
