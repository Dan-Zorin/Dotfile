local o = vim.opt
local g = vim.g

-- line numbers
o.relativenumber = true
o.number = true

-- tabs & indentation
o.tabstop = 4
o.shiftwidth = 4
o.expandtab = true
o.autoindent = true

-- line wrapping
o.wrap = false

-- search settings
o.ignorecase = true
o.smartcase = true

-- appearance
o.termguicolors = true

-- backspace
o.backspace = "indent,eol,start"

-- clipboard
o.clipboard:append("unnamedplus")

-- split windows
o.splitright = true
o.splitbelow = true

-- treat - as a word
o.iskeyword:append("-")

-- swap files
o.swapfile = false
o.backup = false
o.undofile = false
