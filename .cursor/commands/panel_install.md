# panel_install - Install REPL Status Panel Extension

## Install Panel Extension
cd agile_bot/bots/base_bot/src/display_panel/extension; .\rebuild.ps1; cursor --install-extension repl-status-panel-0.18.0.vsix --force

## Uninstall Panel Extension
cursor --uninstall-extension agilebot.repl-status-panel

## Rebuild and Reinstall Panel Extension
cursor --uninstall-extension agilebot.repl-status-panel; cd agile_bot/bots/base_bot/src/display_panel/extension; .\rebuild.ps1; cursor --install-extension repl-status-panel-0.18.0.vsix --force

