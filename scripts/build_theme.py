"""Generate the Islands Zed theme from IntelliJ Islands palette values.

Source values come from JetBrains/intellij-community (Apache-2.0):
  platform/platform-resources/src/themes/islands/ManyIslandsDark.theme.json
  platform/platform-resources/src/themes/islands/ManyIslandsLight.theme.json
  platform/platform-resources/src/themes/islands/IslandSchemeDark.xml
  platform/platform-resources/src/themes/expUI/expUI_lightScheme.xml
"""
import json, sys

def a(hex6, alpha="ff"):
    h = hex6.lstrip("#").lower()
    return "#" + (h if len(h) == 8 else h + alpha)

def style(color, italic=False, bold=False, **kw):
    s = {"color": a(color)}
    if italic: s["font_style"] = "italic"
    if bold: s["font_weight"] = 700
    s.update(kw)
    return s

PAL = {
  "dark": dict(
    gap="#26282C", island="#191A1C", island_inline="#212326", popup="#26282C",
    border="#26282C", border_strong="#33353B", control_border="#40434A",
    text="#D1D3D9", editor_text="#BCBEC4", muted="#9FA2A8", placeholder="#73767C", disabled="#4C4F56",
    link="#71A1FE", accent="#3871E1", icon="#C3C5CB", icon_disabled="#5F6269",
    hover="#FFFFFF17", pressed="#FFFFFF29", list_hover="#FFFFFF10",
    selection="#2A4371", selection_muted="#233558", selection_inactive="#33353B",
    tab_active="#233558", tab_active_border="#2E4D89",
    caret="#CED0D6", caret_row="#1F2024", editor_selection="#214283",
    line_number="#4B5059", line_number_active="#A1A3AB",
    indent="#323438", indent_active="#4E5157", invisible="#6F737A",
    read_hl="#373B39", write_hl="#402F33", bracket_hl="#43454A",
    search="#2D543F", search_active="#BA9752",
    added="#549159", modified="#375FAD", deleted="#868A91",
    file_added="#73BD79", file_modified="#70AEFF", file_ignored="#D69A6B", file_conflict="#DE6A66", file_deleted="#6F737A",
    err="#F57E84", err_bg="#56272B", err_border="#80383E",
    warn="#D59637", warn_bg="#44321D", warn_border="#694820",
    ok="#6DB083", ok_bg="#203B2A", ok_border="#29583C",
    info_bg="#233558", info_border="#2E4D89",
    ai="#A894F6", ai_bg="#261E3C", ai_border="#4A387B",
    scroll="#FFFFFF21", scroll_hover="#FFFFFF3B",
    inlay_fg="#868A91", inlay_bg="#393B40",
    ansi=dict(black="#26282C", red="#E4656E", green="#4E9D6C", yellow="#C28013", blue="#538AF9",
              magenta="#967BEF", cyan="#4B9B93", white="#C3C5CB",
              bright_black="#5F6269", bright_red="#F57E84", bright_green="#6DB083", bright_yellow="#D59637",
              bright_blue="#71A1FE", bright_magenta="#A894F6", bright_cyan="#6AAEA6", bright_white="#F7F8F9"),
    syn=dict(keyword="#CF8E6D", string="#6AAB73", number="#2AACB8", comment="#7A7E85", doc="#5F826B",
             function="#56A8F5", field="#C77DBB", metadata="#B3AE60", escape="#CF8E6D", tag="#D5B778",
             attr="#BCBEC4", type_param="#16BAAC", lifetime="#20999D", named_arg="#56C1D6", todo="#8BB33D"),
    players=["#CED0D6", "#E4656E", "#4E9D6C", "#C28013", "#967BEF", "#4B9B93", "#CF7659", "#538AF9"],
  ),
  "light": dict(
    gap="#E9EAEE", island="#FFFFFF", island_inline="#F7F8F9", popup="#FFFFFF",
    border="#E9EAEE", border_strong="#D1D3D9", control_border="#D1D3D9",
    text="#000000", editor_text="#080808", muted="#5F6269", placeholder="#73767C", disabled="#9FA2A8",
    link="#2F5EB9", accent="#3871E1", icon="#73767C", icon_disabled="#C3C5CB",
    hover="#00000012", pressed="#00000020", list_hover="#00000008",
    selection="#D0DFFE", selection_muted="#E3EBFE", selection_inactive="#E9EAEE",
    tab_active="#E3EBFE", tab_active_border="#A7C5FF",
    caret="#000000", caret_row="#F5F8FE", editor_selection="#A6D2FF",
    line_number="#AEB3C2", line_number_active="#767A8A",
    indent="#EBECF0", indent_active="#AEB3C2", invisible="#ADADAD",
    read_hl="#EDEBFC", write_hl="#FCE8F4", bracket_hl="#93D9D9",
    search="#FCD47E", search_active="#F2BF57",
    added="#7FC784", modified="#88ADF7", deleted="#767A8A",
    file_added="#067D17", file_modified="#0A64D0", file_ignored="#9E880D", file_conflict="#C54E58", file_deleted="#73767C",
    err="#C54E58", err_bg="#FFF6F5", err_border="#FFC4C5",
    warn="#A56906", warn_bg="#FFF6E9", warn_border="#F4CD9A",
    ok="#338555", ok_bg="#F5FAF3", ok_border="#BBDBC2",
    info_bg="#F7F8FF", info_border="#BDD3FF",
    ai="#8060DB", ai_bg="#EDE8FD", ai_border="#A894F6",
    scroll="#00000020", scroll_hover="#00000045",
    inlay_fg="#73767C", inlay_bg="#EBECF0",
    ansi=dict(black="#000000", red="#C54E58", green="#338555", yellow="#A56906", blue="#2F5EB9",
              magenta="#6C4EBB", cyan="#2A6C67", white="#9FA2A8",
              bright_black="#5F6269", bright_red="#E4656E", bright_green="#4E9D6C", bright_yellow="#C28013",
              bright_blue="#3871E1", bright_magenta="#8060DB", bright_cyan="#31827B", bright_white="#FFFFFF"),
    syn=dict(keyword="#0033B3", string="#067D17", number="#1750EB", comment="#8C8C8C", doc="#8C8C8C",
             function="#00627A", field="#871094", metadata="#9E880D", escape="#0037A6", tag="#0033B3",
             attr="#174AD4", type_param="#007E8A", lifetime="#20999D", named_arg="#174AD4", todo="#008DDE"),
    players=["#000000", "#C54E58", "#338555", "#A56906", "#6C4EBB", "#2A6C67", "#B45E43", "#2F5EB9"],
  ),
}

def build(mode):
    p = PAL[mode]; s = p["syn"]; t = p["editor_text"]
    st = {
      "background.appearance": "opaque",
      # The "sea" between islands: window chrome, title bar, status bar, splits.
      "background": a(p["gap"]),
      "title_bar.background": a(p["gap"]), "title_bar.inactive_background": a(p["gap"]),
      "status_bar.background": a(p["gap"]),
      # Borders take the gap colour so splits read as gaps, not lines.
      "border": a(p["border"]), "border.variant": a(p["border"]),
      "border.focused": a(p["accent"]), "border.selected": a(p["tab_active_border"]),
      "border.transparent": "#00000000", "border.disabled": a(p["border_strong"]),
      "pane_group.border": a(p["gap"]), "pane.focused_border": "#00000000",
      "panel.focused_border": "#00000000",
      # The islands themselves.
      "surface.background": a(p["island"]), "panel.background": a(p["island"]),
      "elevated_surface.background": a(p["popup"]),
      "panel.overlay_background": a(p["popup"]), "panel.overlay_hover": a(p["hover"]),
      "panel.indent_guide": a(p["indent"]), "panel.indent_guide_hover": a(p["indent_active"]),
      "panel.indent_guide_active": a(p["indent_active"]),
      "toolbar.background": a(p["island"]),
      "tab_bar.background": a(p["island"]),
      "tab.inactive_background": a(p["island"]), "tab.active_background": a(p["tab_active"]),
      "editor.background": a(p["island"]), "editor.gutter.background": a(p["island"]),
      "editor.subheader.background": a(p["island_inline"]),
      "editor.foreground": a(t), "editor.code_lens.foreground": a(p["placeholder"]),
      "editor.active_line.background": a(p["caret_row"]),
      "editor.highlighted_line.background": a(p["caret_row"]),
      "editor.debugger_active_line.background": a(p["selection_muted"]),
      "editor.line_number": a(p["line_number"]), "editor.active_line_number": a(p["line_number_active"]),
      "editor.hover_line_number": a(p["line_number_active"]),
      "editor.invisible": a(p["invisible"]),
      "editor.wrap_guide": a(p["indent"]), "editor.active_wrap_guide": a(p["indent_active"]),
      "editor.indent_guide": a(p["indent"]), "editor.indent_guide_active": a(p["indent_active"]),
      "editor.document_highlight.read_background": a(p["read_hl"]),
      "editor.document_highlight.write_background": a(p["write_hl"]),
      "editor.document_highlight.bracket_background": a(p["bracket_hl"]),
      "search.match_background": a(p["search"], "99"),
      "search.active_match_background": a(p["search_active"], "aa"),
      "element.background": a(p["island"]), "element.hover": a(p["hover"]),
      "element.active": a(p["pressed"]), "element.selected": a(p["selection"]),
      "element.disabled": a(p["island"]), "element.selection_background": a(p["editor_selection"], "80"),
      "drop_target.background": a(p["accent"], "33"), "drop_target.border": a(p["accent"]),
      "ghost_element.background": "#00000000", "ghost_element.hover": a(p["list_hover"]),
      "ghost_element.active": a(p["pressed"]), "ghost_element.selected": a(p["selection"]),
      "ghost_element.disabled": "#00000000",
      "text": a(p["text"]), "text.muted": a(p["muted"]), "text.placeholder": a(p["placeholder"]),
      "text.disabled": a(p["disabled"]), "text.accent": a(p["link"]),
      "icon": a(p["icon"]), "icon.muted": a(p["muted"]), "icon.disabled": a(p["icon_disabled"]),
      "icon.placeholder": a(p["placeholder"]), "icon.accent": a(p["link"]),
      "debugger.accent": a(p["err"]),
      "link_text.hover": a(p["link"]),
      "scrollbar.thumb.background": a(p["scroll"]), "scrollbar.thumb.hover_background": a(p["scroll_hover"]),
      "scrollbar.thumb.active_background": a(p["scroll_hover"]), "scrollbar.thumb.border": "#00000000",
      "scrollbar.track.background": "#00000000", "scrollbar.track.border": "#00000000",
      "minimap.thumb.background": a(p["scroll"]), "minimap.thumb.hover_background": a(p["scroll_hover"]),
      "minimap.thumb.active_background": a(p["scroll_hover"]), "minimap.thumb.border": "#00000000",
      "editor.diff_hunk.added.background": a(p["added"], "26"),
      "editor.diff_hunk.added.hollow_background": a(p["added"], "10"),
      "editor.diff_hunk.added.hollow_border": a(p["added"], "80"),
      "editor.diff_hunk.deleted.background": a(p["err"], "26"),
      "editor.diff_hunk.deleted.hollow_background": a(p["err"], "10"),
      "editor.diff_hunk.deleted.hollow_border": a(p["err"], "80"),
      "terminal.background": a(p["island"]), "terminal.ansi.background": a(p["island"]),
      "terminal.foreground": a(t), "terminal.bright_foreground": a(p["text"]),
      "terminal.dim_foreground": a(p["placeholder"]),
      "version_control.added": a(p["file_added"]), "version_control.modified": a(p["file_modified"]),
      "version_control.deleted": a(p["file_deleted"]), "version_control.renamed": a(p["file_modified"]),
      "version_control.conflict": a(p["file_conflict"]), "version_control.ignored": a(p["file_ignored"]),
      "version_control.word_added": a(p["added"], "40"), "version_control.word_deleted": a(p["err"], "40"),
      "version_control.conflict_marker.ours": a(p["added"], "33"),
      "version_control.conflict_marker.theirs": a(p["modified"], "33"),
    }
    for name, col in p["ansi"].items():
        st[f"terminal.ansi.{name}"] = a(col)
        if not name.startswith("bright_"):
            st[f"terminal.ansi.dim_{name}"] = a(col, "99")
    status = dict(
        error=(p["err"], p["err_bg"], p["err_border"]), warning=(p["warn"], p["warn_bg"], p["warn_border"]),
        success=(p["ok"], p["ok_bg"], p["ok_border"]), info=(p["link"], p["info_bg"], p["info_border"]),
        hint=(p["inlay_fg"], p["inlay_bg"], p["inlay_bg"]), predictive=(p["placeholder"], p["island"], p["border_strong"]),
        created=(p["file_added"], p["ok_bg"], p["ok_border"]), modified=(p["file_modified"], p["info_bg"], p["info_border"]),
        deleted=(p["err"], p["err_bg"], p["err_border"]), renamed=(p["file_modified"], p["info_bg"], p["info_border"]),
        conflict=(p["file_conflict"], p["err_bg"], p["err_border"]), ignored=(p["file_ignored"], p["island"], p["border_strong"]),
        hidden=(p["disabled"], p["island"], p["border_strong"]), unreachable=(p["placeholder"], p["island"], p["border_strong"]),
    )
    for k, (fg, bg, bd) in status.items():
        st[k] = a(fg); st[f"{k}.background"] = a(bg); st[f"{k}.border"] = a(bd)
    st["players"] = [{"cursor": a(c), "background": a(c), "selection": a(p["editor_selection"] if i == 0 else c, "ff" if i == 0 else "3d")}
                     for i, c in enumerate(p["players"])]
    st["syntax"] = {
      "keyword": style(s["keyword"]), "boolean": style(s["keyword"]),
      "string": style(s["string"]), "string.escape": style(s["escape"]), "string.regex": style(s["string"]),
      "string.special": style(s["string"]), "string.special.symbol": style(s["field"]),
      "number": style(s["number"]),
      "comment": style(s["comment"], italic=(mode == "light")), "comment.doc": style(s["doc"], italic=True),
      # IDEA colors declarations only; calls use the default identifier color.
      "function": style(t), "function.method": style(t),
      "function.definition": style(s["function"]), "function.method.definition": style(s["function"]),
      "function.special": style(s["function"]), "function.special.definition": style(s["function"]),
      "type.builtin": style(s["keyword"]), "type.interface": style(t),
      "keyword.control": style(s["keyword"]),
      "property": style(s["field"]), "variable.member": style(s["field"]),
      "constant": style(s["field"], italic=True), "enum": style(t), "variant": style(s["field"], italic=True),
      "attribute": style(s["metadata"]), "preproc": style(s["metadata"]),
      "type": style(t), "constructor": style(t), "namespace": style(t),
      "variable": style(t), "variable.parameter": style(t), "variable.special": style(s["keyword"]),
      "operator": style(t), "punctuation": style(t), "punctuation.bracket": style(t),
      "punctuation.delimiter": style(t), "punctuation.special": style(s["keyword"]),
      "punctuation.list_marker": style(s["keyword"]), "punctuation.markup": style(s["keyword"]),
      "tag": style(s["tag"]), "selector": style(s["tag"]), "selector.pseudo": style(s["keyword"]),
      "label": style(s["lifetime"], italic=True), "lifetime": style(s["lifetime"], italic=True),
      "title": style(s["keyword"], bold=True), "emphasis": style(t, italic=True),
      "emphasis.strong": style(t, bold=True), "text.literal": style(s["string"]),
      "link_text": style(s["function"]), "link_uri": style(s["function"]),
      "embedded": style(t), "primary": style(t),
      "hint": style(p["inlay_fg"]), "predictive": style(p["placeholder"], italic=True),
      "diff.plus": style(p["file_added"]), "diff.minus": style(p["err"]),
    }
    if mode == "dark":
        st["syntax"]["attribute"] = style(s["metadata"])
    return {"name": f"Islands UI {mode.title()}", "appearance": mode, "style": st}

if __name__ == "__main__":
    out = {"$schema": "https://zed.dev/schema/themes/v0.2.0.json", "name": "Islands UI",
           "author": "Dmytro (palette from JetBrains IntelliJ Islands, Apache-2.0)",
           "themes": [build("dark"), build("light")]}
    json.dump(out, open(sys.argv[1], "w"), indent=2); print("wrote", sys.argv[1])
