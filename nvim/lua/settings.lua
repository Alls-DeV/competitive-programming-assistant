local g = vim.g
local o = vim.o
local opt = vim.opt

-- Better editor UI
o.number = true
o.numberwidth = 2
o.relativenumber = true

-- Better editing experience
o.expandtab = true
o.smarttab = true
o.cindent = true
o.autoindent = true
o.tabstop = 4
o.shiftwidth = 0
o.softtabstop = -1 -- If negative, shiftwidth value is used

-- Makes neovim and host OS clipboard play nicely with each other
o.clipboard = 'unnamedplus'

-- Case insensitive searching UNLESS /C or capital in search
o.ignorecase = true
o.smartcase = true

-- Enables mouse support
opt.mouse = "a"
