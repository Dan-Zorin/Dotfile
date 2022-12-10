local setup, nvimtree = pcall(require, "nvim-tree")
if not setup then
    return
end

-- recommended settings
vim.g.loaded = 1
vim.g.loaded_netrwPlugin = 1

-- change arrow colors
vim.cmd([[ highlight NvimTreeIndentMarker guifg=#5F5399]])

nvimtree.setup({
    renderer = {
        icons = {
            glyphs = {
                folder = {
                    arrow_closed = "",
                    arrow_open = "",
                },
            },
        },
    },
    actions = {
        open_file = {
            window_picker = {
                enable = false
            }
        }
    }
})