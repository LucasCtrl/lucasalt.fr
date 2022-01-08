---
title: "Dark theme implementation with vanilla CSS"
category: "Frontend"
author: "Lucas Albert"
date: "2022-01-03"
headerImage: true
source: "Lucas Albert"
---

At the beginning, light-on-dark scheme (dark mode) was a standard due to hardware limitation, then dark-on-light scheme (light mode) came up to have a similar look that ink on paper and became the norm. Since 2018-2019, dark mode was reintroduced by some designers and by a new CSS property.

<!--more-->

Now, most of the web offer you to select your theme as well as your OS and this feature became a standard.

I this post, I'm gonna implement a theme detector as well as a theme toggler. The theme detector will detect the theme that the user is currently using on it's browser or it's OS when the user visit the website for the first time. The theme toggler will allow the user to switch from one theme to another. To enhance the user experience, the active theme will be stored in the local storage. That will allow the browser to remember the last theme that the user used the last time he visit the website.

## HTML

Nothing fancy here, I created a simple page with Emmet. I just included an import for my CSS and my JS. The button will be my switch to change the theme.

```html [index.html]
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

## CSS

Working with variables
`:root` variables for default theme (in this case, white)
`.dark-theme` change variables value (in this case, dark)

```css
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
```

Apply those variable to the content.
By default, white theme, if class `dark-theme` applied in one of the parent element (`html`, `body`), all value in `:root` are replaced by the values defined in `dark-theme`. If unapplied, restore to default.

```css
body {
  background-color: var(--background);
}

h1 {
  color: var(--heading);
}

p {
  color: var(--content);
}
```

Full css with some reset and fancy font.
```css [main.css]
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

## JS

Now CSS and HTML are created, need to change the theme by clicking a button or by checking default OS/browser theme.

Can check default user theme with
```js
window.matchMedia("(prefers-color-scheme: dark)").matches // True or False
```

Store the theme in localStorage, able the website to load previous theme configuration.
In this case, key `theme`, value `dark` or `light` depending the activated theme.


First thing, get default theme for OS/browser or previous theme configuration
```js
function getCurrentTheme() {
  if (
    localStorage.theme == "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    // Apply "dark" theme if
    // - previous visit was on dark theme
    // - OS/Browser theme is dark
  } else {
    // Apply "light" theme
  }
}
```

```js [app.js]
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
