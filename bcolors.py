class bcolors:
    # Standard Colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Extended colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'

    @staticmethod
    def color256(fg=None, bg=None):
        if fg is not None and (0 <= fg <= 255):
            fg_color = f'\033[38;5;{fg}m'
        else:
            fg_color = ''
        
        if bg is not None and (0 <= bg <= 255):
            bg_color = f'\033[48;5;{bg}m'
        else:
            bg_color = ''
        return fg_color + bg_color


def print_standard_colors():
    print(bcolors.HEADER + "This is a header" + bcolors.ENDC)
    print(bcolors.OKBLUE + "This text is blue" + bcolors.ENDC)
    print(bcolors.OKCYAN + "This text is cyan" + bcolors.ENDC)
    print(bcolors.OKGREEN + "This text is green" + bcolors.ENDC)
    print(bcolors.WARNING + "This is a warning" + bcolors.ENDC)
    print(bcolors.FAIL + "This indicates a failure" + bcolors.ENDC)
    print(bcolors.BOLD + "This text is bold" + bcolors.ENDC)
    print(bcolors.UNDERLINE + "This text is underlined" + bcolors.ENDC)
    # New colors
    print(bcolors.RED + "This text is red" + bcolors.ENDC)
    print(bcolors.GREEN + "This text is green" + bcolors.ENDC)
    print(bcolors.YELLOW + "This text is yellow" + bcolors.ENDC)
    print(bcolors.BLUE + "This text is blue" + bcolors.ENDC)
    print(bcolors.MAGENTA + "This text is magenta" + bcolors.ENDC)
    print(bcolors.CYAN + "This text is cyan" + bcolors.ENDC)
    print(bcolors.WHITE + "This text is white" + bcolors.ENDC)
    # Bright colors
    print(bcolors.BRIGHT_RED + "This text is bright red" + bcolors.ENDC)
    print(bcolors.BRIGHT_GREEN + "This text is bright green" + bcolors.ENDC)
    print(bcolors.BRIGHT_YELLOW + "This text is bright yellow" + bcolors.ENDC)
    print(bcolors.BRIGHT_BLUE + "This text is bright blue" + bcolors.ENDC)
    print(bcolors.BRIGHT_MAGENTA + "This text is bright magenta" + bcolors.ENDC)
    print(bcolors.BRIGHT_CYAN + "This text is bright cyan" + bcolors.ENDC)
    print(bcolors.BRIGHT_WHITE + "This text is bright white" + bcolors.ENDC)
    # Background colors
    print(bcolors.BG_RED + "This text has a red background" + bcolors.ENDC)
    print(bcolors.BG_GREEN + "This text has a green background" + bcolors.ENDC)
    print(bcolors.BG_YELLOW + "This text has a yellow background" + bcolors.ENDC)
    print(bcolors.BG_BLUE + "This text has a blue background" + bcolors.ENDC)
    print(bcolors.BG_MAGENTA + "This text has a magenta background" + bcolors.ENDC)
    print(bcolors.BG_CYAN + "This text has a cyan background" + bcolors.ENDC)
    print(bcolors.BG_WHITE + "This text has a white background" + bcolors.ENDC)
    # Bright background colors
    print(bcolors.BG_BRIGHT_RED + "This text has a bright red background" + bcolors.ENDC)
    print(bcolors.BG_BRIGHT_GREEN + "This text has a bright green background" + bcolors.ENDC)
    print(bcolors.BG_BRIGHT_YELLOW + "This text has a bright yellow background" + bcolors.ENDC)
    print(bcolors.BG_BRIGHT_BLUE + "This text has a bright blue background" + bcolors.ENDC)
    print(bcolors.BG_BRIGHT_MAGENTA + "This text has a bright magenta background" + bcolors.ENDC)
    print(bcolors.BG_BRIGHT_CYAN + "This text has a bright cyan background" + bcolors.ENDC)
    print(bcolors.BG_BRIGHT_WHITE + "This text has a bright white background" + bcolors.ENDC)

def print_256_colors():
    for i in range(256):
        print(bcolors.color256(fg=i) + f'Color {i}' + bcolors.ENDC, end=' ')
        if (i + 1) % 16 == 0:
            print(' ')

# def print_true_colors():
#     for r in range(0, 256, 51):
#         for g in range(0, 256, 51):
#             for b in range(0, 256, 51):
#                 print(bcolors.true_color(fg=(r, g, b)) + f'RGB({r},{g},{b})' + bcolors.ENDC, end=' ')
#             print()

if __name__ == "__main__":
    print_standard_colors()
    print_256_colors()
    # print_true_colors()
