"""Split a 2x2 multiview PNG into deterministic per-view PNGs."""
from pathlib import Path
import argparse
from PIL import Image

VIEWS = ("front", "left", "right", "behind")

def split_one(path: Path, out_dir: Path | None = None) -> list[Path]:
    out_dir = out_dir or path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    with Image.open(path) as im:
        w, h = im.size
        boxes = ((0, 0, w // 2, h // 2), (w // 2, 0, w, h // 2),
                 (0, h // 2, w // 2, h), (w // 2, h // 2, w, h))
        stem = path.stem.removesuffix("-멀티뷰")
        outputs = []
        for view, box in zip(VIEWS, boxes):
            target = out_dir / f"{stem}-{view}.png"
            im.crop(box).save(target, "PNG")
            outputs.append(target)
    return outputs

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--out-dir", type=Path)
    args = parser.parse_args()
    outputs = [p for src in args.inputs for p in split_one(src, args.out_dir)]
    print(f"exported {len(outputs)} files")

if __name__ == "__main__":
    main()
