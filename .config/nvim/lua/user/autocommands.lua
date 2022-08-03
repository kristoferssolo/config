vim.cmd([[
    augroup _general_settings
        autocmd!
        autocmd FileType qf,help,man,lspinfo nnoremap <silent> <buffer> q :close<CR>
        autocmd TextYankPost * silent!lua require('vim.highlight').on_yank({higroup = 'Visual', timeout = 200})
        autocmd BufWinEnter * :set formatoptions-=cro
        autocmd FileType qf set nobuflisted
        autocmd BufWritePre * %s/\s\+$//e
        autocmd InsertEnter * norm zz
        highlight CursorLine ctermbg=White cterm=bold guibg=#222222
        highlight CursorColumn ctermbg=White cterm=bold guibg=#222222
    augroup end

    augroup _git
        autocmd!
        autocmd FileType gitcommit setlocal wrap
        autocmd FileType gitcommit setlocal spell
    augroup end

    augroup _markdown
        autocmd!
        autocmd FileType markdown,vimwiki setlocal wrap
        autocmd FileType markdown,vimwiki setlocal spell
    augroup end

    augroup _auto_resize
        autocmd!
        autocmd VimResized * tabdo wincmd =
    augroup end

    augroup _alpha
        autocmd!
        autocmd User AlphaReady set showtabline=0 | autocmd BufUnload <buffer> set showtabline=2
    augroup end

    augroup _lsp
        autocmd!
        autocmd BufWritePre,InsertLeave * lua vim.lsp.buf.formatting()
    augroup end

    augroup _run
        autocmd!
        autocmd FileType python imap <buffer> <C-b> <esc><cmd>w<CR><cmd>exec '!python3' shellescape(@%, 1)<CR>
        autocmd FileType python map <buffer> <C-b> <cmd>w<CR><cmd>exec '!python3' shellescape(@%, 1)<CR>
        autocmd FileType rust imap <buffer> <C-b> <esc><cmd>w<CR><cmd>exec '!cargo run'<CR>
        autocmd FileType rust map <buffer> <C-b> <cmd>w<CR><cmd>exec '!cargo run'<CR>
    augroup end
]])