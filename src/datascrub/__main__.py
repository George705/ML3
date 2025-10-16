import argparse
from .core import process_csv, preview_diff

def main():
    parser = argparse.ArgumentParser(prog="datascrub", description="Mask PII in CSV files.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan", help="Mask a CSV file")
    p_scan.add_argument("input", help="Input CSV path")
    p_scan.add_argument("--out", default="sanitized.csv", help="Output CSV path")
    p_scan.add_argument("--delimiter", default=",", help="CSV delimiter")
    p_scan.add_argument("--dry-run", action="store_true", help="Preview changes without writing output")

    args = parser.parse_args()

    if args.cmd == "scan":
        if args.dry_run:
            diffs = preview_diff(args.input, delimiter=args.delimiter)
            if not diffs:
                print("No PII patterns found.")
            else:
                for row_idx, before, after in diffs:
                    print(f"row {row_idx}: '{before}' -> '{after}'")
        else:
            count = process_csv(args.input, args.out, delimiter=args.delimiter)
            print(f"Masked {count} cell(s). Wrote: {args.out}")

if __name__ == "__main__":
    main()
