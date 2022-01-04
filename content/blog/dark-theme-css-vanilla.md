---
title: "Dark theme implementation with vanilla CSS"
category: "Frontend"
author: "Lucas Albert"
date: "2022-01-03"
headerImage: true
source: "Lucas Albert"
---

```html
<html>
  <head>
    <title>Dark theme implementation</title>
    <link rel="stylesheet" href="main.css">
  </head>
  <body>
    <h1>Hello world!</h1>
    <p>This is an exemple of dark theme implementation.</p>
    <button id="themeToggler">Toggle theme</button>
    <script src="app.js"></script>
  </body>
</html>
```

```css - main.css
:root {
  --background: #f9fafb; /* White-Light blue */
  --heading: #1d4ed8; /* Dark blue */
  --content: #000000; /* Black */
}

.dark-theme {
  --background: #111827; /* Black-Dark blue */
  --heading: #3b82f6; /* Light blue */
  --content: #ffffff; /* White */
}

html, body {
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background-color: var(--background);
}

h1 {
  color: var(--heading);
}

p {
  color: var(--content);
}
```

```js - app.js
// Turn dark mode on
function darkThemeOn() {
  localStorage.theme = "dark";
  document.body.classList.add("dark-theme");
}

// Turn light mode on
function lightThemeOn() {
  localStorage.theme = "light";
  document.body.classList.remove("dark-theme");
}

// Function at startup
function main() {
  if (
    localStorage.theme == "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    darkThemeOn();
  } else {
    lightThemeOn();
  }
}

main()

// Toggler event
document.querySelector("#themeToggler").addEventListener("click", (e) => {
  if (localStorage.theme === "dark") {
    lightThemeOn();
  } else {
    darkThemeOn();
  }
});
```
