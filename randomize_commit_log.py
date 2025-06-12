import random

# Read all lines from commit.log
with open('commit.log', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

# Select 15 random lines
selected = random.sample(lines, min(15, len(lines)))

# Overwrite commit.log with the selected lines
with open('commit.log', 'w') as f:
    for line in selected:
        f.write(line + '\n')

print(f"commit.log updated with {len(selected)} random dates.") 