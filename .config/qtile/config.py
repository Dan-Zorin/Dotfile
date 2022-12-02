import os
import subprocess
from libqtile import layout, bar, widget, hook 
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

home = os.path.expanduser('~')
mod = "mod4" # super key
mod1 = "alt"
mod2 = "control"
myTerm = "alacritty"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [
# SUPER + FUNCTION KEYS
    Key([mod], "F1", lazy.spawn("brave")),
    Key([mod], "F2", lazy.spawn("code")),
    Key([mod], "F3", lazy.spawn("spotify")),
    Key([mod], "F4", lazy.spawn("discord")),
# SUPER + ... KEYS
    Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'FiraCode:bold:pixelsize=14'")),
    Key([mod], "return", lazy.spawn(myTerm)),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "x", lazy.shutdown()),
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
# SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
# CONTROL + ALT KEYS
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
# ALT + ... KEYS
    Key(["mod1"], "w", lazy.spawn('garuda-welcome')),
# CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),
# MEDIA KEYS
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
# SCREENSHOTS
    Key([], "Print", lazy.spawn('flameshot gui')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
# CHANGE FOCUS
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, mod2], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),
    Key([mod, mod2], "l", lazy.layout.grow(), lazy.layout.increase_nmaster()),
# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating())
]

groups = [Group(f"{i+1}", label="") for i in range(8)]

for i in groups:
    keys.extend([
#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

layout_theme={
    "margin": 15,
    "border_width":1,
    "border_focus": "#ff00ff",
    "border_normal": "#f4c2c2"
}

layouts=[
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Columns(**layout_theme),
]

# COLORS FOR THE BAR
def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#ff5050", "#ff5050"], # color 3
            ["#f4c2c2", "#f4c2c2"], # color 4
            ["#ffffff", "#ffffff"], # color 5
            ["#ffd47e", "#ffd47e"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#000000", "#000000"], # color 8
            ["#c40234", "#c40234"], # color 9
            ["#6790eb", "#6790eb"], # color 10
            ["#ff00ff", "#ff00ff"], #11
            ["#4c566a", "#4c566a"], #12 
            ["#282c34", "#282c34"], #13
            ["#212121", "#212121"], #14
            ["#e75480", "#e75480"], #15 
            ["#2aa899", "#2aa899"], #16 
            ["#abb2bf", "#abb2bf"],# color 17
            ["#81a1c1", "#81a1c1"], #18 
            ["#56b6c2", "#56b6c2"], #19 
            ["#b48ead", "#b48ead"], #20 
            ["#e06c75", "#e06c75"], #21
            ["#fb9f7f", "#fb9f7f"], #22
            ["#ffd47e", "#ffd47e"]] #23

colors = init_colors()

# WIDGETS FOR THE BAR
def init_widgets_defaults():
    return dict(
        font="Fira Code",
        fontsize=12,
        padding=3,
    )

widget_defaults=init_widgets_defaults()

def init_widgets_list():
    widgets_list=[
        widget.Spacer(
            length=10,
            background='#1F1D2E',
        ),
        widget.Image(
            filename='~/.config/qtile/Assets/launch_Icon.png',
            margin=2,
            background='#1F1D2E',
            decorations=[
                PowerLineDecoration(
                    path='rounded_left',
                    override_colour='#1F1D2E', 
                    size=10
                )
            ],
        ),
        widget.GroupBox(
            fontsize=16,
            borderwidth=3,
            highlight_method='block',
            active='#7F61A7',
            block_highlight_text_color="#CFB3E5",
            highlight_color='#4B427E',
            inactive='#BD85CB',
            foreground='#4B427E',
            background='#4B427E',
            this_current_screen_border='#52548D',
            this_screen_border='#52548D',
            other_current_screen_border='#52548D',
            other_screen_border='#52548D',
            urgent_border='#52548D',
            rounded=True,
            disable_drag=True,
            decorations=[
                PowerLineDecoration(
                    path='rounded_left',
                    override_colour='#4B427E', 
                    size=10
                )
            ],
            ),
        widget.CurrentLayoutIcon(
            background='#52548D',
            padding=0,
            scale=0.5,
        ),
        widget.CurrentLayout(
            background='#52548D',
            font='JetBrains Mono Bold',
            decorations=[
                PowerLineDecoration(
                    path='rounded_left',
                    override_colour='#52548D', 
                    size=10
                )
            ],
        ),
        widget.WindowName(
            background='#7676B2',
            format="{name}",
            font='JetBrains Mono Bold',
            empty_group_string = 'Desktop',
            decorations=[
                PowerLineDecoration(
                    path='rounded_right',
                    override_colour='#7676B2', 
                    size=10
                )
            ],
        ),
        widget.OpenWeather(
            app_key='50dfe3c4af787e95cfb00325885f0019',
            font="JetBrains Mono Bold",
            background='#52548D',
            cityid=3076586,
            format='{icon}  {main_temp}°{units_temperature}'
        ),
        widget.Spacer(
            length=15,
            background='#52548D',
        ),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=2,
            background='#52548D',
        ),
        widget.CheckUpdates(
            font="JetBrains Mono Bold",
            background='#52548D',
            display_format='{updates}',
            distro='Arch_checkupdates'
        ),
        widget.Spacer(
            length=15,
            background='#52548D',
        ),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=0,
            background='#52548D',
        ),
        widget.Memory(format='{MemUsed: .0f}{mm}',
            font="JetBrains Mono Bold",
            fontsize=12,
            padding=10,
            background='#52548D',
            decorations=[
                PowerLineDecoration(
                    path='rounded_right',
                    override_colour='#52548D', 
                    size=10
                )
            ],
        ),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=0,
            background='#4B427E',
        ),
        widget.PulseVolume(
            font='JetBrains Mono Bold',
            fontsize=12,
            padding=10,
            background='#4B427E',
            decorations=[
                PowerLineDecoration(
                    path='rounded_right',
                    override_colour='#4B427E', 
                    size=10
                )
            ],
        ),
        widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            padding=0,
            background='#1F1D2E',
        ),
        widget.Clock(
            format='%I:%M %p',
            padding=10,
            background='#1F1D2E',
            font="JetBrains Mono Bold",
        ),
        widget.Spacer(
            length=10,
            background='#1F1D2E',
        )
    ]
    return widgets_list

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

screens=[
    Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=30, opacity=0.85, margin=[10,15,-3,15])),
    Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=30, opacity=0.85, margin=[10,15,-3,15]))
]

# MOUSE CONFIGURATION
mouse=[
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder=None
dgroups_app_rules=[]
main = None

@hook.subscribe.startup_once
def start_once():
    home=os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

follow_mouse_focus=True
bring_front_click=False
cursor_warp=False

floating_layout=layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(title='branchdialog'),
        Match(title='Open File'),
        Match(title='pinentry'),
        Match(wm_class='ssh-askpass'),
        Match(wm_class='lxpolkit'),
        Match(wm_class='yad'),
    ]
)

auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart" 

wmname = "LG3D"