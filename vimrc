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
syntax on



"Keybindings
"{ completion
inoremap {<CR>  {<CR>}<Esc>O
inoremap {}     {}
"jk for escape 
imap jk         <Esc>
"ctrl-a to select all 
map <C-a> <esc>ggVG<CR>
set belloff=all
"add a single char in Nmode
:nnoremap <Space> i_<Esc>r
"enter new line in Nmode
nnoremap <CR> o<Esc>0"_D
"tab
nnoremap <Tab> >>
vnoremap <Tab> >
nnoremap <S-Tab> <<
vnoremap <S-Tab> <
"navigate with Ctrl+j/k
nnoremap <C-j> <C-e>
nnoremap <C-k> <C-y>
":q with Delete
nnoremap <Del> :q<CR>



"Append template to new C++ files
autocmd BufNewFile *.cpp 0r /home/griffith/CP/Library/Template.cpp



"Compile
noremap <F7> :w <CR> :term ++rows=10 stressBuild.sh %:r <CR>
inoremap <F7> <ESC> :w <CR> :term ++rows=10 stressBuild.sh %:r <CR>
noremap <F8> :w <CR> :term ++rows=10 build.sh %:r <CR>
inoremap <F8> <ESC> :w <CR> :term ++rows=10 build.sh %:r <CR>

"Run
noremap <F9> :vertical terminal ++cols=60 ./%:r <CR>

"Compile and run
noremap <F10> :w <CR> :!build.sh %:r <CR> :vertical terminal ++cols=60 ./%:r <CR>
inoremap <F10> <ESC> :w <CR> :!build.sh %:r <CR> :vertical terminal ++cols=60 ./%:r <CR>



" WSL yank support
let s:clip = '/mnt/c/Windows/System32/clip.exe'  " change this path according to your mount point
if executable(s:clip)
    augroup WSLYank
        autocmd!
        autocmd TextYankPost * if v:event.operator ==# 'y' | call system(s:clip, @0) | endif
    augroup END
endif
