---
title: 'My personal homepage'
publishDate: 2025-12-25
published: false
---

It's been a long time since I wanted my own homepage. For me, this was not only something that I wanted to use as a tool but also a playground to learn new stuff.

Requirements:
- Self hosted
- Personalized

Here come Glance.

## Install Glance
Many installation process present on the [GitHub repo](https://github.com/glanceapp/glance/blob/main/README.md#installation). But I always prefer starting from scratch.
Right now I like to work with docker containers and with compose file.
In the near future, I'll move to Proxmox to simplify my setup.

### Create `docker-compose.yml` file
```yml
services:
  glance:
    container_name: glance
    image: glanceapp/glance
    restart: unless-stopped
    volumes:
      - ./config:/app/config
    ports:
      - 8080:8080
```

### Create the basic config
Create a folder called `config`. Create a file called `glance.yml`

```sh
mkdir config && touch ./config/glance.yml
```

Edit `glance.yml` with minimal configuration

```yml
pages:
  - name: Home
    columns:
      - size: full
```

### Start the container
```sh
docker compose up -d
```

Check your glance app at `<yourIpAddress:8080>`

## Configuring Glance
Add or remove widget

### Adding a searchbar at the top of the page
First need to create an area where the widget will be added. In our case a [`head-widget`](https://github.com/glanceapp/glance/blob/main/docs/configuration.md#head-widgets).

Then check the documentation of the [Search widget](https://github.com/glanceapp/glance/blob/main/docs/configuration.md#search-widget).

```yml
pages:
  - name: Home
    # Start
    head-widgets:
      - type: search
        search-engine: duckduckgo
        bangs:
          - title: YouTube
            shortcut: "!yt"
            url: https://www.youtube.com/results?search_query={QUERY}
    # End
    columns:
      - size: full
```
