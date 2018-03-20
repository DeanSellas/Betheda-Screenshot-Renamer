@echo off
title Bethesda Renamer

REM Path Where File Is Located
cd /D D:\
cd D:\Google Drive\Documents\GitHub\Bethesda Screenshot Renamer

REM Runs Python Script: use Prefix of the game, Location of Game, and New Location for Screenshot (leave empty if you want same location)
python bethBacker.py rename-sse backup-sse