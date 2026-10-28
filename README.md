# Islands UI for Zed

Dark and light Zed themes that use the colors of the **Islands** UI from
IntelliJ-based IDEs (IntelliJ IDEA, PyCharm, RustRover, and others).

- **Islands UI Dark**: the "Islands Dark" UI theme plus its editor color scheme.
- **Islands UI Light**: the "Islands Light" UI theme plus the "Light" editor color scheme.

Colors are read from JetBrains' Apache-2.0 sources and mapped onto Zed's theme
tokens by `scripts/build_theme.py`. See [NOTICE](NOTICE) for attribution.

## Install (dev extension)

1. Clone this repository.
2. In Zed, open the command palette and run `zed: install dev extension`.
3. Pick the cloned folder, then select **Islands UI Dark** or **Islands UI Light**
   with `theme selector: toggle`.

## Settings for a closer match

Add to your Zed `settings.json`:

```jsonc
{
  "theme": { "mode": "system", "dark": "Islands UI Dark", "light": "Islands UI Light" },
  "ui_font_family": "Inter",
  "ui_font_size": 13,
  "buffer_font_family": "JetBrains Mono",
  "buffer_font_size": 13,
  "buffer_line_height": { "custom": 1.4 },
  "tab_bar": { "show_nav_history_buttons": false },
  "project_panel": { "indent_size": 16 },
  "scrollbar": { "show": "auto" }
}
```

## What a theme cannot do

Zed themes only set colors. The rounded panels separated by gaps that define
the Islands look need a change to Zed itself. The theme gets part of the way
there: window chrome and the borders between panels use the darker "gap" color,
while panels and the editor use the lighter "island" color.

A prototype of the layout change lives in a Zed fork on the `islands-layout`
branch. It adds this setting:

```jsonc
"islands": { "enabled": true, "gap": 6, "corner_radius": 10 }
```

## Regenerating the theme

```sh
python3 scripts/build_theme.py themes/islands-ui.json
```

## License

Apache-2.0. Not affiliated with or endorsed by JetBrains.
