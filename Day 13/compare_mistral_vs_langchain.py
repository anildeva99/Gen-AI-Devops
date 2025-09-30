# ===========================
# Utility: Print Side by Side
# ===========================
def print_side_by_side(raw_output, lc_output):
    """Print two outputs side by side in columns"""
    terminal_width = shutil.get_terminal_size((160, 20)).columns
    col_width = terminal_width // 2 - 4

    raw_output = raw_output.replace("\n", "\n\n")
    lc_output = lc_output.replace("\n", "\n\n")

    raw_lines = textwrap.wrap(raw_output, col_width)
    lc_lines = textwrap.wrap(lc_output, col_width)

    max_lines = max(len(raw_lines), len(lc_lines))
    raw_lines += [""] * (max_lines - len(raw_lines))
    lc_lines += [""] * (max_lines - len(lc_lines))

    print(f"{YELLOW}{'Raw Mistral API'.ljust(col_width)}{RESET} || "
          f"{GREEN}{'LangChain + Mistral'.ljust(col_width)}{RESET}")
    print("─" * terminal_width)

    for r, l in zip(raw_lines, lc_lines):
        print(f"{YELLOW}{r.ljust(col_width)}{RESET} || {GREEN}{l.ljust(col_width)}{RESET}")

    print("\n" + "═" * terminal_width + "\n")

# ===========================
# Interactive Loop
# ===========================
print(f"{CYAN}🤖 Compare Raw Mistral vs LangChain+Mistral (memory only, type 'exit' to quit){RESET}\n")

while True:
    user_input = input(f"{CYAN}You: {RESET}")
    if user_input.lower() in ["exit", "quit", "q"]:
        print(f"{CYAN}Goodbye {RESET}")
        break

    raw_output = mistral_raw_call(user_input)
    lc_output = mistral_langchain_call(user_input)

    print_side_by_side(raw_output, lc_output)
