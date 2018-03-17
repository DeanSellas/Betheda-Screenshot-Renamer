@echo off
title Bethesda Renamer

REM Path Where File Is Located
cd /D D:\
cd D:\Google Drive\Documents\GitHub\Bethesda Screenshot Renamer

REM Runs Python Script: use Prefix of the game, Location of Game, and New Location for Screenshot (leave empty if you want same location)
REM first item: game prefix; second item: game location; third item: where to save screenshot (leave blank if you want to just rename it and not relocate)
python renamer.py "rename" "sse" "G:\Games\Steam\steamapps\common\Skyrim Special Edition" "D:\Google Drive\Pictures\Games\Skyrim"