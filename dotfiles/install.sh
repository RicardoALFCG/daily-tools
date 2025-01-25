#!/bin/bash

echo "Stowing dotfiles..."
stow -v -t ~ zshrc

echo "All dotfiles have been stowed successfully!"
