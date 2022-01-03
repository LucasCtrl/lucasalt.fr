---
title: "Dark theme implementation with vanilla CSS"
category: "Frontend"
author: "Lucas Albert"
date: "2021-03-01"
headerImage: true
source: "Lucas Albert"
---

```html
<html>
  <head>
    <title>Dark theme implementation</title>
  </head>
  <body>
    <h1>Hello world!</h1>
    <p>This is an exemple of dark theme implementation.</p>
  </body>
</html>
```

```css
::root {
  --background: #111827; // Black-Dark blue
  --heading: #3b82f6; // Light blue
  --paragraph: #ffffff; // White
}

.dark-theme {
  --background: #f9fafb; // White-Light blue
  --heading: #1d4ed8; // Dark blue
  --content: #000000; // Black
}

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

```js
if (
  localStorage.theme === 'dark' ||
  (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
) {
  localStorage.theme = 'dark'
  document.documentElement.classList.add('dark-theme')
} else {
  localStorage.theme = 'light'
  document.documentElement.classList.remove('dark-theme')
}
```
