
# Dotfiles

This repository contains my personal configuration files (dotfiles) for various development tools and work environments. It aims to centralize, document, and version these configurations for quick deployment and to enhance productivity across multiple systems.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Customization](#customization)
- [Updating](#updating)
- [Acknowledgments](#acknowledgments)
- [Contribution](#contribution)
- [License](#license)

## Project Structure

This repository includes configurations for several applications and environments, including:

- **Hyprland**: Configuration for `hyprland` window manager.
- **Neofetch**: Configuration for `neofetch` tool.
- **Rofi**: Configuration for `rofi`, with custom theme.
- **Waybar**: Configuration for `waybar`, for a light task bar.
- **Miscellaneous Tools**: Scripts for `hyprland`, `waybar` and others.

## Prerequisites

Before installing these dotfiles, ensure `hyprland` is installed.

## Installation

### 1. Clone the Repository

Clone the repository into your home directory:

```bash
git clone https://github.com/leo-jasoncoulais/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
```

### 2. Link the Dotfiles

You can either use the provided installation script to automate the symbolic linking of dotfiles, or perform the linking manually.

#### Running the Installation Script

```bash
chmod +x install.sh
./install.sh
```

## Customization

Each configuration file is designed to be modular. Modify the settings according to your specific needs.

## Updating

To synchronize your dotfiles with the latest changes, pull the updates from the repository and re-run the installation script.

```bash
git pull origin main
./install.sh
```

## Acknowledgments

I'd like to thank [Catppuccin](https://github.com/catppuccin) for his work, which I've taken over in part to build my working environment. 

## Contribution

Contributions to improve these dotfiles are welcome. If you’d like to suggest enhancements:

1. Open an *issue* to discuss a feature or modification.
2. Submit a *pull request* with your changes.

## License

These configurations are provided under the MIT License. See the [LICENSE](LICENSE) file for details.
