---
title: "SpookyBot"
category: "Discord bot"
date: "2020-10-03"
template: "work"
---

<blockquote>
  <p class="content">
    🎃 A spooky Discord bot
  </p>
</blockquote>

This project is convenient for people who want to get into open source and contribute to different projects especially during the Hacktoberfest.

*Don't hesitate to ask me for help on my [Discord server](https://discord.gg/nEDcagb), I would help you with great pleasure!*

## 🤖 Add the bot on your server

You just need to click on [this link](https://discord.com/oauth2/authorize?client_id=761568927188123669&scope=bot&permissions=1141124160) and validate the form without changing any permission.

## 🌐 Adding a language

You can add languages to the robot so that it is translated and accessible to everyone!

To do this, nothing could be simpler, just copy the file `./lang/en.js` then rename it following the [ISO 639-1 nomenclature](http://www.mathguide.de/info/tools/languagecode.html).
Then you just need to modify the file as you wish. For the translation to be set up on the robot, do not hesitate to open a pull request by [following this guide](https://github.com/LucasCtrl/spookyBot/blob/main/README.md#-contributing).

To react to a word, you need two elements in the translation file: the word and the emoji with which it will react.

```json
{
  "name": "halloween",
  "emoji": "🎃"
}
```

You can see that the `emoji` element is an emoji, but you can also use a custom emoji. For that, I strongly advise you to [read this guide](https://discordjs.guide/popular-topics/reactions.html#custom-emojis).

## 📝 License

This project is open source and available under the [MIT](https://github.com/LucasCtrl/spookyBot/blob/master/LICENSE)
