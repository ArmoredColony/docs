How to Install
=================================

Installation is simple. This extension is distributed as a downloadable package.

Step 1. Download the Extension
---------------------------------

Download the extension bundle from the official distribution page.

Step 2. Drag and Drop Installation
-----------------------------------

Locate your Blender extensions directory and copy the extension folder directly into it.

.. important::

   Make sure Blender is closed before installing the extension to avoid file lock conflicts.

Supported installation method:

- Download the archive file
- Extract the contents if necessary
- Move the extension folder into the extensions directory

Example directory structure:

::

    blender_extensions/
    ├── PixiePivot/
    │   ├── __init__.py
    │   ├── operators/
    │   ├── assets/
    │   └── manifest.toml

Step 3. Enable the Extension
-----------------------------

Launch Blender and navigate to:

``Edit → Preferences → Extensions``

Search for the extension name and enable it.

.. warning::

   Do not manually edit the internal files of the extension unless you know what you are doing.

   Modifying packaged scripts may cause update failures or runtime errors.

Verification
-------------

After enabling the extension, open the 3D viewport and confirm that the tool panel appears.

.. note::

   If the extension does not appear immediately, restart Blender.

   Some UI elements are loaded lazily during startup.