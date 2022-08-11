"General editor settings
set tabstop=4
set shiftwidth=4
set autoindent
set smartindent
set number
set relativenumber
set incsearch
set laststatus=2
set statusline+=%F
set clipboard=unnamedplus
set mouse=a
syntax on
set noswapfile
"colorscheme zellner 



"Keybindings
"{ completion
inoremap {<CR>  {<CR>}<Esc>O
inoremap {}     {}
"jk for escape 
imap jk         <Esc>
"ctrl+a to select all 
map <C-a> <esc>ggVG<CR>
set belloff=all
"add a single char in N-mode
:nnoremap <Space> i_<Esc>r
"tab
nnoremap <Tab> >>
vnoremap <Tab> >
nnoremap <S-Tab> <<
vnoremap <S-Tab> <
"navigate with ctrl+j/k
nnoremap <C-j> <C-e>
nnoremap <C-k> <C-y>
"after compile remove errormarker and testcase
nnoremap \\ <C-w>w:q<CR>:RemoveErrorMarkers<CR>
"move in I-mode with ctrl+h/j/k/l
inoremap <C-k> <C-o>gk
inoremap <C-h> <Left>
inoremap <C-l> <Right>
inoremap <C-j> <C-o>gj



"Append template to new c++ files
autocmd BufNewFile *.cpp 0r /home/alls/Library/Template.cpp



"compile without -DALE
set makeprg=build.sh\ %:r
autocmd filetype cpp nnoremap <F8> :w <bar> Make <CR>
autocmd filetype cpp inoremap <F8> <ESC> :w <bar> Make <CR>

"test solution with testcase
autocmd filetype cpp nnoremap <F9> :Test<CR>
autocmd filetype cpp inoremap <F9> <ESC> :Test<CR>

"debug one testcase
autocmd filetype cpp nnoremap <F10> :Debug 
autocmd filetype cpp inoremap <F10> <ESC> :Debug 

"debug full screen terminal
autocmd filetype cpp nnoremap <F11> :!./%:rdebug.exe<CR>
autocmd filetype cpp inoremap <F11> <ESC> :!./%:rdebug.exe<CR>

"submit the solution online
autocmd filetype cpp nnoremap <F12> :Submit<CR>
autocmd filetype cpp inoremap <F12> <ESC> :Submit<CR>

"automate testing 
call plug#begin()
Plug 'searleser97/cpbooster.vim'
call plug#end()



"highlight errors
let &errorformat="%f:%l:%c: %t%*[^:]:%m,%f:%l: %t%*[^:]:%m," . &errorformat 
execute pathogen#infect()

" plugin
" https://github.com/tpope/vim-pathogen
" https://github.com/tpope/vim-dispatch
" https://github.com/vim-scripts/errormarker.vim
" https://github.com/searleser97/cpbooster
