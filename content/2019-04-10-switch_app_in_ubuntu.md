Tags: bash, gnome

After updating to Ubuntu 18, I realized a change in the app switching flow due to the change of desktop environment. Back then with Unity, the `alt + num` would take you to the lastest window of the app in the position on the dock. Gnome, on the other hand, shows all the windows of the app and you spend addition taps to open them. I live with this, because of reasons, until today when I accidentally find out the hotkey for workspace switching. Hopefully if I put each window of a same app on different workspaces, switching to that app would open right away the window of the current workspace.

Well things are not always as we hope. Apps aren't separated into workspaces for app switcher.

But the good news is, you can set it:

```bash
gsettings set org.gnome.shell.app-switcher current-workspace-only true
```

Now this seems like I solve the problem by changing the problem itself. But using workspaces doesn't only allow switching app like I used to, but also prevents opening unwanted window by mistake. You know, like when seniors come to your laptop for discussion and see you misclick into a page full of seasonal anime previews.

But being me, it leaves a bad taste not being able to solve the original problem anyway. With some digging around, I finally find the setting for the app switching flow:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action cycle-windows
```

Translator notes: reasons mean laziness.
