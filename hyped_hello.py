import sys, time, random, os, math

def rgb(r,g,b): return f"\033[38;2;{r};{g};{b}m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_write(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def rainbow_line(text):
    out = ""
    for i, ch in enumerate(text):
        r = int(128 + 127 * (1 + math.sin(i / max(1, len(text)) * 2 * math.pi)))
        g = int(128 + 127 * (1 + math.sin((i / max(1, len(text))) * 2 * math.pi + 2)))
        b = int(128 + 127 * (1 + math.sin((i / max(1, len(text))) * 2 * math.pi + 4)))
        out += f"{rgb(r,g,b)}{ch}"
    out += RESET
    print(out)

def confetti(duration=1.2, density=60):
    cols = max(40, min(120, os.get_terminal_size().columns))
    end = time.time() + duration
    while time.time() < end:
        line = []
        for _ in range(min(density, cols)):
            ch = random.choice("•∙●✦✶*")
            r,g,b = [random.randint(50,255) for _ in range(3)]
            line.append(f"{rgb(r,g,b)}{ch}{RESET}")
        print("".join(line))
        time.sleep(0.08)

if __name__ == "__main__":
    print(BOLD + rgb(255,165,0) + "\n=== HYPED HELLO WORLD ===" + RESET + "\n")
    confetti(0.8, density=30)
    type_write("Loading hype engine...", 0.03)
    time.sleep(0.4)
    type_write("Initializing colors...", 0.03)
    time.sleep(0.4)
    rainbow_line("HELLO, WORLD!")
    confetti(0.9, density=45)
    print(BOLD + rgb(100,255,180) + "\n— done. stay curious." + RESET + "\n")
