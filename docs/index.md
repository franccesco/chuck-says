---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
# Chuck Norris Facts, right in your terminal!

Because, who wouldn't want that? You better...

Get your day started as soon you see that sweet Chuck Norris fact of the day in your terminal; there's more than 600+ facts here, baby!
They're all real... allegedly.

_This package was completely made to write a blog post. It's not meant to be a 'real' project. It's fun though._
_You can check out the post at: https://codingdose.info/2019/06/08/create-a-project-page-for-your-repositories-easily-with-Jekyll/_

# Installation and Usage

Install this package right now before Chuck installs his foot on your face.
```bash
$ pip install --user chuck-says
```

Worried about how to execute it before Chuck executes you? Just call **Chuck**!

```
# Automatically add Cowsay
$ chuck
  ________________________________________
/ Chuck Norris doesn't need a debugger, he \
| just stares down the bug until the code  |
\ confesses.                               /
  ----------------------------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||

# Output fact only if you want to integrate it with another 'cow'
$ chuck -n | cowsay -f eyes
 _______________________________________
/ Chuck Norris has never won an Academy \
| Award for acting... because he's not  |
\ acting.                               /
 ---------------------------------------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
```

To have a fun fact whenever you open your terminal just edit your shell configuration file.
For Bash:
```bash
echo chuck >> ~/.bashrc
```

For Fish:
```fish
# Edit your fish_greeting function
~ function fish_greeting
             chuck
  end

# And save it
~ funcsave fish_greeting
```

# Collaboration

Want to add a fact? Are you a first timer and want to make your first pull request? Is my coding style a piece of garbage that makes your eyes bleed? Fear not!
1. Get that fork going, boy.
2. Make your changes in the **develop** branch.
3. Make a pull request including your changes.

Boom, your done, get that approved pull request into your CV right now goddammit.

# How it works

Who the hell knows? I just made this yesterday.

-------------

![chuck -n | cowsay -f dragon | lolcat -t -a -s 120](/chuck_animated.gif)
