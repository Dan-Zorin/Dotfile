#!/bin/sh

# new line character
NL=$'\n'

# choose from possible options
CHOOSE=$(gum choose \
    "🎁NEW:" \
    "👌IMPROVE:" \
    "🐛BUG FIX:" \
    "❌REMOVED:" \
    "🚀STABLE RELEASE:")

# get user's commit message
TEXT=$(gum input --placeholder "text")      

# show commit message and ask for confirmation then run git commit
gum confirm "$CHOOSE $TEXT $NL$NL commit?" && git commit -m "$CHOOSE $TEXT"
