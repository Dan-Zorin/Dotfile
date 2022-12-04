:syntax on

set encoding=UTF-8

:set t_Co=256

:set noerrorbells

:set expandtab
:set smarttab
:set tabstop=4 
:set softtabstop=4
:set shiftwidth=4

:set smartindent
:set autoindent

:set number relativenumber

:set nowrap
:set incsearch
:set clipboard=unnamedplus

:set smartcase

:set noswapfile
:set nobackup
:set undodir=~/.vim/undodir
:set undofile

call plug#begin('~/.vim/plugged')
    Plug 'wakatime/vim-wakatime'
	Plug 'tpope/vim-surround'
    Plug 'frazrepo/vim-rainbow'
	Plug 'scrooloose/nerdtree'
    Plug 'ryanoasis/vim-devicons'
	Plug 'valloric/youcompleteme'
    Plug 'airblade/vim-gitgutter'
    Plug 'suan/vim-instant-markdown'
    Plug 'ap/vim-css-color'
call plug#end()
