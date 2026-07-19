" Folding toggle
exmap togglefold obcommand editor:toggle-fold
nmap zo :togglefold<CR>
nmap zc :togglefold<CR>
nmap za :togglefold<CR>

" Window management
exmap splitv obcommand workspace:split-vertical
exmap splith obcommand workspace:split-horizontal  
exmap closewin obcommand workspace:close

nmap <C-,>s :splith<CR>
nmap <C-,>v :splitv<CR>
nmap <C-,>w :closewin<CR>

" Toggle checkbox
exmap togglecheck obcommand editor:toggle-checklist-status
nmap <C-,>t :togglecheck<CR>

exmap focustimeblock obcommand curaai-custom-plugin:focus-cursor-to-current-time-block-anchor
noremap <C-,>c :focustimeblock<CR>

noremap H ^
noremap L $