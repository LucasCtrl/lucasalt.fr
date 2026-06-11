---
title: "Test page"
publishDate: 2025-09-29
published: false
tags:
  - development
  - misc
---

## Headings

# H1 — heading

## H2 — heading

### H3 — heading

#### H4 — heading

## Paragraph

Labore cupidatat est ut ullamco. Laboris cupidatat dolore ullamco et est aliqua amet et id cillum. Excepteur officia labore non cupidatat laborum consectetur quis. Officia cillum mollit exercitation aliqua ullamco labore cillum incididunt culpa. Aute ipsum culpa eu fugiat in ex et consequat in pariatur adipisicing consequat occaecat id. Lorem eu incididunt aute eiusmod voluptate.

Enim exercitation consectetur mollit dolore dolore laboris commodo ipsum sunt Lorem in nostrud. Aliqua do consequat et nisi dolor. Nulla amet ipsum dolore incididunt voluptate incididunt et proident sunt sit et et veniam. Quis sint nostrud do laborum sit commodo.

## Lists

### Ordered list

1. Firstly
2. Secondly
3. Thirdly

### Unordered list

- Chapter
  - Section
    - Paragraph

### ToDo list

- [ ] Job
  - [x] Step 1
  - [x] Step 2
  - [ ] Step 3

## Block Quote

> This line shows the _block quote_.

## Tables

| Company                      | Contact          | Country |
| :--------------------------- | :--------------- | ------: |
| Alfreds Futterkiste          | Maria Anders     | Germany |
| Island Trading               | Helen Bennett    |      UK |
| Magazzini Alimentari Riuniti | Giovanni Rovelli |   Italy |

## Links

<http://127.0.0.1:4000>

## Footnote

Click the hook will locate the footnote[^footnote], and here is another footnote[^fn-nth-2].

## Inline code

This is an example of `Inline Code`.

But what are layers you will ask. Think about the `Shift` key. When you press on the letter `a`, you have a lowercase `a`. By pressing on `Shift + a`, you will go to a layer for uppercase letters and an uppercase `A` will appear on your screen. With a 40% keyboard, you will not only have 1 or 2 layers but 3 or 4 with specific purposes (layer 1 for uppercase letters, layer 2 for symbols, layer 3 for numbers, ...).

## Filepath

Here is the `/path/to/the/file.extend`{: .filepath}.

## Code blocks

### Common

```text
This is a common code snippet, without syntax highlight and line number.
```

### Specific Language

```bash
if [ $? -ne 0 ]; then
  echo "The command was not successful.";
  #do the needful / exit
fi;
```

```python
def main():
  outputFolder = 'dist'

  # Delete 'dist' folder if he exists
  if os.path.exists(outputFolder):
    shutil.rmtree(outputFolder)

  # Create 'dist' folder
  if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

  copyStaticContent(outputFolder)

if __name__ == '__main__':
  main()
```

## Images

![Small image example](https://i.imgur.com/dgSkt3r_d.webp?maxwidth=520&shape=thumb&fidelity=high)

![I'm a figcaption as well as a alternative text](https://images.unsplash.com/photo-1595044426077-d36d9236d54a?w=1280&auto=format&fit=crop)

![Photo by Jezael Melgoza on Unsplash](/img/jezael-melgoza-2FiXtdnVhjQ-unsplash.jpg)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat libero enim, ultricies ultricies justo gravida non. Quisque at suscipit nunc, ut fermentum felis. Nulla facilisi. Mauris ac mauris nec nisl interdum scelerisque. Mauris pharetra nunc rhoncus, sollicitudin lacus non, iaculis nibh. Cras nec consectetur dolor. Nullam pretium nisl in felis mollis fringilla. Fusce convallis vestibulum metus, non tristique elit consequat non. Maecenas ut dolor sit amet nulla placerat congue in ac mauris. Vivamus tempus enim massa. Donec varius justo ac arcu scelerisque, nec dapibus nisi maximus. Proin sagittis condimentum metus, eget posuere nisl euismod non. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam tristique risus velit, eu dapibus mauris gravida vitae. Praesent nec dui augue. Nulla facilisi.

[^footnote]: The footnote source

[^fn-nth-2]: The 2nd footnote source
