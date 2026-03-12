import re

with open("build_map.py", "r", encoding="utf-8") as f:
    content = f.read()

# Pattern 1: f"{W}/thumb/X/XX/FILENAME/800px-FILENAME" -> f"{T}FILENAME"
# Matches: f"{W}/thumb/a/a2/Some_File.jpg/800px-Some_File.jpg"
def replace_thumb(m):
    filename = m.group(1)
    return f'f"{{T}}{filename}"'

content = re.sub(
    r'f"\{W\}/thumb/[a-f0-9]/[a-f0-9]{2}/([^/]+)/800px-[^"]*"',
    replace_thumb,
    content
)

# Pattern 2: f"{W}/X/XX/FILENAME" (no thumb) -> f"{T}FILENAME"
def replace_direct(m):
    filename = m.group(1)
    return f'f"{{T}}{filename}"'

content = re.sub(
    r'f"\{W\}/[a-f0-9]/[a-f0-9]{2}/([^"]+)"',
    replace_direct,
    content
)

with open("build_map.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Done - all URLs converted to thumb.php format")
