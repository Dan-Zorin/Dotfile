### BASICS ###
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Load starship prompt
__main() {
    local major="${BASH_VERSINFO[0]}"
    local minor="${BASH_VERSINFO[1]}"

    if ((major > 4)) || { ((major == 4)) && ((minor >= 1)); }; then
        source <("/usr/bin/starship" init bash --print-full-init)
    else
        source /dev/stdin <<<"$("/usr/bin/starship" init bash --print-full-init)"
    fi
}
__main
unset -f __main

# Adding to the path #
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

# ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# Check the window size after each command and, if necessary,
shopt -s checkwinsize


### ALIASES ###
# colorize the grep command output for ease of use
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# continue download
alias wget="wget -c"

# confirm before overwriting something
alias cp="cp -i"
alias mv="mv -i"
alias rm="rm -i"

# create dir and cd into it
mkcd ()
{
    [ ! -z "$1" ] && mkdir -p "$1" && cd "$_"
}

# navigation
alias ..='cd ../'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

tut()
{
    cd "/home/ton1czech/CODING/Tutorials/$1"
}

pts()
{
    cd "/home/ton1czech/CODING/Projects/$1"
}

# super list dir command
alias ls="exa -lah --color=always --group-directories-first"
alias lt="exa -aT --color=always --group-directories-first"

# sync .files inside git repository Dotfiles
alias config="/usr/bin/git --git-dir=$HOME/Dotfiles --work-tree=$HOME"


### git commands ###
# git clone
gcl()
{
    git clone https://github.com/$1
}

# git pull
alias gll="git pull"
glb()
{
    git pull origin $1
}

# git add
alias gaa="git add ."
gaw()
{
    git add $1
}

# git commit
gcm()
{
    git commit -m "$*"
}
gcmn()
{
    git commit -m "🎁NEW: $*"
}
gcmi()
{
    git commit -m "👌IMPROVE: $*"
}
gcmb()
{
    git commit -m "🐛BUG FIX: $*"
}
gcmr ()
{
    git commit -m "❌REMOVED: $*"
}

# git push
alias gpp="git push origin master"
gpb ()
{
    git push origin $1
}


### FUN COMMANDS ###
alias truth="curl -L git.io/unix"


### EXtractor for all kinds of archives ###
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH=$BUN_INSTALL/bin:$PATH

nvm use --lts
