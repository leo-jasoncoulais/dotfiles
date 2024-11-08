#!/bin/bash

if [[ $(dirname $(dirname "$(realpath "$BASH_SOURCE")")) != $HOME ]]; then
    echo "Please run this script from your home directory"
    exit 1
fi

# Install dependencies

sudo pacman -Syyu
sudo pacman -S --noconfirm zsh curl neofetch waybar rofi
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
echo 'export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH' >> ~/.zshrc

# Install dotfiles

ln -sf ~/.config/waybar ~/dotfiles/waybar
ln -sf ~/.config/rofi ~/dotfiles/rofi
ln -sf ~/.config/hypr ~/dotfiles/hyprland
ln -sf ~/.config/neofetch ~/dotfiles/neofetch

# Install scripts

ln -sf ~/.local/bin ~/dotfiles/scripts

# Install fonts

ln -sf /usr/share/fonts/JetBrainsFonts ~/dotfiles/JetBrainsFonts

# Complete

echo "Finished installing dotfiles"
echo "Please restart your shell to apply changes"
