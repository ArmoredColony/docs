# PIXIE PIVOT CHANGELOG

## 1.3.0
09/Jun/2026

### Added
- Align Only modal toggle <kbd>T</kbd> → Use the 3D cursor orientation but not its location (preserves the current Transform Pivot Point mode).
- Internal Setting to restore the 3D cursor to its previous location when double-tapping the activation key.
- Internal Setting to limit raycasting in Edit Mode for better performance in certain situations.
- Main Panel can be dragged to a new position directly in the viewport and supports window resizing.
- Mouse Panel/HUD has an alternate, compact mode that displays the toggled states with their hotkey instead of the full word (B instead of [Bounds].
- Support for snapping to non-mesh objects that have mesh representations (curves with radius, text, etc).

### Changed
- Setting the Origin mode will apply to all selected objects.
- Main Panel styling for better readibility.
- The Reset Pivot key <kbd>D</kbd> can now be set independently from the activation key and appears in the Main Panel.

### Fixed
 - Scene raycast hitting invisible objects in Local View.
 - Edit Mode slowdown when hovering outside mesh geometry, caused by not caching the center calculation.
 - Crash when raycasting non-mesh objects (e.g. curves with radius).
 - Crash when scaling the gizmo with <kbd>+</kbd> or <kbd>-</kbd> (modal hotkeys).

### Removed
- Lock Cursor Location (replaced with Align Only).

## 1.2.2
16/March/2026

### Fixed
- ValueError when using edge normals and `linked_faces` was different than 2.

## 1.2.1
12/March/2026

### Fixed
- AttributeError `build_element_styles` when resetting certain Prop Groups.

## 1.2.0
12/March/2026

### Added
- Support for targeting mesh elements while in Object Mode.
- Snap/align between multiple objects (still limited to mesh objects).
- Lock Cursor Location → Prevents the 3D cursor from changing location while still allowing it to rotate/align in place.
- Bounding Box Calculation preferences: Accurate (default) vs Fast.

### Changed
- Converted the add-on into an extension.

### Removed
- Anchor to Selection → Too much dev time; may re-add if the API exposes transform_orientation and transform_pivot_point results. Replaced with simpler **Lock Cursor Location**.
- Release Checking → It was pretty useless anyway (no updating and version notifications were super hidden).


## 1.1.4
09/February/2026

### Changed
- Setting the Origin no longer forces GLOBAL Orientation and MEDIAN_POINT Pivot, instead it keeps your previous settings.


## 1.1.3
11/October/2025

### Fixed
- Error when enabling `anchor_to_selection` and no selection was available.


## 1.1.2
06/October/2025

### Added
- Behavior Preference **Double Tap Resets To** with pivot reset options.

### Changed
- Pressing <kbd>D</kbd><kbd>D</kbd> now resets the pivot to the previous non-cursor settings instead of always resetting to GLOBAL Orientation and MEDIAN_POINT pivot point.


## 1.1.1
06/September/2025

### Fixed
- AttributeError → `view3d_utils` was not being imported correctly from `bpy_extras`.


## 1.1.0
03/September/2025

### Added
- New Toggle Key 'Anchor to Selection' <kbd>T</kbd>: Allows aligning to other elements while keeping your pivot point near your selection.

### Fixed
- Incorrect HUD position when the 3d region was not at the bottom left.
- Obscure case where release_check would say an update was available if the addon crashed (failed version check returned (0, 0, 0) instead of None).

### Changed
- Only draw HUDs in a single 3DView (the one that called Pixie Pivot).
- Mouse HUD is slightly bigger (0.8 of the Fixed HUD size instead of 0.7).

## 1.0.0
28/August/2025

### Initial Release
