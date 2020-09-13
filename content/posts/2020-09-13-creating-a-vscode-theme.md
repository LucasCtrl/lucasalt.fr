---
title: "Creating a VS Code theme"
category: "VSCode"
author: "Lucas Albert"
date: "2020-09-13"
thumbnail: "../thumbnails/vscode.png"
hero: "../images/vscode.png"
source: "Lucas Albert"
sourceURL: "none"
template: "post"
---

[Visual Studio Code](https://code.visualstudio.com) is a free open source text editor with a great possibility of customization. By adding some extensions and themes, you can make VS Code yours. In this post, I'm going to cover the creation of a VS Code theme from scratch.

# Creating the extension

## Installing Yeoman
Before creating the theme, you need to have some applications installed on your computer like VS Code (obviously 😁), [Node.js](https://nodejs.org) and [Git](https://git-scm.com/). Then we can start the process of creating an extension.

First, we need to install [Yeoman](https://yeoman.io/). Yeoman is a tool that allow you to use boilerplates made by some peoples or organizations. In this case, Yeoman is going to create our project scaffolding.

For installing Yeoman, you just need to user the following command:

```bash
# With NPM
$ npm install -g yo generator-code
# Or with Yarn
$ yarn install -g yo generator-code
```

## Creating the extension's scaffolding


https://code.visualstudio.com/api/get-started/your-first-extension

Create the extension with `yo code`
Debug the extension

```bash
$ yo code
```

# Create your custom theme

https://code.visualstudio.com/api/extension-guides/color-theme

# Deploy the extension on the market place


Example here -> [GMK Dots theme](https://github.com/LucasCtrl/vscode-gmk-dots-theme)
