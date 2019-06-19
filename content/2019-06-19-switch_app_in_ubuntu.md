Tags: bash, gnome

Some configs for gnome in ubuntu 18:

- Clicking on app/shortcuting to app (super + num) results in cycling through the windows of app:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action cycle-windows
```

- Prevent clicking/shortcuting to windows for other workspaces:

```bash
gsettings set org.gnome.shell.app-switcher current-workspace-only true
```

- Prevent cycling through apps (alt + tab) to include windows for other workspaces:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock isolate-workspaces true
```
