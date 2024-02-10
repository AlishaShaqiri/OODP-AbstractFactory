# Cross-Platform GUI Library

This is a cross-platform GUI library implemented in Python, designed to support specific look and feel standards for Windows, macOS, and Linux using the Abstract Factory pattern. The library aims to facilitate the creation of GUI applications that seamlessly adapt their appearance to match the design standards of the target operating system.

## Motivation

GUI applications often require platform-specific styling to ensure a consistent and native user experience across different operating systems. By implementing the Abstract Factory pattern, this library provides a structured approach to create a consistent set of widgets (buttons, checkboxes, windows) that conform to the design standards of Windows, macOS, and Linux.

## Features

- Support for creating GUI components (buttons, checkboxes, windows) tailored to the look and feel of Windows, macOS, and Linux.
- Encapsulation of platform-specific styling logic within factory classes, promoting code modularity and maintainability.
- Simple integration with existing Python projects, allowing developers to easily incorporate platform-specific GUI elements into their applications.

## Structure

- `gui_factory.py`: Contains the Abstract Factory pattern implementation for creating GUI components.
- `main.py`: Demonstrates the usage of the cross-platform GUI library by creating an application with buttons and windows.

