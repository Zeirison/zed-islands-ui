"""Generate the Islands UI icon theme from IntelliJ's new UI icons.

Usage: python3 scripts/build_icon_theme.py <intellij-community checkout> <repo root>

The icons come from JetBrains/intellij-community (Apache-2.0). Each one ships a
light variant (`name.svg`) and a dark variant (`name_dark.svg`).
"""
import json, shutil, sys
from pathlib import Path

EXPUI = "platform/icons/src/expui"
FILE_TYPES = f"{EXPUI}/fileTypes"
NODES = f"{EXPUI}/nodes"
KOTLIN = "plugins/kotlin/base/resources/resources/org/jetbrains/kotlin/idea/icons/expui"
PYTHON = "python/python-parser/resources/icons/com/jetbrains/python/parser/expui"

# Zed icon key -> source icon (without the .svg / _dark.svg suffix).
# Keys that Zed already knows keep its suffix mapping; new keys are added to
# FILE_SUFFIXES and FILE_STEMS below.
FILE_ICONS = {
    "default": f"{FILE_TYPES}/anyType",
    "c": f"{FILE_TYPES}/c",
    "cpp": f"{FILE_TYPES}/cpp",
    "c_header": f"{FILE_TYPES}/h",
    "csharp": f"{FILE_TYPES}/Csharp",
    "css": f"{FILE_TYPES}/css",
    "sass": f"{FILE_TYPES}/css",
    "csv": f"{FILE_TYPES}/csv",
    "diff": f"{FILE_TYPES}/patch",
    "docker": f"{FILE_TYPES}/docker",
    "editorconfig": f"{FILE_TYPES}/editorConfig",
    "font": f"{FILE_TYPES}/font",
    "git": f"{FILE_TYPES}/ignored",
    "gradle": f"{FILE_TYPES}/gradle",
    "graphql": f"{FILE_TYPES}/graphql",
    "groovy": f"{FILE_TYPES}/groovy",
    "html": f"{FILE_TYPES}/html",
    "http": f"{FILE_TYPES}/http",
    "image": f"{FILE_TYPES}/image",
    "ipynb": f"{FILE_TYPES}/jupyter",
    "java": f"{FILE_TYPES}/java",
    "java_class": f"{FILE_TYPES}/javaClass",
    "javascript": f"{FILE_TYPES}/javaScript",
    "json": f"{FILE_TYPES}/json",
    "kotlin": f"{KOTLIN}/kotlin",
    "kotlin_script": f"{KOTLIN}/kotlinScript",
    "kotlin_gradle": f"{KOTLIN}/kotlinGradleScript",
    "log": f"{FILE_TYPES}/text",
    "manifest": f"{FILE_TYPES}/manifest",
    "markdown": f"{FILE_TYPES}/markdown",
    "perl": f"{FILE_TYPES}/perl",
    "php": f"{EXPUI}/language/php",
    "properties": f"{FILE_TYPES}/properties",
    "python": f"{PYTHON}/python",
    "regexp": f"{FILE_TYPES}/regexp",
    "rst": f"{FILE_TYPES}/rst",
    "scala": f"{EXPUI}/language/scala",
    "settings": f"{FILE_TYPES}/config",
    "sql": f"{FILE_TYPES}/sql",
    "swift": f"{FILE_TYPES}/swiftLang",
    "template": f"{FILE_TYPES}/xml",
    "terminal": f"{FILE_TYPES}/shell",
    "terraform": f"{FILE_TYPES}/terraform",
    "text": f"{FILE_TYPES}/text",
    "toml": f"{FILE_TYPES}/toml",
    "typescript": f"{FILE_TYPES}/typeScript",
    "archive": f"{FILE_TYPES}/archive",
    "binary": f"{FILE_TYPES}/binaryData",
    "windows": f"{FILE_TYPES}/microsoftWindows",
    "xsd": f"{FILE_TYPES}/xsd",
    "yaml": f"{FILE_TYPES}/yaml",
}

FILE_SUFFIXES = {
    "h": "c_header", "hpp": "c_header", "hh": "c_header", "hxx": "c_header",
    "csv": "csv", "tsv": "csv",
    "gradle": "gradle", "groovy": "groovy", "gvy": "groovy",
    "http": "http", "rest": "http",
    "png": "image", "jpg": "image", "jpeg": "image", "gif": "image", "webp": "image",
    "bmp": "image", "ico": "image", "svg": "image", "tiff": "image", "avif": "image",
    "class": "java_class",
    "kts": "kotlin_script", "gradle.kts": "kotlin_gradle",
    "mf": "manifest",
    "pl": "perl", "pm": "perl",
    "properties": "properties", "env": "properties",
    "rst": "rst",
    "sql": "sql",
    "txt": "text",
    "zip": "archive", "jar": "archive", "tar": "archive", "gz": "archive",
    "tgz": "archive", "7z": "archive", "rar": "archive", "xz": "archive",
    "bin": "binary", "exe": "windows", "dll": "windows", "bat": "windows", "cmd": "windows",
    "xsd": "xsd",
    "gitignore": "git", "gitattributes": "git", "gitmodules": "git", "dockerignore": "docker",
}

FILE_STEMS = {}

DIRECTORY = f"{NODES}/folder"
NAMED_DIRECTORIES = {
    ".github": f"{NODES}/folderGithub",
    "src": f"{NODES}/sourceRoot",
    "lib": f"{NODES}/sourceRoot",
    "test": f"{NODES}/testRoot",
    "tests": f"{NODES}/testRoot",
    "spec": f"{NODES}/testRoot",
    "resources": f"{NODES}/resourcesRoot",
    "assets": f"{NODES}/resourcesRoot",
    "target": f"{NODES}/excludeRoot",
    "build": f"{NODES}/excludeRoot",
    "dist": f"{NODES}/excludeRoot",
    "out": f"{NODES}/excludeRoot",
    "node_modules": f"{NODES}/excludeRoot",
    ".idea": f"{NODES}/excludeRoot",
    "docs": f"{NODES}/javaDocFolder",
    "logs": f"{NODES}/logFolder",
}

CHEVRON_COLLAPSED = f"{EXPUI}/general/chevronRight"
CHEVRON_EXPANDED = f"{EXPUI}/general/chevronDown"


def main(source_root: Path, repo_root: Path):
    icons_dir = repo_root / "icons"
    if icons_dir.exists():
        shutil.rmtree(icons_dir)

    def icon(source: str, mode: str) -> str:
        name = Path(source).name
        suffix = "_dark" if mode == "dark" else ""
        src = source_root / f"{source}{suffix}.svg"
        if not src.exists():
            src = source_root / f"{source}.svg"
        dest = icons_dir / mode / f"{name}.svg"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        return f"./icons/{mode}/{name}.svg"

    themes = []
    for mode in ("dark", "light"):
        folder = icon(DIRECTORY, mode)
        themes.append({
            "name": f"Islands UI Icons {mode.title()}",
            "appearance": mode,
            "directory_icons": {"collapsed": folder, "expanded": folder},
            "named_directory_icons": {
                name: {"collapsed": icon(path, mode), "expanded": icon(path, mode)}
                for name, path in NAMED_DIRECTORIES.items()
            },
            "chevron_icons": {
                "collapsed": icon(CHEVRON_COLLAPSED, mode),
                "expanded": icon(CHEVRON_EXPANDED, mode),
            },
            "file_stems": FILE_STEMS,
            "file_suffixes": FILE_SUFFIXES,
            "file_icons": {key: {"path": icon(path, mode)} for key, path in FILE_ICONS.items()},
        })

    out = {
        "$schema": "https://zed.dev/schema/icon_themes/v0.3.0.json",
        "name": "Islands UI Icons",
        "author": "Dmytro (icons from JetBrains IntelliJ Platform, Apache-2.0)",
        "themes": themes,
    }
    dest = repo_root / "icon_themes" / "islands-ui-icons.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print("wrote", dest, "and", sum(1 for _ in icons_dir.rglob("*.svg")), "icons")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
