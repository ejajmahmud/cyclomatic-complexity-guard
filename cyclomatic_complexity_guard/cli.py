"""CLI for cyclomatic-complexity-guard."""
import sys
import argparse
from .guard import ComplexityGuard


def main():
    parser = argparse.ArgumentParser(description="Cyclomatic Complexity Guard")
    parser.add_argument("--demo", action="store_true", help="Run complexity analysis demonstration")
    args = parser.parse_args()

    guard = ComplexityGuard()
    if args.demo:
        complex_code = """def deeply_nested(x, y, z):
    if x > 0:
        if y > 0:
            for i in range(10):
                if z and i % 2 == 0:
                    return True
    return False
"""
        report = guard.analyze_source(complex_code, max_allowed=3)
        print("Complexity Report:", report)
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
