{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
    buildInputs = with pkgs; [
      python3
      geckodriver
    ] ++ (with pkgs.python3Packages; [
      beautifulsoup4
      # selenium was broken for so long on nix and you need to be on the latest
      # unstable channel to get the right version
      selenium
      pyperclip
    ]);
}
