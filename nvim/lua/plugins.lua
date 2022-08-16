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
        
end)
