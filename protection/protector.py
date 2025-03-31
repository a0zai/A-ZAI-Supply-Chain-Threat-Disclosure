import os
import re

SUSPICIOUS_PATTERNS = [
    r"a0z-\w{2,5}",
    r"socket\.socket\(",
    r"base64\.b64encode",
    r"Fernet\(",
    r"sendall\("
]

def scan_files():
    infected = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(('.py', '.js', '.json', '.html', '.md')):
                try:
                    with open(os.path.join(root, file), "r", errors="ignore") as f:
                        content = f.read()
                        for pattern in SUSPICIOUS_PATTERNS:
                            if re.search(pattern, content):
                                infected.append(os.path.join(root, file))
                                break
                except:
                    continue
    return infected

if __name__ == "__main__":
    results = scan_files()
    if results:
        print("⚠️ Potential malicious patterns found:")
        for r in results:
            print(f" - {r}")
    else:
        print("✅ No suspicious patterns detected.")
