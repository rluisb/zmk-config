from pathlib import Path

keymap = Path("config/lily58.keymap").read_text()

expected = (
    'tapping-term-ms = <280>;',
    'flavor = "balanced";',
    'require-prior-idle-ms = <150>;',
    'hold-trigger-on-release;',
    'tap_hold: tap_hold {',
    'space_hold_tap: space_hold_tap {',
    'tapping-term-ms = <220>;',
    'flavor = "hold-preferred";',
    '&layer_hold_tap 1 LEFT_META',
    '&mo 1',
    '&kp N1      &kp N2      &kp N3      &kp N4       &kp N5       &kp N6',
    '&kp N7      &kp N8      &kp N9      &kp N0       &kp MINUS    &kp EQUAL',
    '&kp F1      &kp F2      &kp F3      &kp F4       &kp F5       &kp F6',
    '&kp F7      &kp F8      &kp F9      &kp F10      &kp F11      &kp F12',
    '&kp HOME',
    '&kp PAGE_DOWN',
    '&kp PAGE_UP',
    '&kp END',
    '&kp PRINTSCREEN',
    '&kp LEFT',
    '&kp DOWN',
    '&kp UP_ARROW',
    '&kp RIGHT',
    '&bt BT_SEL 0',
    '&bt BT_SEL 4',
    '&out OUT_TOG',
    'bindings = <&to 2>;',
    'bindings = <&to 3>;',
)

forbidden = (
    'conditional_layers {',
    'nav_layer {',
    'raise {',
    '&layer_hold_tap 2 DELETE',
    'bindings = <&to 5>;',
)

missing = [value for value in expected if value not in keymap]
unexpected = [value for value in forbidden if value in keymap]
assert not missing, f"missing expected keymap configuration: {missing}"
assert not unexpected, f"obsolete keymap configuration remains: {unexpected}"
