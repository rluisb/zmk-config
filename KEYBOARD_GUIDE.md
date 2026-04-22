# ⌨️ Lily58 Keymap Guide

This guide matches the current `config/lily58.keymap`.

## Base layers

There are two base layers:

- **Layer 0 — macOS**
- **Layer 3 — Linux**

Both base layers share the same core layout:

- Home-row mods on `A S D F` and `H J K L`
- Plain `SPACE` on the thumb cluster
- `Lower` on `&mo 1`
- `Raise` on `&mo 2`

On both base layers, the left thumb cluster now works like this:

- macOS: `LC(SPACE)`, **Lower**, **Raise**, `SPACE`
- Linux: `PRINTSCREEN`, **Lower**, **Raise**, `SPACE`

That means Lower/Raise are reachable directly from either base layer without giving up the plain space key.

## Home-row mods

These keys are hold-taps:

- Left hand: `A=GUI`, `S=ALT`, `D=SHIFT`, `F=CTRL`
- Right hand: `H=GUI`, `J=ALT`, `K=SHIFT`, `L=CTRL`

Tap sends the letter. Hold sends the modifier.

## Lower and Raise layers

- **Layer 1 — Lower**
- **Layer 2 — Raise**

They are momentary layers, activated only while the thumb key is held.

## Navigation overlay

The navigation layer is:

- **Layer 6 — nav_layer**

It is a **conditional layer** that turns on only when **both Lower and Raise are active at the same time**.

So the logic is:

- hold **Lower** only → layer 1
- hold **Raise** only → layer 2
- hold **Lower + Raise together** → layer 6 overlays navigation

When layer 6 is active, the right-hand home row becomes:

- `H` → `HOME`
- `J` → `PAGE_DOWN`
- `K` → `PAGE_UP`
- `L` → `END`

## Combos

### Base-layer home-row combos

These combos are restricted to the two base layers only (`macOS` and `Linux`) and require a short idle window before they can trigger.

- `S + D` → toggle output (`USB ↔ Bluetooth`)
- left `S` + right `S` → jump to **Fortnite** layer

Safety tuning applied:

- combo scope limited to layers `0` and `3`
- `require-prior-idle-ms = 150`

### Other defined combos

The keymap still includes two non-home-row combos:

- quick return to **macOS base layer**
- quick jump to **adjust/utility** layer

Their behavior was left unchanged.

## Fortnite layer

- **Layer 5 — Fortnite**

Its internal key layout was intentionally left unchanged.

## Maintenance notes

- Removed the unused `os_leader` behavior block
- Fixed nav layer key naming to valid ZMK keycodes (`PAGE_DOWN`)
- Fixed the conditional nav target to the real nav layer index (`6`)
