import os
import re

PATTERNS = [r"a0z-\w{2,5}"]

def collect_fragments():
    fragments = []
    for root, dirs, files in os.walk("."):
        for name in dirs + files:
            for pattern in PATTERNS:
                if re.search(pattern, name):
                    fragments.append(name)
    return fragments

if __name__ == "__main__":
    keys = collect_fragments()
    print(f"🔑 Collected Fragments: {keys}")
