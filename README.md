# Islands UI for Zed

Dark and light Zed themes that use the colors of the **Islands** UI from
IntelliJ-based IDEs (IntelliJ IDEA, PyCharm, RustRover, and others).

- **Islands UI Dark**: the "Islands Dark" UI theme plus its editor color scheme.
- **Islands UI Light**: the "Islands Light" UI theme plus the "Light" editor color scheme.

- **Islands UI Icons Dark / Light**: an icon theme with IDEA's new UI file and
  folder icons. Folders named `src`, `test`, `resources`, `target`, `build`,
  `node_modules` and similar get IDEA's source, test, resource and excluded
  folder colors.

Colors are read from JetBrains' Apache-2.0 sources and mapped onto Zed's theme
tokens by `scripts/build_theme.py`. See [NOTICE](NOTICE) for attribution.

![Islands UI Dark with the islands layout](screenshots/islands-dark.png)

## Install (dev extension)

1. Clone this repository.
2. In Zed, open the command palette and run `zed: install dev extension`.
3. Pick the cloned folder, then select **Islands UI Dark** or **Islands UI Light**
   with `theme selector: toggle`, and **Islands UI Icons Dark** or
   **Islands UI Icons Light** with `icon theme selector: toggle`.

Icons cover the file types IDEA ships under Apache-2.0 (Java, Kotlin, Python,
JavaScript, TypeScript, C/C++, C#, PHP, Scala, Swift, web, config and data
files). Languages whose IDEA icons are not open source, such as Rust, Go and
Ruby, keep Zed's default icons.

## Settings for a closer match

Add to your Zed `settings.json`:

```jsonc
{
  "theme": { "mode": "system", "dark": "Islands UI Dark", "light": "Islands UI Light" },
  "icon_theme": { "mode": "system", "dark": "Islands UI Icons Dark", "light": "Islands UI Icons Light" },
  "ui_font_family": "Inter",
  "ui_font_size": 13,
  "buffer_font_family": "JetBrains Mono",
  "buffer_font_size": 13,
  "buffer_line_height": { "custom": 1.4 },
  "tab_bar": { "show_nav_history_buttons": false },
  "tabs": { "file_icons": true, "git_status": true },
  "project_panel": { "indent_size": 16 },
  "scrollbar": { "show": "auto" }
}
```

## What a theme cannot do

Zed themes only set colors. The rounded panels separated by gaps that define
the Islands look need a change to Zed itself. The theme gets part of the way
there: window chrome and the borders between panels use the darker "gap" color,
while panels and the editor use the lighter "island" color.

A prototype of the layout change lives on the `islands-layout` branch of
[Zeirison/zed](https://github.com/Zeirison/zed/tree/islands-layout). It draws
the editor and docks as rounded islands, editor tabs as pills, and project
panel rows as inset rounded highlights. Enable it with:

```jsonc
"islands": { "enabled": true, "gap": 6, "corner_radius": 10 }
```

## Regenerating the theme

```sh
python3 scripts/build_theme.py themes/islands-ui.json
python3 scripts/build_icon_theme.py /path/to/intellij-community .
```

## License

Apache-2.0. Not affiliated with or endorsed by JetBrains.
