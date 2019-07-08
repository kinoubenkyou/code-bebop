Tags: bash, gnome, ubuntu

Some configs regarding app switching for Gnome in Ubuntu 18:

- Clicking on app/hot-keying to app (super + num) results in cycling through the windows of an app:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action cycle-windows
```

- Prevent clicking/hot-keying to windows of other workspaces:

```bash
gsettings set org.gnome.shell.app-switcher current-workspace-only true
```

- Prevent cycling through apps (alt + tab) to include windows of other workspaces:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock isolate-workspaces true
```
