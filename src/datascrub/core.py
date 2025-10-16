from typing import List, Tuple
import csv
from .patterns import mask_all

def process_csv(in_path: str, out_path: str, delimiter: str = ",") -> int:
    masked_cells = 0
    with open(in_path, newline="", encoding="utf-8") as f_in, open(out_path, "w", newline="", encoding="utf-8") as f_out:
        reader = csv.reader(f_in, delimiter=delimiter)
        writer = csv.writer(f_out, delimiter=delimiter)
        for row in reader:
            new_row = []
            for cell in row:
                masked = mask_all(cell)
                if masked != cell:
                    masked_cells += 1
                new_row.append(masked)
            writer.writerow(new_row)
    return masked_cells

def preview_diff(in_path: str, delimiter: str = ",", max_rows: int = 10) -> List[Tuple[int, str, str]]:
    diffs: List[Tuple[int, str, str]] = []
    with open(in_path, newline="", encoding="utf-8") as f_in:
        reader = csv.reader(f_in, delimiter=delimiter)
        for i, row in enumerate(reader):
            masked_row = [mask_all(c) for c in row]
            for before, after in zip(row, masked_row):
                if before != after:
                    diffs.append((i, before, after))
                    if len(diffs) >= max_rows:
                        return diffs
    return diffs
