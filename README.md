# Color Brackets — AI Updated

AI updated version of the Color Brackets plugin.

Compatibility patch for **IntelliJ IDEA 2026.2**, based on **Color Brackets 2024.6.1.8 by LJYXP**. Changes the declared upper build limit from `261.*` to `262.*` and labels the result `2024.6.1.8-local-262`. Compiled code and resources are unchanged.

## Use

1. Download version **2024.6.1.8** from the [original plugin on JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24560-color-brackets/versions).
2. With Python 3.9 or newer, run:

   ```sh
   python3 patch.py /path/to/ColorBrackets-2024.6.1.8.jar
   ```

3. In IntelliJ, open **Settings → Plugins → gear menu → Install Plugin from Disk**, choose the generated `ColorBrackets-2024.6.1.8-local-262.jar`, and restart the IDE.

Keep your original JAR as a backup. To undo the update, reinstall the original plugin.

## Verification

JetBrains Plugin Verifier **1.411** reports **Compatible** against IntelliJ IDEA **2026.2.3**, build **262.10968.63**, with no compatibility problems or warnings. This checks binary compatibility; bracket coloring has not been visually tested in a running editor. Future release series and EAP builds have not been verified.

## Original plugin

All credit for the plugin goes to **LJYXP**. This is an unofficial AI-assisted compatibility update, not a vendor release. Only the patch script is published here; the original and modified plugin binaries are not included. The original plugin remains subject to its [author's license](https://github.com/LCCDX/intellij-editor-assist-for-csharp/blob/main/ColorBrackets_license.md).
