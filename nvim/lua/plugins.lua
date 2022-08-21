return require('packer').startup(function()
    
        -- Package Manager
        use 'wbthomason/packer.nvim'
    
        -- Competitive programming automate setup
        use 'searleser97/cpbooster.vim'
        
        -- Better highlight
        use {
            'nvim-treesitter/nvim-treesitter',
            run = function() require('nvim-treesitter.install').update({ with_sync = true }) end,
        }
        
        -- LSP
        use 'williamboman/nvim-lsp-installer'
        use 'neovim/nvim-lspconfig'

        -- Statusline
        use {
            'nvim-lualine/lualine.nvim',
            requires = { 'kyazdani42/nvim-web-devicons', opt = true }
        }
        
        -- Autopairs
        use 'windwp/nvim-autopairs'
        
        -- Comment
        use 'numToStr/Comment.nvim'
end)
