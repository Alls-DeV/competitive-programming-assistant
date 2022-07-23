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
"after compile remove errormarker
nnoremap \\ <C-w>w:q<CR>:RemoveErrorMarkers<CR>
"move in I-mode with ctrl+h/j/k/l
inoremap <C-k> <C-o>gk
inoremap <C-h> <Left>
inoremap <C-l> <Right>
inoremap <C-j> <C-o>gj



"Append template to new c++ files
autocmd BufNewFile *.cpp 0r /home/alls/Library/Template.cpp



"Compile and run
set makeprg=build.sh\ %:r
autocmd filetype cpp nnoremap <F8> :w <bar> Make <CR>
autocmd filetype cpp inoremap <F8> <ESC> :w <bar> Make <CR>
autocmd filetype cpp nnoremap <F9> :vertical terminal ++shell ++cols=60 ./%:r.exe<CR>
autocmd filetype cpp nnoremap <F10> :!./%:r.exe<CR>
"compile without .exe for stress test
noremap <F12> :w<CR>:!g++ -o %:r %:r.cpp<CR>


let &errorformat="%f:%l:%c: %t%*[^:]:%m,%f:%l: %t%*[^:]:%m," . &errorformat 
execute pathogen#infect()

" plugin
" https://github.com/tpope/vim-pathogen
" https://github.com/tpope/vim-dispatch
" https://github.com/vim-scripts/errormarker.vim
