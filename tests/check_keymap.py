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
    'then-layer = <4>;',
    '&layer_hold_tap 1 LEFT_META',
)

missing = [value for value in expected if value not in keymap]
assert not missing, f"missing expected keymap configuration: {missing}"
